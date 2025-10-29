---
title: Obtenir le numéro de version de l application qui a créé le document Excel avec C++
linktitle: Obtenir le numéro de version de l application
type: docs
weight: 210
url: /fr/cpp/get-the-version-number-of-the-application-that-created-the-excel-document/
description: Apprenez comment récupérer le numéro de version de l application qui a créé un document Excel en utilisant Aspose.Cells avec C++.
---

{{% alert color="primary" %}}

Souvent, vous avez besoin de connaître le numéro de version de l'application qui a créé un document Microsoft Excel. Aspose.Cells fournit la propriété [**Workbook.GetVersion()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getversion/) à cette fin.

{{% /alert %}}

Le code d'exemple suivant démontre l'utilisation de la propriété [**Workbook.GetVersion()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getversion/). Il charge des fichiers Excel créés avec Microsoft Excel 2003, 2007, 2010, et 2013 et affiche le numéro de version de l'application qui a créé ces documents Excel.

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
