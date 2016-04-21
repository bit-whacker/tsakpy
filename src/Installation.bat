@echo off
REM Batch command to easily invoke the pip install function.
REM User can quickly install the required python module 
REM Runs on Windows


:start
cls
echo.
echo.
echo Installing required packages
echo ============================
echo Installing Tweepy
pip install tweepy
echo ============================
echo Installing TextBlob
pip install textblob
echo ============================
echo Installing pattern
pip install pattern
echo ============================
echo Installing SpaCy
python -m spacy.en.download all
echo ============================


pause
exit