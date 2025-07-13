# redmine-tickets-create

# 概要
実行することで，Redmine上でチケットを作成するスクリプト．
”生成するチケットの情報”は，生成したいチケットに合わせて変更してください．
”生成するチケットの情報”と”POSTリクエストでチケットを作成”の部分をループで回せば一度の実行で複数のチケットを作成することもできます．
また，このスクリプトをsystemd timerやCronJobで定期実行することで，チケットを自動で定期的に作成することができます．
RedmineAPIやurlの管理には環境変数の使用をお勧めします．`Python 3.12.3`で実行しました．

# 事前準備（このスクリプトの入力）
`REDMINE_URL`：RedmineサーバのURL

`API_KEY`：Redmineの個人設定ページから取得できる「APIアクセスキー」．[RedmineのUIにアクセス]→[個人設定]→[APIアクセスキー]で取得する．

`PROJECT_IDENTIFIER`：Redmineプロジェクトの識別子（IDではなく識別子名）．URL上の`/projects/XXX`の`XXX`にあたる部分．

`SUBJECT`：チケットの件名．自由記述．

`ASSIGNED_TO_ID`：チケットの担当者のユーザID（数値）.[RedmineのUIにアクセス]→[管理]→[ユーザー]でユーザごとにIDを取得する．

`tracker_id`：チケットのトラッカーのID（数値）．環境によって異なるので事前に確認する必要がある．[RedmineのUIにアクセス]→[管理]→[トラッカー]で取得する．

`priority_id`チケットの優先度のID（数値）．環境によって異なるので事前に確認する必要がある．[RedmineのUIにアクセス]→[管理]→[選択肢の値]で取得する．


# 説明
仮想環境を使用する際は以下のコマンドを実行してください．

コマンドとその実行結果
```bash
monitoring@monitoring-master-ml:~/ticket-related/redmine-tickets-create$ python3 -m venv .venv
monitoring@monitoring-master-ml:~/ticket-related/redmine-tickets-create$
```

仮想環境をアクティベートする方法

コマンドとその実行結果
```bash
monitoring@monitoring-master-ml:~/ticket-related/redmine-tickets-create$ source .venv/bin/activate
(.venv) monitoring@monitoring-master-ml:~/ticket-related/redmine-tickets-create$
```

ticket-create.pyを実行するためには最低でもrequestsモジュールが必要です．以下のコマンドを実行し，インストールしてください．

コマンドとその実行結果
```bash
(.venv) monitoring@monitoring-master-ml:~/ticket-related/redmine-tickets-create$ pip3 install requests
Collecting requests
  Using cached requests-2.32.4-py3-none-any.whl.metadata (4.9 kB)
Collecting charset_normalizer<4,>=2 (from requests)
  Using cached charset_normalizer-3.4.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (35 kB)
Collecting idna<4,>=2.5 (from requests)
  Using cached idna-3.10-py3-none-any.whl.metadata (10 kB)
Collecting urllib3<3,>=1.21.1 (from requests)
  Using cached urllib3-2.5.0-py3-none-any.whl.metadata (6.5 kB)
Collecting certifi>=2017.4.17 (from requests)
  Downloading certifi-2025.7.9-py3-none-any.whl.metadata (2.4 kB)
Using cached requests-2.32.4-py3-none-any.whl (64 kB)
Downloading certifi-2025.7.9-py3-none-any.whl (159 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 159.2/159.2 kB 4.8 MB/s eta 0:00:00
Using cached charset_normalizer-3.4.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (148 kB)
Using cached idna-3.10-py3-none-any.whl (70 kB)
Using cached urllib3-2.5.0-py3-none-any.whl (129 kB)
Installing collected packages: urllib3, idna, charset_normalizer, certifi, requests
Successfully installed certifi-2025.7.9 charset_normalizer-3.4.2 idna-3.10 requests-2.32.4 urllib3-2.5.0
(.venv) monitoring@monitoring-master-ml:~/ticket-related/redmine-tickets-create$
```

スクリプトの実行結果

![image](https://github.com/user-attachments/assets/35d35335-9f84-410e-a5f7-cfebeb516a92)

APIによるチケットの発行後，そのレスポンスとして返されたチケット情報を`response.json`で取得，確認しています．不要であれば37行目をコメントアウトしてください．

RedmineのWeb UIから，発行されたチケット内容を確認できます．

![image](https://github.com/user-attachments/assets/db606aa7-a3cd-496a-bb38-4d5b871e9c88)

# 注意
このスクリプトではAPIキーといった機密情報や，具体的なチケットの内容についての情報をできる限り含まないようにしてあります．
実際に使用する際は，各変数を環境に応じて設定し`response.json`やRedmineAPIに関する記事を参考にチケットの内容をカスタマイズして使用してください．





