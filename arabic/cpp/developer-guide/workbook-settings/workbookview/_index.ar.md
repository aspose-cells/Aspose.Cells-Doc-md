---
title: كيفية التحكم في عرض المصنف باستخدام C++
linktitle: كيفية التحكم في عرض دفتر العمل
type: docs
weight: 600
url: /ar/cpp/how-to-control-workbook-view/
description: تعلم كيفية التحكم في عرض المصنف باستخدام واجهة برمجة التطبيقات Aspose.Cells for C++.
keywords: كيفية التحكم في عرض دفتر العمل، تعيين عرض الإكسل، التحكم في عرض دفتر العمل، تعيين عرض دفتر العمل، التحكم في عرض الإكسل.
---

## **سيناريوهات الاستخدام المحتملة**
عند الحاجة لضبط عرض صفحات Excel، تحتاج إلى معرفة كيفية التحكم في كل وحدة، مثل أشرطة التمرير الأفقية والعمودية، وما إذا كنت تريد إخفاء ملفات Excel المفتوحة، وما إلى ذلك. يوفر ذلك Aspose.Cells. يوفر Aspose.Cells الخصائص والطرق التالية لمساعدتك على تحقيق أهدافك.

- [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/ishscrollbarvisible/)
- [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/isvscrollbarvisible/)
- [**WorkbookSettings.IsHidden**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/ishidden/)
- [**WorkbookSettings.IsMinimized**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/isminimized/)
- [**WorkbookSettings.GetWindowHeight()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getwindowheight/)
- [**WorkbookSettings.GetWindowWidth()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getwindowwidth/)
- [**WorkbookSettings.GetWindowLeft()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getwindowleft/)
- [**WorkbookSettings.GetWindowTop()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getwindowtop/)

## **كيفية التحكم في عرض المصنف باستخدام Aspose.Cells for C++**
يوضح هذا المثال كيف:

1. إنشاء دفتر عمل.
1. إضافة بيانات إلى الخلايا في ورقة العمل الأولى.
1. إخفاء شرائط التمرير الأفقية والعمودية لعرض دفتر العمل.

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
    cell = cells.Get(u"C1");
    cell.PutValue(u"Price");

    cell = cells.Get(u"A2");
    cell.PutValue(u"Apple");
    cell = cells.Get(u"A3");
    cell.PutValue(u"Mango");
    cell = cells.Get(u"A4");
    cell.PutValue(u"Blackberry");
    cell = cells.Get(u"A5");
    cell.PutValue(u"Cherry");

    cell = cells.Get(u"B2");
    cell.PutValue(5);
    cell = cells.Get(u"B3");
    cell.PutValue(3);
    cell = cells.Get(u"B4");
    cell.PutValue(6);
    cell = cells.Get(u"B5");
    cell.PutValue(4);

    cell = cells.Get(u"C2");
    cell.PutValue(5);
    cell = cells.Get(u"C3");
    cell.PutValue(20);
    cell = cells.Get(u"C4");
    cell.PutValue(30);
    cell = cells.Get(u"C5");
    cell.PutValue(60);

    // Apply style to cell E10
    cell = cells.Get(u"E10");
    Style temp = workbook.CreateStyle();
    temp.GetFont().SetColor(Color::Red());
    cell.SetStyle(temp);

    // Hide horizontal and vertical scrollbars
    workbook.GetSettings().SetIsHScrollBarVisible(false);
    workbook.GetSettings().SetIsVScrollBarVisible(false);

    // Save the workbook
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```

معاينة ملف النتائج:
<br>
<image src="result.png" width="70%" />
