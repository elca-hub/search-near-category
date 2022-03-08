# カテゴリ分類API
指定されたデータと同じクラスタのデータを取得するAPI

## つまりどういうことだってばよ
検索した本と同じカテゴリの本をレコメンド(推薦)する際に用いることができる

## セットアップ
1. リポジトリのクローン
```bash
git clone [このリポジトリのHTTPS]
```

2. リポジトリに移動
```bash
cd search-near-category
```

3. build(念の為)
```bash
docker-compose build
```

4. apiの起動
```bash
docker-compose up api
```

5. apiが起動したかの確認
```bash
curl http://localhost:8080 # {"Hello": "World"}
```

## データの作成
```bash
curl http://localhost:8080/data/create?q=1000
```
`q=[データ件数]`という感じ

実際に実装する際はデータ自体は既に準備されている

## データの取得
```bash
curl http://localhost:8080/data/view
```
JSON形式でレスポンス

## クラスタリング
```bash
curl http://localhost:8080/data/category/create
```
データの件数によっては多少時間がかかる

## 同じクラスタのデータを取得
```bash
curl http://localhost:8080/data/category/near/2
```
一番最後がクラスタのID。デフォルトだとクラスタ数が5なので、0〜4を指定できる
