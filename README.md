# ETL

這裏你可以找到我們做 ETL 的 python 和 bash script 原始碼。

## 原由
使用 rotten_tomato.py 爬下的原始資料 json 檔有下列問題:
* 文件開頭結尾分別缺少 [ 和 ]
* 含有大量空值物件: {"Show": ""}
* 重複物件
* 所有的 Season 應屬於同一個 field

## 解決方式
* bash script 增加 [ 和 ]
* bash script 刪除空值物件
* deduplicate.py 這支檔案用來刪除重複物件
* bash script 將所有 Season 物件放在 "tomato" field 底下
