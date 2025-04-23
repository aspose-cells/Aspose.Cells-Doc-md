---
title: إضافة اتصال Pivot باستخدام Node.js عبر C++
linktitle: إضافة اتصال المحور
type: docs
weight: 30
url: /ar/nodejs-cpp/add-pivot-connection/
description: تعلم كيفية إضافة اتصال Pivot باستخدام Aspose.Cells for Node.js via C++.
keywords: إضافة اتصال Pivot بدون Office 2013، Office 2016، Office 2019 وOffice 365 Node.js عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**

إذا كنت تريد ربط مقسم وجدول محوري في Excel، تحتاج إلى النقر بزر الماوس الأيمن على المقسم واختيار "اتصالات التقرير...". في قائمة الخيارات، يمكنك العمل على خانة الاختيار. بالمثل، إذا كنت تريد ربط مقسم وجدول محوري باستخدام API الخاص بـ Aspose.Cells برمجيًا، يرجى استخدام [**Slicer.addPivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#addPivotConnection-PivotTable-). سيقوم بربط المقسم والجدول المحوري.

## **ربط المنقي والجدول المحوري**

الكود النموذجي التالي يحمل [ملف Excel النموذجي](add-pivot-connection.xlsx) الذي يحتوي على مقسم موجود. يصل إلى المقسم ثم يربط المقسم والجدول المحوري. أخيرًا، يحفظ المصنف كـ [ملف Excel المخرجي](add-pivot-connection-out.xlsx).

## **الكود المثالي**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "add-pivot-connection.xlsx");

// Load sample Excel file containing slicer.
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access the first PivotTable inside the PivotTable collection.
const pivotTable = worksheet.getPivotTables().get(0); 

// Access the first slicer inside the slicer collection.
const slicer = worksheet.getSlicers().get(0);

// Adds PivotTable connection.
slicer.addPivotConnection(pivotTable);

workbook.save(path.join(dataDir, "add-pivot-connection-out.xlsx"));
```
