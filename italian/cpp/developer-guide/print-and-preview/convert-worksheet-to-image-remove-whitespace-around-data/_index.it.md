---
title: Convertire il foglio di lavoro in immagine  Rimuovere lo spazio bianco intorno ai dati con C++
linktitle: Convertire il foglio di lavoro in immagine  Rimuovere lo spazio bianco intorno ai dati
type: docs
weight: 40
url: /it/cpp/convert-worksheet-to-image-remove-whitespace-around-data/
description: Impara come convertire un foglio di lavoro in immagine e rimuovere lo spazio bianco intorno ai dati utilizzando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

A volte è necessario presentare immagini del foglio elettronico in applicazioni o pagine web. Ad esempio, potresti aver bisogno di inserire immagini in un documento di Word, un file PDF, una presentazione PowerPoint o qualche altro documento. Fondamentalmente, desideri renderizzare un foglio elettronico come un'immagine in modo che possa essere incollato in altre applicazioni. Aspose.Cells ti consente di convertire i fogli di lavoro di Microsoft Excel in immagini.

{{% /alert %}}

## **Rimuovi spazi vuoti intorno ai dati**

L'API [**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/) converte un foglio elettronico in un file immagine con eventuali attributi specificati, ad esempio formato immagine, fogli paginati, ecc. Sono supportati diversi formati di immagine, come BMP, GIF, JPG, TIFF e EMF.

Quando utilizzi la funzione di conversione del foglio in immagine, l'immagine risultante ha uno spazio bianco, ovvero un bordo, di default. Puoi rimuoverlo impostando i margini di configurazione della pagina superiore, inferiore, sinistro e destro del foglio di origine a 0 e specificando gli attributi [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) di conseguenza.

Il seguente frammento di codice rimuove gli spazi vuoti intorno ai dati nell'immagine di output.

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

    // Open the template file
    Workbook book(srcDir + u"Book1.xlsx");

    // Get the first worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Define LoadOptions and set LoadFilter
    LoadOptions options;
    options.SetLoadFilter(new LoadFilter(LoadDataFilterOptions::All));

    // Specify your print area if you want
    // sheet.GetPageSetup().SetPrintArea(u"A1:H8");

    // To remove the white border around the image.
    sheet.GetPageSetup().SetLeftMargin(0);
    sheet.GetPageSetup().SetRightMargin(0);
    sheet.GetPageSetup().SetBottomMargin(0);
    sheet.GetPageSetup().SetTopMargin(0);

    // Define ImageOrPrintOptions
    ImageOrPrintOptions imgOptions;
    imgOptions.SetImageType(Aspose::Cells::Drawing::ImageType::Emf);

    // Set only one page would be rendered for the image
    imgOptions.SetOnePagePerSheet(true);
    imgOptions.SetPrintingPage(PrintingPageType::IgnoreBlank);

    // Create the SheetRender object based on the sheet with its
    // ImageOrPrintOptions attributes
    SheetRender sr(sheet, imgOptions);

    // Convert the image
    sr.ToImage(0, outDir + u"outputRemoveWhitespaceAroundData.emf");

    std::cout << "Image converted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
