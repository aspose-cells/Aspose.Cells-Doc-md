---
title: دمج أو إلغاء دمج نطاق خلايا باستخدام Node.js عبر C++
linktitle: دمج أو إلغاء دمج مجموعة من الخلايا
type: docs
weight: 190
url: /ar/nodejs-cpp/merge-or-unmerge-range-of-cells/
description: دمج وإلغاء دمج الخلايا في نطاق في Excel باستخدام كود Node.js عبر C++.
keywords: دمج وإلغاء دمج الخلايا في نطاق باستخدام Node.js، دمج وإلغاء دمج الخلايا في نطاق باستخدام Node.js، دمج وإلغاء دمج الخلايا في النطاق باستخدام Node.js، دمج وإلغاء دمج الخلايا في نطاق باستخدام Node.js، دمج وإلغاء دمج الخلايا في Excel باستخدام Node.js، دمج وإلغاء دمج الخلايا في Excel باستخدام Node.js، دمج وإلغاء دمج خلايا في Excel باستخدام Node.js، دمج خلايا في Excel باستخدام Node.js، إلغاء دمج خلايا في Excel باستخدام Node.js، دمج خلايا في النطاق باستخدام Node.js
---

{{% alert color="primary" %}}

يمكنك استخدام Aspose.Cells لدمج أو تقسيم مجموعة من الخلايا. يوفر Aspose.Cells الأساليب [**Range.merge()**](https://reference.aspose.com/cells/nodejs-cpp/range/#merge--) و [**Range.unMerge()**](https://reference.aspose.com/cells/nodejs-cpp/range/#unMerge--) لهذا الغرض. يشرح هذا المقال كيفية دمج مجموعة من الخلايا في خلية واحدة.

{{% /alert %}}

## **مثال**

يعرض الكود النموذجي التالي أولاً إنشاء نطاق - A1:D4 - ثم دمج الخلايا في النطاق إلى خلية واحدة باستخدام الطريقة [**Range.merge()**](https://reference.aspose.com/cells/nodejs-cpp/range/#merge--). بالمثل، يمكنك تقسيم الخلايا عن طريق إنشاء نطاق واستدعاء الطريقة [**Range.unMerge()**](https://reference.aspose.com/cells/nodejs-cpp/range/#unMerge--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create a workbook
const workbook = new AsposeCells.Workbook();

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Create a range
const range = worksheet.getCells().createRange("A1:D4");

// Merge range into a single cell
range.merge();

// Save the workbook
workbook.save(path.join(dataDir, "output.out.xlsx"));
```
