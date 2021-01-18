# ETL

這裏你可以找到我們做 ETL 的 python 和 bash script 原始碼。

## rotten_tomato ETL相關:
## 原由
使用 rotten_tomato.py 爬下的原始資料 json 檔有下列問題:
* 文件開頭結尾分別缺少 [ 和 ]
* 含有大量空值物件: {"Show": ""}
* 重複物件
* 所有的 Season 應屬於同一個 field
* 每個物件之間缺少逗號

## 解決方式
* json_fix.sh bash script 增加 [ 和 ]
* json_fix.sh bash script 刪除空值物件
* deduplicate.py 這支檔案用來刪除重複物件
* json_fix.sh bash script 將所有 Season 物件放在 "tomato" field 底下

## Omdb、Tomato_data、imdb 三份不同來源資料，整理、合併成建模使用:
### Omdb資料ETL過程:
* Omdb_data_first_Transform.ipynb 資料前處理
* Feature_Comapny_Transfrom.ipynb 將特徵:公司做資料前處理
* Omda_data_merge_company.ipynb 將omdb_data與Company_data 合併
* Omdb_Data visualization.ipynb 資料視覺化

### imdb艾美獎資料ETL過程:
* Emmy_Prime_first_transform.ipynb 資料前處理
* Emmy_Primetime_second_transform.ipynb 將個人獎項以及團體獎分開
