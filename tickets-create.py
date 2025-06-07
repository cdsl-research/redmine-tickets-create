import requests

# Redmineの設定（例）
REDMINE_URL = "https://your-redmine.example.com"  # ← ダミーURL
API_KEY = "your_redmine_api_key" # ← ダミー値  

# チケットの詳細設定（例）
PROJECT_IDENTIFIER = 'your_project' # ダミープロジェクト
SUBJECT = "ticket-create-test"
ASSIGNED_TO_ID = 21

# 生成するチケットの情報（例）        
data = {
    "issue" :{
        "project_id" : PROJECT_IDENTIFIER ,
        "subject" : SUBJECT,
        "tracker_id" : 4,
        "priority_id" : 2,
        "assigned_to_id" :ASSIGNED_TO_ID,
    }  
}

# POSTリクエストでチケットを作成
response = requests.post(
    f"{REDMINE_URL}/issues.json",
    json=data,
    headers={
        'X-Redmine-API-key' : API_KEY,
        'Content-Type': 'application/json'
    }
)

# チケット作成のエラーについて
if response.status_code == 201:
    print("チケット作成成功！")
    print(response.json())
else:
    print("チケット作成失敗")
    print("ステータスコード:", response.status_code)
    print("レスポンス:", response.text)
    
