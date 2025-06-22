
## 📘 Новый `README.md` для `Mind Garden UI`

````md
# 🌱 Mind Garden UI

Интерактивная мультиагентная сцена с подключением ИИ через OpenRouter.

---

## 🚀 Быстрый старт

1. **Установи зависимости:**

```bash
npm install
````

2. **Создай файл `.env` и добавь свой API-ключ:**

```env
VITE_OPENROUTER_API_KEY=your_openrouter_api_key
```

3. **Запусти приложение:**

```bash
npm run dev
```

Откроется по адресу: `http://localhost:5173`

---

## 🧠 Описание

* Каждый агент имеет **роль**, **настроение** и **поведение**
* Используется **LLM через OpenRouter** для генерации реплик
* Поддержка **реакций на другие реплики** и **паузы** между ответами
* Визуальное отображение сцены, таймлайн и консоль наставника

---

## 🌐 Подключаемые модели

Через OpenRouter можно использовать:

* `openchat/openchat-7b`
* `mistralai/mistral-7b-instruct`
* `nousresearch/nous-hermes-2`
* и многие другие

🔗 Зарегистрируйся и получи ключ: [https://openrouter.ai](https://openrouter.ai)

---

## 🛠 Структура проекта

```
src/
├── components/         # UI-компоненты
├── llm_agent.js        # Генерация реплик через API
├── App.jsx             # Основной интерфейс
public/
.env.example             # Пример файла переменных
README.md                # Этот файл
```

---

## ⚖️ Лицензия

MIT © Pavel Chumakov, 2025

---

## 🙌 Благодарности

* OpenRouter.ai за доступ к LLM
* Комьюнити OSS

```

---
