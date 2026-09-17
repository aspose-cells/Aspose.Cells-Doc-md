---
title: إدراج جدول محوري
description: إنشاء وتنسيق الجداول المحورية لملفات جداول بيانات Excel باستخدام Aspose.Cells لـ Node.js عبر Java.
linktitle: الجداول المحورية
url: /ar/nodejs-java/create-pivot-table/
type: docs
weight: 160
keywords: إنشاء جدول محوري, إدراج جدول محوري, تنسيق جدول محوري, Aspose.Cells لـ Node.js عبر Java.
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **إنشاء جدول محوري**
من الممكن استخدام Aspose.Cells لإضافة جداول محورية إلى جداول البيانات برمجياً.

### **نموذج كائنات الجدول المحوري**
توفر Aspose.Cells مجموعة من الفئات المستخدمة لإنشاء الجداول المحورية والتحكم فيها. اللبنات الأساسية هي:
- `PivotField` يمثل حقلاً في `PivotTable`.
- `PivotFieldCollection` يمثل مجموعة من جميع كائنات `PivotField` في `PivotTable`.
- `PivotTable` يمثل جدولاً محورياً في ورقة العمل.
- `PivotTableCollection` يمثل مجموعة من جميع كائنات `PivotTable` في ورقة العمل.

### **إنشاء جدول محوري بسيط باستخدام Aspose.Cells**
1. أضف بيانات إلى ورقة العمل باستخدام طريقة `putValue` للخلية. سيتم استخدام هذه البيانات كمصدر بيانات للجدول المحوري.
2. أضف جدولاً محورياً إلى ورقة العمل عن طريق استدعاء طريقة `add` لمجموعة `PivotTables` المغلفة داخل كائن ورقة العمل.
3. قم بالوصول إلى كائن `PivotTable` الجديد من مجموعة `PivotTables` بتمرير فهرس الجدول المحوري.
4. استخدم أياً من كائنات `PivotTable` (الموضحة أعلاه) لإدارة الجدول المحوري.

بعد تنفيذ كود المثال، تتم إضافة جدول محوري إلى ورقة العمل.

```javascript
var dataDir = "./";

// Instantiating a Workbook object
var workbook = new AsposeCells.Workbook();

// Obtaining the reference of the newly added worksheet
var sheet = workbook.getWorksheets().get(0);

var cells = sheet.getCells();

// Setting the value to the cells
var cell = cells.get("A1");
cell.putValue("Sport");
cell = cells.get("B1");
cell.putValue("Quarter");
cell = cells.get("C1");
cell.putValue("Sales");

cell = cells.get("A2");
cell.putValue("Golf");
cell = cells.get("A3");
cell.putValue("Golf");
cell = cells.get("A4");
cell.putValue("Tennis");
cell = cells.get("A5");
cell.putValue("Tennis");
cell = cells.get("A6");
cell.putValue("Tennis");
cell = cells.get("A7");
cell.putValue("Tennis");
cell = cells.get("A8");
cell.putValue("Golf");

cell = cells.get("B2");
cell.putValue("Qtr3");
cell = cells.get("B3");
cell.putValue("Qtr4");
cell = cells.get("B4");
cell.putValue("Qtr3");
cell = cells.get("B5");
cell.putValue("Qtr4");
cell = cells.get("B6");
cell.putValue("Qtr3");
cell = cells.get("B7");
cell.putValue("Qtr4");
cell = cells.get("B8");
cell.putValue("Qtr3");

cell = cells.get("C2");
cell.putValue(1500);
cell = cells.get("C3");
cell.putValue(2000);
cell = cells.get("C4");
cell.putValue(600);
cell = cells.get("C5");
cell.putValue(1500);
cell = cells.get("C6");
cell.putValue(4070);
cell = cells.get("C7");
cell.putValue(5000);
cell = cells.get("C8");
cell.putValue(6430);

var pivotTables = sheet.getPivotTables();

// Adding a PivotTable to the worksheet
var index = pivotTables.add("=A1:C8", "E3", "PivotTable2");

// Accessing the instance of the newly added PivotTable
var pivotTable = pivotTables.get(index);

// Unshowing grand totals for rows.
pivotTable.setRowGrand(false);

// Draging the first field to the row area.
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, 0);

// Draging the second field to the column area.
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, 1);

// Draging the third field to the data area.
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, 2);

// Saving the Excel file
workbook.save(dataDir + "pivotTable_test_out.xls");
```

{{% alert color="primary" %}}
عند تعيين نطاق من الخلايا كمصدر بيانات، يجب أن يمتد النطاق من أعلى اليسار إلى أسفل اليمين. على سبيل المثال، "A1:C3" صالح ولكن "C3:A1" غير صالح.
{{% /alert %}}

## Related Articles
- [Add Filter Fields to a Pivot Table in Aspose.Cells for Node.js via Java](/cells/ar/nodejs-java/add-page-field-in-pivot-table/)
- [Apply Styles to Pivot Tables in Aspose.Cells for Node.js via Java](/cells/ar/nodejs-java/apply-style-to-pivot-table/)
- [Modify Page Field Layout in Pivot Table](/cells/ar/nodejs-java/change-page-field-layout/)
- [Filtering Pivot Tables by Label or Value](/cells/ar/nodejs-java/filter-by-label-or-value-of-pivot-table/)
- [Manage Pivot Table Value Fields in Aspose.Cells for Node.js via Java](/cells/ar/nodejs-java/manage-value-fields/)

{{< app/cells/assistant language="nodejs-java" >}}