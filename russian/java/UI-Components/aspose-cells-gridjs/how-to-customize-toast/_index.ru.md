---
title: как настроить внешний вид UI для подсказки сообщения toast в GridJs  
type: docs
weight: 250
url: /ru/java/aspose-cells-gridjs/how-to-customize-toast/
description: В этой статье описывается, как настраивать внешний вид UI для toast сообщений в GridJs.
keywords: GridJs,настройка,toast,UI,внешний вид,визуальный,сообщение,оповещение
aliases:
aliases:
  - /java/aspose-cells-gridjs/customize-toast/
  - /java/aspose-cells-gridjs/customize-ui-alert/
  - /java/aspose-cells-gridjs/customize-message-tips/
  - /java/aspose-cells-gridjs/customize-notification/
  - /java/aspose-cells-gridjs/customize-popup-message/
  - /java/aspose-cells-gridjs/customize-ui-message/
  - /java/aspose-cells-gridjs/customize-toast-styling/
  - /java/aspose-cells-gridjs/customize-toast-theme/
  - /java/aspose-cells-gridjs/customize-message/




---

# Руководство по пользовательским Toast для GridJs

## Обзор

GridJs предоставляет гибкую систему пользовательских уведомлений toast, которая позволяет заменять стандартные сообщения toast на собственные реализации уведомлений. Это руководство демонстрирует различные подходы к настройке уведомлений toast в соответствии с требованиями вашего приложения.

## Оглавление

- [Основное использование](#basic-usage)
- [Примеры интеграции](#integration-examples)
  - [Красивый пользовательский toast](#1-beautiful-custom-toast)
  - [Библиотека Toastr](#2-toastr-library-integration)
  - [SweetAlert2](#3-sweetalert2-integration)
  - [Vue + Element UI](#4-vue--element-ui)
  - [React + Ant Design](#5-react--ant-design)
- [Расширенные случаи использования](#advanced-use-cases)
  - [Логирование и аналитика](#6-logging-and-analytics)
  - [Мобильно-дружелюбный тост](#7-mobile-friendly-toast)
- [Референс API](#api-reference)
- [Лучшие практики](#best-practices)

---

## Basic Usage

### Simple Alert Example

The most basic custom toast can be implemented using the native `alert()` function:

```javascript
const xs = x_spreadsheet('#spreadsheet');

// Define custom toast function
function myToast(title, content, callback) {
  alert(`${title}: ${content}`);
  if (callback) callback();
}

// Set custom toast
xs.customToast(myToast);
```

**Параметры:**
- `title` (строка): Заголовок уведомления-тоста
- `content` (строка): Содержание сообщения тоста
- `callback` (функция, необязательно): функция обратного вызова для выполнения после закрытия тоста

---

## Integration Examples

### 1. Beautiful Custom Toast

Create a visually appealing toast notification without external dependencies:

```javascript
function beautifulToast(title, content, callback) {
  // Create dimmer overlay
  const dimmer = document.createElement('div');
  Object.assign(dimmer.style, {
    position: 'fixed',
    top: 0, left: 0, right: 0, bottom: 0,
    background: 'rgba(0,0,0,0.5)',
    zIndex: 9999
  });

  // Create toast element
  const toast = document.createElement('div');
  Object.assign(toast.style, {
    position: 'fixed',
    top: '50%', left: '50%',
    transform: 'translate(-50%, -50%)',
    background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
    color: 'white',
    padding: '20px 30px',
    borderRadius: '10px',
    boxShadow: '0 10px 40px rgba(0,0,0,0.3)',
    zIndex: 10000,
    minWidth: '300px'
  });

  toast.innerHTML = `
    <div style="display: flex; justify-content: space-between; margin-bottom: 10px; font-weight: bold;">
      <span>${title}</span>
      <span class="close" style="cursor: pointer;">×</span>
    </div>
    <div>${content}</div>
  `;

  const remove = () => {
    document.body.removeChild(toast);
    document.body.removeChild(dimmer);
    if (callback) callback();
  };

  toast.querySelector('.close').onclick = remove;
  dimmer.onclick = remove;

  document.body.appendChild(dimmer);
  document.body.appendChild(toast);

  // Auto-dismiss after 3 seconds
  setTimeout(remove, 3000);
}

xs.customToast(beautifulToast);
```

**Особенности:**
- Градиентный фон
- Модальный слой
- Нажатие для закрытия
- Автоматическое закрытие через 3 секунды
- Кнопка закрытия

---

### 2. Toastr Library Integration

Integrate the popular [Toastr](https://github.com/CodeSeven/toastr) library for toast notifications.

**Prerequisites:**
```html
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/toastr.js/latest/toastr.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/toastr.js/latest/toastr.min.js"></script>
```

**Реализация:**
```javascript
xs.customToast((title, content, callback) => {
  toastr.options = {
    closeButton: true,
    progressBar: true,
    positionClass: 'toast-top-right',
    timeOut: 3000
  };
  toastr.info(content, title);
  if (callback) callback();
});
```

**Настройки кастомизации:**
- `closeButton`: отображает кнопку закрытия
- `progressBar`: отображает прогресс-бар таймера
- `positionClass`: управляет положением тоста (верхний правый, нижний левый и т. д.)
- `timeOut`: время автоматического закрытия в миллисекундах

---

### 3. SweetAlert2 Integration

Use [SweetAlert2](https://sweetalert2.github.io/) for beautiful, customizable alert dialogs.

**Prerequisites:**
```html
<script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
```

**Реализация:**
```javascript
xs.customToast((title, content, callback) => {
  Swal.fire({
    title: title,
    html: content,
    icon: 'info',
    confirmButtonText: 'OK'
  }).then(() => {
    if (callback) callback();
  });
});
```

**Доступные иконки:**
- `успех`
- `ошибка`
- `предупреждение`
- `информация`
- `вопрос`

---

### 4. Vue + Element UI

Integration with Vue.js and Element UI's notification component.

```javascript
new Vue({
  el: '#app',
  mounted() {
    const xs = x_spreadsheet('#spreadsheet');

    xs.customToast((title, content, callback) => {
      this.$notify({
        title: title,
        message: content,
        type: 'info',
        duration: 3000,
        onClose: callback
      });
    });
  }
});
```

**Типы уведомлений:**
- `успех`
- `предупреждение`
- `информация`
- `ошибка`

---

### 5. React + Ant Design

Integration with React and Ant Design's message component.

```javascript
import { message } from 'antd';

const App = () => {
  useEffect(() => {
    const xs = x_spreadsheet('#spreadsheet');

    xs.customToast((title, content, callback) => {
      message.info({
        content: `${title}: ${content}`,
        duration: 3,
        onClose: callback
      });
    });
  }, []);

  return <div id="spreadsheet"></div>;
};
```

**Альтернативные компоненты Ant Design:**
- `message.success()`
- `message.error()`
- `message.warning()`
- `notification.open()` (для более сложных уведомлений)

---

## Advanced Use Cases

### 6. Logging and Analytics

Combine custom toast with logging and analytics tracking:

```javascript
xs.customToast((title, content, callback) => {
  // Log to console
  console.log(`[Toast] ${title}:`, content);

  // Track in analytics system
  if (window.analytics) {
    analytics.track('toast_shown', {
      title: title,
      content: content,
      timestamp: new Date().toISOString()
    });
  }

  // Display custom notification
  showMyCustomToast(title, content, callback);
});
```

**Использование:**
- Отладочное логирование
- Отслеживание поведения пользователя
- Мониторинг ошибок
- Метрики производительности

---

### 7. Mobile-Friendly Toast

Create a mobile-optimized toast notification:

```javascript
function mobileToast(title, content, callback) {
  const toast = document.createElement('div');
  Object.assign(toast.style, {
    position: 'fixed',
    bottom: '20px',
    left: '50%',
    transform: 'translateX(-50%)',
    background: '#323232',
    color: 'white',
    padding: '12px 24px',
    borderRadius: '24px',
    fontSize: '14px',
    zIndex: 10000,
    maxWidth: '80%',
    textAlign: 'center',
    boxShadow: '0 4px 12px rgba(0,0,0,0.3)'
  });

  toast.textContent = `${title}: ${content}`;
  document.body.appendChild(toast);

  setTimeout(() => {
    document.body.removeChild(toast);
    if (callback) callback();
  }, 2000);
}

xs.customToast(mobileToast);
```

**Функции оптимизации для мобильных устройств:**
- Расположение в нижней части (удобно для большего пальца)
- Ширина на основе процентного отношения (максимум 80%)
- Краткое время отображения (2 секунды)
- Большие области для нажимания
- Без всплывающего слоя (не блокирующее)

---

## API Reference

### `customToast(toastFunction)`

Sets a custom toast notification function for the spreadsheet instance.

**Parameters:**
- `toastFunction` (Function | null): Custom toast function with signature `(title, content, callback) => void`
  - Pass `null` to restore default toast behavior

**Returns:**
- The spreadsheet instance (for method chaining)

**Example:**
```javascript
// Set custom toast
xs.customToast(myToastFunction);

// Restore default
xs.customToast(null);

// Method chaining
xs.customToast(myToast)
  .loadData(data)
  .setActiveSheet(0);
```

---

## Best Practices

### 1. Always Handle the Callback

Ensure you call the callback function if provided, as it may contain important cleanup or continuation logic:

```javascript
function myToast(title, content, callback) {
  // ... show toast ...
  if (callback) callback();  // ✅ Always call
}
```

### 2. Не блокирующие уведомления

Для улучшения пользовательского опыта используйте ненавязчивые уведомления toast вместо модальных окон:

```javascript
// ❌ Blocks user interaction
alert(`${title}: ${content}`);

// ✅ Non-blocking
showToastNotification(title, content);
```

### 3. Подходящая длительность

Выбирайте соответствующую автоматическую продолжительность в зависимости от длины содержимого:

```javascript
const duration = content.length > 50 ? 5000 : 3000;
setTimeout(remove, duration);
```

### 4. Доступность

Обеспечьте доступность вашего пользовательского toast:

```javascript
toast.setAttribute('role', 'alert');
toast.setAttribute('aria-live', 'polite');
toast.setAttribute('aria-atomic', 'true');
```

### 5. Обработка ошибок

Оборачивайте функцию toast в try-catch, чтобы избежать поломки таблицы:

```javascript
xs.customToast((title, content, callback) => {
  try {
    // Your toast implementation
    myCustomToast(title, content);
  } catch (error) {
    console.error('Toast error:', error);
  } finally {
    if (callback) callback();
  }
});
```

### 6. Очистка ресурсов

Всегда очищайте элементы DOM и слушатели событий:

```javascript
function myToast(title, content, callback) {
  const toast = document.createElement('div');
  // ... setup toast ...

  const remove = () => {
    document.body.removeChild(toast);
    // Clean up any event listeners
    toast.onclick = null;
    if (callback) callback();
  };

  document.body.appendChild(toast);
  setTimeout(remove, 3000);
}
```

### 7. Восстановление по умолчанию при необходимости

Предоставьте возможность восстановить поведение всплывающего сообщения по умолчанию:

```javascript
// Set custom toast
xs.customToast(myToast);

// Later, restore default
xs.customToast(null);
```

---

## Troubleshooting

### Toast Not Showing

**Problem:** Custom toast function is called but nothing appears.

**Solutions:**
1. Check z-index values (ensure they're higher than spreadsheet elements)
2. Verify the toast element is appended to `document.body`
3. Check browser console for JavaScript errors

### Callback Not Working

**Problem:** Operations after toast don't execute.

**Solution:** Ensure you're calling the callback function:
```javascript
if (callback) callback();  // Don't forget this!
```

### Утечки памяти

**Проблема:** Страница становится медленной после большого количества уведомлений toast.

**Решение:** Очистите DOM-элементы и слушатели событий:
```javascript
const remove = () => {
  document.body.removeChild(toast);
  toast.onclick = null;  // Remove event listeners
  if (callback) callback();
};
```

### Проблемы отображения на мобильных устройствах

**Проблема:** Тост выглядит плохо на мобильных устройствах.

**Решения:**
1. Используйте ширину в процентах: `maxWidth: '80%'`
2. Add viewport meta tag: `<meta name="viewport" content="width=device-width, initial-scale=1">`
3. Используйте относительные размеры шрифта: `fontSize: '14px'` вместо фиксированных пикселей

---



