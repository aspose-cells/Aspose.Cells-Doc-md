---
title: Spara ODS fil i ODF 1.1, 1.2 och 1.3 specifikationer med C++
linktitle: Spara som ODF 1.1, 1.2 och 1.3
description: Konvertera Excel till ODF 1.1, 1.2 och 1.3 specifikationer med Aspose.Cells och C++.
type: docs
weight: 230
url: /sv/cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cells stöder att spara en ODS-fil (**OpenDocument Spreadsheet**) i ODF (**OpenDocument Format**) 1.1, 1.2 och 1.3 specifikationer. Aspose.Cells har egenskapen [**OdsSaveOptions.GetOdfStrictVersion()**](https://reference.aspose.com/cells/cpp/aspose.cells/odssaveoptions/getodfstrictversion/) som specificerar ODF-versionen för att spara ODS-filer. Standardvärdet för denna egenskap är [**OpenDocumentFormatVersionType.Odf12**](https://reference.aspose.com/cells/cpp/aspose.cells.ods/opendocumentformatversiontype/), så ODS-filen som sparas utan denna inställning använder 1.2-specifikationerna.

{{% /alert %}}

Nedan skapar exempel på kod ett arbetsboksobjekt, lägger till ett värde i cell A1 på första arbetsbladet och sparar sedan ODS-filen i ODF 1.1, 1.2 och 1.3-specifikationer. Som standard sparas ODS-filen i ODF 1.2-specifikation.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put some value in cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");
    cell.PutValue(u"Welcome to Aspose!");

    // Save ODS in ODF 1.2 version which is default
    OdsSaveOptions options;
    workbook.Save(outDir + u"ODF1.2_out.ods", options);

    // Save ODS in ODF 1.1 version
    options.SetOdfStrictVersion(OpenDocumentFormatVersionType::Odf11);
    workbook.Save(outDir + u"ODF1.1_out.ods", options);

    // Save ODS in ODF 1.3 version
    options.SetOdfStrictVersion(OpenDocumentFormatVersionType::Odf13);
    workbook.Save(outDir + u"ODF1.3_out.ods", options);

    std::cout << "ODS files saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
