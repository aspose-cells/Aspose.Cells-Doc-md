---
title: Specifica il massimo numero di righe di formula condivisa con C++
linktitle: Specificare il Numero Massimo di Righe della Formula Condivisa
type: docs
weight: 40
url: /it/cpp/specify-maximum-rows-of-shared-formula/
description: Impara come specificare il massimo numero di righe di formula condivisa nei file Excel usando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**

Il massimo predefinito di righe per la formula condivisa è 64. Può essere qualsiasi numero, ad esempio, 1000. Le prestazioni della formula condivisa cambiano con un diverso numero di righe. Pertanto, Aspose.Cells fornisce la proprietà [**GetMaxRowsOfSharedFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxrowsofsharedformula/) che può essere utilizzata per specificare il massimo numero di righe della formula condivisa. La formula condivisa verrà suddivisa in diverse formule condivise se il totale delle righe della formula condivisa supera tale limite, come mostrato nello screenshot seguente.

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)

## **Specificare il numero massimo di righe della formula condivisa**

Il seguente esempio di codice spiega l'uso della proprietà [**GetMaxRowsOfSharedFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxrowsofsharedformula/). Imposta il massimo numero di righe della formula condivisa a 5 e aggiunge la formula condivisa nella cella D1 per 100 righe, salvando in un file Excel di output [output Excel file](61767856.xlsx). Se estrai il contenuto del file Excel di output e controlli *sheet1.xml*, vedrai che la formula condivisa si suddivide ogni 5 righe, come evidenziato nello screenshot sopra.

## **Codice di Esempio**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook wb;

    // Set the max rows of shared formula to 5
    wb.GetSettings().SetMaxRowsOfSharedFormula(5);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell D1
    Cell cell = ws.GetCells().Get(u"D1");

    // Set the shared formula in 100 rows
    cell.SetSharedFormula(u"=Sum(A1:A2)", 100, 1);

    // Save the output Excel file
    wb.Save(u"outputSpecifyMaximumRowsOfSharedFormula.xlsx");

    std::cout << "Shared formula set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
