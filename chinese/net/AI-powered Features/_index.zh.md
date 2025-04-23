---
title: AI驱动功能
type: docs
weight: 200
url: /zh/net/ai-powered-features/
keywords: AI、电子表格、AI功能、AI力量、Excel AI、OpenAI、Cells AI。
description: 本文为使用AI驱动功能处理电子表格文件的逐步指南。
---


# 新用户指南：使用Cells AI

欢迎使用Cells AI！本指南将带您了解配置和使用Cells AI库的基本步骤。

## 目录
1. [配置AI模型](#configure-ai-model)
2. [创建AI实例](#create-ai-instance)
3. [使用AI处理文件](#process-files-with-ai)
4. [使用代理设置](#use-proxy-settings-if-you-can-not-access-the-ai-server-directly)

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
#### 使用预定义AI模型
```csharp
Config.Model = Model.Gpt4OMini;
```

## 创建AI实例

您需要通过提供API根URL和您的API密钥来初始化CellsAI实例。必要时，也可以提供完整的API网址。

### 示例：
#### 使用AI聊天根URL初始化
```csharp
String APIKey = "sk-xxxxx";
String APIRootUrl = "https://api.openai.com/";
CellsAI cellsAI = new CellsAI(APIRootUrl, APIKey);
```
#### 使用AI聊天完整URL初始化
```csharp
String APIKey = "sk-xxxxx";
String FullAPIRootUrl = "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions";
CellsAI cellsAI = new CellsAI(FullAPIRootUrl, true, APIKey);
```

## 使用AI处理文件

配置好AI模型并创建实例后，您可以使用AI的能力处理电子表格文件。

### 概要总结电子表格：
#### 获取电子表格摘要
```csharp
// Get summary of the spreadsheet
string summary = cellsAI.SpreadsheetSummarize("c:/student.xlsx");
```

#### 您还可以将摘要输出到TextWriter：
```csharp
// Use TextWriter way, Output summary to a TextWriter (Console)
TextWriter writer = Console.Out;
await cellsAI.SpreadsheetSummarize("c:/student.xlsx", writer);
```
### 关于电子表格提问：
#### 您可以询问关于电子表格内容的问题：
```csharp
// Ask a question about the spreadsheet
await cellsAI.SpreadsheetQuestion("c:/student.xlsx", "Who is the best student?", writer);
```
### 根据用户请求创建电子表格：
#### 示例：

您可以根据具体需求创建新的电子表格。例如，生成每周菜单：
```csharp
await cellsAI.BuildSpreadsheet("Provide weekly daily three-meal recipes, including nutritional value, preparation methods, ingredients, and cost, one day per row, and add total cost at last row.", null, "c:/foodsweekly.xlsx");
```

您还可以基于历史数据进行销售预估：

```csharp
await cellsAI.BuildSpreadsheet("Based on the sales history data from row 3 to row 10, predict the sales situation for the next year. Add it in row 11.", "c:/Sales Report Year.xlsx", "c:/Sales Report Forcast.xlsx");

```
或者，用排名更新学生成绩：
```csharp
await cellsAI.BuildSpreadsheet("Add a new column named \"Ranking\" and fill in the content of this column based on the students' total scores ranking", "c:\\student_score.xlsx", "c:\\student_score_with_rank.xlsx");
```
使用本地化请求的AI模型：

您可以使用阿里巴巴的千问AI模型或其他本地化AI模型。以下是如何指定地区：
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

### 获取Excel公式：
#### 您可以直接从电子表格查询Excel公式：
```csharp
// Get formula from the spreadsheet
string formula = cellsAI.GetExcelFormula("c:/student.xlsx", "get the total score for Xiaomin");
```
## 如果无法直接访问AI服务器，请使用代理设置

如果您在代理后面工作，可以配置代理设置以允许Cells AI连接到服务器。

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

## 其他功能与自定义
Cells AI支持多种自定义，例如调整AI模型、设置地区和修改数据输出。请确保探索API并尝试不同配置以适应您的具体用例。

## 结论
Cells AI使您能够处理电子表格，自动化任务，并利用AI为您的Excel应用程序提供支持。  

有关更多信息，请参阅 [API文档](https://reference.aspose.com/cells/net/aspose.cells.ai/) 或[支持论坛](https://forum.aspose.com/c/cells/9)。

快乐编码！
