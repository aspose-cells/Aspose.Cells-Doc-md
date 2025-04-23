---
title: إضافة حقل محسوب في جدول محوري باستخدام C++
linktitle: إضافة حقل محسوب في جدول الدوران
type: docs
weight: 130
url: /ar/cpp/add-calculated-field-in-pivot-table/
description: كيفية إضافة حقل محسوب في جدول محوري باستخدام Aspose.Cells for C++.
keywords: إضافة حقل محسوب في جدول الدوران.
---

## **سيناريوهات الاستخدام المحتملة**
عند إنشاء جدول دوران استنادًا إلى بيانات معروفة، تجد أن البيانات فيه ليست كما تريد. البيانات التي تريدها هي مجموعة من هذه البيانات الأصلية. على سبيل المثال، قد تحتاج إلى جمع، أو طرح، أو ضرب، وقسمة البيانات الأصلية قبل أن ترغب في البيانات. في هذا الوقت، تحتاج إلى بناء حقل محسوب وتعيين الصيغة المقابلة للحساب. ثم قم بإجراء بعض الإحصائيات والعمليات الأخرى على الحقل المحسوب. 

## **إضافة حقل محسوب في جدول دوران في Excel**
لإدراج حقل محسوب في جدول دوران في Excel، اتبع الخطوات التالية:

1. حدد جدول الدوران الذي تريد إضافة حقل محسوب إليه. 
2. انتقل إلى علامة تبويب تحليل جدول الدوران على شريط القوائم.
3. انقر على "الحقول والعناصر والمجموعات" ثم حدد "حقل محسوب" من القائمة المنسدلة.
4. في حقل الاسم، أدخل اسمًا للحقل المحسوب.
5. في حقل "Formula"، ادخل الصيغة للحساب الذي ترغب في القيام به باستخدام أسماء الحقول المحورية المناسبة والعمليات الرياضية. 
<br>
<img src="1.png" width=80% />
6. انقر "موافق" لإنشاء الحقل المحسوب.
7. سيظهر الحقل المحسوب الجديد في قائمة حقل PivotTable تحت قسم القيم.
8. اسحب الحقل المحسوب إلى قسم القيم في PivotTable لعرض القيم المحسوبة.
<br>
<img src="2.png" width=80% />

## **إضافة حقل محسوب في جدول محوري باستخدام C++**
إضافة حقل محسوب إلى ملف إكسل باستخدام Aspose.Cells. يُرجى الاطلاع على الشيفرة المرفقة. بعد تنفيذ شيفرة الأمثلة، سيتم إضافة جدول محوري مع حقل محسوب إلى ورقة العمل.
1. حدد البيانات الأصلية وأنشئ جدول محوري. 
2. أنشئ الحقل المحسوب وفقًا لحقل PivotField الحالي في الجدول المحوري.
3. أضف الحقل المحسوب إلى منطقة البيانات. 
4. أخيرًا، يحفظ الدفتر بتنسيق [XLSX الناتج](out.xlsx). 

## **الكود المثالي**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Creating a Workbook object
    Workbook workbook;

    // Obtaining the reference of the newly added worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Setting the values to the cells
    Cell cell = cells.Get("A1");
    cell.PutValue(u"Fruit");

    cell = cells.Get("B1");
    cell.PutValue(u"Count");

    cell = cells.Get("C1");
    cell.PutValue(u"Price");

    cell = cells.Get("A2");
    cell.PutValue(u"Apple");

    cell = cells.Get("A3");
    cell.PutValue(u"Mango");

    cell = cells.Get("A4");
    cell.PutValue(u"Blackberry");

    cell = cells.Get("A5");
    cell.PutValue(u"Cherry");

    cell = cells.Get("B2");
    cell.PutValue(5);

    cell = cells.Get("B3");
    cell.PutValue(3);

    cell = cells.Get("B4");
    cell.PutValue(6);

    cell = cells.Get("B5");
    cell.PutValue(4);

    cell = cells.Get("C2");
    cell.PutValue(5);

    cell = cells.Get("C3");
    cell.PutValue(20);

    cell = cells.Get("C4");
    cell.PutValue(30);

    cell = cells.Get("C5");
    cell.PutValue(60);

    // Adding a PivotTable to the worksheet
    int32_t i = ws.GetPivotTables().Add(u"=A1:C5", u"D10", u"PivotTable1");

    // Accessing the instance of the newly added PivotTable
    PivotTable pivotTable = ws.GetPivotTables().Get(i);
    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);

    // Adding a calculated field to PivotTable and dragging it to data area
    pivotTable.AddCalculatedField(u"total", u"=Count*Price", true);

    pivotTable.RefreshData();
    pivotTable.CalculateData();

    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```
