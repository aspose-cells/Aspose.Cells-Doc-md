---
title: Aggiungi hyperlink immagine con C++
linktitle: Aggiungi collegamenti ipertestuali alle immagini
type: docs
weight: 140
url: /it/cpp/add-image-hyperlinks/
description: Impara come aggiungere hyperlink immagine tramite l API Aspose.Cells for C++.
keywords: Aggiungi collegamenti ipertestuali alle immagini, Inserisci collegamenti ipertestuali alle immagini
---

{{% alert color="primary" %}} 

I collegamenti ipertestuali sono utili per accedere a informazioni su altre schede di lavoro o su siti web. Microsoft Excel consente agli utenti di aggiungere collegamenti ipertestuali su testi nelle celle e su immagini. I collegamenti ipertestuali alle immagini possono facilitare la navigazione in una scheda di lavoro, ad esempio, come pulsanti avanti e indietro, o loghi che collegano a siti specifici. Questo documento spiega come inserire collegamenti ipertestuali alle immagini in una scheda di lavoro utilizzando Aspose.Cells.

{{% /alert %}} 

Aspose.Cells consente di aggiungere collegamenti ipertestuali alle immagini nei fogli di calcolo in fase di esecuzione. È possibile impostare e modificare la descrizione e l'indirizzo dello schermo del collegamento. Il seguente codice di esempio illustra come aggiungere un collegamento ipertestuale a un'immagine in una scheda di lavoro.

```c++
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

    // Instantiate a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Insert a string value to a cell
    worksheet.GetCells().Get(u"C2").PutValue(u"Image Hyperlink");

    // Set the 4th row height
    worksheet.GetCells().SetRowHeight(3, 100);

    // Set the C column width
    worksheet.GetCells().SetColumnWidth(2, 21);

    // Add a picture to the C4 cell
    int index = worksheet.GetPictures().Add(3, 2, 4, 3, srcDir + u"aspose-logo.jpg");

    // Get the picture object
    Picture pic = worksheet.GetPictures().Get(index);

    // Set the placement type
    pic.SetPlacement(PlacementType::FreeFloating);

    // Add an image hyperlink
    Hyperlink hlink = pic.AddHyperlink(u"http://www.aspose.com/");

    // Specify the screen tip
    hlink.SetScreenTip(u"Click to go to Aspose site");

    // Save the Excel file
    workbook.Save(outDir + u"ImageHyperlink_out.xls");

    std::cout << "Image hyperlink added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
