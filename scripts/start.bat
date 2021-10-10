@echo off

rem バッチファイルの上層のディレクトリに移動
cd /d %~dp0..

rem ログ格納ディレクトリがない場合
if not exist .\logs\ mkdir logs

rem 最新の「6005」と「6006」を再取得し、date_timelog.txtとしてlogsディレクトリに保存する。
set yyyy=%date:~0,4%
set mm=%date:~5,2%
set dd=%date:~8,2%

set timepz=%time: =0%
set hh=%timepz:~0,2%
set mm2=%timepz:~3,2%
set ss=%timepz:~6,2%

set today=%yyyy%%mm%%dd%_%hh%%mm2%%ss%

wevtutil qe System /c:3 /f:Text /rd:true "/q:*[System[(EventID=6005 or EventID=6006)]]" > .\logs\%today%_timelog.txt

rem バッチファイルと同じディレクトリに移動
cd /d %~dp0

rem CSVをtimelog.xlsxにマージする。&テキストログの余計な部分を削除する。
python convert.py ../logs/%today%_timelog.txt