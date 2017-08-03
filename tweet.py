
#アクセストークン
CK='<customer key>'
CS='<customer secret>'
AT='<access token>'
AS='<access secret>'

#読み込むテキストファイル
file_name='<読み込み先>'

#ファイルを読みに行く間隔
sleep_time=<秒単位で指定>

#投稿先URL
url = "https://api.twitter.com/1.1/statuses/update.json"

#ここより下は分かる人のみ弄って下さい
#--------------------------------------------------------------------------------------------------
from requests_oauthlib import OAuth1Session
import time

tweeted_text="initialize"
new_tweet_text="initialize"


def tweet(text):
  #ツイート内容
  params = {"status":text}
  
  #ツイート実行
  twitter = OAuth1Session(CK, CS, AT, AS)
  req = twitter.post(url,params=params)
  
  #ツイート結果表示
  if req.status_code==200:
    print("以下の内容をツイートしました : ",text)
  else:
    print("Error: %d  以下の内容をツイートできませんでした : "%req.status_code,text)


num=0
while(num==0):
 #テキストファイル読み込み
  load_file=open(file_name,'r',encoding="utf-8")
  new_tweet_text=load_file.read()

  #前回読み込んだファイルと付きあわせて、変更されていればツイートして、ツイート内容をtweeted_textに保存する
  if new_tweet_text!=tweeted_text:
    tweeted_text=new_tweet_text
    tweet(new_tweet_text)
    load_file.close()
  else:
    load_file.close()
    print("ファイルの内容が前回ツイートと同じだったので、ツイートしませんでした。")
  time.sleep(sleep_time) 
