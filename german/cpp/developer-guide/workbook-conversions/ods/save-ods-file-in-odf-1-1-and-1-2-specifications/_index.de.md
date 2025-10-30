---
title: ODS Datei in ODF 1.1, 1.2 und 1.3 mit C++ speichern
linktitle: Als ODF 1.1, 1.2 und 1.3 speichern
description: Excel in ODF 1.1, 1.2 und 1.3 mit Aspose.Cells unter Verwendung von C++ konvertieren.
type: docs
weight: 230
url: /de/cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt das Speichern einer ODS-Datei (**OpenDocument Tabelle**) im ODF (**OpenDocument Format**) 1.1, 1.2 und 1.3 Spezifikationen. Aspose.Cells hat [**OdsSaveOptions.GetOdfStrictVersion()**](https://reference.aspose.com/cells/cpp/aspose.cells/odssaveoptions/getodfstrictversion/) Eigenschaft, die die ODF-Version für das Speichern von ODS-Dateien angibt. Der Standardwert dieser Eigenschaft ist [**OpenDocumentFormatVersionType.Odf12**](https://reference.aspose.com/cells/cpp/aspose.cells.ods/opendocumentformatversiontype/), daher verwendet die gespeicherte ODS-Datei ohne diese Einstellung die Spezifikation 1.2.

{{% /alert %}}

Der folgende Beispielcode erstellt ein Arbeitsmappe-Objekt, fügt einigen Wert in Zelle A1 auf dem ersten Arbeitsblatt hinzu und speichert dann die ODS-Datei in den ODF 1.1, 1.2 und 1.3 Spezifikationen. Standardmäßig wird die ODS-Datei im ODF 1.2 Spezifikation gespeichert.

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
{{< app/cells/assistant language="cpp" >}}
