---
title: как настроить внешний вид UI для модального окна в GridJs  
type: docs
weight: 250
url: /ru/net/aspose-cells-gridjs/how-to-customize-ui-window/
description: В этой статье описывается, как настроить внешний вид UI для модального окна в GridJs.
keywords: GridJs,настройка,модал,UI,внешний вид,визуальный,окно
aliases:
aliases:
  - /net/aspose-cells-gridjs/customize-appearence/
  - /net/aspose-cells-gridjs/customize-ui-window/
  - /net/aspose-cells-gridjs/customize-modal/
  - /net/aspose-cells-gridjs/customize-modal-window/
  - /net/aspose-cells-gridjs/customize-dialog/
  - /net/aspose-cells-gridjs/customize-popup/
  - /net/aspose-cells-gridjs/customize-modal-dialog/
  - /net/aspose-cells-gridjs/customize-modal-style/
  - /net/aspose-cells-gridjs/customize-modal-theme/
  - /net/aspose-cells-gridjs/customize-window-appearance/
  - /net/aspose-cells-gridjs/customize-dialog-appearance/
  - /net/aspose-cells-gridjs/customize-popup-window/
  - /net/aspose-cells-gridjs/customize-modal-ui/

---

# Руководство по стилизации модальных окон GridJs

## Оглавление

- [Обзор](#overview)
- [Имя CSS-класса](#css-class-naming)
- [Быстрый старт](#quick-start)
- [Красивые примеры стилей](#beautiful-style-examples)
- [Галерея тем](#theme-gallery)
- [Расширенные техники](#advanced-techniques)
- [Адаптивный дизайн](#responsive-design)
- [Лучшие практики](#best-practices)

---

## Overview

GridJs provides a powerful modal system with built-in support for custom styling. Each modal window has a unique `name` attribute that generates specific CSS classes, enabling isolated style customization without affecting other modals.

### Key Features

- ✅ **Isolated Styling** - Each modal has unique CSS classes
- ✅ **No Style Conflicts** - Styles only affect targeted modals
- ✅ **Easy Customization** - Simple CSS overrides
- ✅ **Theme Support** - Multiple themes per application

---

## Имя CSS-класса

### Доступные имена модальных окон

| Тип модального окна | Имя | CSS-класс |
|------------|------|-----------|
| Сортировка | `sort` | `.x-spreadsheet-modal-sort` |
| Валидация | `validation` | `.x-spreadsheet-modal-validation` |
| Поиск | `search` | `.x-spreadsheet-modal-search` |
| Управление | `control` | `.x-spreadsheet-modal-control` |
| Загрузка | `download` | `.x-spreadsheet-modal-download` |
| Электронная почта | `email` | `.x-spreadsheet-modal-email` |
| InputSuggest | `input-suggest` | `.x-spreadsheet-modal-input-suggest` |
| InsertURL | `insert-url` | `.x-spreadsheet-modal-insert-url` |
| Link | `link` | `.x-spreadsheet-modal-link` |
| Печать | `print` | `.x-spreadsheet-modal-print` |
| Поворот текста | `text-rotate` | `.x-spreadsheet-modal-text-rotate` |
| Валидация данных | `data-validation` | `.x-spreadsheet-modal-component-data-validation` |
| Больше форматов чисел | `more-number-formats` | `.x-spreadsheet-modal-more-number-formats` |
| Предупреждение валидации | `validation-alert` | `.x-spreadsheet-modal-validation-alert` |
| Вставка/Удаление | `insert-delete` | `.x-spreadsheet-modal-insert-delete` |



---

## Quick Start

### Basic Customization

```css
/* Target specific modal */
.x-spreadsheet-modal-search {
    border-radius: 12px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.12);
}

/* Customize header */
.x-spreadsheet-modal-search .x-spreadsheet-modal-header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 20px;
}

/* Style buttons */
.x-spreadsheet-modal-search .x-spreadsheet-buttons button:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}
```

---

## Beautiful Style Examples

### Example 1: Modern Gradient Theme 🎨

Perfect for contemporary applications with vibrant design.

```css
.x-spreadsheet-modal-search {
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 10px 40px rgba(102, 126, 234, 0.2);
    border: none;
}

.x-spreadsheet-modal-search .x-spreadsheet-modal-header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 24px;
    font-size: 18px;
    font-weight: 600;
}

.x-spreadsheet-modal-search .x-spreadsheet-modal-content {
    padding: 24px;
    background: #f8f9fa;
}

.x-spreadsheet-modal-search input[type="text"] {
    border: 2px solid #e0e0e0;
    border-radius: 8px;
    padding: 10px 14px;
    transition: all 0.3s ease;
}

.x-spreadsheet-modal-search input[type="text"]:focus {
    border-color: #667eea;
    box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    outline: none;
}

.x-spreadsheet-modal-search .x-spreadsheet-buttons button.primary {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border-radius: 8px;
    padding: 10px 24px;
    border: none;
}

.x-spreadsheet-modal-search .x-spreadsheet-buttons button.primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
}
```

### Пример 2: Минималистическая чистая тема 🤍

Идеально подходит для профессиональных и корпоративных приложений.

```css
.x-spreadsheet-modal-download {
    border-radius: 12px;
    box-shadow: 0 4px 24px rgba(0, 0, 0, 0.08);
    border: 1px solid #e5e7eb;
}

.x-spreadsheet-modal-download .x-spreadsheet-modal-header {
    background: white;
    color: #1f2937;
    padding: 20px 24px;
    border-bottom: 1px solid #e5e7eb;
    font-weight: 600;
}

.x-spreadsheet-modal-download input,
.x-spreadsheet-modal-download select {
    border: 1px solid #d1d5db;
    border-radius: 6px;
    padding: 10px 12px;
    transition: all 0.2s ease;
}

.x-spreadsheet-modal-download input:focus {
    border-color: #3b82f6;
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
    outline: none;
}

.x-spreadsheet-modal-download .x-spreadsheet-buttons button.primary {
    background: #3b82f6;
    color: white;
    border-radius: 6px;
    padding: 10px 20px;
    border: none;
}
```

### Пример 3: Тема тёмного режима 🌙

Отлично подходит для приложений с поддержкой тёмного режима.

```css
.x-spreadsheet-modal-print {
    background: #1f2937;
    border-radius: 12px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
    border: 1px solid #374151;
}

.x-spreadsheet-modal-print .x-spreadsheet-modal-header {
    background: #111827;
    color: #f9fafb;
    padding: 20px 24px;
    border-bottom: 1px solid #374151;
}

.x-spreadsheet-modal-print select,
.x-spreadsheet-modal-print input {
    background: #374151;
    border: 1px solid #4b5563;
    color: #f9fafb;
    border-radius: 6px;
    padding: 10px 12px;
}

.x-spreadsheet-modal-print select:focus {
    border-color: #60a5fa;
    background: #4b5563;
    outline: none;
}

.x-spreadsheet-modal-print .x-spreadsheet-buttons button.primary {
    background: #3b82f6;
    color: white;
    border-radius: 6px;
}
```

### Пример 4: Игривый цветной дизайн 🌈

Идеально подходит для креативных и веселых приложений.

```css
.x-spreadsheet-modal-link {
    border-radius: 20px;
    overflow: hidden;
    box-shadow: 0 12px 48px rgba(236, 72, 153, 0.2);
    border: 3px solid #ec4899;
}

.x-spreadsheet-modal-link .x-spreadsheet-modal-header {
    background: linear-gradient(135deg, #ec4899 0%, #8b5cf6 100%);
    color: white;
    padding: 24px;
    font-weight: 700;
}

.x-spreadsheet-modal-link input[type="text"] {
    border: 2px solid #f9a8d4;
    border-radius: 12px;
    padding: 12px 16px;
}

.x-spreadsheet-modal-link input[type="text"]:focus {
    border-color: #ec4899;
    box-shadow: 0 0 0 4px rgba(236, 72, 153, 0.1);
}

.x-spreadsheet-modal-link .x-spreadsheet-buttons button.primary {
    background: linear-gradient(135deg, #ec4899 0%, #8b5cf6 100%);
    color: white;
    border-radius: 12px;
    padding: 12px 28px;
}

.x-spreadsheet-modal-link .x-spreadsheet-buttons button.primary:hover {
    transform: translateY(-3px) scale(1.02);
    box-shadow: 0 8px 24px rgba(236, 72, 153, 0.4);
}
```

### Пример 5: Корпоративная профессиональная тема 💼

Подходит для бизнес-приложений и корпоративных решений.

```css
.x-spreadsheet-modal-sort {
    border-radius: 8px;
    box-shadow: 0 6px 28px rgba(0, 0, 0, 0.12);
    border: 1px solid #dee2e6;
}

.x-spreadsheet-modal-sort .x-spreadsheet-modal-header {
    background: linear-gradient(180deg, #ffffff 0%, #f8f9fa 100%);
    color: #212529;
    padding: 18px 24px;
    border-bottom: 2px solid #0066cc;
    font-weight: 600;
}

.x-spreadsheet-modal-sort select,
.x-spreadsheet-modal-sort input {
    border: 1px solid #ced4da;
    border-radius: 4px;
    padding: 10px 14px;
}

.x-spreadsheet-modal-sort select:focus {
    border-color: #0066cc;
    box-shadow: 0 0 0 3px rgba(0, 102, 204, 0.08);
}

.x-spreadsheet-modal-sort .x-spreadsheet-buttons button.primary {
    background: #0066cc;
    color: white;
    border-radius: 4px;
    padding: 10px 24px;
}

.x-spreadsheet-modal-sort .x-spreadsheet-buttons button.primary:hover {
    background: #0052a3;
}
```

---

## Theme Gallery

### Glass Morphism 🔮

```css
.x-spreadsheet-modal-component-data-validation {
    background: rgba(255, 255, 255, 0.7);
    backdrop-filter: blur(10px);
    border-radius: 20px;
    border: 1px solid rgba(255, 255, 255, 0.3);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
}

.x-spreadsheet-modal-component-data-validation .x-spreadsheet-modal-component-header {
    background: rgba(255, 255, 255, 0.5);
    backdrop-filter: blur(20px);
    border-bottom: 1px solid rgba(0, 0, 0, 0.1);
}
```

### Нейроморфизм 🎭

```css
.x-spreadsheet-modal-validation {
    background: #e0e5ec;
    border-radius: 20px;
    box-shadow: 
        9px 9px 16px rgba(163, 177, 198, 0.6),
        -9px -9px 16px rgba(255, 255, 255, 0.5);
    border: none;
}

.x-spreadsheet-modal-validation .x-spreadsheet-buttons button {
    background: #e0e5ec;
    border-radius: 12px;
    box-shadow: 
        5px 5px 10px rgba(163, 177, 198, 0.6),
        -5px -5px 10px rgba(255, 255, 255, 0.5);
}
```

### Материальный дизайн 📱

```css
.x-spreadsheet-modal-email {
    border-radius: 4px;
    box-shadow: 
        0 11px 15px -7px rgba(0,0,0,.2),
        0 24px 38px 3px rgba(0,0,0,.14);
}

.x-spreadsheet-modal-email .x-spreadsheet-modal-header {
    background: #6200ea;
    color: white;
    font-weight: 500;
    letter-spacing: 0.0125em;
}

.x-spreadsheet-modal-email .x-spreadsheet-buttons button {
    text-transform: uppercase;
    letter-spacing: 0.089em;
}
```

---

## Advanced Techniques

### Custom Dimmer Overlay

```css
.x-spreadsheet-dimmer.active {
    background: rgba(0, 0, 0, 0.5);
    backdrop-filter: blur(4px);
}

.x-spreadsheet-modal-component-mask-data-validation {
    background: rgba(99, 102, 241, 0.1);
    backdrop-filter: blur(8px);
}
```

### Пользовательский ползунок

```css
.x-spreadsheet-modal-content::-webkit-scrollbar {
    width: 8px;
}

.x-spreadsheet-modal-content::-webkit-scrollbar-thumb {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 10px;
}
```

### Интеграция Значков

```css
.x-spreadsheet-modal-search input[type="text"] {
    padding-left: 40px;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 24 24' fill='none' stroke='%23999' stroke-width='2'%3E%3Ccircle cx='11' cy='11' r='8'/%3E%3Cpath d='m21 21-4.35-4.35'/%3E%3C/svg%3E");
    background-repeat: no-repeat;
    background-position: 12px center;
}
```

---

## Responsive Design

### Mobile Optimization

```css
@media (max-width: 768px) {
    .x-spreadsheet-modal-search {
        width: 95% !important;
        margin: 0 auto;
    }

    .x-spreadsheet-modal-search .x-spreadsheet-modal-header {
        padding: 16px;
        font-size: 16px;
    }

    .x-spreadsheet-modal-search .x-spreadsheet-buttons {
        flex-direction: column;
    }

    .x-spreadsheet-modal-search .x-spreadsheet-buttons button {
        width: 100%;
        margin: 4px 0;
    }
}
```

### Регулировка планшета

```css
@media (min-width: 769px) and (max-width: 1024px) {
    .x-spreadsheet-modal-component-data-validation {
        width: 80% !important;
    }
}
```

---

## Best Practices

### 1. Use Specific Selectors

✅ **Good:**
```css
.x-spreadsheet-modal-search .x-spreadsheet-buttons button {
    /* Styles only affect search modal buttons */
}
```

❌ **Плохо:**
```css
.x-spreadsheet-modal button {
    /* Affects all modals */
}
```

### 2. Поддержание доступности

```css
.x-spreadsheet-modal-download .x-spreadsheet-buttons button:focus {
    outline: 2px solid #3b82f6;
    outline-offset: 2px;
}

.x-spreadsheet-modal-download input:focus {
    border-color: #3b82f6;
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}
```

### 3. Плавные переходы

```css
.x-spreadsheet-modal-sort {
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.x-spreadsheet-modal-sort .x-spreadsheet-buttons button {
    transition: background-color 0.2s ease,
                transform 0.2s ease,
                box-shadow 0.2s ease;
}
```

### 4. Последовательные интервалы

```css
.x-spreadsheet-modal-download .x-spreadsheet-modal-header {
    padding: 20px 24px; /* Consistent padding */
}

.x-spreadsheet-modal-download .x-spreadsheet-modal-content {
    padding: 24px; /* Matches header sides */
}

.x-spreadsheet-modal-download .x-spreadsheet-buttons {
    padding: 16px 24px; /* Consistent with header */
}
```

### 5. Тестирование темного режима

```css
@media (prefers-color-scheme: dark) {
    .x-spreadsheet-modal-search {
        background: #1f2937;
        color: #f9fafb;
    }

    .x-spreadsheet-modal-search input {
        background: #374151;
        color: #f9fafb;
        border-color: #4b5563;
    }
}
```

### 6. Оптимизация производительности

```css
/* Use transform instead of position changes */
.x-spreadsheet-modal-search .x-spreadsheet-buttons button:hover {
    transform: translateY(-2px); /* GPU accelerated */
    /* Avoid: top: -2px; */
}

/* Use will-change for animations */
.x-spreadsheet-modal-search {
    will-change: transform, opacity;
}
```

### 7. Поддержание визуальной иерархии

```css
/* Primary action stands out */
.x-spreadsheet-modal-sort .x-spreadsheet-buttons button.primary {
    background: #3b82f6;
    font-weight: 600;
}

/* Secondary actions are subtle */
.x-spreadsheet-modal-sort .x-spreadsheet-buttons button:not(.primary) {
    background: transparent;
    color: #6b7280;
}
```

---

## Complete Example: Search Modal Makeover

```css
/* Complete styling for search modal */
.x-spreadsheet-modal-search {
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
    border: none;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto;
}

.x-spreadsheet-modal-search .x-spreadsheet-modal-header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 24px;
    font-size: 18px;
    font-weight: 600;
}

.x-spreadsheet-modal-search .x-spreadsheet-modal-content {
    padding: 24px;
    background: #f8f9fa;
}

.x-spreadsheet-modal-search .x-spreadsheet-form-fields {
    background: white;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 16px;
}

.x-spreadsheet-modal-search label {
    color: #4b5563;
    font-size: 13px;
    font-weight: 500;
    margin-bottom: 8px;
    display: block;
}

.x-spreadsheet-modal-search input[type="text"] {
    width: 100%;
    border: 2px solid #e5e7eb;
    border-radius: 8px;
    padding: 10px 14px;
    font-size: 14px;
    transition: all 0.2s ease;
}

.x-spreadsheet-modal-search input[type="text"]:focus {
    border-color: #667eea;
    box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    outline: none;
}

.x-spreadsheet-modal-search .x-spreadsheet-buttons {
    display: flex;
    justify-content: flex-end;
    gap: 12px;
    padding-top: 20px;
}

.x-spreadsheet-modal-search .x-spreadsheet-buttons button {
    padding: 10px 20px;
    border-radius: 8px;
    font-weight: 500;
    font-size: 14px;
    border: none;
    cursor: pointer;
    transition: all 0.2s ease;
}

.x-spreadsheet-modal-search .x-spreadsheet-buttons button.primary {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
}

.x-spreadsheet-modal-search .x-spreadsheet-buttons button.primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
}

.x-spreadsheet-modal-search .x-spreadsheet-buttons button:not(.primary) {
    background: white;
    color: #667eea;
    border: 2px solid #667eea;
}

.x-spreadsheet-modal-search .x-spreadsheet-buttons button:not(.primary):hover {
    background: #f3f4f6;
}

/* Mobile responsive */
@media (max-width: 768px) {
    .x-spreadsheet-modal-search {
        width: 95% !important;
    }

    .x-spreadsheet-modal-search .x-spreadsheet-buttons {
        flex-direction: column;
    }

    .x-spreadsheet-modal-search .x-spreadsheet-buttons button {
        width: 100%;
    }
}
```

---

## Resources

- **Example File**: [`modal-custom-styles-example.css`](./modal-custom-styles-example.css)
- **Color Palettes**: [Coolors.co](https://coolors.co/)
- **Gradient Generator**: [CSS Gradient](https://cssgradient.io/)
- **Shadow Generator**: [Box Shadows](https://box-shadow.dev/)

---




