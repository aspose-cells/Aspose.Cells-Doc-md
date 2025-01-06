---
title: AI-powered Features
type: docs
weight: 200
keywords: AI,spreadsheet,AI features,AI power,Excel AI,OpenAI,Cells AI
description: This article is a Step-by-Step guide to use AI-powered features for processing spreadsheet files.
---


# New User Guide: Working with Cells AI

Welcome to Cells AI! This guide will walk you through the basic steps to configure and use the Cells AI library.

## Table of Contents
1. [Configure AI Model](#configure-ai-model)
2. [Create AI Instance](#create-ai-instance)
3. [Process Files with AI](#process-files-with-ai)
4. [Using Proxy Settings](#using-proxy-settings)

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
#### Use predefined AI model
```csharp
Config.Model = Model.Gpt4OMini;
```

## Create AI Instance

You need to initialize an instance of CellsAI by providing the API root URL and your API key. Alternatively, you can provide the full API URL if needed.

### Example:
#### Initialize with AI chat root URL
```csharp
String APIKey = "sk-xxxxx";
String APIRootUrl = "https://api.openai.com/";
CellsAI cellsAI = new CellsAI(APIRootUrl, APIKey);
```
#### Initialize with AI chat full URL
```csharp
String APIKey = "sk-xxxxx";
String FullAPIRootUrl = "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions";
CellsAI cellsAI = new CellsAI(FullAPIRootUrl, true, APIKey);
```

## Process Files with AI

Once you have configured the AI model and created an AI instance, you can use the AI's capabilities to process spreadsheets files.

### Summarize a Spreadsheet::
#### Get summary of the spreadsheet
```csharp
// Get summary of the spreadsheet
string summary = cellsAI.SpreadsheetSummarize("c:/student.xlsx");
```

#### You can also output the summary to a TextWriter:
```csharp
// Use TextWriter way, Output summary to a TextWriter (Console)
TextWriter writer = Console.Out;
await cellsAI.SpreadsheetSummarize("c:/student.xlsx", writer);
```
### Ask Questions About a Spreadsheet:
#### You can ask questions about the content of a spreadsheet:
```csharp
// Ask a question about the spreadsheet
await cellsAI.SpreadsheetQuestion("c:/student.xlsx", "Who is the best student?", writer);
```
### Build a Spreadsheet Based on User Requests:
#### Example:

You can create a new spreadsheet based on a specific request. For example, generating a weekly meal plan:
```csharp
await cellsAI.BuildSpreadsheet("Provide weekly daily three-meal recipes, including nutritional value, preparation methods, ingredients, and cost, one day per row, and add total cost at last row.", null, "c:/foodsweekly.xlsx");
```

You can also forecast sales based on historical data:

```csharp
await cellsAI.BuildSpreadsheet("Based on the sales history data from row 3 to row 10, predict the sales situation for the next year. Add it in row 11.", "c:/Sales Report Year.xlsx", "c:/Sales Report Forcast.xlsx");

```
Or, update student scores with a ranking:
```csharp
await cellsAI.BuildSpreadsheet("Add a new column named \"Ranking\" and fill in the content of this column based on the students' total scores ranking", "c:\\student_score.xlsx", "c:\\student_score_with_rank.xlsx");
```
Using AI Model with Localized Requests:

You can use Alibaba's Qianwen AI model or other localized AI models. Here's how you can specify a locale:
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

### Getting Excel Formulas:
#### You can query Excel formulas directly from the spreadsheet:
```csharp
// Get formula from the spreadsheet
string formula = cellsAI.GetExcelFormula("c:/student.xlsx", "get the total score for Xiaomin");
```
## Use Proxy Settings if You Can't Access the AI Server Directly

If you are working behind a proxy, you can configure proxy settings to allow Cells AI to connect to the server.

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

##  Additional Features and Customizations
Cells AI allows various customizations, such as adjusting the AI model, setting locales, and modifying data outputs. Make sure to explore the API and experiment with different configurations for your specific use case.

## Conclusion
Cells AI empowers you to process spreadsheets, automate tasks, and leverage AI for your Excel-based applications.  

For further details, refer to the  [api documentation](https://reference.aspose.com/cells/net/aspose.cells.ai/) or the [support forum](https://forum.aspose.com/c/cells/9).

Happy coding!
