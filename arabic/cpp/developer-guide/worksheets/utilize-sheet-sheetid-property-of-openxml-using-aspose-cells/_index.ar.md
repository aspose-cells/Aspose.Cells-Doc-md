---
title: استغل خاصية Sheet.SheetId من OpenXml باستخدام C++
linktitle: استغل خاصية Sheet.SheetId من OpenXml
type: docs
weight: 200
url: /ar/cpp/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/
description: يوضح هذا المقال كيفية استغلال خاصية Sheet.SheetId من OpenXml باستخدام واجهة برمجة تطبيقات أو مكتبة C++ لمعالجة إكسل بشكل برمجي.
keywords: معرف الورقة من نوع openxml c++، معرف ورقة العمل في إكسل باستخدام C++
---

## **سيناريوهات الاستخدام المحتملة**

يوجد الخاصية  *Sheet.SheetId* داخل *DocumentFormat.OpenXml.Spreadsheet* وهي جزء من OpenXml. يمكنك رؤية هذه الخاصية وقيمتها داخل *workbook.xml* كما هو موضح في اللقطة الشاشة التالية. توفر Aspose.Cells الخاصية المعادلة كـ [**Worksheet.GetTabId()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettabid/).

![todo:image_alt_text](utilize-sheet-sheetid-property-of-openxml-using-aspose-cells_1.png)

## **الاستفادة من خاصية Sheet.SheetId في الشكل المفتوحXML باستخدام Aspose.Cells**

يقوم الكود البرمجي العيني التالي بتحميل [ملف Excel عيني](51740716.xlsx)، يقرأ تعريف معرف ورقتها أو تبويبها، ثم يعين له معرف تبويب جديد ويحفظه ك[ملف Excel الناتج](51740717.xlsx). يرجى أيضاً النظر إلى مخرجات الكونسول المعروضة في الكود أدناه للإشارة.

## **الكود المثالي**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load source Excel file
    Workbook wb(u"sampleSheetId.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Print its Sheet or Tab Id on console
    std::cout << "Sheet or Tab Id: " << ws.GetTabId() << std::endl;

    // Change Sheet or Tab Id
    ws.SetTabId(358);

    // Save the workbook
    wb.Save(u"outputSheetId.xlsx");

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **مخرجات الوحدة**

{{< highlight java >}}

Sheet or Tab Id: 1297

{{< /highlight >}}
