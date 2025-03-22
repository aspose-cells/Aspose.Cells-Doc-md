---
title: Get the Version Number of the Application that Created the Excel Document with C++
linktitle: Get the Version Number of the Application
type: docs
weight: 210
url: /cpp/get-the-version-number-of-the-application-that-created-the-excel-document/
description: Learn how to retrieve the version number of the application that created an Excel document using Aspose.Cells with C++.
---

{{% alert color="primary" %}}

Often you need to know the version number of the application that created a Microsoft Excel document. Aspose.Cells provides the [**Workbook.BuiltInDocumentProperties.Version**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/version/) property for this purpose.

{{% /alert %}}

The following sample code demonstrates the use of the [**Workbook.BuiltInDocumentProperties.Version**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/version/) property. It loads Excel files created with Microsoft Excel 2003, 2007, 2010, and 2013 and prints the version number of the application that created these Excel documents.

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