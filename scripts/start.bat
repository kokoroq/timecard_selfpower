@echo off

rem �o�b�`�t�@�C���̏�w�̃f�B���N�g���Ɉړ�
cd /d %~dp0..

rem ���O�i�[�f�B���N�g�����Ȃ��ꍇ
if not exist .\logs\ mkdir logs

rem �ŐV�́u6005�v�Ɓu6006�v���Ď擾���Adate_timelog.txt�Ƃ���logs�f�B���N�g���ɕۑ�����B
set yyyy=%date:~0,4%
set mm=%date:~5,2%
set dd=%date:~8,2%

set timepz=%time: =0%
set hh=%timepz:~0,2%
set mm2=%timepz:~3,2%
set ss=%timepz:~6,2%

set today=%yyyy%%mm%%dd%_%hh%%mm2%%ss%

wevtutil qe System /c:3 /f:Text /rd:true "/q:*[System[(EventID=6005 or EventID=6006)]]" > .\logs\%today%_timelog.txt

rem �o�b�`�t�@�C���Ɠ����f�B���N�g���Ɉړ�
cd /d %~dp0

rem CSV��timelog.xlsx�Ƀ}�[�W����B&�e�L�X�g���O�̗]�v�ȕ������폜����B
python convert.py ../logs/%today%_timelog.txt