---
title: Verstecken von überlagertem Inhalt mit CrossHideRight beim Speichern nach HTML mit C++
linktitle: Verbergen von überlagertem Inhalt mit CrossHideRight beim Speichern als HTML
type: docs
weight: 100
url: /de/cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/
description: Verwenden Sie CrossHideRight mit Aspose.Cells in C++, um überlagerten Inhalt beim Speichern nach HTML zu verbergen.
---

## **Mögliche Verwendungsszenarien**

Beim Speichern Ihrer Excel-Datei als HTML können Sie verschiedene Kreuztypen für Zelltexte angeben. Standardmäßig generiert Aspose.Cells HTML entsprechend Microsoft Excel. Wenn Sie den Kreuztyp auf [**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype) ändern, werden alle Textüberlagerungen oder Überlappungen rechts im Zelltext verborgen.

## **Verstecken überlagerter Inhalte mit CrossHideRight beim Speichern in Html**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](64716894.xlsx) und speichert sie nach [Ausgabe-HTML](64716893.zip), nachdem [**HtmlSaveOptions.GetHtmlCrossStringType()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/gethtmlcrossstringtype/) auf [**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype) gesetzt wurde. Der Screenshot zeigt, wie [**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype) die Ausgabe-HTML vom Standard beeinflusst.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Beispielcode**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample Excel file
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    Workbook wb(sourceDir + u"sampleHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.xlsx");

    // Specify HtmlSaveOptions - Hide Overlaid Content with CrossHideRight while saving to Html
    HtmlSaveOptions opts;
    opts.SetHtmlCrossStringType(HtmlCrossType::CrossHideRight);

    // Save to HTML with HtmlSaveOptions
    wb.Save(outputDir + u"outputHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.html", opts);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
