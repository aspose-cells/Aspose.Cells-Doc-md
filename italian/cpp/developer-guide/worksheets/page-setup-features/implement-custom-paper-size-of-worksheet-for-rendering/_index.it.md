---
title: Implementare dimensione personalizzata della carta del foglio di lavoro per il rendering con C++
linktitle: Implementa la dimensione della carta personalizzata del foglio di lavoro per la resa
type: docs
weight: 70
url: /it/cpp/implement-custom-paper-size-of-worksheet-for-rendering/
description: Questo articolo spiega come usare l API C++ per impostare una dimensione personalizzata della carta per i fogli di lavoro desiderati durante il rendering di un file Excel in formato PDF in modo programmatico.
keywords: impostare dimensione personalizzata della carta durante il rendering di Excel in PDF C++
---

## **Possibili Scenari di Utilizzo**

 Non esiste un'opzione diretta per creare dimensioni personalizzate della carta in MS Excel; tuttavia, puoi impostare una dimensione personalizzata della carta dei fogli di lavoro desiderati durante il rendering di file Excel in formato PDF. Questo documento spiega come impostare una dimensione personalizzata della carta di un foglio di lavoro usando le API di Aspose.Cells.

## **Implementare un formato carta personalizzato del foglio di lavoro per il rendering**

 Aspose.Cells consente di impostare la dimensione di carta desiderata del foglio di lavoro. Puoi usare il metodo [**CustomPaperSize**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/custompapersize/) della classe [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) per specificare una dimensione personalizzata della pagina. Il seguente esempio illustra come specificare una dimensione personalizzata della carta per il primo foglio di lavoro nel workbook. Vedi anche [output PDF](45056028.pdf) generato con questo codice come riferimento.

## **Screenshot**

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)

## **Codice di Esempio**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create workbook object
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Set custom paper size in unit of inches
    ws.GetPageSetup().CustomPaperSize(6, 4);

    // Access cell B4
    Cell b4 = ws.GetCells().Get("B4");

    // Add the message in cell B4
    b4.PutValue(u"Pdf Page Dimensions: 6.00 x 4.00 in");

    // Save the workbook in pdf format
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    wb.Save(outputDir + u"outputCustomPaperSize.pdf");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
