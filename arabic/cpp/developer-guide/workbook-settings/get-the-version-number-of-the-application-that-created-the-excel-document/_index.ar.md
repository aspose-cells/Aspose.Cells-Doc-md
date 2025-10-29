---
title: الحصول على رقم إصدار التطبيق الذي أنشأ مستند Excel باستخدام C++
linktitle: الحصول على رقم إصدار التطبيق
type: docs
weight: 210
url: /ar/cpp/get-the-version-number-of-the-application-that-created-the-excel-document/
description: تعلم كيفية استرجاع رقم إصدار التطبيق الذي أنشأ مستند Excel باستخدام Aspose.Cells مع C++.
---

{{% alert color="primary" %}}

غالبًا ما تحتاج إلى معرفة رقم الإصدار للتطبيق الذي أنشأ مستند Microsoft Excel. توفر Aspose.Cells الخاصية [**Workbook.GetVersion()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getversion/) لهذا الغرض.

{{% /alert %}}

يوضح الكود النموذجي التالي استخدام الخاصية [**Workbook.GetVersion()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getversion/). يقوم بتحميل ملفات Excel التي أنشئت باستخدام Microsoft Excel 2003، 2007، 2010، و2013 ويطبع رقم إصدار التطبيق الذي أنشأ هذه المستندات Excel.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create a workbook reference
    Workbook workbook;

    // Print the version number of Excel 2003 XLS file
    workbook = Workbook(srcDir + u"Excel2003.xls");
    std::cout << "Excel 2003 XLS Version: " << workbook.GetBuiltInDocumentProperties().GetVersion().ToUtf8() << std::endl;

    // Print the version number of Excel 2007 XLS file
    workbook = Workbook(srcDir + u"Excel2007.xls");
    std::cout << "Excel 2007 XLS Version: " << workbook.GetBuiltInDocumentProperties().GetVersion().ToUtf8() << std::endl;

    // Print the version number of Excel 2010 XLS file
    workbook = Workbook(srcDir + u"Excel2010.xls");
    std::cout << "Excel 2010 XLS Version: " << workbook.GetBuiltInDocumentProperties().GetVersion().ToUtf8() << std::endl;

    // Print the version number of Excel 2013 XLS file
    workbook = Workbook(srcDir + u"Excel2013.xls");
    std::cout << "Excel 2013 XLS Version: " << workbook.GetBuiltInDocumentProperties().GetVersion().ToUtf8() << std::endl;

    // Print the version number of Excel 2007 XLSX file
    workbook = Workbook(srcDir + u"Excel2007.xlsx");
    std::cout << "Excel 2007 XLSX Version: " << workbook.GetBuiltInDocumentProperties().GetVersion().ToUtf8() << std::endl;

    // Print the version number of Excel 2010 XLSX file
    workbook = Workbook(srcDir + u"Excel2010.xlsx");
    std::cout << "Excel 2010 XLSX Version: " << workbook.GetBuiltInDocumentProperties().GetVersion().ToUtf8() << std::endl;

    // Print the version number of Excel 2013 XLSX file
    workbook = Workbook(srcDir + u"Excel2013.xlsx");
    std::cout << "Excel 2013 XLSX Version: " << workbook.GetBuiltInDocumentProperties().GetVersion().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
