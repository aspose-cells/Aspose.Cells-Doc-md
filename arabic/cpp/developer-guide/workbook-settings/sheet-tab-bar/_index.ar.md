---
title: كيفية التحكم في شريط علامات تبويب الورقة باستخدام C++
linktitle: كيفية التحكم في شريط علامة الورقة
type: docs
weight: 600
url: /ar/cpp/how-to-control-sheet-tab-bar/
description: تعلم كيفية التحكم في شريط علامات تبويب الورقة من خلال واجهة برمجة التطبيقات Aspose.Cells for C++.
keywords: كيفية التحكم في شريط تبويب الورقة، تشغيل شريط تبويب الورقة، تعيين شريط تبويب الورقة، التحكم في شريط تبويب الورقة. 
---

## **سيناريوهات الاستخدام المحتملة**
عند الحاجة لضبط عرض شريط صفحات Excel، تحتاج إلى معرفة كيفية التحكم في علامة تبويب الورقة، مثل إخفاؤها أو إظهارها، وتغيير عرض الشريط، وتحديد التبويب المرئي الأول، وما إلى ذلك. يدعم Aspose.Cells هذه الميزات. يوفر Aspose.Cells الخصائص والطرق التالية لمساعدتك على تحقيق أهدافك.

- [**WorkbookSettings.GetShowTabs()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshowtabs/)
- [**WorkbookSettings.GetSheetTabBarWidth()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getsheettabbarwidth/)
- [**WorkbookSettings.GetFirstVisibleTab()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getfirstvisibletab/)

## **كيفية التحكم في شريط علامات تبويب الورقة باستخدام Aspose.Cells for C++**
يوضح هذا المثال كيف:

1. إنشاء دفتر عمل.
1. إضافة بيانات إلى الخلايا في ورقة العمل الأولى.
1. عرض علامة الورقة وتعيين عرض شريط التبويب.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook object
    Workbook workbook;

    // Obtain the reference to the newly added worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Setting the value to the cells
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

    // Display the sheet tab and set the width of the tab bar
    workbook.GetSettings().SetShowTabs(true);
    workbook.GetSettings().SetSheetTabBarWidth(150);

    // Save the workbook
    workbook.Save(u"out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

معاينة ملف النتائج:
<br>
<image src="result.png" width="70%" />

{{< app/cells/assistant language="cpp" >}}
