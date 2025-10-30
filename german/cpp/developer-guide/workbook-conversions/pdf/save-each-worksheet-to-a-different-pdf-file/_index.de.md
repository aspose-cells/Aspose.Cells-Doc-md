---
title: Jede Arbeitsblatt in eine separate PDF Datei mit C++ speichern
linktitle: Jede Arbeitsblatt in eine separate PDF Datei speichern
type: docs
weight: 130
url: /de/cpp/save-each-worksheet-to-a-different-pdf-file/
description: Lernen Sie, wie Sie jedes Arbeitsblatt in einer Excel Datei mit Aspose.Cells for C++ in eine separate PDF Datei speichern.
---

{{% alert color="primary" %}} 

Aspose.Cells unterstützt die Konvertierung von XLS-Dateien (mit Bildern, Diagrammen usw.) in PDF-Dokumente. Aspose.Cells for C++ kann unabhängig arbeiten, um eine Tabelle in PDF umzuwandeln, ohne Aspose.PDF für C++ für die Konvertierung verwenden zu müssen. Die Konvertierung erfordert keine Software, um temporäre Dateien zu erstellen oder zu verwenden, da der gesamte Vorgang im Speicher erfolgen kann.

{{% /alert %}} 

## **Jedes Arbeitsblatt in eine separate PDF-Datei speichern**
Wenn Sie jede Tabelle in Ihrer Vorlage-Exceldatei in verschiedene PDF-Dateien speichern möchten, können Sie dies einfach erreichen. Versuchen Sie, einen Tabellenindex mit [**PdfSaveOptions.GetSheetSet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getsheetset/)-Option festzulegen, um diese in PDF zu rendern.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Get the Excel file path
    U16String filePath = srcDir + u"input.xlsx";

    // Instantiate a new workbook and open the Excel file from its location
    Workbook workbook(filePath);

    // Get the count of the worksheets in the workbook
    int sheetCount = workbook.GetWorksheets().GetCount();

    // Define PdfSaveOptions
    PdfSaveOptions pdfSaveOptions;

    // Take PDFs of each sheet
    for (int j = 0; j < sheetCount; j++)
    {
        Worksheet ws = workbook.GetWorksheets().Get(j);

        // Set worksheet to output
        SheetSet sheetSet(Vector<int32_t>{ ws.GetIndex() });
        pdfSaveOptions.SetSheetSet(sheetSet);

        // Save the workbook with the current worksheet as PDF
        workbook.Save(srcDir + u"worksheet-" + ws.GetName() + u".out.pdf", pdfSaveOptions);
    }

    std::cout << "PDFs generated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}} 

Wenn Ihre Tabelle Formeln enthält, ist es am besten, [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) direkt vor dem Rendern der Tabelle in das PDF-Format aufzurufen. Dadurch werden die formelabhängigen Werte neu berechnet und die korrekten Werte im PDF angezeigt.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
