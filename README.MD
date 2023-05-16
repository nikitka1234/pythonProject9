# Новостной портал
Любой желающий может поделиться выдуманной новостью

## Описание
Проект для 4 модуля курса PythonPro от онлайн-школы Учи.Дома

## Технологии
- Python
- Flask
- Flask-WTF
- Flask-SQLAlchemy

## Установка проекта
1. склонировать репозиторий
```text
git clone [link]
```
2. Установка виртуального окружения внутри папки проекта. Запуск виртуального окружения
```commandline
python -m venv venv
Windows: venv\Scripts\activate
GitBash: source venv/Scripts/activate
Linux: source venv/bin/activate
```
3. Установка зависимостей
```commandline
pip install -r requirements.txt
```
4. Добавить файл .env
```text
nano .env

Содержимое файла:
    SECRET_KEY=SECRET_KEY
    DATABASE_URI=sqlite:///db.sqlite3
```
5. Запуск проекта
```commandline
flask --debug run
```