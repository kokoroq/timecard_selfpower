#! python3
# coding: utf-8
import pandas as pd
import re
import datetime
import os
import codecs
import sys

from pandas.tseries.offsets import Second

def main():
    #TEXTから起動と終了の最新データの日付を取得
    with codecs.open(sys.argv[1], "r", "sjis") as f:
        logs = f.readlines()
    
    #TEXTの整形
        del logs[0:15]

    poweron = logs[18]
    poweronDate = re.search("[0-9]{4}\-[0-9]{2}\-[0-9]{2}", poweron)
    #年-月-日
    poweronDate = poweronDate.group()
    poweronTime = re.search("[0-9]{2}\:[0-9]{2}\:[0-9]{2}", poweron)
    #時:分:秒
    poweronTime = poweronTime.group()
    poweroff = logs[3]
    poweroffDate = re.search("[0-9]{4}\-[0-9]{2}\-[0-9]{2}", poweroff)
    #年-月-日
    poweroffDate = poweroffDate.group()
    poweroffTime = re.search("[0-9]{2}\:[0-9]{2}\:[0-9]{2}", poweroff)
    #時:分:秒
    poweroffTime = poweroffTime.group()

    #Excelのデータを準備
    poweronDateYear = int(poweronDate[0:4])
    poweronDateMonth = int(poweronDate[5:7])
    poweronDateDay = int(poweronDate[8:10])
    poweroffDateYear = int(poweroffDate[0:4])
    poweroffDateMonth = int(poweroffDate[5:7])
    poweroffDateDay = int(poweroffDate[8:10])
    poweronTimeHour = int(poweronTime[0:2])
    poweronTimeMinute = int(poweronTime[3:5])
    poweronTimeSecond = int(poweronTime[6:8])
    poweroffTimeHour = int(poweroffTime[0:2])
    poweroffTimeMinute = int(poweroffTime[3:5])
    poweroffTimeSecond = int(poweroffTime[6:8])

    poweronDatetime = datetime.datetime(year=poweronDateYear, month=poweronDateMonth, day=poweronDateDay, hour=poweronTimeHour, minute=poweronTimeMinute, second=poweronTimeSecond)
    poweroffDatetime = datetime.datetime(year=poweroffDateYear, month=poweroffDateMonth, day=poweroffDateDay, hour=poweroffTimeHour, minute=poweroffTimeMinute, second=poweroffTimeSecond)
    #勤務時間
    myWorkingTime = poweroffDatetime - poweronDatetime

    #エクセルへ記入(新規作成 or 追記)
    argvName = sys.argv[1]

    if not os.path.isfile("../My_Working_Time.xlsx"):

        df_exclf =pd.DataFrame([[poweronDate + "/" + poweronTime, poweroffDate + "/" + poweroffTime, str(myWorkingTime)]], index=[argvName[8:31]], columns=["Start-up", "Shutdown", "Working time"]) 
        df_exclf.to_excel("../My_Working_Time.xlsx", sheet_name="Time Data")
    else:
        df_exclf = pd.read_excel("../My_Working_Time.xlsx", index_col=0)
        df_exclf2 =pd.DataFrame([[poweronDate + "/" + poweronTime, poweroffDate + "/" + poweroffTime, str(myWorkingTime)]], index=[argvName[8:31]], columns=["Start-up", "Shutdown", "Working time"]) 
        df_exclf = pd.concat([df_exclf, df_exclf2])
        df_exclf.to_excel("../My_Working_Time.xlsx", sheet_name="Time Data")

    #整形したテキストログを保存
    with codecs.open(sys.argv[1], "w", "utf-8") as f2:
        for log in logs:
            f2.write(log)

if __name__ == "__main__":
    main()