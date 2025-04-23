---
title: Specificera dokumentversion av Excel filen med inbyggda dokumentegenskaper med C++
linktitle: Specificera dokumentversion
type: docs
weight: 20
url: /sv/cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/
description: Lär dig att specificera dokumentversionen av en Excel fil med hjälp av inbyggda dokumentegenskaper och Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

Du kan ändra **Version-nummer** på en Excel-fil genom att högerklicka på filen, välja Egenskaper > Detaljer och redigera fältet **Version-nummer**. Använd [**BuiltInDocumentPropertyCollection.GetDocumentVersion()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getdocumentversion/)-egenskapen för att ändra det programmässigt med Aspose.Cells API:er.

## **Ange dokumentversionen för Excel-filen med hjälp av inbyggda dokumentegenskaper**

Följande exempel kod skapar en arbetsbok och ändrar dess inbyggda dokumentegenskaper, inklusive Titel, Författare och Versionsnummer. Kontrollera den [genererade Excel-filen](64716811.xlsx) och skärmbilden som visar det ändrade Versionsnumret med [**BuiltInDocumentPropertyCollection.GetDocumentVersion()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getdocumentversion/) egenskapen.

![todo:image_alt_text](specify-document-version-of-the-excel-file-using-builtin-document-properties_1.png)

## **Exempelkod**

```cpp
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

    // Set the title
    bdpc.SetTitle(u"Aspose File Format APIs");

    // Set the author
    bdpc.SetAuthor(u"Aspose APIs Developers");

    // Set the document version
    bdpc.SetDocumentVersion(u"Aspose.Cells Version - 18.3");

    // Save the workbook in xlsx format
    wb.Save(u"outputSpecifyDocumentVersionOfExcelFile.xlsx", SaveFormat::Xlsx);

    std::cout << "Document properties set and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
