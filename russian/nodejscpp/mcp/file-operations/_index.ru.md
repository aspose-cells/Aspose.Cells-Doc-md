---
title: Файл Excel и операции с данными
linktitle: Файл и операции с данными
type: docs
weight: 10
url: /ru/nodejs-cpp/mcp/file-operations
keywords: "Операции с файлами Excel, операции с данными Excel, создание рабочей книги Excel, лист Excel, чтение данных Excel, запись данных Excel"
description: "Операции с файлами и данными Excel  создание рабочих книг, управление листами, чтение и запись данных Excel с автоматизацией AI"
---

# Операции с файлами и данными Excel

Управляйте **файлами Excel** и **операциями с данными** с помощью автоматизации на базе AI. Создавайте **рабочие книги Excel**, управляйте **листами** и выполняйте **операции чтения/записи данных Excel**.

## Доступные инструменты

- `create_workbook` - Создание новых **рабочих книг Excel** с автоматизацией **AI Excel**
- `create_worksheet` - Добавление **листов Excel** в существующие **рабочие книги Excel**
- `get_workbook_info` - Получение метаданных и информации о **рабочей книге Excel**
- `read_data_from_excel` - Чтение данных из **листов Excel** с помощью **AI-поддержки**
- `write_data_to_excel` - Запись данных в **листы Excel** через **Excel MCP**

## Создание рабочих книг Excel

### Создать базовую рабочую книгу
```json
{
  "tool": "create_workbook",
  "parameters": {
    "filepath": "reports/sales-report.xlsx"
  }
}
```

### Создать рабочую книгу с пользовательским листом
```json
{
  "tool": "create_workbook",
  "parameters": {
    "filepath": "reports/financial-report.xlsx",
    "sheet_name": "Financial Data"
  }
}
```

## Управление листами

### Добавить новый лист
```json
{
  "tool": "create_worksheet",
  "parameters": {
    "filepath": "reports/sales-report.xlsx",
    "sheet_name": "Summary Report"
  }
}
```

### Получить информацию о рабочей книге
```json
{
  "tool": "get_workbook_info",
  "parameters": {
    "filepath": "reports/sales-report.xlsx"
  }
}
```

## Запись данных в Excel

### Записать заголовки и данные
```json
{
  "tool": "write_data_to_excel",
  "parameters": {
    "filepath": "reports/sales-report.xlsx",
    "sheet_name": "Sales Data",
    "data": [
      ["Product", "Category", "Unit Price", "Quantity", "Total", "Status"],
      ["Laptop Pro", "Electronics", 1299.99, 5, "", "In Stock"],
      ["Wireless Mouse", "Electronics", 89.99, 15, "", "In Stock"],
      ["Office Chair", "Furniture", 299.99, 8, "", "Low Stock"]
    ]
  }
}
```

### Записать данные в пользовательскую позицию
```json
{
  "tool": "write_data_to_excel",
  "parameters": {
    "filepath": "reports/analysis.xlsx",
    "sheet_name": "Data Analysis",
    "start_cell": "C3",
    "data": [
      ["Name", "Score", "Grade", "Double Score", "Bonus"],
      ["Alice", 95, "A", "", ""],
      ["Bob", 87, "B", "", ""],
      ["Charlie", 92, "A", "", ""]
    ]
  }
}
```

## Читать данные из Excel

### Читать полный используемый диапазон
```json
{
  "tool": "read_data_from_excel",
  "parameters": {
    "filepath": "reports/sales-report.xlsx",
    "sheet_name": "Sales Data"
  }
}
```

### Читать определённый диапазон
```json
{
  "tool": "read_data_from_excel",
  "parameters": {
    "filepath": "reports/analysis.xlsx",
    "sheet_name": "Data Analysis",
    "start_cell": "C3",
    "end_cell": "G6"
  }
}
```

### Читать из позиции по умолчанию
```json
{
  "tool": "read_data_from_excel",
  "parameters": {
    "filepath": "reports/basic-data.xlsx",
    "sheet_name": "Sheet1",
    "start_cell": "A1"
  }
}
```

## Пример полного рабочего процесса

### 1. Создайте свой первый отчет Excel
```json
{
  "tool": "create_workbook",
  "parameters": {
    "filepath": "reports/monthly-report.xlsx",
    "sheet_name": "Monthly Sales"
  }
}
```

### 2. Добавить лист с резюме
```json
{
  "tool": "create_worksheet",
  "parameters": {
    "filepath": "reports/monthly-report.xlsx",
    "sheet_name": "Summary"
  }
}
```

### 3. Записать данные о продажах
```json
{
  "tool": "write_data_to_excel",
  "parameters": {
    "filepath": "reports/monthly-report.xlsx",
    "sheet_name": "Monthly Sales",
    "data": [
      ["Month", "Product", "Sales", "Target", "Variance"],
      ["January", "Product A", 5000, 4500, ""],
      ["January", "Product B", 3200, 3000, ""],
      ["February", "Product A", 5500, 4500, ""],
      ["February", "Product B", 3400, 3000, ""]
    ]
  }
}
```

### 4. Проверить данные
```json
{
  "tool": "read_data_from_excel",
  "parameters": {
    "filepath": "reports/monthly-report.xlsx",
    "sheet_name": "Monthly Sales",
    "start_cell": "A1",
    "end_cell": "E5"
  }
}
```

### 5. Проверить структуру рабочей книги
```json
{
  "tool": "get_workbook_info",
  "parameters": {
    "filepath": "reports/monthly-report.xlsx"
  }
}
```

## Лучшие практики

1. **Пути к файлам**: Используйте относительные пути для лучшей переносимости
2. **Названия листов**: Используйте описательные имена для рабочих листов
3. **Структура данных**: Организуйте данные с ясными заголовками
4. **Чтение диапазонов**: Указывайте диапазоны для больших наборов данных
5. **Обработка ошибок**: Проверяйте наличие файла перед операциями

## Общие шаблоны

### Шаблон импорта данных
1. Создайте рабочую книгу
2. Написать необработанные данные
3. Проверить чтением наоборот
4. Обработать формулами

### Мульти-Листовые отчёты
1. Создать рабочую книгу с основным листом
2. Добавить сводные/аналитические листы
3. Записать данные на каждый лист
4. Связать листы с помощью формул

### Валидация данных
1. Записать данные
2. Читать обратно определённые диапазоны
3. Проверить целостность данных
4. Обрабатывать отсутствующие значения 
{{< app/cells/assistant language="nodejs-cpp" >}}
