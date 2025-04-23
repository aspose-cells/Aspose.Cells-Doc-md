--- 
title: Esporta Commenti durante il salvataggio del file Excel in HTML con C++ 
linktitle: Esportazione dei commenti durante il salvataggio del file Excel in HTML 
type: docs 
weight: 40 
url: /it/cpp/export-comments-while-saving-excel-file-to/ 
description: Impara come esportare i commenti durante il salvataggio dei file Excel in HTML usando Aspose.Cells con C++. 
--- 

## **Possibili Scenari di Utilizzo**

Quando salvi il tuo file Excel in HTML, i commenti non vengono esportati. Tuttavia, Aspose.Cells offre questa funzionalità usando la proprietà [**HtmlSaveOptions.IsExportComments**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/isexportcomments/). Se la imposti su **true**, l'HTML mostrerà anche i commenti presenti nel file Excel.

## **Esporta commenti durante il salvataggio del file di Excel in HTML**

Il seguente esempio di codice spiega l'uso della proprietà [**HtmlSaveOptions.IsExportComments**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/isexportcomments/). Lo screenshot mostra l'effetto del codice sull'HTML quando viene impostato su **true**. Scarica il [file Excel di esempio](50528260.xlsx) e l'[HTML generato](5052826.txt) come riferimento.

![todo:image_alt_text](export-comments-while-saving-excel-file-to-html_1.png)

## **Codice di Esempio**

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
