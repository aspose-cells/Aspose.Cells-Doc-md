---
title: Zeichnen einer Zeitleiste beim Rendern von Excel nach PDF mit C++
linktitle: Zeitleiste beim Rendern von Excel in PDF zeichnen
type: docs
weight: 60
url: /de/cpp/draw-timeline-while-rendering-excel-to-pdf/
description: Verwalten Sie Zeitleisten von Excel Dateien mit Aspose.Cells für C++.
keywords: Zeitleiste ohne Office 2013, Office 2016, Office 2019 und Office 365 in PDF rendern
---

## **Zeitleiste beim Rendern von Excel in PDF zeichnen**
Wenn Sie eine Excel-Datei mit einer Zeitleiste haben und diese beim Export nach PDF mit den Zeitleisten-Einstellungen behalten möchten, unterstützt Aspose.Cells dies jetzt standardmäßig. Exportieren Sie einfach die Excel-Datei mit Zeitleiste nach PDF, und das erstellte PDF zeigt die Zeitleiste.

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](input.xlsx), die eine vorhandene Zeitachse enthält. Anschließend speichert er die Arbeitsmappe als [ausgegebene PDF-Datei](out.pdf). Der folgende Screenshot vergleicht die Quell-Excel-Datei und die generierte PDF-Datei.

<img src="out.png" width="60%">

## **Beispielcode**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file
    U16String inputFilePath(u"input.xlsx");
    std::unique_ptr<Workbook> wb = std::make_unique<Workbook>(inputFilePath);

    // Save file to pdf
    U16String outputFilePath(u"out.pdf");
    wb->Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Workbook saved successfully as PDF!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

```cpp
#include <aspose.cells.h>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();
    // Load the sample Excel file
    Workbook workbook(u"input.xlsx");

    // Save the workbook as a PDF file
    workbook.Save(u"output.pdf", SaveFormat::Pdf);
    Aspose::Cells::Cleanup();
    return 0;

}
```

