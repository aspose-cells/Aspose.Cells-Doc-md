---
title: Estrai immagini dai fogli di lavoro usando ImageOrPrintOptions con C++
linktitle: Estrai immagini dai fogli di lavoro
type: docs
weight: 140
url: /it/cpp/extract-images-from-worksheets-using-imageorprintoptions/
description: Impara come estrarre immagini da fogli di lavoro Excel e salvarle in un’unità locale usando Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

Gli utenti di Microsoft Excel possono aggiungere immagini ai fogli di lavoro. Con Aspose.Cells, è possibile leggere le immagini dai file di Microsoft Excel e salvarle su un disco locale. Questo articolo mostra come fare.

{{% /alert %}} 

Il codice di esempio di seguito mostra come estrarre immagini da un file di Excel e salvarle.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Open a template Excel file
    Workbook workbook(srcDir + u"sampleExtractImagesFromWorksheets.xlsx");

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the first Picture in the first worksheet
    Picture pic = worksheet.GetPictures().Get(0);

    // Define ImageOrPrintOptions
    ImageOrPrintOptions printoption;

    // Specify the image format
    printoption.SetImageType(ImageType::Jpeg);

    // Save the image
    pic.ToImage(outDir + u"outputExtractImagesFromWorksheets.jpg", printoption);

    std::cout << "Image extracted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
