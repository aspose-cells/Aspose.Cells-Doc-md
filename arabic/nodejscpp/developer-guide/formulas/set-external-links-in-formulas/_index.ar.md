---
title: تعيين الروابط الخارجية في الصيغ باستخدام Node.js عبر C++
linktitle: تحديد الروابط الخارجية في الصيغ
type: docs
weight: 20
url: /ar/nodejs-cpp/set-external-links-in-formulas/
description: تعرف على كيفية تعيين الروابط الخارجية في الصيغ باستخدام Aspose.Cells for Node.js via C++. 
keywords: تعيين روابط خارجية في الصيغ باستخدام Node.js عبر C++، تضمين ملفات خارجية في الصيغ باستخدام Node.js عبر C++ 
---

{{% alert color="primary" %}} 

أحيانًا، من الضروري تضمين روابط لملفات خارجية في الصيغ، على سبيل المثال، لتقييم قيمة خلية أو نطاق بناءً عليها. يوفر Aspose.Cells for Node.js via C++ هذه الميزة ويشرح هذا المستند كيفية استخدامها.

{{% /alert %}} 

يظهر الكود النموذجي أدناه كيفية تضمين الملفات الخارجية في الصيغ.



```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get first Worksheet
const sheet = workbook.getWorksheets().get(0);

// Get Cells collection
const cells = sheet.getCells();

// Set formula with external links
cells.get("A1").setFormula(`=SUM('[${filePath}]Sheet1'!A2, '[${filePath}]Sheet1'!A4)`);

// Set formula with external links
cells.get("A2").setFormula(`='[${filePath}]Sheet1'!A8`);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```
