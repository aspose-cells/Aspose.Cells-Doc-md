---
title: العمل مع ContentTypeProperties باستخدام C++
linktitle: العمل مع خصائص نوع الوسائط
type: docs
weight: 150
url: /ar/cpp/working-with-contenttypeproperties/
description: إضافة ContentTypeProperties مخصصة إلى ملف إكسل باستخدام Aspose.Cells مع C++.
---

يوفر Aspose.Cells طريقة [**Workbook.ContentTypeProperties.Add**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/contenttypepropertycollection/add/) لإضافة ContentTypeProperties مخصصة إلى ملف إكسل. يمكنك أيضًا جعل الخاصية اختيارية عن طريق تعيين خاصية [**ContentTypeProperty.IsNillable**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/contenttypeproperty/isnillable/) إلى **true**. يوضح مقتطف الكود التالي كيف يتم إضافة Properties مخصصة اختيارية إلى ملف إكسل. تُظهر الصورة التالية كلا الخاصيتين اللتين تمت إضافتهما بواسطة الكود النموذجي.

![todo:image_alt_text](working-with-contenttypeproperties_1.jpg)

يتم إرفاق ملف الإخراج الذي تم إنشاؤه بواسطة مقتطف الكود للإشارة.

[ملف الإخراج](95584314.xlsx)

## **الكود المثالي**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook with XLSX format
    Workbook workbook(FileFormatType::Xlsx);

    // Add content type properties
    int index = workbook.GetContentTypeProperties().Add(u"MK31", u"Simple Data");
    workbook.GetContentTypeProperties().Get(index).SetIsNillable(false);

    // Get current date and time
    time_t now = time(nullptr);
    char buffer[80];
    strftime(buffer, sizeof(buffer), "%Y-%m-%dT%H:%M:%S", localtime(&now));
    U16String dateTime(buffer);

    // Add another content type property with current date and time
    index = workbook.GetContentTypeProperties().Add(u"MK32", dateTime, u"DateTime");
    workbook.GetContentTypeProperties().Get(index).SetIsNillable(true);

    // Save the workbook
    workbook.Save(outDir + u"WorkingWithContentTypeProperties_out.xlsx");

    std::cout << "Content type properties added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
