---
title: تنفيذ النطاقات غير المتتالية باستخدام Node.js عبر C++
linktitle: تنفيذ النطاقات غير المتتالية
type: docs
weight: 700
url: /ar/nodejs-cpp/implementing-non-sequential-ranges/
description: تعلم كيفية إنشاء نطاقات غير متتالية مسماة باستخدام Aspose.Cells for Node.js via C++. استخدم نطاقات الخلايا غير المجاورة بكفاءة.
---

{{% alert color="primary" %}} 

عادةً، تكون النطاقات المسماة مستطيلة مع خلايا متصلة ومجاورة لبعضها البعض. لكن أحيانًا، قد تحتاج إلى استخدام نطاق خلايا غير متتالية حيث لا تكون الخلايا مجاورة. يدعم Aspose.Cells for Node.js via C++ إنشاء نطاق مسمى مع خلايا غير متجاورة.

{{% /alert %}} 

يعرض العينة البرمجية أدناه كيفية إنشاء نطاق غير متتلسل مسمى باستخدام Aspose.Cells for Node.js via C++.


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a Name for non sequenced range
const index = workbook.getWorksheets().getNames().add("NonSequencedRange");

const name = workbook.getWorksheets().getNames().get(index);

// Creating a non sequence range of cells
name.setRefersTo("=Sheet1!$A$1:$B$3,Sheet1!$D$5:$E$6");

// Save the workbook
workbook.save(path.join(dataDir, "Output.out.xlsx"));
``` 
