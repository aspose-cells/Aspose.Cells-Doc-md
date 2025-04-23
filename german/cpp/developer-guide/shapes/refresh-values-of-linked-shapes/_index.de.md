---
title: Aktualisieren Sie die Werte verbundener Formen mit C++
linktitle: Aktualisieren von Werten verknüpfter Formen
type: docs
weight: 3200
url: /de/cpp/refresh-values-of-linked-shapes/
description: Lernen Sie, wie Sie die Werte verbundener Formen in Excel Dateien mit Aspose.Cells for C++ aktualisieren.
---

{{% alert color="primary" %}}

Manchmal haben Sie eine verknüpfte Form in Ihrer Excel-Datei, die mit einigen Zellen verknüpft ist. In Microsoft Excel ändert sich beim Ändern des Werts der verknüpften Zelle auch der Wert der verknüpften Form. Dies funktioniert auch gut mit Aspose.Cells, wenn Sie Ihre Arbeitsmappe im XLS- oder XLSX-Format speichern möchten. Wenn Sie Ihre Arbeitsmappe jedoch im PDF- oder HTML-Format speichern möchten, müssen Sie die [**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/updateselectedvalue/)-Methode aufrufen, um den Wert der verknüpften Form zu aktualisieren.

{{% /alert %}}

## Beispiel

Das folgende Screenshot zeigt die Quell-Excel-Datei, die im untenstehenden Beispielcode verwendet wird. Es enthält ein verbundenes Bild, das mit den Zellen A1 bis E4 verknüpft ist. Wir werden den Wert der Zelle B4 mit Aspose.Cells ändern und dann die [**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/updateselectedvalue/)-Methode aufrufen, um den Wert des Bildes zu aktualisieren und als PDF zu speichern.

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)

Sie können die [Quell-Excel-Datei](95584291.xlsx) und das [Ausgabepdf](95584292.pdf) über die bereitgestellten Links herunterladen.

### C++-Code zum Aktualisieren der Werte verbundener Formen

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook from source file
    Workbook workbook(srcDir + u"sampleRefreshValueOfLinkedShapes.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Change the value of cell B4
    Cell cell = worksheet.GetCells().Get(u"B4");
    cell.PutValue(100);

    // Update the value of the Linked Picture which is linked to cell B4
    worksheet.GetShapes().UpdateSelectedValue();

    // Save the workbook in PDF format
    workbook.Save(outDir + u"outputRefreshValueOfLinkedShapes.pdf", SaveFormat::Pdf);

    std::cout << "Linked shapes value refreshed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
