---
title: تحويل Excel إلى JSON باستخدام C++
linktitle: تحويل Excel إلى JSON
type: docs
weight: 300
url: /ar/cpp/convert-excel-to-json/
description: تعلم كيفية تحويل ملف Excel إلى JSON باستخدام Aspose.Cells باستخدام C++.
keywords: تصدير الدفتر إلى JSON بدون Office 2013، Office 2016، Office 2019 و Office 365
---

{{% alert color="primary" %}}

تدعم Aspose.Cells تحويل دفتر العمل إلى ملف Json (كائن التبادل بيانات الجافا) .

{{% /alert %}}

## **تحويل دفتر العمل Excel إلى JSON**

لا حاجة للقلق حول كيفية تحويل ملف Excel إلى JSON، لأن مكتبة Aspose.Cells for C++ تقدم أفضل الحلول. توفر API Aspose.Cells دعمًا لتحويل جداول البيانات إلى تنسيق JSON. لتصدير دفتر العمل إلى JSON، مرر [**SaveFormat.Json**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) كوسيط ثانٍ لطريقة [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). يمكنك أيضًا استخدام فئة [**JsonSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/jsonsaveoptions/) لتحديد إعدادات إضافية لتصدير ورقة العمل إلى JSON.

يعرض المثال البرمجي التالي تصدير دفتر عمل Excel إلى JSON. يرجى مراجعة الكود لتحويل الملف المصدر (sample.xlsx) إلى ملف JSON الناتج بواسطة الكود للمراجعة.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    U16String inputFilePath(u"sample.xlsx");
    Workbook workbook(inputFilePath);

    // Convert the workbook to JSON file.
    U16String outputFilePath(u"sample_out.json");
    workbook.Save(outputFilePath, SaveFormat::Json);

    std::cout << "Workbook converted to JSON successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

يوضح المثال البرمجي التالي الذي يستخدم فئة JsonLoadOptions لتحديد إعدادات إضافية تصدير دفتر عمل Excel إلى JSON. يرجى مراجعة الكود لتحويل الملف المصدر (sample.xlsx) إلى ملف JSON الناتج بواسطة الكود للمراجعة.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create an options of saving the file.
    JsonSaveOptions options;

    // Set the exporting range.
    options.SetExportArea(CellArea::CreateCellArea(u"B1", u"C4"));

    // Load your source workbook
    Workbook workbook(u"sample.xlsx");

    // Convert the workbook to json file.
    workbook.Save(u"sample_out.json", options);

    std::cout << "Workbook successfully converted to JSON!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{< app/cells/assistant language="cpp" >}}
