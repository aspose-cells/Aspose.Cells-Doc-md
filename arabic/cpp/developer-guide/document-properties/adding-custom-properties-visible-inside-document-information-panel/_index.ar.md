---
title: إضافة خصائص مخصصة مرئية داخل لوحة معلومات المستند باستخدام C++
linktitle: إضافة خصائص مخصصة مرئية داخل لوحة معلومات المستند
type: docs
weight: 300
url: /ar/cpp/adding-custom-properties-visible-inside-document-information-panel/
description: تعلّم كيفية إضافة خصائص مخصصة تظهر في لوحة معلومات المستند باستخدام Aspose.Cells مع C++.
---

## **إضافة خصائص مخصصة مرئية داخل لوحة معلومات الوثيقة**

يمكن استخدام Aspose.Cells لإضافة خصائص مخصصة داخل كائن جدول البيانات والتي يمكن رؤيتها داخل لوحة معلومات المستند. يمكنك فتح لوحة المعلومات المستندية في Microsoft Excel باستخدام أوامر قائمة الملف > معلومات > الخصائص > عرض قائمة معلومات المستند.

 يرجى استخدام طريقة [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/contenttypepropertycollection/add/) لإضافة خاصية مخصصة ستكون مرئية في لوحة معلومات المستند.

 يضيف رمز النموذج التالي خاصيتين مخصصتين. الخاصية الأولى بدون نوع معين والخاصية الثانية من نوع تاريخ ووقت. بمجرد فتح ملف إكسل الناتج الذي تم إنشاؤه بواسطة هذا الرمز، سترى هاتين الخاصيتين داخل لوحة معلومات المستند.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook object with specified format
    Workbook workbook(FileFormatType::Xlsx);

    // Add simple property without any type
    workbook.GetContentTypeProperties().Add(u"MK31", u"Simple Data");

    // Add date time property with type
    workbook.GetContentTypeProperties().Add(u"MK32", u"04-Mar-2015", u"DateTime");

    // Save the workbook
    workbook.Save(srcDir + u"AddingCustomPropertiesVisible_out.xlsx");

    std::cout << "Custom properties added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **مقال ذو صلة**

{{% alert color="primary" %}}

- [استخدام أجزاء XML المخصصة في Aspose.Cells](/cells/ar/cpp/use-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
