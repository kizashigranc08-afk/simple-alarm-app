# simple-alarm-app

シンプルなアラームアプリ + ミニWebツール集。

フレームワーク不使用。純粋な HTML / CSS / JavaScript のみ。

## アプリ一覧

| ファイル | 内容 |
|---|---|
| `alarm.html` | アラームアプリ（メイン） |
| `timer.html` | タイマー（ダークテーマ） |
| `index.html` | タスク管理アプリ |

## 起動方法

```bash
python3 serve.py
# → http://localhost:3456
```

## alarm.html の機能

- 現在時刻リアルタイム表示
- アラーム追加・削除・ON/OFF トグル
- 時刻になったら音で通知（Web Audio API）
- 設定は localStorage に永続化
