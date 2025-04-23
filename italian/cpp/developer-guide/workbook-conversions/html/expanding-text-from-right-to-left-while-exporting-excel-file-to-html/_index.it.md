---
title: Espansione del testo da destra a sinistra durante l esportazione di Excel in HTML con C++
linktitle: Espansione del testo da destra a sinistra durante l esportazione di un file Excel in HTML
type: docs
weight: 60
url: /it/cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/
description: Scopri come espandere il testo da destra a sinistra durante l esportazione di file Excel in HTML usando Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

Aspose.Cells for C++ supporta ora l'espansione del testo da destra a sinistra durante l'esportazione di file Excel in HTML. Questa funzione è stata implementata dalla versione v8.9.0.0. Se il tuo file Excel di origine contiene testo che si espande da destra a sinistra, Aspose.Cells lo esporterà correttamente in HTML.

{{% /alert %}} 

## **Espansione del testo da destra a sinistra durante l'esportazione di un file Excel in HTML**

Il seguente esempio di codice converte il [file Excel di esempio](5115502.xlsx) in HTML. Questa schermata mostra come appare il file Excel in Microsoft Excel 2013.

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_1.png)

Questa schermata mostra l'[HTML di output generato con la versione precedente](5115509).

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_2.png)

Questa schermata mostra l'[HTML di output generato con la versione più recente](5115508).

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_3.png)

Come puoi vedere nelle schermate, la versione più recente espande correttamente il testo allineato a destra a sinistra, proprio come Microsoft Excel.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load source excel file inside the workbook object
    Workbook wb(srcDir + u"sample.xlsx");

    // Save workbook in html format
    U16String outputPath = srcDir + u"ExpandTextFromRightToLeft_out_" + CellsHelper::GetVersion() + u".html";
    wb.Save(outputPath, SaveFormat::Html);

    std::cout << "Workbook saved successfully in HTML format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
