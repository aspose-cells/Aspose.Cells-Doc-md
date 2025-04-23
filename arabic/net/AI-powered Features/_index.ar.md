---
title: الميزات المدعومة بواسطة الذكاء الاصطناعي
type: docs
weight: 200
url: /ar/net/ai-powered-features/
keywords: الذكاء الاصطناعي، جدول البيانات، ميزات الذكاء الاصطناعي، قوة الذكاء الاصطناعي، Excel AI، OpenAI، Cells AI.
description: هذه المقالة دليل خطوة بخطوة لاستخدام الميزات المعتمدة على الذكاء الاصطناعي لمعالجة ملفات جداول البيانات.
---


# دليل المستخدم الجديد: العمل مع Cells AI

مرحبًا بك في Cells AI! سيرشدك هذا الدليل عبر الخطوات الأساسية لتكوين واستخدام مكتبة Cells AI.

## جدول المحتويات
1. [تكوين نموذج الذكاء الاصطناعي](#configure-ai-model)
2. [إنشاء مثيل للذكاء الاصطناعي](#create-ai-instance)
3. [معالجة الملفات باستخدام الذكاء الاصطناعي](#process-files-with-ai)
4. [استخدام إعدادات الوكيل](#use-proxy-settings-if-you-can-not-access-the-ai-server-directly)

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
#### استخدام نموذج الذكاء الاصطناعي المحدد مسبقًا
```csharp
Config.Model = Model.Gpt4OMini;
```

## إنشاء مثيل للذكاء الاصطناعي

تحتاج إلى تهيئة مثيل من CellsAI عن طريق تقديم عنوان URL للجذر الخاص بواجهة برمجة التطبيقات ومفتاح API الخاص بك. بدلاً من ذلك، يمكنك تقديم عنوان URL الكامل لواجهة برمجة التطبيقات إذا لزم الأمر.

### مثال:
#### التهيئة باستخدام عنوان URL للجذر لمحادثة الذكاء الاصطناعي
```csharp
String APIKey = "sk-xxxxx";
String APIRootUrl = "https://api.openai.com/";
CellsAI cellsAI = new CellsAI(APIRootUrl, APIKey);
```
#### التهيئة باستخدام عنوان URL الكامل لمحادثة الذكاء الاصطناعي
```csharp
String APIKey = "sk-xxxxx";
String FullAPIRootUrl = "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions";
CellsAI cellsAI = new CellsAI(FullAPIRootUrl, true, APIKey);
```

## معالجة الملفات باستخدام الذكاء الاصطناعي

بمجرد أن تقوم بتهيئة نموذج الذكاء الاصطناعي وإنشاء مثيل للذكاء الاصطناعي، يمكنك استخدام قدرات الذكاء الاصطناعي لمعالجة ملفات الجداول.

### تلخيص جدول البيانات::
#### الحصول على ملخص لجدول البيانات
```csharp
// Get summary of the spreadsheet
string summary = cellsAI.SpreadsheetSummarize("c:/student.xlsx");
```

#### يمكنك أيضًا إخراج الملخص إلى كاتب نصوص:
```csharp
// Use TextWriter way, Output summary to a TextWriter (Console)
TextWriter writer = Console.Out;
await cellsAI.SpreadsheetSummarize("c:/student.xlsx", writer);
```
### طرح الأسئلة حول جدول البيانات:
#### يمكنك طرح أسئلة حول محتوى جدول البيانات:
```csharp
// Ask a question about the spreadsheet
await cellsAI.SpreadsheetQuestion("c:/student.xlsx", "Who is the best student?", writer);
```
### بناء جدول بيانات استنادًا إلى طلبات المستخدم:
#### مثال:

يمكنك إنشاء جدول بيانات جديد بناءً على طلب معين. على سبيل المثال، إعداد خطة وجبات أسبوعية:
```csharp
await cellsAI.BuildSpreadsheet("Provide weekly daily three-meal recipes, including nutritional value, preparation methods, ingredients, and cost, one day per row, and add total cost at last row.", null, "c:/foodsweekly.xlsx");
```

يمكنك أيضًا التنبؤ بالمبيعات استنادًا إلى البيانات التاريخية:

```csharp
await cellsAI.BuildSpreadsheet("Based on the sales history data from row 3 to row 10, predict the sales situation for the next year. Add it in row 11.", "c:/Sales Report Year.xlsx", "c:/Sales Report Forcast.xlsx");

```
أو، تحديث درجات الطلاب مع ترتيب:
```csharp
await cellsAI.BuildSpreadsheet("Add a new column named \"Ranking\" and fill in the content of this column based on the students' total scores ranking", "c:\\student_score.xlsx", "c:\\student_score_with_rank.xlsx");
```
استخدام نموذج الذكاء الاصطناعي مع الطلبات المحلية:

يمكنك استخدام نموذج Alibaba's Qianwen للذكاء الاصطناعي أو نماذج ذكاء اصطناعي محلية أخرى. إليك كيف يمكنك تحديد المنطقة:
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

### الحصول على صيغ Excel:
#### يمكنك استعلام صيغ Excel مباشرة من جدول البيانات:
```csharp
// Get formula from the spreadsheet
string formula = cellsAI.GetExcelFormula("c:/student.xlsx", "get the total score for Xiaomin");
```
## استخدم إعدادات الوكيل إذا لم تتمكن من الوصول إلى خادم الذكاء الاصطناعي مباشرةً

إذا كنت تعمل خلف وكيل، يمكنك تكوين إعدادات الوكيل للسماح لـ Cells AI بالاتصال بالخادم.

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

## ميزات إضافية وتخصيصات
يسمح Cells AI بتخصيصات متنوعة، مثل تعديل نموذج الذكاء الاصطناعي، وضبط المناطق المحلية، وتعديل مخرجات البيانات. تأكد من استكشاف واجهة برمجة التطبيقات وتجربة تكوينات مختلفة لاحتياجك الخاص.

## الخاتمة
يمكنك Cells AI من معالجة جداول البيانات، وأتمتة المهام، والاستفادة من الذكاء الاصطناعي لتطبيقاتك المعتمدة على إكسل.  

للمزيد من التفاصيل، يرجى الرجوع إلى [توثيق API](https://reference.aspose.com/cells/net/aspose.cells.ai/) أو [منتدى الدعم](https://forum.aspose.com/c/cells/9).

تجارة سعيدة!
