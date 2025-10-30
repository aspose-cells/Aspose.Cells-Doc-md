---
title: Automatisches Anpassen der Spalten und Zeilen beim Laden von HTML in Arbeitsmappe mit C++
linktitle: Spalten und Zeilen automatisch anpassen beim Laden von HTML in Arbeitsmappe
type: docs
weight: 120
url: /de/cpp/autofit-columns-and-rows-while-loading-html-in-workbook/
description: Lernen Sie, wie man Spalten und Zeilen automatisch anpasst, während HTML in eine Arbeitsmappe mit Aspose.Cells for C++ geladen wird.
---

## **Mögliche Verwendungsszenarien**

Sie können Spalten und Zeilen automatisch anpassen, während Sie Ihre HTML-Datei im Workbook-Objekt laden. Bitte setzen Sie die [**HtmlLoadOptions.GetAutoFitColsAndRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getautofitcolsandrows/)-Eigenschaft zu **true** für diesen Zweck.

## **Spalten und Zeilen automatisch anpassen beim Laden von HTML in Arbeitsmappe**

Der folgende Beispielcode lädt zunächst den Beispiel-HTML-Code ohne Ladeoptionen in Workbook und speichert ihn im XLSX-Format. Danach wird der Beispiel-HTML-Code erneut in Workbook geladen, diesmal jedoch nachdem die [**HtmlLoadOptions.GetAutoFitColsAndRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getautofitcolsandrows/)-Eigenschaft auf **true** gesetzt wurde, und im XLSX-Format gespeichert. Bitte laden Sie beide Ausgabe-Excel-Dateien herunter, d.h. [Ausgabe Excel-Datei ohne AutoFitColsAndRows](outputWithout_AutoFitColsAndRows.xlsx) und [Ausgabe Excel-Datei mit AutoFitColsAndRows](outputWith_AutoFitColsAndRows.xlsx). Der folgende Screenshot zeigt die Wirkung der [**HtmlLoadOptions.GetAutoFitColsAndRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getautofitcolsandrows/)-Eigenschaft auf beide Ausgabe-Excel-Dateien.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **Beispielcode**

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

    // Sample HTML string
    U16String sampleHtml(u"<html><body><table><tr><td>This is sample text.</td><td>Some text.</td></tr><tr><td>This is another sample text.</td><td>Some text.</td></tr></table></body></html>");

    // Convert HTML string to memory stream
    std::string utf8Data = sampleHtml.ToUtf8();
    Vector<uint8_t> ms(utf8Data.size());
    std::memcpy(ms.GetData(), utf8Data.data(), utf8Data.size());

    // Load memory stream into workbook
    Workbook wb(ms);

    // Save the workbook in xlsx format
    wb.Save(outDir + u"outputWithout_AutoFitColsAndRows.xlsx");

    // Specify the HTMLLoadOptions and set AutoFitColsAndRows = true
    HtmlLoadOptions opts;
    opts.SetAutoFitColsAndRows(true);

    // Load memory stream into workbook with the above HTMLLoadOptions
    Workbook wbWithOptions(ms, opts);

    // Save the workbook in xlsx format
    wbWithOptions.Save(outDir + u"outputWith_AutoFitColsAndRows.xlsx");

    std::cout << "HTML to Excel conversion completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
