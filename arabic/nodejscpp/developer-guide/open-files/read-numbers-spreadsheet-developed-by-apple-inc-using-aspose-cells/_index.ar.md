---
title: قراءة جداول بيانات Numbers التي طورتها Apple Inc. باستخدام Aspose.Cells for Node.js via C++
linktitle: قراءة جدول بيانات الأرقام المطور من قبل Apple Inc. باستخدام Aspose.Cells
type: docs
weight: 140
url: /ar/nodejs-cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/
description: تعلم كيفية قراءة جداول بيانات Numbers التي طورتها Apple Inc. باستخدام Aspose.Cells for Node.js via C++. 
---

## **سيناريوهات الاستخدام المحتملة**

Numbers هو تطبيق جدول بيانات طورته Apple Inc. يمكن لـ Aspose.Cells قراءة جداول بيانات Numbers، لكنه لا يدعم الكتابة إليها. يمكنه قراءة بيانات، وأنماط، وصيغ جداول بيانات Numbers.

## **قراءة جداول بيانات Numbers التي طورتها Apple Inc. باستخدام Aspose.Cells for Node.js via C++**

الرمز النموذجي التالي يُحمّل [Sample Numbers Spreadsheet](sampleNumbersByAppleInc.numbers) ويحوّله إلى [Output PDF Format](outputNumbersByAppleInc.pdf). ستحتاج إلى استخدام فئة [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) وتحديد [**LoadFormat.Numbers**](https://reference.aspose.com/cells/nodejs-cpp/loadformat) كمعامل في منشئها لتحميله بنجاح. يرجى تنزيل كلاهما من الروابط المقدمة. يمكنك تجربة الكود مع أي جدول بيانات Numbers. يرجى أيضًا قراءة تعليقات الكود للمزيد من المساعدة.

## **الكود المثالي**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleNumbersByAppleInc.numbers");
const outputFilePath = path.join(dataDir, "outputNumbersByAppleInc.pdf");

// Specify load options, we want to load Numbers spreadsheet
const opts = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Numbers);

// Load the Numbers spreadsheet in workbook with above load options
const wb = new AsposeCells.Workbook(sourceFilePath, opts);

// Save the workbook to pdf format
wb.save(outputFilePath, AsposeCells.SaveFormat.Pdf);
```

