---
title: Форматирование ячейки Excel
linktitle: Форматирование ячейки
type: docs
weight: 40
url: /ru/nodejs-cpp/mcp/cell-formatting
keywords: "Форматирование ячейки Excel, стили ячеек Excel, границы Excel, выравнивание Excel, фоновые цвета Excel, автоматизация форматирования Excel с AI"
description: "Форматирование ячейки Excel  применение фонов, границ, выравнивания, числовых форматов и стилей ячеек с помощью автоматизации AI"
---

# Форматирование ячеек Excel

Применяйте профессиональное **форматирование ячеек Excel** с помощью автоматизации на базе AI. Стиль **ячеек Excel** с фонами, границами, выравниванием, числовыми форматами и расширенными свойствами ячеек.

## Доступные инструменты

- `cell_format` - **Форматирование ячеек Excel** (фон, границы, выравнивание, числовой формат) через **Excel MCP**
- `cell_format_batch` - массовое применение **форматирования ячеек Excel** с помощью **AI автоматизации**

## Форматирование одной ячейки

### Базовое оформление ячейки
```json
{
  "tool": "cell_format",
  "parameters": {
    "filepath": "reports/formatted-report.xlsx",
    "sheet_name": "Data",
    "range": "A1:F1",
    "background_color": "#4472C4",
    "horizontal_align": "center",
    "vertical_align": "middle",
    "border_style": "thick",
    "text_wrap": true
  }
}
```

### Профессиональное оформление заголовка
```json
{
  "tool": "cell_format",
  "parameters": {
    "filepath": "reports/sales-report.xlsx",
    "sheet_name": "Sales Data",
    "range": "A1:F1",
    "background_color": "#2E5984",
    "horizontal_align": "center",
    "vertical_align": "middle",
    "border_style": "thick",
    "border_color": "#000000",
    "text_wrap": true
  }
}
```

### Форматирование чисел
```json
{
  "tool": "cell_format",
  "parameters": {
    "filepath": "reports/financial.xlsx",
    "sheet_name": "Budget",
    "range": "C2:C10",
    "number_format": "$#,##0.00",
    "horizontal_align": "right"
  }
}
```

## Массовое форматирование ячеек

### Полное оформление отчета
```json
{
  "tool": "cell_format_batch",
  "parameters": {
    "filepath": "reports/financial-report.xlsx",
    "sheet_name": "Sheet1",
    "format_ranges": [
      {
        "range": "A1:F1",
        "background_color": "#2E5984",
        "horizontal_align": "center",
        "vertical_align": "middle",
        "border_style": "thick",
        "border_color": "#000000"
      },
      {
        "range": "B2:B4",
        "number_format": "$#,##0.00",
        "horizontal_align": "right"
      },
      {
        "range": "C2:C4",
        "number_format": "0",
        "horizontal_align": "center"
      },
      {
        "range": "D2:F5",
        "number_format": "$#,##0.00",
        "horizontal_align": "right"
      },
      {
        "range": "A5:F5",
        "border_style": "thick",
        "border_sides": ["top"]
      }
    ]
  }
}
```

### Расширенные стили границ
```json
{
  "tool": "cell_format_batch",
  "parameters": {
    "filepath": "reports/border-demo.xlsx",
    "sheet_name": "Sheet1",
    "format_ranges": [
      {
        "range": "A5:A7",
        "border_style": "thin",
        "border_color": "#000000",
        "border_sides": ["all"]
      },
      {
        "range": "B5:B7",
        "border_style": "medium",
        "border_color": "#FF0000",
        "border_sides": ["outline"]
      },
      {
        "range": "C5:C7",
        "border_style": "dashed",
        "border_color": "#0000FF",
        "border_sides": ["top", "bottom"]
      },
      {
        "range": "D5:D7",
        "border_style": "dotted",
        "border_color": "#00FF00",
        "border_sides": ["left", "right"]
      },
      {
        "range": "E5:E7",
        "border_style": "double",
        "border_color": "#FF00FF",
        "border_sides": ["all"]
      }
    ]
  }
}
```

### Демонстрация выравнивания текста
```json
{
  "tool": "cell_format_batch",
  "parameters": {
    "filepath": "reports/alignment-demo.xlsx",
    "sheet_name": "Sheet1",
    "format_ranges": [
      {
        "range": "A10",
        "horizontal_align": "left",
        "vertical_align": "top",
        "background_color": "#FFE6E6"
      },
      {
        "range": "B10",
        "horizontal_align": "center",
        "vertical_align": "middle",
        "background_color": "#E6FFE6"
      },
      {
        "range": "C10",
        "horizontal_align": "right",
        "vertical_align": "bottom",
        "background_color": "#E6E6FF"
      },
      {
        "range": "D10",
        "horizontal_align": "justify",
        "vertical_align": "justify",
        "text_wrap": true,
        "background_color": "#FFFFE6"
      },
      {
        "range": "E10",
        "horizontal_align": "fill",
        "indent": 2,
        "background_color": "#FFE6FF"
      }
    ]
  }
}
```

### Эффекты вращения текста
```json
{
  "tool": "cell_format_batch",
  "parameters": {
    "filepath": "reports/rotation-demo.xlsx",
    "sheet_name": "Sheet1",
    "format_ranges": [
      {
        "range": "D1",
        "text_rotation": 45,
        "horizontal_align": "center",
        "vertical_align": "middle"
      },
      {
        "range": "E1",
        "text_rotation": -45,
        "horizontal_align": "center",
        "vertical_align": "middle"
      },
      {
        "range": "F1",
        "text_rotation": 90,
        "horizontal_align": "center",
        "vertical_align": "middle"
      }
    ]
  }
}
```

## Обзор параметров форматирования

### Цвета фона
- `"#FFFFFF"` - Белый
- `"#4472C4"` - Профессиональный синий
- `"#E6F3FF"` - Светло-голубой
- `"#FFFF00"` - Желтый
- `"#FFE6E6"` - Светло-красный
- `"#E6FFE6"` - Светло-зеленый
- `"#F0F8FF"` - Алиса голубой

### Горизонтальное выравнивание
- `"left"` - Выравнивание по левому краю
- `"center"` - Выравнивание по центру
- `"right"` - Выравнивание по правому краю
- `"justify"` - Выровнять по ширине
- `"fill"` - Заполнить ячейку

### Вертикальное выравнивание
- `"top"` - Выравнивание по верху
- `"middle"` - Выравнивание по центру
- `"bottom"` - Выравнивание по низу
- `"justify"` - Выравнивание по вертикали

### Стиль границы
- `"none"` - Без границы
- `"thin"` - Тонкая линия
- `"medium"` - Средняя линия
- `"thick"` - Толстая линия
- `"dashed"` - Пунктирная линия
- `"dotted"` - Точечная линия
- `"double"` - Двойная линия

### Стороны границы
- `["all"]` - Все стороны
- `["top", "bottom"]` - Верхняя и нижняя
- `["left", "right"]` - Левая и правая
- `["outline"]` - Только внешняя граница
- `["inside"]` - Только внутренняя граница

### Форматы чисел
- `"General"` - Общий формат
- `"0"` - Целое число
- `"0.00"` - Две десятичные дроби
- `"0%"` - Процент
- `"$#,##0.00"` - Валюта с разделителем тысяч
- `"yyyy-mm-dd"` - Формат даты
- `"h:mm AM/PM"` - Формат времени

### Свойства текста
- `text_wrap: true` - Перенос текста в ячейке
- `text_rotation: 45` - Поворот текста (градусы)
- `indent: 2` - Уровень отступа текста
- `locked: true` - Блокировка ячейки для защиты
- `hidden: true` - Скрытие формулы ячейки

## Примеры расширенного форматирования

### Стайлинг финансового отчета
```json
{
  "tool": "cell_format_batch",
  "parameters": {
    "filepath": "reports/financial-complete.xlsx",
    "sheet_name": "Sheet1",
    "format_ranges": [
      {
        "range": "D2:D5",
        "background_color": "#F0F8FF"
      },
      {
        "range": "E2:E5",
        "background_color": "#FFF0F0"
      },
      {
        "range": "F2:F5",
        "background_color": "#F0FFF0",
        "border_style": "double",
        "border_sides": ["all"]
      }
    ]
  }
}
```

### Выделение для проверки данных
```json
{
  "tool": "cell_format_batch",
  "parameters": {
    "filepath": "reports/data-validation.xlsx",
    "sheet_name": "Data",
    "format_ranges": [
      {
        "range": "A2:A10",
        "background_color": "#90EE90"
      },
      {
        "range": "B2:B10",
        "background_color": "#FFB6C1"
      },
      {
        "range": "C2:C10",
        "background_color": "#87CEEB",
        "border_style": "thin",
        "border_sides": ["all"]
      }
    ]
  }
}
```

### Настройки защиты
```json
{
  "tool": "cell_format",
  "parameters": {
    "filepath": "reports/protected.xlsx",
    "sheet_name": "Sheet1",
    "range": "B1:B5",
    "locked": false,
    "hidden": true
  }
}
```

## Лучшие практики

1. **Цветовая гармония**: Используйте комплементарные цвета для профессионального вида
2. **Контраст**: Обеспечьте читаемость текста на фоне
3. **Последовательность**: Применяйте согласованное форматирование к похожим данным
4. **Границы**: Используйте границы для разделения разделов и выделения важной информации
5. **Форматы чисел**: Применяйте соответствующие форматы чисел к типам данных

## Общие случаи использования

### Заголовки отчётов
- Темный фон с белым текстом
- Выравнивание по центру
- Толстые границы
- Включено перенос текста

### Финансовые данные
- Форматирование валюты
- Выравнивание по правому краю для чисел
- Выделение отрицательных значений
- Тысячные разделители

### Информационные индикаторы
- Цветовые фоны по коду
- Выравнивание по центру
- Жирные границы
- Четкое визуальное различие

### Таблицы данных
- Чередование цветов строк
- Постоянная ширина колонок
- Соответствующие форматы чисел
- Ясное оформление заголовков

## Обработка ошибок

### Недопустимый цветовой код
```json
{
  "tool": "cell_format",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "range": "A1",
    "background_color": "invalid-color"
  }
}
```
**Результат**: Использует цвет фона по умолчанию

### Недопустимый формат числа
```json
{
  "tool": "cell_format",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "range": "A1",
    "number_format": "invalid-format"
  }
}
```
**Результат**: Использует стандартный формат в качестве запасающего варианта 
{{< app/cells/assistant language="nodejs-cpp" >}}
