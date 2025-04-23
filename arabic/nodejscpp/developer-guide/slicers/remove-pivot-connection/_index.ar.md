---
title: إزالة اتصال Pivot باستخدام Node.js عبر C++
linktitle: إزالة اتصال الجدول المحوري
type: docs
weight: 30
url: /ar/nodejs-cpp/remove-pivot-connection/
description: تعلم كيفية إزالة اتصال Pivot باستخدام Aspose.Cells for Node.js via C++.
keywords: إزالة اتصال Pivot بدون Office 2013، Office 2016، Office 2019 وOffice 365 Node.js عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**

 إذا كنت تريد فك ربط مقسم وجدول محوري في Excel، تحتاج إلى النقر بزر الماوس الأيمن على المقسم واختيار "اتصالات التقرير...". في قائمة الخيارات، يمكنك العمل على خانة الاختيار. بالمثل، إذا كنت تريد فك ربط مقسم وجدول محوري باستخدام API الخاص بـ Aspose.Cells برمجيًا، يرجى استخدام [**Slicer.removePivotConnection(PivotTable)**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#removePivotConnection-pivottable-). سيقوم بفصل المقسم والجدول المحوري.

## **فصل قالب التصفية عن جدول المحور**

الكود النموذجي التالي يحمل [ملف Excel النموذجي](remove-pivot-connection.xlsx) الذي يحتوي على مقسم موجود. يصل إلى المقسم ثم يفكه. أخيرًا، يحفظ المصنف كـ [ملف Excel المخرجي](remove-pivot-connection-out.xlsx).

## **الكود المثالي**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "remove-pivot-connection.xlsx");
// Load sample Excel file containing slicer.
const workbook = new AsposeCells.Workbook(filePath);
// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Access the first PivotTable inside the PivotTable collection.
const pivotTable = worksheet.getPivotTables().get(0);
// Access the first slicer inside the slicer collection.
const slicer = worksheet.getSlicers().get(0);
// Remove PivotTable connection.
slicer.removePivotConnection(pivotTable);
// Save the workbook in output XLSX format.
workbook.save(path.join(dataDir, "remove-pivot-connection-out.xlsx"));
``` 
