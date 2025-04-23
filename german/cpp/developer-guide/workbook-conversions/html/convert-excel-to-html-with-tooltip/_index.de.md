---
title: Excel in HTML mit Tooltip konvertieren mit C++
linktitle: Excel in HTML mit Tooltip konvertieren
type: docs
weight: 200
url: /de/cpp/convert-excel-to-html-with-tooltip/
description: Excel in HTML konvertieren, während Tooltips mit Aspose.Cells und C++ hinzugefügt werden.
---

## **Excel in HTML mit Tooltip konvertieren**

Es kann Fälle geben, in denen der Text im generierten HTML abgeschnitten ist und Sie möchten den vollständigen Text als Tooltip beim Hover-Ereignis anzeigen. Aspose.Cells unterstützt dies durch Bereitstellung der [**HtmlSaveOptions.GetAddTooltipText()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getaddtooltiptext/)-Eigenschaft. Das Setzen der [**HtmlSaveOptions.GetAddTooltipText()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getaddtooltiptext/)-Eigenschaft auf **true** fügt den vollständigen Text als Tooltip im generierten HTML hinzu.

Das folgende Bild zeigt den Tooltip in der generierten HTML-Datei.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

 Das folgende Code-Beispiel lädt die [Quellexcel-Datei](98107416.xlsx) und generiert die [Ausgabe-HTML-Datei](98107417.zip) mit Tooltip.

Beispielcode

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/HtmlSaveOptions.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");

    // Open the template file
    Workbook workbook(sourceDir + u"AddTooltipToHtmlSample.xlsx");

    // Setup HTML save options
    HtmlSaveOptions options;
    options.SetAddTooltipText(true);  // Enable tooltip text in output

    // Save as HTML
    workbook.Save(outputDir + u"AddTooltipToHtmlSample_out.html", options);

    std::cout << "Workbook saved with tooltip text added!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
