import os
import subprocess
import requests
import json

def create_github_repo(token, repo_name="super-clicker", description="Увлекательная игра-кликер с красивым дизайном и возможностью запуска через Telegram Web App"):
    """Создает репозиторий на GitHub с помощью API"""
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    data = {
        "name": repo_name,
        "private": False,
        "auto_init": True,
        "description": description
    }
    
    response = requests.post(
        "https://api.github.com/user/repos",
        headers=headers,
        json=data
    )
    
    if response.status_code == 201:
        print(f"Репозиторий {repo_name} успешно создан!")
        repo_info = response.json()
        return repo_info['clone_url']
    else:
        print(f"Ошибка при создании репозитория: {response.status_code}")
        print(response.text)
        return None

def setup_git_remote(clone_url):
    """Настраивает удаленный репозиторий и загружает файлы"""
    
    try:
        # Устанавливаем конфигурацию git
        subprocess.run(["git", "config", "user.name", "OpenClaw"], check=True, cwd=r"C:\Users\Дмитрий\Desktop\кликер")
        subprocess.run(["git", "config", "user.email", "openclaw@example.com"], check=True, cwd=r"C:\Users\Дмитрий\Desktop\кликер")
        
        # Добавляем удаленный репозиторий
        subprocess.run(["git", "remote", "add", "origin", clone_url], check=True, cwd=r"C:\Users\Дмитрий\Desktop\кликер")
        
        # Загружаем файлы
        subprocess.run(["git", "branch", "-M", "main"], check=True, cwd=r"C:\Users\Дмитрий\Desktop\кликер")
        subprocess.run(["git", "push", "-u", "origin", "main"], check=True, cwd=r"C:\Users\Дмитрий\Desktop\кликер")
        
        print("Файлы успешно загружены в репозиторий!")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при работе с git: {e}")
        return False

def main():
    token = "YOUR_GITHUB_TOKEN_HERE"  # Ваш токен
    
    # Создаем репозиторий
    clone_url = create_github_repo(token)
    
    if clone_url:
        print(f"Клонирование по адресу: {clone_url}")
        
        # Настройка и загрузка файлов
        if setup_git_remote(clone_url):
            print(f"\nГотово! Ваш репозиторий доступен по адресу: {clone_url.replace('.git', '')}")
        else:
            print("Не удалось загрузить файлы в репозиторий")

if __name__ == "__main__":
    main()