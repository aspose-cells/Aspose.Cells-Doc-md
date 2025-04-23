---
title: Konvertera arbetsbok till JSON med C++
linktitle: Konvertera arbetsbok till JSON
type: docs
weight: 300
url: /sv/cpp/convert-workbook-to-json/
description: Lär dig hur man konverterar Excel arbetsböcker till JSON format med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells stödjer konvertering av en arbetsbok till JSON (JavaScript Object Notation).

{{% /alert %}}

## **Konvertera Excel-arbetsbok till JSON**

API:et Aspose.Cells ger stöd för att konvertera kalkylblad till JSON-format. För att exportera arbetsboken till JSON, skicka [**SaveFormat::Json**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) som andra parameter till [**Workbook::Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) metoden. Du kan också använda [**JsonSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/jsonsaveoptions/)-klassen för att specificera ytterligare inställningar för export av arbetsbladet till JSON.

Följande kodexempel visar hur man exporterar det aktiva arbetsbladet till JSON med hjälp av [**SaveFormat::Json**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) enum-medlem. Se koden för att konvertera [källfilen](book1.xlsx) till [utdata JSON-fil](book1.json) som genereras av koden för referens.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Save the workbook as JSON
    U16String outputFilePath = srcDir + u"book1.json";
    workbook.Save(outputFilePath);

    std::cout << "Workbook converted to JSON successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Avancerade ämnen**
- [Konvertera CSV till JSON](/cells/sv/cpp/convert-csv-to-json/)
- [Konvertera Excel till JSON](/cells/sv/cpp/convert-excel-to-json/)
- [Konvertera JSON till CSV](/cells/sv/cpp/convert-json-to-csv/)
- [Konvertera JSON till Excel](/cells/sv/cpp/convert-json-to-excel/)
