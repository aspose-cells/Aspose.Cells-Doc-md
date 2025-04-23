---
title: Convert Excel to JSON med C++
linktitle: Konvertera Excel till JSON
type: docs
weight: 300
url: /sv/cpp/convert-excel-to-json/
description: Lär dig hur man konverterar Excel fil till JSON med Aspose.Cells och C++.
keywords: Exportera arbetsbok till json utan Office 2013, Office 2016, Office 2019 och Office 365
---

{{% alert color="primary" %}}

Aspose.Cells stödjer att konvertera en arbetsbok till JSON-fil (JavaScript Object Notation).

{{% /alert %}}

## **Konvertera Excel-arbetsbok till JSON**

Det är ingen anledning att undra hur man konverterar Excel-arbetsbok till JSON, för bibliotek Aspose.Cells for C++ har den bästa lösningen. API:n Aspose.Cells stöder konvertering av kalkylblad till JSON-format. För att exportera arbetsboken till JSON, skicka [**SaveFormat.Json**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) som andra parameter till [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) metoden. Du kan även använda klassen [**JsonSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/jsonsaveoptions/) för att specificera ytterligare inställningar för export av kalkylblad till JSON.

Nedan visar kodexemplet export av Excel-arbetsbok till JSON. Se koden för att konvertera [källdokument](sample.xlsx) till den JSON-fil som genereras av koden för referens.

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

Nästa kodexempel använder JsonSaveOptions-klassen för att specificera ytterligare inställningar och visar export av Excel-arbetsbok till JSON. Se koden för att konvertera [källdokument](sample.xlsx) till den JSON-fil som genereras av koden för referens.

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

