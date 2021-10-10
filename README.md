# timecard_selfpower for Windows
- 日々の勤務時間を記録するプログラムです。
- コンピューターのパワーオン/オフの時間を記録するため、稼働時間を確認する目的等にも使用できます。

- The program records your working time.
- It records power on/off times of your computer. For example, you can also use to find out operating hours.

## Start
- `scripts`ディレクトリにある`start.bat`を起動すると、初回は`scripts`ディレクトリと同じ階層に`logs`ディレクトリとその中に現在の詳細ログが生成されます。また、これまでのログをまとめた`My_Working_Time.xlsx`が`scripts`ディレクトリと同じ階層に生成されます。
- 2回目以降は、`start.bat`を起動すると`logs`ディレクトリに新たに詳細ログが生成され、`My_Working_Time.xlsx`にログが追記されます。

- When you run `start.bat` in the `scripts` directory for the first time, the program will generate `logs` directory in the previous hierarchy and the detailed log in it. and it will also generate `My_Working_Time.xlsx` that summarizes each log in the same hierarchy for the `scripts` directory.
- After the second time, the program will generate the current detailed log in `logs` directory and add the current time in `My_Working_Time.xlsx` when you run `start.bat`.

### Tree
.  
├─ scripts/  
│&nbsp;&emsp;├ convert.py  
│&nbsp;&emsp;└ start.bat  
│  
├─ logs/&emsp;&emsp;#Generate directory  
│&nbsp;&emsp;└YYYYMMDD_hhmmss_timelog.txt&emsp;&emsp;#Generate text file  
│  
├─ My_Working_Time.xlsx&emsp;&emsp;#Generate xlsx file  


## Tips
- タスクスケジューラに「ログオン時」でトリガーを指定して、`start.bat`を設定するとユーザー利用開始時に自動でログを取ることができます。

- You can automatically get log when the user logon with the Task Scheduler set `start.bat` as "at logon" trigger.
