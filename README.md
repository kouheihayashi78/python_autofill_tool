# Python Auto-fill Tool Setup

## 1. Python 3.13.0 のインストール
以下のリンクから Python 3.13.0 をダウンロードしてインストールしてください:  
[Download Python 3.13.0](https://www.python.org/downloads/)

---

## 2. 環境変数の設定
ターミナルで以下のコマンドを実行します:

```bash
vi ~/.zshrc
```

## 3. zshrcファイルに下記のコマンドを入力
```bash
export PYTHON_HOME="/Library/Frameworks/Python.framework/Version/3.13/bin"
export PATH="$PYTHON_HOME:$PATH"
alias python='python3'
alias pip='pip3'
```

## 4. 保存後、以下のコマンドで環境変数を反映
```bash
source ~/.zshrc
```

## 5. 必要なライブラリをインストール
```bash
pip install selenium --break-system-packages
pip install jpholiday --break-system-packages
pip install python-dotenv
```

## 6. .envファイルを作成し以下のように記述
CLIENT_ID="kingoftimeのid"  
CLIENT_SECRET="kingoftimeのパスワード"  
CLIENT_START_TIME="開始時間"  
CLIENT_START_BREAK="休憩開始時間"  
CLIENT_END_BREAK="休憩終了時間"  
CLIENT_END_TIME="退勤時間"  
CLIENT_MESSAGE="入力するメッセージ"  

## 7. スクリプトの実行
```bash
python kingoftime.py
```