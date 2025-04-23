---
title: Berechnung der Excel 2016 MINIFS und MAXIFS Funktionen mit C++
description: Dieser Artikel stellt vor, wie man mit der Aspose.Cells Bibliothek die MINIFS und MAXIFS Funktionen in Microsoft Excel 2016 mit C++ berechnet.
keywords: Aspose.Cells, Excel, 2016, MINIFS Funktion, MAXIFS Funktion, Berechnung
type: docs
weight: 300
url: /de/cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/
---

## **Mögliche Verwendungsszenarien**
 Microsoft Excel 2016 unterstützt MINIFS- und MAXIFS-Funktionen. Diese Funktionen werden in Excel 2013 oder früheren Versionen nicht unterstützt. Aspose.Cells unterstützt ebenfalls die Berechnung dieser Funktionen. Das folgende Screenshot zeigt die Verwendung dieser Funktionen. Lesen Sie die roten Kommentare im Screenshot, um zu erfahren, wie diese Funktionen funktionieren.

![todo:image_alt_text](calculation-of-excel-2016-minifs-and-maxifs-functions_1.png)

## **Berechnung der Excel 2016 MINIFS- und MAXIFS-Funktionen**
 Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](5115149.xlsx) und ruft die Methode [Workbook.CalculateFormula()](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) auf, um die Formelbechnung mit Aspose.Cells durchzuführen, und speichert dann die Ergebnisse in der [Ausgabe-PDF](5115154.pdf).

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/PdfSaveOptions.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load your source workbook containing MINIFS and MAXIFS functions
    Workbook workbook(srcDir + u"sampleMINIFSAndMAXIFS.xlsx");

    // Perform Aspose.Cells formula calculation
    workbook.CalculateFormula();

    // Save the calculations result in pdf format
    PdfSaveOptions options;
    options.SetOnePagePerSheet(true);
    workbook.Save(outDir + u"outputMINIFSAndMAXIFS.pdf", options);

    std::cout << "PDF saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
