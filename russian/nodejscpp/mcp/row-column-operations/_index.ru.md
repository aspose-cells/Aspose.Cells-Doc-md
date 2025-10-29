---
title: Операции с строками и столбцами Excel
linktitle: Операции со строками и столбцами
type: docs
weight: 50
url: /ru/nodejs-cpp/mcp/row-column-operations
keywords: "Операции с строками и столбцами Excel, управление макетами Excel, вставка строк, удаление столбцов, изменение размера ячеек Excel"
description: "Операции со строками и столбцами Excel  вставка, удаление, изменение размера, скрытие/отображение строк и столбцов с помощью автоматизации ИИ"
---

# Операции со строками и столбцами Excel

Управляйте **операциями со строками и столбцами Excel** с помощью автоматизации на базе ИИ. Вставляйте, удаляйте, изменяйте размер, скрывайте/показывайте **строки** и **столбцы** Excel для идеального управления макетом таблицы.

## Доступные инструменты

- `row_column_operations` - **операции со строками/столбцами Excel** (вставка, удаление, изменение размера, скрытие/отображение) с **ИИ Excel**
- `row_column_operations_batch` - выполнение нескольких **операций со строками/столбцами Excel** пакетно с помощью **Excel MCP**

## Одиночные операции

### Вставка строк
```json
{
  "tool": "row_column_operations",
  "parameters": {
    "filepath": "reports/layout-test.xlsx",
    "sheet_name": "Data",
    "operation": "insert_rows",
    "rows": "5",
    "count": 2
  }
}
```

### Удаление столбцов
```json
{
  "tool": "row_column_operations",
  "parameters": {
    "filepath": "reports/cleanup.xlsx",
    "sheet_name": "Sheet1",
    "operation": "delete_columns",
    "columns": "C:D"
  }
}
```

### Установка высоты строки
```json
{
  "tool": "row_column_operations",
  "parameters": {
    "filepath": "reports/formatted.xlsx",
    "sheet_name": "Report",
    "operation": "set_row_height",
    "rows": "1",
    "height": 30
  }
}
```

### Установка ширины столбца
```json
{
  "tool": "row_column_operations",
  "parameters": {
    "filepath": "reports/formatted.xlsx",
    "sheet_name": "Report",
    "operation": "set_column_width",
    "columns": "A:F",
    "width": 15
  }
}
```

## Групповые операции

### Комплексная настройка макета
```json
{
  "tool": "row_column_operations_batch",
  "parameters": {
    "filepath": "reports/professional-layout.xlsx",
    "sheet_name": "Summary Report",
    "operations": [
      {
        "operation": "set_row_height",
        "rows": "3",
        "height": 30
      },
      {
        "operation": "set_row_height",
        "rows": "4:6",
        "height": 20
      },
      {
        "operation": "set_column_width",
        "columns": "C",
        "width": 20
      },
      {
        "operation": "set_column_width",
        "columns": "D:G",
        "width": 15
      },
      {
        "operation": "auto_fit_rows",
        "rows": "7:10"
      }
    ]
  }
}
```

### Вставка и удаление операций
```json
{
  "tool": "row_column_operations_batch",
  "parameters": {
    "filepath": "reports/restructure.xlsx",
    "sheet_name": "Sheet1",
    "operations": [
      {
        "operation": "insert_rows",
        "rows": "5",
        "count": 2
      },
      {
        "operation": "insert_columns",
        "columns": "D",
        "count": 1
      },
      {
        "operation": "delete_rows",
        "rows": "8:9"
      }
    ]
  }
}
```

### Операции скрытия и отмены скрытия
```json
{
  "tool": "row_column_operations_batch",
  "parameters": {
    "filepath": "reports/visibility.xlsx",
    "sheet_name": "Sheet1",
    "operations": [
      {
        "operation": "hide_rows",
        "rows": "15:16"
      },
      {
        "operation": "hide_columns",
        "columns": "H:I"
      },
      {
        "operation": "unhide_rows",
        "rows": "15"
      },
      {
        "operation": "unhide_columns",
        "columns": "H"
      }
    ]
  }
}
```

### Операции автоматической подгонки
```json
{
  "tool": "row_column_operations_batch",
  "parameters": {
    "filepath": "reports/auto-sized.xlsx",
    "sheet_name": "Data",
    "operations": [
      {
        "operation": "auto_fit_columns",
        "columns": "A:F"
      },
      {
        "operation": "auto_fit_rows",
        "rows": "1:20"
      }
    ]
  }
}
```

## Справочник типов операций

### Вставка операций
- `insert_rows` - Вставить новые строки в указанном положении
- `insert_columns` - Вставить новые столбцы в указанном положении

### Удаление операций  
- `delete_rows` - Удалить указанные строки
- `delete_columns` - Удалить указанные столбцы

### Операции изменения размера
- `set_row_height` - Установить высоту строки в пунктах
- `set_column_width` - Установить ширину столбца в символах
- `auto_fit_rows` - Автоматическая подгонка высоты строк по содержимому
- `auto_fit_columns` - Автоматическая подгонка ширины столбцов по содержимому

### Операции видимости
- `hide_rows` - Скрыть указанные строки
- `unhide_rows` - Показать скрытые строки
- `hide_columns` - Скрыть указанные столбцы
- `unhide_columns` - Показать скрытые столбцы

## Спецификации диапазонов

### Диапазоны строк
- `"1"` - Одна строка (строка 1)
- `"1:3"` - Диапазон строк (строки 1-3)
- `"5:10"` - Несколько последовательных строк

### Диапазоны столбцов
- `"A"` - Один столбец (столбец A)
- `"A:C"` - Диапазон столбцов (столбцы A-C)
- `"D:F"` - Несколько последовательных столбцов

## Расширенные примеры

### Настройка заголовка отчета
```json
{
  "tool": "row_column_operations_batch",
  "parameters": {
    "filepath": "reports/header-setup.xlsx",
    "sheet_name": "Report",
    "operations": [
      {
        "operation": "set_row_height",
        "rows": "1:2",
        "height": 35
      },
      {
        "operation": "set_column_width",
        "columns": "A",
        "width": 25
      },
      {
        "operation": "set_column_width",
        "columns": "B:E",
        "width": 12
      },
      {
        "operation": "set_column_width",
        "columns": "F",
        "width": 18
      }
    ]
  }
}
```

### Макет таблицы данных
```json
{
  "tool": "row_column_operations_batch",
  "parameters": {
    "filepath": "reports/data-table.xlsx",
    "sheet_name": "Data",
    "operations": [
      {
        "operation": "insert_rows",
        "rows": "1",
        "count": 1
      },
      {
        "operation": "set_row_height",
        "rows": "1",
        "height": 25
      },
      {
        "operation": "auto_fit_columns",
        "columns": "A:J"
      },
      {
        "operation": "set_row_height",
        "rows": "2:100",
        "height": 18
      }
    ]
  }
}
```

### Макет презентации
```json
{
  "tool": "row_column_operations_batch",
  "parameters": {
    "filepath": "reports/presentation.xlsx",
    "sheet_name": "Summary",
    "operations": [
      {
        "operation": "hide_columns",
        "columns": "B:C"
      },
      {
        "operation": "hide_rows",
        "rows": "10:15"
      },
      {
        "operation": "set_column_width",
        "columns": "A",
        "width": 30
      },
      {
        "operation": "set_column_width",
        "columns": "D:G",
        "width": 15
      }
    ]
  }
}
```

## Руководство по измерениям

### Высота строк (по пунктам)
- `15` - Стандартная высота строки
- `20` - Немного выше для читаемости
- `25` - Хорошо для заголовков
- `30` - Большие заголовки
- `40` - Очень большой для названий

### Ширина столбцов (символы)
- `8` - Узкие столбцы (даты, коды)
- `12` - Стандартные данные столбцов
- `15` - Средние текстовые столбцы
- `20` - Широкие текстовые столбцы
- `25` - Очень широкие для описаний
- `30` - Очень широкие для длинных текстов

## Лучшие практики

1. **Размер заголовка**: делайте заголовки выше и шире для усиления внимания
2. **Последовательность данных**: используйте одинаковую высоту строк для данных
3. **Автоподгонка**: используйте автоматическую подгонку для динамического размера контента
4. **Скрывать пустые**: скрывайте пустые строки/столбцы для более аккуратного вида
5. **Логическая группировка**: группировать связанные операции изменения размера пакетами

## Общие шаблоны

### Шаблон настройки отчета
1. Вставьте строки заголовка вверху
2. Установите высоту строки заголовка
3. Автоматическая подгонка данных по столбцам
4. Установка стандартной высоты строки данных
5. Скрытие неиспользуемых областей

### Шаблон импорта данных
1. Вставьте строки для новых данных
2. Автоматическая подгонка столбцов по содержимому
3. Стандартизация высоты строк
4. Скрытие столбцов вычислений

### Шаблон презентации
1. Скрытие строк/столбцов с деталями
2. Увеличение области резюме
3. Установка презентабельных размеров
4. Показывать только релевантные данные

## Обработка ошибок

### Недопустимый диапазон строк
```json
{
  "tool": "row_column_operations",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1", 
    "operation": "set_row_height",
    "rows": "0",
    "height": 20
  }
}
```
**Результат**: ошибка - номера строк начинаются с 1

### Недопустимый диапазон столбцов
```json
{
  "tool": "row_column_operations",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "operation": "set_column_width", 
    "columns": "ZZ",
    "width": 10
  }
}
```
**Результат**: может быть успешно выполнено, но за пределами обычного использования

### Отсутствуют обязательные параметры
```json
{
  "tool": "row_column_operations",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "operation": "set_row_height",
    "rows": "1"
  }
}
```
**Результат**: ошибка - требуется параметр высоты 
{{< app/cells/assistant language="nodejs-cpp" >}}
