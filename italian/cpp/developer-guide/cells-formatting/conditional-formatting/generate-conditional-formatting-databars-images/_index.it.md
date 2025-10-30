---
title: Genera immagini di DataBars di formattazione condizionale con C++
linktitle: Genera immagini di formattazione condizionale DataBars
description: Aspose.Cells è una libreria C++ per lavorare con i file di fogli di calcolo. Supporta la generazione di barre dati e immagini formattate condizionatamente, permettendo agli utenti di personalizzare la visualizzazione del foglio di calcolo in base al valore delle celle. Questo articolo introdurrà come usare la libreria Aspose.Cells per generare barre dati e immagini formattate condizionatamente.
keywords: Aspose.Cells, Formattazione Condizionale, Barre di Dati, Immagini, Fogli di Calcolo
type: docs
weight: 40
url: /it/cpp/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

A volte è necessario generare immagini delle barre di dati formattate condizionalmente. È possibile utilizzare il [**DataBar.ToImage()**](https://reference.aspose.com/cells/cpp/aspose.cells/databar/toimage/) metodo di Aspose.Cells per generare queste immagini. Questo articolo mostra come generare un'immagine di DataBar utilizzando Aspose.Cells.

{{% /alert %}}

Il seguente esempio di codice genera l'immagine DataBar della cella C1. Prima accede all'oggetto condizione di formato della cella, e da quell'oggetto, accede all'oggetto [**DataBar**](https://reference.aspose.com/cells/cpp/aspose.cells/databar/) e usa il suo metodo [**ToImage()**](https://reference.aspose.com/cells/cpp/aspose.cells/databar/toimage/) per generare l'immagine della cella. Infine, salva l'immagine sul disco.

```cpp
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"sampleGenerateDatabarImage.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cell cell = worksheet.GetCells().Get(u"C1");

    int idx = worksheet.GetConditionalFormattings().Add();
    FormatConditionCollection fcc = worksheet.GetConditionalFormattings().Get(idx);
    fcc.AddCondition(FormatConditionType::DataBar);
    fcc.AddArea(CellArea::CreateCellArea(u"C1", u"C4"));

    DataBar dbar = fcc.Get(0).GetDataBar();

    ImageOrPrintOptions opts;
    opts.SetImageType(ImageType::Png);

    Vector<uint8_t> imgBytes = dbar.ToImage(cell, opts);

    std::ofstream outFile((outDir + u"outputGenerateDatabarImage.png").ToUtf8(), std::ios::binary);
    outFile.write(reinterpret_cast<const char*>(imgBytes.GetData()), imgBytes.GetLength());
    outFile.close();

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
