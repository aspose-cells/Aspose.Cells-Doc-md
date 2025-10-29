---
title: Шрифт Excel и форматирование текста
linktitle: Шрифт и форматирование текста
type: docs
weight: 30
url: /ru/nodejs-cpp/mcp/font-formatting
keywords: "Форматирование шрифта Excel, Форматирование текста Excel, Настройки шрифта Excel, Стиль шрифта AI Excel, Автоматизация шрифта Excel"
description: "Форматирование шрифта и текста Excel  применяйте стили шрифта, цвета, размеры и эффекты текста с помощью автоматизации AI"
---

# Форматирование шрифта и текста Excel

Применяйте профессиональное **форматирование шрифтов Excel** с помощью автоматизации на базе AI. Оформляйте **текст Excel** шрифтами, цветами, размерами и специальными эффектами для аккуратных таблиц.

## Доступные инструменты

- `font_settings` - **Настройка шрифтов Excel** (семейство, размер, жирный, курсив, цвет и др.) с точностью **AI Excel**
- `font_settings_batch` - Применяйте **настройки шрифтов Excel** к нескольким диапазонам пакетно с помощью **spreadsheet MCP**

## Операции с одним шрифтом

### Базовая стилизация шрифта
```json
{
  "tool": "font_settings",
  "parameters": {
    "filepath": "reports/styled-report.xlsx",
    "sheet_name": "Data",
    "range": "A1:F1",
    "font_name": "Arial",
    "font_size": 14,
    "bold": true,
    "font_color": "#FFFFFF"
  }
}
```

### Эффекты текста
```json
{
  "tool": "font_settings",
  "parameters": {
    "filepath": "reports/effects-demo.xlsx",
    "sheet_name": "Sheet1",
    "range": "A2",
    "italic": true,
    "underline": true,
    "strikethrough": true,
    "font_color": "#FF0000"
  }
}
```

### Специальные символы
```json
{
  "tool": "font_settings",
  "parameters": {
    "filepath": "reports/scientific.xlsx",
    "sheet_name": "Formulas",
    "range": "A3",
    "font_size": 10,
    "subscript": true
  }
}
```

## Пакетные операции с шрифтом

### Полное оформление заголовков
```json
{
  "tool": "font_settings_batch",
  "parameters": {
    "filepath": "reports/professional-report.xlsx",
    "sheet_name": "Summary Report",
    "font_ranges": [
      {
        "range": "C3:G3",
        "font_name": "Arial Black",
        "font_size": 16,
        "bold": true,
        "italic": true,
        "underline": true,
        "font_color": "#FF0000"
      },
      {
        "range": "D4:D6",
        "font_name": "Calibri",
        "font_size": 12,
        "bold": true,
        "font_color": "#0066CC"
      },
      {
        "range": "E4:E6",
        "font_name": "Times New Roman",
        "italic": true,
        "font_color": "#006600"
      }
    ]
  }
}
```

### Показ эффектов текста
```json
{
  "tool": "font_settings_batch",
  "parameters": {
    "filepath": "reports/text-effects.xlsx",
    "sheet_name": "Effects Demo",
    "font_ranges": [
      {
        "range": "A3",
        "font_size": 10,
        "subscript": true
      },
      {
        "range": "B3",
        "font_size": 10,
        "superscript": true
      },
      {
        "range": "C3",
        "strikethrough": true,
        "underline": true,
        "font_color": "#CC0000"
      }
    ]
  }
}
```

### Стиль профессиональных отчетов
```json
{
  "tool": "font_settings_batch",
  "parameters": {
    "filepath": "reports/financial-report.xlsx",
    "sheet_name": "Sheet1",
    "font_ranges": [
      {
        "range": "A1:F1",
        "font_name": "Arial",
        "font_size": 14,
        "bold": true,
        "font_color": "#FFFFFF"
      },
      {
        "range": "A5:F5",
        "bold": true,
        "font_size": 12
      },
      {
        "range": "F2:F5",
        "bold": true,
        "font_color": "#006600"
      }
    ]
  }
}
```

## Справочник по параметрам шрифта

### Семейства шрифтов
- `"Arial"` - Чистый, современный без засечек
- `"Calibri"` - Стандартный шрифт Microsoft Office
- `"Times New Roman"` - Традиционный шрифт с засечками
- `"Arial Black"` - Жирный дисплейный шрифт
- `"Courier New"` - Моноширинный шрифт

### Размеры шрифтов
- `8` - Очень маленький текст
- `10` - Маленький текст
- `11` - Размер по умолчанию
- `12` - Стандартный текст
- `14` - Большой текст
- `16` - Размер заголовка
- `18` - Большой заголовок

### Цвета шрифта (Коды Hex)
- `"#000000"` - Черный
- `"#FFFFFF"` - Белый
- `"#FF0000"` - Красный
- `"#0066CC"` - Синий
- `"#006600"` - Зеленый
- `"#FF6600"` - Оранжевый
- `"#800080"` - Фиолетовый

### Эффекты текста
- `bold: true` - Жирный текст
- `italic: true` - Курсивный текст
- `underline: true` - Подчеркнутый текст
- `strikethrough: true` - Текст с зачеркнутыми линиями
- `subscript: true` - Текст с нижним индексом (H₂O)
- `superscript: true` - Текст с верхним индексом (x²)

## Продвинутое оформление шрифтов

### Пример научной нотации
```json
{
  "tool": "font_settings_batch",
  "parameters": {
    "filepath": "reports/scientific.xlsx",
    "sheet_name": "Formulas",
    "font_ranges": [
      {
        "range": "A1",
        "font_name": "Times New Roman",
        "font_size": 12,
        "bold": true
      },
      {
        "range": "B1",
        "font_size": 10,
        "subscript": true
      },
      {
        "range": "C1",
        "font_size": 10,
        "superscript": true
      }
    ]
  }
}
```

### Цветовая кодировка данных
```json
{
  "tool": "font_settings_batch",
  "parameters": {
    "filepath": "reports/color-coded.xlsx",
    "sheet_name": "Status Report",
    "font_ranges": [
      {
        "range": "A2:A5",
        "font_color": "#008000",
        "bold": true
      },
      {
        "range": "B2:B5",
        "font_color": "#FF8C00",
        "italic": true
      },
      {
        "range": "C2:C5",
        "font_color": "#DC143C",
        "strikethrough": true
      }
    ]
  }
}
```

## Лучшие практики

1. **Последовательность**: Используйте однородные стили шрифтов во всех отчетах
2. **Иерархия**: Используйте размеры шрифтов для создания визуальной иерархии
3. **Читаемость**: Обеспечьте достаточный контраст между текстом и фоном
4. **Эффекты**: Используйте текстовые эффекты умеренно для выделения
5. **Профессионально**: Используйте стандартные офисные шрифты для отчетов

## Общие случаи использования

### Заголовки отчетов
- Жирный шрифт большего размера
- Контрастные цвета
- Профессиональные семейства шрифтов

### Акцентирование данных
- Жирный или курсив для важных значений
- Цветовая кодировка для индикаторов статуса
- Зачёркивание для устаревших данных

### Научные документы
- Индекс для химических формул
- Надстрочный индекс для математических выражений
- Моноширинный для кода или данных

## Обработка ошибок

### Недопустимая семейство шрифтов
```json
{
  "tool": "font_settings",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "range": "A1",
    "font_name": "NonExistentFont"
  }
}
```
**Результат**: Возврат к шрифту системы по умолчанию

### Недопустимый цветовой код
```json
{
  "tool": "font_settings",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "range": "A1",
    "font_color": "invalid-color"
  }
}
```
**Результат**: Использует черный цвет по умолчанию 
{{< app/cells/assistant language="nodejs-cpp" >}}
