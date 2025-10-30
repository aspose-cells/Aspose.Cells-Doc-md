---
title: Exportieren Sie Dokument Arbeitsbuch und Blatt Eigenschaften bei Excel zu HTML Konvertierung mit C++
linktitle: Exportieren von Dokument , Arbeitsbuch und Arbeitsblatt Eigenschaften in Excel in HTML Konvertierung
type: docs
weight: 50
url: /de/cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
description: Erfahren Sie, wie Sie Dokument , Arbeitsbuch und Arbeitsblatt Eigenschaften beim Konvertieren von Excel Dateien in HTML mit Aspose.Cells for C++ exportieren oder vermeiden können.
---

## **Mögliche Verwendungsszenarien**

Wenn eine Microsoft Excel-Datei mit Microsoft Excel oder Aspose.Cells in HTML exportiert wird, werden auch verschiedene Arten von Dokument-, Arbeitsbuch- und Arbeitsblatt-Eigenschaften exportiert, wie im folgenden Screenshot gezeigt wird. Sie können das Exportieren dieser Eigenschaften vermeiden, indem Sie [**HtmlSaveOptions.GetExportDocumentProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportdocumentproperties/), [**HtmlSaveOptions.GetExportWorkbookProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworkbookproperties/) und [**HtmlSaveOptions.GetExportWorksheetProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworksheetproperties/) auf **false** setzen. Der Standardwert dieser Eigenschaften ist **true**. Der folgende Screenshot zeigt, wie diese Eigenschaften im exportierten HTML aussehen.

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **Exportieren von Dokument-, Arbeitsbuch- und Arbeitsblatt-Eigenschaften in Excel in HTML-Konvertierung**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](61767776.xlsx) und konvertiert sie in HTML, ohne die Dokument-, Arbeitsmappen- und Arbeitsblatt-Eigenschaften im [Ausgabe-HTML](61767779.zip) zu exportieren.

## **Beispielcode**

```c++
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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sampleExportDocumentWorkbookAndWorksheetPropertiesInHTML.xlsx";

    // Path of output HTML file
    U16String outputFilePath = outDir + u"outputExportDocumentWorkbookAndWorksheetPropertiesInHTML.html";

    // Load the sample Excel file
    Workbook workbook(inputFilePath);

    // Specify Html Save Options
    HtmlSaveOptions options;

    // We do not want to export document, workbook and worksheet properties
    options.SetExportDocumentProperties(false);
    options.SetExportWorkbookProperties(false);
    options.SetExportWorksheetProperties(false);

    // Export the Excel file to Html with Html Save Options
    workbook.Save(outputFilePath, options);

    std::cout << "Excel file exported to HTML successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
