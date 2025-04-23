---
title: Genera anteprima del foglio di lavoro con C++
linktitle: Generare un anteprima del foglio di lavoro
type: docs
weight: 110
url: /it/cpp/generate-thumbnail-of-the-worksheet/
description: Genera miniature dei fogli di lavoro come immagini usando Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

Può essere utile generare anteprime dai fogli di lavoro. Un'anteprima è un'immagine ridotta che può essere incollata in un documento Word o una presentazione PowerPoint per dare un'anteprima di ciò che c'è nel foglio di lavoro. Può essere aggiunta a una pagina Web con un collegamento per scaricare il documento originale e ha una serie di altri utilizzi.

{{% /alert %}} 

Aspose.Cells for C++ ti consente di esportare i fogli di lavoro in file immagine, rendendo semplice la generazione di miniature. Il seguente esempio di codice dimostra come esportare i fogli di lavoro in file immagine usando C++.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load source workbook
    Workbook book(srcDir + u"sampleGenerateThumbnailOfWorksheet.xlsx");

    // Configure image rendering options
    ImageOrPrintOptions imgOptions;
    imgOptions.SetImageType(ImageType::Bmp);
    imgOptions.SetVerticalResolution(200);
    imgOptions.SetHorizontalResolution(200);
    imgOptions.SetOnePagePerSheet(true);
    imgOptions.SetDesiredSize(600, 600, true); // Set thumbnail dimensions

    // Access first worksheet
    WorksheetCollection worksheets = book.GetWorksheets();
    Worksheet sheet = worksheets.Get(0);

    // Render worksheet to image
    SheetRender sr(sheet, imgOptions);
    sr.ToImage(0, outDir + u"outputGenerateThumbnailOfWorksheet.bmp");

    std::cout << "Worksheet thumbnail generated successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
