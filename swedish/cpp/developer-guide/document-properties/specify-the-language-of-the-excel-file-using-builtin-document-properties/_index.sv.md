---
title: Specificera språket för Excel filen med inbyggda dokumentegenskaper med C++
linktitle: Specificera språket för Excel filen
type: docs
weight: 30
url: /sv/cpp/specify-the-language-of-the-excel-file-using-builtin-document-properties/
description: Lär dig att ändra språket för en Excel fil programmässigt med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

Du kan ändra språk för en Excel-fil genom att högerklicka på filen, välja Egenskaper > Detaljer och redigera fältet Språk. Använd [**BuiltInDocumentPropertyCollection.GetLanguage()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlanguage/)-egenskapen för att ändra det programmässigt med Aspose.Cells API:er.

## **Ange språket för Excel-filen med hjälp av inbyggda dokumentegenskaper**

Följande exempel kod skapar en arbetsbok och ändrar dess inbyggda dokumentegenskap som heter Språk. Kontrollera den [genererade Excel-filen](64716891.xlsx) och skärmbilden som visar det ändrade Språket med [**BuiltInDocumentPropertyCollection.GetLanguage()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlanguage/) egenskapen.

![todo:image_alt_text](specify-the-language-of-the-excel-file-using-builtin-document-properties_1.png)

## **Exempelkod**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Properties;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook wb;

    // Access built-in document property collection
    BuiltInDocumentPropertyCollection bdpc = wb.GetBuiltInDocumentProperties();

    // Set the language of the Excel file
    bdpc.SetLanguage(u"German, French");

    // Save the workbook in xlsx format
    wb.Save(u"..\\Data\\02_OutputDirectory\\outputSpecifyLanguageOfExcelFileUsingBuiltInDocumentProperties.xlsx", SaveFormat::Xlsx);

    std::cout << "Language set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
