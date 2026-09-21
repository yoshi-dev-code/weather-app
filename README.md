# 天気アプリ

都市名を入力すると、現在の気温を取得できるWebアプリです。

## 公開URL

https://weather-app-frontend-3ape.onrender.com

## 主な機能

- 都市名から現在の気温を検索
- WeatherAPIを利用した天気情報の取得
- 検索中のローディング表示
- エラー表示
- レスポンシブ対応

## 使用技術

### フロントエンド
- React
- Vite
- JavaScript
- CSS

### バックエンド
- Python
- Flask
- Flask-CORS

### API
- WeatherAPI

### インフラ・その他
- Render
- Git
- GitHub
- 環境変数によるAPIキー管理

## 構成

ReactからFlask APIへリクエストを送り、
FlaskからWeatherAPIへアクセスして現在の気温を取得します。

React → Flask → WeatherAPI

## 工夫した点

- APIキーをソースコードに直接記述せず、環境変数で管理
- フロントエンドとバックエンドを分離
- 外部APIのエラーや通信失敗を考慮した処理
- Renderを利用してフロントエンド・バックエンドを公開