# Inspired by https://postd.cc/auto-documented-makefile/
MAKEFLAGS += --warn-undefined-variables
SHELL = /bin/bash
.SHELLFLAGS = -e -o pipefail -c
.DEFAULT_GOAL = help

# SHLVLが未定義（＝シェルがcmdやpowershell）の場合、"Git for Windows"のbashを使用する
ifndef SHLVL
    SHELL = C:\Program Files\Git\bin\bash.exe
endif

# .を含まないターゲットをすべてPHONYターゲットにする
.PHONY: $(shell grep -oE ^[a-zA-Z0-9%_-]+: $(MAKEFILE_LIST) | sed 's/://')

# PythonのデフォルトエンコーディングをUTF-8にする
export PYTHONUTF8 = 1

## プロジェクト特有の変数設定
# poetryの実行コマンド
POETRY ?= poetry
# pre-commitの実行コマンド
PRE_COMMIT ?= $(POETRY) run pre-commit
# pytestの実行コマンド
PYTEST ?= $(POETRY) run pytest
PYTEST_FLAGS ?= -s -v
# toxの実行コマンド
TOX ?= $(POETRY) run tox
TOX_FLAGS ?=

help: ## ヘルプメッセージを表示する
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9%_-]+:.*?## / {printf "    \033[36m%-16s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

## Project Tasks
env: ## 環境を確認する
	@cat /etc/os-release 2>/dev/null || cmd.exe /c ver 2>/dev/null
	$(POETRY) run python -V
	$(POETRY) --version
	$(POETRY) show

setup: ## 開発環境をセットアップする。リポジトリをクローンしたらまずはじめに1回実行すること。
	$(POETRY) install
	$(PRE_COMMIT) install && $(PRE_COMMIT) install-hooks

lint-local:
	$(PRE_COMMIT) run --all-files

lint: lint-pre-commit lint-poetry-lock ## プロジェクト全体に対して静的解析ツールを実行する

lint-pre-commit: ## pre-commitの全フックを実行する
	$(PRE_COMMIT) run --all-files --show-diff-on-failure

pre-commit-%: ## pre-commitのフックを実行する。%にフック名を指定する（ex: pre-commit-black）
	$(PRE_COMMIT) run $* --all-files --show-diff-on-failure

lint-poetry-lock: ## pyproject.tomlとpoetry.lockの整合性がとれているかチェックする
	$(POETRY) lock --no-update --check

test: ## 自動テストを実行する
	$(PYTEST) $(PYTEST_FLAGS)

tox: ## 複数バージョンで自動テストを実行する
	$(TOX) $(TOX_FLAGS)

apidoc: ## ソースコードからAPIドキュメントを生成する
	$(POETRY) run sphinx-apidoc -e -f -o docs/api dsflow

doc_suffix := ## Sphinxドキュメントの拡張子。デフォルトでは.htmlになる
build-docs: ## Sphinxでドキュメントをビルドする
	$(POETRY) run sphinx-build -M html docs docs/_build \
		$(if $(doc_suffix),-D html_file_suffix=$(doc_suffix),)

build-aspx: doc_suffix=.aspx # 拡張子を上書きしてbuild-docsを実行
build-aspx: build-docs ## Sphinxでドキュメントをビルドする（SharePoint向け）
# PyData Sphinx Themeのversion switcherをaspxに対応させる
	@sed -i 's@\.html@.aspx@g' ./docs/_build/html/_static/scripts/pydata-sphinx-theme.js

project_version := $(shell python -c "import re; print(re.search(r'version\s*=\s*\"([.0-9a-zA-Z_-]*)\".*', open('pyproject.toml', encoding='utf-8').read()).group(1))")
version_files := pyproject.toml flowchart_explorer/__init__.py
update-version: ## プロジェクトのバージョンをアップデートする。新しいバージョンとしてNEW_VERSION変数を指定すること。
	$(if $(NEW_VERSION),,$(error "NEW_VERSION"変数を設定してください（例: `make NEW_VERSION=0.1.2 update-version`）))
	@for file in $(version_files); do \
		python -c "import sys, re; sys.stdout.write(re.sub(r'$(project_version)', '$(NEW_VERSION)', sys.stdin.read()))" < $$file > tmpfile && mv tmpfile $$file; \
	done

clean: ## 成果物をクリーンアップする
	@$(RM) -r docs/_build dist htmlcov .coverage* coverage.xml
