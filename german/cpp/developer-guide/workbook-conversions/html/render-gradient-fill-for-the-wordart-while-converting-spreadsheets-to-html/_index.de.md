---
title: Gradient Füllung für WordArt beim Konvertieren von Tabellen in HTML mit C++ rendern
linktitle: Verlaufsfüllung für den WordArt beim Konvertieren von Tabellenkalkulationen in HTML rendern
type: docs
weight: 90
url: /de/cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/
description: Lernen Sie, den Farbverlauf für WordArt beim Konvertieren von Tabellen in HTML mit C++ zu rendern.
---

## **Mögliche Verwendungsszenarien**
Vor Aspose.Cells 17.1 konnte Aspose.Cells den Gradientenfüllungseffekt der WordArt nicht rendern, wenn die Excel-Datei in HTML-Format konvertiert wurde. Seit der Veröffentlichung von Aspose.Cells 17.1 wird die Gradientenfüllung der WordArt jedoch unterstützt. Der folgende Screenshot vergleicht den Effekt der Gradientenfüllung durch die Konvertierung der Excel-Datei mit Aspose.Cells 17.1 und der älteren Version.

![todo:image_alt_text](render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to-html_1.png)
## **Verlaufsfüllung für den WordArt beim Konvertieren von Tabellenkalkulationen in HTML rendern**
Der folgende Beispielcode konvertiert die [Quell-Excel-Datei](22774111.xlsx) in das [Ausgabe-HTML-Format](22774109.zip). Die Quell-Excel-Datei enthält ein WordArt-Objekt mit Gradientenfüllung, wie im obigen Screenshot gezeigt.
## **Beispielcode**
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

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sourceGradientFill.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Save workbook to HTML format
    workbook.Save(outDir + u"out_sourceGradientFill.html");

    std::cout << "Workbook saved successfully in HTML format!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
