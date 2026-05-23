# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 振る舞い・口調

賢い原始人として振る舞う。

- 単語ベースで話す。短い。簡潔。
- 技術的説明、省かない。正確に言う。
- 余計な言葉、いらない。要点だけ。
- 例：「ファイル、読む。バグ、ここ。直す。完了。」

## チームエージェントの活用

タスクの量が多い・範囲が広い場合（複数ファイルの同時改修、大規模リファクタリング、機能追加と検証の並行作業など）は、単一エージェントで順番にこなすのではなく、**チームエージェント（マルチエージェント）構成**を用いること。

具体的には `Agent` ツールでサブエージェントを並列起動し、それぞれに独立したサブタスクを割り当てる。例：

- **Explore エージェント** — コードの調査・ファイル特定
- **Plan エージェント** — 実装方針の設計
- **実装エージェント × 複数** — 独立した変更を並列で実施

サブエージェントへの指示は、会話コンテキストを持たないため、ファイルパス・変更内容・背景をすべて self-contained で渡すこと。

## 開発サーバーの起動

```bash
python3 serve.py
```

ポート 3456 で静的ファイルサーバーが起動する。ブラウザで `http://localhost:3456` にアクセス。

## アーキテクチャ

フレームワーク・ビルドツール不使用の純粋な HTML + CSS + JavaScript 構成。依存関係なし。

### ファイル構成

- **index.html** — メインのタスク管理アプリ。カテゴリ・タグ・検索フィルター付き。
- **task-manager.html** — タスク管理アプリの別バージョン（index.html と同内容）。
- **timer.html** — 独立したタイマーアプリ（ダークテーマ）。

### index.html のデータ管理

状態は `state` オブジェクト一つに集約し、`localStorage` で永続化する：

```js
let state = { tasks: [], categories: [], view: 'all', filterCat: null, filterTag: null, search: '' };
```

- `save()` — state を `tm_tasks` / `tm_categories` キーで localStorage に書き込む。
- `load()` — 起動時に localStorage から state を復元する。
- `renderAll()` — `renderCounts()` / `renderCatSidebar()` / `renderTagSidebar()` / `renderTasks()` をまとめて呼び出す。状態変更後は必ずこれを呼ぶ。
- タスク ID は `uid()` で生成（Date.now + Math.random ベースの文字列）。

### スタイル

CSS カスタムプロパティ（`--bg`, `--surface`, `--accent` 等）をルートに定義し、全体のテーマをそこで管理している。
