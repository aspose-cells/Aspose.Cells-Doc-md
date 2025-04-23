---
title: Rileva celle fuse in un foglio di lavoro con C++
linktitle: Rileva Celle Unificate
description: Aspose.Cells è una libreria C++ per la gestione di file di fogli di calcolo. Supporta il rilevamento di celle unificate in un foglio di lavoro, rendendo facile per gli utenti identificare e manipolare queste celle. Questo articolo illustrerà come utilizzare la libreria Aspose.Cells per rilevare celle unificate.
keywords: Aspose.Cells, Foglio di lavoro, Unire celle, Rilevare, Identificare, Operare
type: docs
weight: 80
url: /it/cpp/detect-merged-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

Questo articolo fornisce informazioni su come ottenere le aree di celle unite in un foglio di lavoro.

Aspose.Cells consente di ottenere le aree di celle unite in un foglio di lavoro. È anche possibile separarle (dividere). Questo articolo mostra il codice più semplice usando l'API di **Aspose.Cells** per eseguire il compito.

{{% /alert %}}

Il componente fornisce il metodo [**Cells::GetMergedAreas()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmergedareas/) che può ottenere tutte le celle unificate. Il seguente esempio di codice mostra come rilevare celle unificate in un foglio di lavoro.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"SampleInput.xlsx");

    Worksheet wkSheet = workbook.GetWorksheets().Get(u"Sheet2");

    wkSheet.GetCells().Clear();

    Vector<CellArea> areas = wkSheet.GetCells().GetMergedAreas();

    for (int i = 0; i < areas.GetLength(); ++i)
    {
        int frow = areas[i].StartRow;
        int fcol = areas[i].StartColumn;
        int erow = areas[i].EndRow;
        int ecol = areas[i].EndColumn;

        int trows = erow - frow + 1;
        int tcols = ecol - fcol + 1;

        wkSheet.GetCells().UnMerge(frow, fcol, trows, tcols);
    }

    U16String outputPath = outDir + u"MergeTrial.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Worksheet processing completed successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```
