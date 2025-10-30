---
title: Hämta versionsnumret för applikationen som skapade Excel dokumentet med C++
linktitle: Hämta versionsnumret för applikationen
type: docs
weight: 210
url: /sv/cpp/get-the-version-number-of-the-application-that-created-the-excel-document/
description: Lär dig hur du hämtar versionsnumret för applikationen som skapade ett Excel dokument med Aspose.Cells och C++.
---

{{% alert color="primary" %}}

Du behöver ofta veta versionsnumret för programmet som skapade ett Microsoft Excel-dokument. Aspose.Cells tillhandahåller egenskapen [**Workbook.GetVersion()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getversion/) för detta ändamål.

{{% /alert %}}

Följande kodexempel visar användningen av [**Workbook.GetVersion()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getversion/) egenskapen. Den läser Excel-filer skapade med Microsoft Excel 2003, 2007, 2010 och 2013 och skriver ut versionsnumret för applikationen som skapade dessa Excel-dokument.

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
