---
title: مصفاة جدول محوري باستخدام C++
linktitle: مصفاة جدول محوري
type: docs
weight: 130
url: /ar/cpp/add-or-clear-pivot-filter/
description: تعرف على كيفية إضافة مرشح في جدول محوري باستخدام Aspose.Cells باستخدام C++.
keywords: إضافة فلتر في جدول الدوران دون مكتب 2013 أو مكتب 2016 أو مكتب 2019 ومكتب 365.
---

## **سيناريوهات الاستخدام المحتملة**
عندما تنشئ جدول محوري ببيانات معروفة وتريد تصفية الجدول المحوري، تحتاج إلى التعلم واستخدام التصفية. يمكن أن تساعدك في تصفية البيانات التي تريدها بفعالية. باستخدام واجهة برمجة تطبيقات Aspose.Cells، يمكنك إضافة وإزالة التصفية على قيم الحقول في الجداول المحورية. 

## **إضافة تصفية في جدول محوري في إكسل**
إضافة تصفية في جدول محوري في إكسل، اتبع هذه الخطوات:

1. حدد الجدول الدوري Pivot الذي تريد مسح الفلتر منه. 
2. انقر على السهم المنسدل على التصفية التي تريد إضافتها في الجدول المحوري.
3. اختر "أعلى 10" من القائمة المنسدلة.
<br>
<img src="3.png" width=80% />
4. حدد وضع العرض وعدد التصفية.
<br>
<img src="4.png" width=80% />

## **إضافة تصفية في الجدول المحوري**
يرجى رؤية الرمز البريدي العيني التالي. يقوم بتعيين البيانات وإنشاء جدول بيانات محوري بناءً عليها. ثم إضافة فلتر على حقل الصف لجدول البيانات المحوري. أخيرًا، يحفظ الدفتر بتنسيق [XLSX الناتج](filterout.xlsx). بعد تنفيذ رمز المثال، يتم إضافة جدول بيانات محوري بفلتر top10 إلى ورقة العمل.

### **الكود المثالي**
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Set values to cells
    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Fruit");
    cell = cells.Get(u"B1");
    cell.PutValue(u"Count");

    cell = cells.Get(u"A2");
    cell.PutValue(u"Apple");
    cell = cells.Get(u"A3");
    cell.PutValue(u"Mango");
    cell = cells.Get(u"A4");
    cell.PutValue(u"Blackberry");
    cell = cells.Get(u"A5");
    cell.PutValue(u"Cherry");
    cell = cells.Get(u"A6");
    cell.PutValue(u"Guava");
    cell = cells.Get(u"A7");
    cell.PutValue(u"Carambola");
    cell = cells.Get(u"A8");
    cell.PutValue(u"Banana");
    cell = cells.Get(u"B2");
    cell.PutValue(5);
    cell = cells.Get(u"B3");
    cell.PutValue(3);
    cell = cells.Get(u"B4");
    cell.PutValue(6);
    cell = cells.Get(u"B5");
    cell.PutValue(4);
    cell = cells.Get(u"B6");
    cell.PutValue(5);
    cell = cells.Get(u"B7");
    cell.PutValue(2);
    cell = cells.Get(u"B8");
    cell.PutValue(20);

    // Add a PivotTable to the worksheet
    int32_t i = ws.GetPivotTables().Add(u"=A1:B8", u"D10", u"PivotTable1");

    // Access the instance of the newly added PivotTable
    PivotTable pivotTable = ws.GetPivotTables().Get(i);
    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);

    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Count");
    pivotTable.GetDataFields().Get(0).SetFunction(ConsolidationFunction::Sum);

    PivotField field = pivotTable.GetRowFields().Get(0);
    field.SetIsAutoSort(true);
    field.SetIsAscendSort(false);
    field.SetAutoSortField(0);

    // Add top10 filter
    PivotField filterField = pivotTable.GetRowFields().Get(0);
    filterField.FilterTop10(0, PivotFilterType::Count, false, 5);

    pivotTable.RefreshData();
    pivotTable.CalculateData();

    // Save the workbook
    workbook.Save(u"filterout.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **مسح التصفية في الجدول المحوري في إكسل**
مسح الفلتر في الجدول الدوري Pivot في Excel، اتبع هذه الخطوات:

1. حدد الجدول الدوري Pivot الذي تريد مسح الفلتر منه. 
2. انقر على السهم المنسدل للفلتر الذي تريد مسحه في الجدول الدوري Pivot.
3. حدد "مسح الفلتر" من القائمة المنسدلة.
<br>
<img src="1.png" width=80% />
4. إذا كنت ترغب في مسح جميع الفلاتر من الجدول الدوري Pivot، يمكنك أيضًا النقر فوق زر "مسح الفلاتر" في علامة PivotTable Analyze في شريط الشريط في Excel.
<br>
<img src="2.png" width=80% />

## **مسح التصفية في الجدول المحوري**
مسح التصفية في الجدول المحوري باستخدام Aspose.Cells. يرجى الرجوع إلى الشيفرة المرفقة التالية. 
1. ضع البيانات وأنشئ جدول محوري استنادًا إليها. 
2. أضف تصفيةً إلى حقل الصف في الجدول المحوري. 
3. احفظ الدفتر في تنسيق [XLSX الناتج](out_add.xlsx). بعد تنفيذ الشيفرة المثالية، سيتم إضافة جدول محوري مع تصفية أعلى 10 إلى ورقة العمل. 
4. أمسح التصفية على حقل محدد في الجدول المحوري. بعد تنفيذ الشيفرة لمسح التصفية، سيتم مسح التصفية على الحقل المحدد. يرجى التحقق من [XLSX الناتج](out_delete.xlsx).

### **الكود المثالي**
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Set values to cells
    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Fruit");
    cell = cells.Get(u"B1");
    cell.PutValue(u"Count");

    cell = cells.Get(u"A2");
    cell.PutValue(u"Apple");
    cell = cells.Get(u"A3");
    cell.PutValue(u"Mango");
    cell = cells.Get(u"A4");
    cell.PutValue(u"Blackberry");
    cell = cells.Get(u"A5");
    cell.PutValue(u"Cherry");
    cell = cells.Get(u"A6");
    cell.PutValue(u"Guava");
    cell = cells.Get(u"A7");
    cell.PutValue(u"Carambola");
    cell = cells.Get(u"A8");
    cell.PutValue(u"Banana");
    cell = cells.Get(u"B2");
    cell.PutValue(5);
    cell = cells.Get(u"B3");
    cell.PutValue(3);
    cell = cells.Get(u"B4");
    cell.PutValue(6);
    cell = cells.Get(u"B5");
    cell.PutValue(4);
    cell = cells.Get(u"B6");
    cell.PutValue(5);
    cell = cells.Get(u"B7");
    cell.PutValue(2);
    cell = cells.Get(u"B8");
    cell.PutValue(20);

    // Add a PivotTable to the worksheet
    int i = ws.GetPivotTables().Add(u"=A1:B8", u"D10", u"PivotTable1");

    // Access the instance of the newly added PivotTable
    PivotTable pivotTable = ws.GetPivotTables().Get(i);
    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);

    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Count");
    pivotTable.GetDataFields().Get(0).SetFunction(ConsolidationFunction::Sum);

    PivotField field = pivotTable.GetRowFields().Get(0);
    field.SetIsAutoSort(true);
    field.SetIsAscendSort(false);
    field.SetAutoSortField(0);

    // Add top10 filter
    PivotField filterField = pivotTable.GetRowFields().Get(0);
    filterField.FilterTop10(0, PivotFilterType::Count, false, 5);

    pivotTable.RefreshData();
    pivotTable.CalculateData();

    workbook.Save(u"out_add.xlsx");

    // Clear PivotFilter from the specific PivotField
    pivotTable.GetPivotFilters().ClearFilter(field.GetBaseIndex());
    pivotTable.RefreshData();
    pivotTable.CalculateData();

    workbook.Save(u"out_delete.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
