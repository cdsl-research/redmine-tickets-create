# redmine-tickets-create

# 概要
実行することで，Redmine上でチケットを作成するスクリプト．
”生成するチケットの情報”は，生成したいチケットに合わせて変更してください．
”生成するチケットの情報”と”POSTリクエストでチケットを作成”の部分をループで回せば一度の実行で複数のチケットを作成することもできます．
また，このスクリプトをsystemd timerやCronJobで定期実行することで，チケットを自動で定期的に作成することができます．
RedmineAPIやurlの管理には環境変数の使用をお勧めします．

# 説明
ticket-create.pyを実行するためには最低でもrequestsモジュールが必要です．以下のコマンドを実行し，インストールしてください．
```
pip install requests
```
実行結果

![image](https://github.com/user-attachments/assets/35d35335-9f84-410e-a5f7-cfebeb516a92)

APIによるチケットの発行後，そのレスポンスとして返されたチケット情報を`response.json`で取得，確認しています．不要であれば37行目をコメントアウトしてください．

RedmineのWeb UIから，発行されたチケット内容を確認できます．

![image](https://github.com/user-attachments/assets/db606aa7-a3cd-496a-bb38-4d5b871e9c88)

# 注意
このスクリプトではAPIキーといった機密情報や，具体的なチケットの内容についての情報をできる限り含まないようにしてあります．
実際に使用する際は，各変数を環境に応じて設定し`response.json`やRedmineAPIに関する記事を参考にチケットの内容をカスタマイズして使用してください．





