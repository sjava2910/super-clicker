@echo off
set /p GITHUB_TOKEN="Введите ваш GitHub токен: "
set /p REPO_NAME="Введите имя репозитория (по умолчанию super-clicker): "

if "%REPO_NAME%"=="" set REPO_NAME=super-clicker

echo Создание репозитория %REPO_NAME%...

curl -X POST \
  -H "Authorization: token %GITHUB_TOKEN%" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/user/repos \
  -d "{ \"name\": \"%REPO_NAME%\", \"private\": false, \"auto_init\": true, \"description\": \"Увлекательная игра-кликер с красивым дизайном и возможностью запуска через Telegram Web App\" }"

echo.
echo Репозиторий создан! Теперь настройте локальный репозиторий...
cd /d "C:\Users\Дмитрий\Desktop\кликер"

if exist .git (
  echo Удаление существующего .git...
  rmdir /s /q .git
)

git init
git add .
git commit -m "Initial commit: Super Clicker game with Telegram integration"
git remote add origin https://github.com/%USERNAME%/%REPO_NAME%.git
git branch -M main
git push -u origin main

echo.
echo Готово! Репозиторий создан и файлы загружены.
pause