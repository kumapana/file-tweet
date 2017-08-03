# -*- coding: utf-8 -*-

from requests_oauthlib import OAuth1Session
import time

from datetime import datetime
datetime.now().strftime("%Y/%m/%d %H:%M:%S")

tweeted_text="initialize"
new_tweet_text="initialize"

#アクセストークン
CK='<customer key>'
CS='<customer secret>'
AT='<access token>'
AS='<access secret>'

#読み込むテキストファイル
file_name='<読み込み先>'

#投稿先URL
url = "https://api.twitter.com/1.1/statuses/update.json"

def tweet(text):
  #ツイート内容
  params = {"status":text}
  
  #ツイート実行
  twitter = OAuth1Session(CK, CS, AT, AS)
  req = twitter.post(url,params=params)
  
  #ツイート内容をtweeted_textに保存
  tweeted_text=text
  
  #ツイート結果表示
  if req.status_code==200:
    print("OK")
  else:
    print("Error: %d"%req.status_code)


num=0
while(num==0):
 #テキストファイル読み込み
  load_file=open(file_name,'r')
  new_tweet_text=load_file.read()

  #前回読み込んだファイルと付きあわせて、変更されていればツイートする
  if new_tweet_text!=tweeted_text:
    if len.(new_tweet_text.encode("UTF-8"))<=140:
      tweet(new_tweet_text)
      load_file.close()
    else:
      load_file.close()
      print("140文字を超えているため、ツイートしませんでした。")
      return 1
  else:
    load_file.close()
  time.sleep(30) 
