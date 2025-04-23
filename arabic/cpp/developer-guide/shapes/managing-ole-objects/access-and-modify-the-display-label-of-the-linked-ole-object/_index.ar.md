---
title: الوصول وتعديل تسمية العرض للصورة المرتبطة بواسطة ++C
linktitle: الوصول إلى وتعديل التسمية العرضية لكائن Ole المرتبط
type: docs
weight: 100
url: /ar/cpp/access-and-modify-the-display-label-of-the-linked-ole-object/
description: تعلم كيف تصل وتعدل تسمية العرض للكائنات Ole المرتبطة في ملفات إكسل باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

يتيح لك Microsoft Excel تغيير تسمية العرض للكائن Ole كما هو موضح في لقطة الشاشة التالية. يمكنك أيضًا الوصول أو تعديل تسمية العرض للكائن Ole باستخدام واجهات برمجة التطبيقات الخاصة بـ Aspose.Cells مع [**GetLabel()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getlabel/) و [**SetLabel(const U16String\& value)**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/setlabel/).

![todo:image_alt_text](access-and-modify-the-display-label-of-the-linked-ole-object_1.png)

## **الوصول إلى وتعديل التسمية العرضية لكائن Ole المرتبط**

يرجى الاطلاع على كود العينة التالي، يقوم بتحميل [ملف الإكسل عينة](64716810.xlsx) الذي يحتوي على كائن Ole. يقوم الكود بالوصول إلى كائن Ole وتغيير تسميته من Sample APIs إلى Aspose APIs. الرجاء الاطلاع على إخراج وحدة التحكم المطبوع أدناه الذي يظهر تأثير كود العينة على ملف الإكسل العينة للإشارة.

## **الكود المثالي**

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Load the sample Excel file
    U16String inputFilePath = u"sampleAccessAndModifyLabelOfOleObject.xlsx";
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first Ole Object
    OleObject oleObject = ws.GetOleObjects().Get(0);

    // Display the Label of the Ole Object
    std::cout << "Ole Object Label - Before: " << oleObject.GetLabel().ToUtf8() << std::endl;

    // Modify the Label of the Ole Object
    oleObject.SetLabel(u"Aspose APIs");

    // Save workbook to memory stream
    auto ms = wb.SaveToStream();

    // Set the workbook reference to null
    wb = Workbook();

    // Load workbook from memory stream
    wb = Workbook(ms);

    // Access first worksheet
    ws = wb.GetWorksheets().Get(0);

    // Access first Ole Object
    oleObject = ws.GetOleObjects().Get(0);

    // Display the Label of the Ole Object that has been modified earlier
    std::cout << "Ole Object Label - After: " << oleObject.GetLabel().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **مخرجات الوحدة**

{{< highlight java >}}

Ole Object Label - Before: Sample APIs

Ole Object Label - After: Aspose APIs

{{< /highlight >}}
