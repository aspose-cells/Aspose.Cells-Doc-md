---
title: Aggiungi celle alla finestra di watch della formula di Microsoft Excel con C++
linktitle: Aggiungi celle alla finestra di watch della formula
description: Impara come usare Aspose.Cells for C++ per aggiungere celle alla finestra di watch della formula in Excel. Carica o crea un file Excel, manipola celle, imposta formule e salva il file modificato.
keywords: Aspose.Cells, Excel, finestra di watch della formula, celle, aggiunta, C++
type: docs
weight: 60
url: /it/cpp/add-cells-to-microsoft-excel-formula-watch-window/
---

## **Possibili Scenari di Utilizzo**

La finestra di watch di Microsoft Excel è uno strumento utile per monitorare comodamente i valori delle celle e le loro formule in una finestra. Puoi aprire *Watch Window* in Microsoft Excel cliccando su *Formulas > Watch Window*. Ha il pulsante *Add Watch* che può essere usato per aggiungere celle per l'ispezione. Allo stesso modo, puoi usare il metodo [**Worksheet.CellWatches.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells/cellwatchcollection/add/) per aggiungere celle alla *Watch Window* utilizzando l'API di Aspose.Cells.

## **Aggiungere celle alla finestra di visualizzazione della formula di Microsoft Excel**

Il seguente esempio di codice imposta la formula delle celle C1 ed E1 e le aggiunge entrambe alla Watch Window. Successivamente salva il file come [file Excel di output](67338481.xlsx). Se apri il file Excel di output e visualizzi la *Watch Window*, vedrai entrambe le celle come mostrato in questo screenshot.

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **Codice di Esempio**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create empty workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Put some integer values in cell A1 and A2
    ws.GetCells().Get(u"A1").PutValue(10);
    ws.GetCells().Get(u"A2").PutValue(30);

    // Access cell C1 and set its formula
    Cell c1 = ws.GetCells().Get(u"C1");
    c1.SetFormula(u"=Sum(A1,A2)");

    // Add cell C1 into cell watches by name
    ws.GetCellWatches().Add(c1.GetName());

    // Access cell E1 and set its formula
    Cell e1 = ws.GetCells().Get(u"E1");
    e1.SetFormula(u"=A2*A1");

    // Add cell E1 into cell watches by its row and column indices
    ws.GetCellWatches().Add(e1.GetRow(), e1.GetColumn());

    // Save workbook to output XLSX format
    wb.Save(u"outputAddCellsToMicrosoftExcelFormulaWatchWindow.xlsx", SaveFormat::Xlsx);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
