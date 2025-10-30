---
title: Esporta intervallo di celle in un foglio di lavoro in immagine con C++
linktitle: Esporta intervallo di celle in immagine
type: docs
weight: 60
url: /it/cpp/export-range-of-cells-in-a-worksheet-to-image/
description: Impara come esportare un intervallo specifico di celle in un foglio di lavoro in immagine usando Aspose.Cells con C++.
---

## **Possibili Scenari di Utilizzo**

È possibile creare un'immagine di un foglio di lavoro utilizzando Aspose.Cells. Tuttavia, talvolta è necessario esportare solo un intervallo di celle in un foglio di lavoro in un'immagine. Questo articolo spiega come raggiungere questo obiettivo.

## **Esportare un intervallo di celle in un foglio di lavoro in un'immagine**

Per prendere un'immagine di un intervallo, impostare l'area di stampa sull'intervallo desiderato e quindi impostare tutti i margini a 0. Imposta anche [**ImageOrPrintOptions.GetOnePagePerSheet()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getonepagepersheet/) su **true**. Il seguente codice prende un'immagine dell'intervallo D8:G16. Di seguito è riportata un'istantanea del [file di Excel di esempio](47153160.xlsx) usato nel codice. Puoi provare il codice con qualsiasi file di Excel.

## **Screenshot del file di Excel di esempio e la sua immagine esportata**

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**

Eseguendo il codice viene creata un'immagine dell'intervallo D8:G16 soltanto.

**![todo:image_alt_text](Output-Image.png)**

## **Codice di Esempio**

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

    // Create workbook from source file
    Workbook workbook(srcDir + u"sampleExportRangeOfCellsInWorksheetToImage.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the print area with the desired range
    worksheet.GetPageSetup().SetPrintArea(u"D8:G16");

    // Set all margins to 0
    worksheet.GetPageSetup().SetLeftMargin(0);
    worksheet.GetPageSetup().SetRightMargin(0);
    worksheet.GetPageSetup().SetTopMargin(0);
    worksheet.GetPageSetup().SetBottomMargin(0);

    // Set OnePagePerSheet option as true
    ImageOrPrintOptions options;
    options.SetOnePagePerSheet(true);
    options.SetImageType(Aspose::Cells::Drawing::ImageType::Jpeg);
    options.SetHorizontalResolution(200);
    options.SetVerticalResolution(200);

    // Take the image of the worksheet
    SheetRender sr(worksheet, options);
    sr.ToImage(0, outDir + u"outputExportRangeOfCellsInWorksheetToImage.jpg");

    std::cout << "Worksheet image exported successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
