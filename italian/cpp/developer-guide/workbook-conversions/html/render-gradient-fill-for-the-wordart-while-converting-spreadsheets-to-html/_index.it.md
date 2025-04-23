---
title: Effettuare il rendering del riempimento a gradiente per WordArt durante la conversione di fogli di calcolo in HTML con C++
linktitle: Rendere il riempimento a gradienti per il WordArt durante la conversione dei fogli di calcolo in HTML
type: docs
weight: 90
url: /it/cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/
description: Impara a renderizzare il riempimento a gradiente per WordArt durante la conversione di fogli di lavoro in HTML con C++.
---

## **Possibili Scenari di Utilizzo**
Prima di Aspose.Cells 17.1, Aspose.Cells non rendeva il riempimento a gradienti del word art quando il file Excel veniva convertito nel formato HTML. Dall'uscita di Aspose.Cells 17.1, il riempimento a gradienti del word art è supportato. Lo screenshot seguente confronta l'effetto del riempimento a gradienti convertendo il file di Excel utilizzando Aspose.Cells 17.1 e la versione precedente.

![todo:image_alt_text](render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to-html_1.png)
## **Rendi il riempimento a sfumatura per l'WordArt durante la conversione dei fogli di calcolo in HTML**
Il seguente codice di esempio converte il [file excel di origine](22774111.xlsx) nel [formato HTML di output](22774109.zip). Il file excel di origine contiene un'oggetto WordArt con riempimento a sfumatura come mostrato nella schermata sopra.
## **Codice di Esempio**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sourceGradientFill.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Save workbook to HTML format
    workbook.Save(outDir + u"out_sourceGradientFill.html");

    std::cout << "Workbook saved successfully in HTML format!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
