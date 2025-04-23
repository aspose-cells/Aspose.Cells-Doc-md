---
title: تعيين حدود النطاق باستخدام C++
type: docs
weight: 600
url: /ar/cpp/set-range-border/
description: تعلم كيفية تعيين حدود النطاق باستخدام Aspose.Cells مع C++.
---

## **سيناريوهات الاستخدام المحتملة**
عندما ترغب في تعيين الحد لنطاق، لست بحاجة إلى تعيين كل خلية على حدة. يمكنك تعيين الحد على النطاق. يوفر Aspose.Cells هذه الميزة. توفر هذه المقالة رمزًا نموذجيًا يستخدم Aspose.Cells لتعيين حد النطاق.

## **تعيين حدود النطاق في Excel**
لتعيين الحدود لنطاق في Excel، يمكنك اتباع هذه الخطوات:
1. حدد نطاق الخلايا التي ترغب في تطبيق الحد لها.
2. في علامة التبويب "الرئيسية" في الشريط، ابحث عن مجموعة "الخط".
3. ضمن مجموعة "الخط"، انقر فوق زر القائمة المنسدلة "الحدود".
<br>
<img src="border.png" />
4. اختر نوع الحد الذي ترغب في تطبيقه من الخيارات المتاحة في القائمة المنسدلة. يمكنك اختيار أنماط الحدود المعدة مسبقًا أو تخصيص حدودك الخاصة.
5. بمجرد اختيارك لنمط الحد المطلوب، سيتم تطبيق الحد على النطاق المحدد من الخلايا.

## **تعيين حدود النطاق باستخدام Aspose.Cells**
يوضح هذا المثال كيف:

1. إنشاء دفتر عمل.
2. إضافة البيانات إلى خلايا في ورقة العمل الأولى.
3. إنشاء [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range).
4. تعيين الحد الداخلي للنطاق.
5. تعيين الحد الخارجي للنطاق.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new Workbook object
    Workbook workbook;

    // Obtain the reference of the newly added worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Setting the value to the cells
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

    // Create a range (A1:C5)
    Range range = cells.CreateRange(u"A1", u"C5");

    // Set inner border of range
    CellsColor innerColor = workbook.CreateCellsColor();
    innerColor.SetColor(Color::Red());
    range.SetInsideBorders(BorderType::Vertical, CellBorderType::Thin, innerColor);
    innerColor.SetColor(Color::Green());
    range.SetInsideBorders(BorderType::Horizontal, CellBorderType::Thin, innerColor);

    // Set outer border of range
    CellsColor outerColor = workbook.CreateCellsColor();
    outerColor.SetColor(Color::Blue());
    range.SetOutlineBorders(CellBorderType::Thin, outerColor);

    // Save the Workbook
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```
