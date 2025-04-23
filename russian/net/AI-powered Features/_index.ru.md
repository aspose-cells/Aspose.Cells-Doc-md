---
title: Возможности на базе ИИ
type: docs
weight: 200
url: /ru/net/ai-powered-features/
keywords: Искусственный интеллект, таблицы, функции ИИ, мощность ИИ, AI Excel, OpenAI, AI для ячеек.
description: Эта статья является пошаговым руководством по использованию функций на основе ИИ для обработки файлов таблиц.
---


# Руководство для новых пользователей: Работа с Cells AI

Добро пожаловать в Cells AI! Это руководство проведет вас через основные шаги настройки и использования библиотеки Cells AI.

## Оглавление
1. [Настройка модели ИИ](#configure-ai-model)
2. [Создание экземпляра ИИ](#create-ai-instance)
3. [Обработка файлов с помощью ИИ](#process-files-with-ai)
4. [Использование настроек прокси](#use-proxy-settings-if-you-can-not-access-the-ai-server-directly)

---

## Prerequisites

Before using Cells AI, ensure you have the following:
- A valid **API Key** from OpenAI or the other AI provider of your choice.
- A .NET development environment set up for C# programming.

## Configure AI Model

To start using Cells AI, you need to set up an AI model. You can either create a new model or use one of the predefined models.

### Example:
#### Setup a new AI model
```csharp
Config.Model = new Model("gpt-4-32k");
```
#### Использование предопределенной модели ИИ
```csharp
Config.Model = Model.Gpt4OMini;
```

## Создание экземпляра ИИ

Вам нужно инициализировать экземпляр CellsAI, указав базовый URL API и ваш API ключ. В качестве альтернативы можно указать полный URL API, если необходимо.

### Пример:
#### Инициализация с базовым URL API чата ИИ
```csharp
String APIKey = "sk-xxxxx";
String APIRootUrl = "https://api.openai.com/";
CellsAI cellsAI = new CellsAI(APIRootUrl, APIKey);
```
#### Инициализация с полным URL API чата ИИ
```csharp
String APIKey = "sk-xxxxx";
String FullAPIRootUrl = "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions";
CellsAI cellsAI = new CellsAI(FullAPIRootUrl, true, APIKey);
```

## Обработка файлов с помощью ИИ

После настройки модели ИИ и создания экземпляра ИИ, вы можете использовать возможности ИИ для обработки файлов таблиц.

### Резюме таблицы::
#### Получить резюме таблицы
```csharp
// Get summary of the spreadsheet
string summary = cellsAI.SpreadsheetSummarize("c:/student.xlsx");
```

#### Вы также можете вывести резюме в TextWriter:
```csharp
// Use TextWriter way, Output summary to a TextWriter (Console)
TextWriter writer = Console.Out;
await cellsAI.SpreadsheetSummarize("c:/student.xlsx", writer);
```
### Задавайте вопросы о таблице::
#### Вы можете задавать вопросы о содержимом таблицы::
```csharp
// Ask a question about the spreadsheet
await cellsAI.SpreadsheetQuestion("c:/student.xlsx", "Who is the best student?", writer);
```
### Создайте таблицу на основе запросов пользователя::
#### Пример::

Вы можете создать новую таблицу на основе конкретного запроса. Например, составление недельного плана питания::
```csharp
await cellsAI.BuildSpreadsheet("Provide weekly daily three-meal recipes, including nutritional value, preparation methods, ingredients, and cost, one day per row, and add total cost at last row.", null, "c:/foodsweekly.xlsx");
```

Также можно спрогнозировать продажи на основе исторических данных::

```csharp
await cellsAI.BuildSpreadsheet("Based on the sales history data from row 3 to row 10, predict the sales situation for the next year. Add it in row 11.", "c:/Sales Report Year.xlsx", "c:/Sales Report Forcast.xlsx");

```
или обновить оценки студентов с помощью ранжирования::
```csharp
await cellsAI.BuildSpreadsheet("Add a new column named \"Ranking\" and fill in the content of this column based on the students' total scores ranking", "c:\\student_score.xlsx", "c:\\student_score_with_rank.xlsx");
```
Использование модели ИИ с локализованными запросами::

Вы можете использовать модель Qianwen AI от Alibaba или другие локализованные модели ИИ. Вот как указать локаль::
```csharp
// Set to use QwenPlus AI model
Config.Model = Model.QwenPlus;
// Set locale info (e.g., Chinese)
Config.Locale = "zh";

// User request in Chinese
string userRequest = "增加新的一列,列名称是\"排名\" 并根据学生的总分大小排名填入这一列的内容";
string outfile = "D:\\学生排行.xlsx";
string inputfile = "D:\\student_score_zh.xlsx";
await cellsAI.BuildSpreadsheet(userRequest, inputfile, outfile);

```

### Получение формул Excel::
#### Вы можете напрямую запрашивать формулы Excel из таблицы:
```csharp
// Get formula from the spreadsheet
string formula = cellsAI.GetExcelFormula("c:/student.xlsx", "get the total score for Xiaomin");
```
## Используйте настройки прокси, если не можете получить доступ к серверу AI напрямую

Если вы работаете за прокси, вы можете настроить параметры прокси для подключения Cells AI к серверу.

```csharp
// Set up proxy for Cells AI
string proxyAddress = "http://127.0.0.1:58591";
WebProxy proxy = new WebProxy(proxyAddress)
{
    BypassProxyOnLocal = false,  
    UseDefaultCredentials = false,
};

// Apply the proxy setting
cellsAI.Proxy = proxy;
```

## Дополнительные функции и настройки
Cells AI позволяет настраивать различные параметры, такие как выбор модели ИИ, установка локалей и изменение форматов данных. Обязательно исследуйте API и экспериментируйте с разными конфигурациями для вашего конкретного случая использования.

## Заключение
Cells AI дает вам возможность обрабатывать таблицы, автоматизировать задачи и использовать ИИ для ваших приложений на базе Excel.  

Для получения дополнительной информации обратитесь к [документации API](https://reference.aspose.com/cells/net/aspose.cells.ai/) или на [форум поддержки](https://forum.aspose.com/c/cells/9).

Удачного программирования!
