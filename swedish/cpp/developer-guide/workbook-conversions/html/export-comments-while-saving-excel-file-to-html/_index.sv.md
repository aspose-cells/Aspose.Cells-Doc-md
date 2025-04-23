--- 
title: Exportera kommentarer vid sparning av Excel fil till HTML med C++ 
linktitle: Exportera kommentarer vid sparande av Excel fil till HTML 
type: docs 
weight: 40 
url: /sv/cpp/export-comments-while-saving-excel-file-to/ 
description: Lär dig hur du exporterar kommentarer när du sparar Excel filer till HTML med Aspose.Cells och C++. 
--- 

## **Möjliga användningsscenario**

När du sparar din Excel-fil till HTML exporteras inte kommentarer. Aspose.Cells erbjuder dock denna funktion via [**HtmlSaveOptions.IsExportComments**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/isexportcomments/) egenskapen. Om du sätter den till **true** visas kommentarer i din Excel-fil även i HTML. 

## **Exportera kommentarer vid sparande av Excel-fil till HTML**

Följande exempel kod förklarar användningen av [**HtmlSaveOptions.IsExportComments**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/isexportcomments/) egenskapen. Skärmbilden visar effekten av koden på HTML när den är inställd på **true**. Ladda ner gärna [exempel-Excel-filen](50528260.xlsx) och [genererad HTML](5052826.txt) för referens.

![todo:image_alt_text](export-comments-while-saving-excel-file-to-html_1.png)

## **Exempelkod**

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
