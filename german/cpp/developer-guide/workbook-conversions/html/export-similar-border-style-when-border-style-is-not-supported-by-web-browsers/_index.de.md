---
title: Exportiere ähnlichen Rahmenstil, wenn Rahmenstil vom Webbrowser nicht unterstützt wird, mit C++
linktitle: Ähnlichen Rahmenstil exportieren, wenn der Rahmenstil von Webbrowsern nicht unterstützt wird
type: docs
weight: 70
url: /de/cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
description: Erfahren Sie, wie Sie ähnliche Rahmenstile exportieren, wenn sie vom Webbrowser nicht unterstützt werden, mit Aspose.Cells in C++.
---

## **Mögliche Verwendungsszenarien**

Microsoft Excel unterstützt einige Arten von durchgezogenen Grenzen, die vom Webbrowser nicht unterstützt werden. Wenn Sie eine solche Excel-Datei mit Aspose.Cells in HTML umwandeln, werden diese Grenzen entfernt. Allerdings unterstützt Aspose.Cells auch die Anzeige solcher Grenzen mit der [**HtmlSaveOptions.GetExportSimilarBorderStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportsimilarborderstyle/)-Eigenschaft. Bitte setzen Sie deren Wert auf **true**; die unsupported borders werden dann ebenfalls in die HTML-Datei exportiert.

## **Ähnlichen Randstil exportieren, wenn der Randstil von Webbrowsern nicht unterstützt wird**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](64716806.xlsx), die einige unsupported borders enthält, wie im folgenden Screenshot gezeigt. Der Screenshot veranschaulicht außerdem die Auswirkung der [**HtmlSaveOptions.GetExportSimilarBorderStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportsimilarborderstyle/)-Eigenschaft innerhalb des [Ausgabe-HTML](64716804.zip).

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **Beispielcode**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load the sample Excel file
    U16String inputFilePath(u"sampleExportSimilarBorderStyle.xlsx");
    Workbook workbook(inputFilePath);

    // Specify Html Save Options - Export Similar Border Style
    HtmlSaveOptions opts;
    opts.SetExportSimilarBorderStyle(true);

    // Save the workbook in Html format with specified Html Save Options
    U16String outputFilePath(u"outputExportSimilarBorderStyle.html");
    workbook.Save(outputFilePath, opts);

    std::cout << "Workbook saved successfully in HTML format with similar border styles!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
