@echo off
chcp 65001 >nul
echo ============================================
echo  에어비앤비 스크래퍼 실행
echo ============================================
echo.

:: Python 확인
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [오류] Python이 설치되지 않았습니다.
    echo  https://python.org 에서 Python 3.10 이상 설치 후 다시 실행하세요.
    pause
    exit /b 1
)

:: 패키지 설치 확인 및 자동 설치
echo [1/3] 필요 패키지 확인 중...
pip show playwright >nul 2>&1 || pip install playwright
pip show openpyxl >nul 2>&1 || pip install openpyxl
pip show pandas >nul 2>&1 || pip install pandas

:: Playwright 브라우저 설치
echo [2/3] 브라우저 준비 중...
playwright install chromium >nul 2>&1
if %errorlevel% neq 0 (
    python -m playwright install chromium
)

:: 스크래퍼 실행
echo [3/3] 스크래퍼 실행 중...
echo.
python "%~dp0airbnb_scraper.py"

echo.
echo 완료되었습니다. 아무 키나 누르면 닫힙니다.
pause >nul
