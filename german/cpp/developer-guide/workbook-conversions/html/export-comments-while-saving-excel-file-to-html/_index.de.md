--- 
title: Kommentare beim Speichern von Excel Dateien in HTML mit C++ exportieren 
linktitle: Export von Kommentaren beim Speichern von Excel Datei in HTML 
type: docs 
weight: 40 
url: /de/cpp/export-comments-while-saving-excel-file-to/ 
description: Lernen, wie man Kommentare beim Speichern von Excel Dateien in HTML mit Aspose.Cells und C++ exportiert. 
--- 

## **Mögliche Verwendungsszenarien**

Wenn Sie Ihre Excel-Datei in HTML speichern, werden Kommentare nicht exportiert. Aspose.Cells bietet diese Funktion jedoch mit der [**HtmlSaveOptions.IsExportComments**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/isexportcomments/)-Eigenschaft. Wenn Sie sie auf **true** setzen, werden die Kommentare in Ihrem Excel in HTML angezeigt.

## **Kommentare beim Speichern einer Excel-Datei in HTML exportieren**

Das folgende Beispiel erklärt die Verwendung der [**HtmlSaveOptions.IsExportComments**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/isexportcomments/)-Eigenschaft. Das Screenshot zeigt die Wirkung des Codes auf das HTML, wenn sie auf **true** gesetzt ist. Bitte laden Sie die [Beispieldatei Excel](50528260.xlsx) und das [generierte HTML](5052826.txt) als Referenz herunter.

![todo:image_alt_text](export-comments-while-saving-excel-file-to-html_1.png)

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
    U16String inputFilePath = sourceDir + u"sampleExportCommentsHTML.xlsx";
    Workbook workbook(inputFilePath);

    // Export comments - set IsExportComments property to true
    HtmlSaveOptions opts;
    opts.SetIsExportComments(true);

    // Save the Excel file to HTML
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    workbook.Save(outputDir + u"outputExportCommentsHTML.html", opts);

    std::cout << "Excel file exported to HTML with comments successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
