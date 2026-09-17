---
title: جداول الدوران
description: إنشاء وتنسيق جداول الدوران في ملفات جداول البيانات في Excel.
linktitle: جداول الدوران
url: /ar/python-java/create-pivot-table/
type: docs
weight: 160
keywords: إنشاء جدول دوران، إدراج جدول دوران، تنسيق جدول دوران.
ai_search_scope: cells_pythonjava
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

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType

dataDir = "./"
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()

cell = cells.get("A1")
cell.putValue("Sport")
cell = cells.get("B1")
cell.putValue("Quarter")
cell = cells.get("C1")
cell.putValue("Sales")

cell = cells.get("A2")
cell.putValue("Golf")
cell = cells.get("A3")
cell.putValue("Golf")
cell = cells.get("A4")
cell.putValue("Tennis")
cell = cells.get("A5")
cell.putValue("Tennis")
cell = cells.get("A6")
cell.putValue("Tennis")
cell = cells.get("A7")
cell.putValue("Tennis")
cell = cells.get("A8")
cell.putValue("Golf")

cell = cells.get("B2")
cell.putValue("Qtr3")
cell = cells.get("B3")
cell.putValue("Qtr4")
cell = cells.get("B4")
cell.putValue("Qtr3")
cell = cells.get("B5")
cell.putValue("Qtr4")
cell = cells.get("B6")
cell.putValue("Qtr3")
cell = cells.get("B7")
cell.putValue("Qtr4")
cell = cells.get("B8")
cell.putValue("Qtr3")

cell = cells.get("C2")
cell.putValue(1500)
cell = cells.get("C3")
cell.putValue(2000)
cell = cells.get("C4")
cell.putValue(600)
cell = cells.get("C5")
cell.putValue(1500)
cell = cells.get("C6")
cell.putValue(4070)
cell = cells.get("C7")
cell.putValue(5000)
cell = cells.get("C8")
cell.putValue(6430)

pivotTables = sheet.getPivotTables()
index = pivotTables.add("=A1:C8", "E3", "PivotTable2")
pivotTable = pivotTables.get(index)
pivotTable.setRowGrand(False)
pivotTable.addFieldToArea(PivotFieldType.ROW, 0)
pivotTable.addFieldToArea(PivotFieldType.COLUMN, 1)
pivotTable.addFieldToArea(PivotFieldType.DATA, 2)
workbook.save(dataDir + "pivotTable_test_out.xls")
jpype.shutdownJVM()
```

{{% alert color="primary" %}}
عند تعيين نطاق من الخلايا كمصدر بيانات، يجب أن يمتد النطاق من أعلى اليسار إلى أسفل اليمين. على سبيل المثال، "A1:C3" صالح ولكن "C3:A1" غير صالح.
{{% /alert %}}

## مقالات ذات صلة
- [Add Filter Fields to a Pivot Table in Aspose.Cells for Python via Java](/cells/ar/python-java/add-page-field-in-pivot-table/)
- [Apply Styles to Pivot Tables in Aspose.Cells for Python via Java](/cells/ar/python-java/apply-style-to-pivot-table/)
- [Modify Page Field Layout in Pivot Table](/cells/ar/python-java/change-page-field-layout/)
- [Filtering Pivot Tables by Label or Value](/cells/ar/python-java/filter-by-label-or-value-of-pivot-table/)
- [Manage Pivot Table Value Fields in Aspose.Cells for Python via Java](/cells/ar/python-java/manage-value-fields/)

{{< app/cells/assistant language="python" >}}