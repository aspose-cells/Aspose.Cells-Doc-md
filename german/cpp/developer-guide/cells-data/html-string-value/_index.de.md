---
title: HTML Reichtext innerhalb der Zelle mit C++ hinzufügen
linktitle: Html String Wert
type: docs
weight: 50
url: /de/cpp/adding-html-rich-text-inside-the-cell/
description: Lernen Sie, wie Sie HTML Reichtext innerhalb der Zelle durch die Aspose.Cells for C++ API hinzufügen.
keywords: HTML Rich Text in der Zelle hinzufügen, HTML Rich Text in der Zelle setzen, HTML Rich Text in der Zelle hinzufügen
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt die Umwandlung von Microsoft Excel-orientiertem HTML in XLS/XLSX-Format. Das bedeutet, dass das von Microsoft Excel generierte HTML mit Aspose.Cells wieder in das XLS/XLSX-Format konvertiert werden kann.

Wenn einfacher HTML-Code vorliegt, kann Aspose.Cells ihn in HTML-Reichtext umwandeln. Aspose.Cells bietet die Methode [**Cell::GetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/), die einfachen HTML-Code nehmen und in formatierten Zelltext umwandeln kann.

{{% /alert %}}

Im folgenden Beispielcode wird gezeigt, wie man HTML-Rich-Text in der Zelle hinzufügt. Bitte beachten Sie den Screenshot der Ausgabedatei in Excel.

![todo:image_alt_text](adding-html-rich-text-inside-the-cell_1)

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

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Set HTML formatted text in the cell
    cell.SetHtmlString(u"<Font Style=\"FONT-WEIGHT: bold;FONT-STYLE: italic;TEXT-DECORATION: underline;FONT-FAMILY: Arial;FONT-SIZE: 11pt;COLOR: #ff0000;\">This is simple HTML formatted text.</Font>");

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "HTML formatted text added to cell A1 successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## Verwandte Artikel

- [Listenpunkte anzeigen, indem Sie den Zellenwert mit HTML einstellen](/cells/de/cpp/display-bullets-by-setting-cell-value-using/)
- [Holen Sie sich HTML5-String aus der Zelle](/cells/de/cpp/get-html5-string-from-cell/)
