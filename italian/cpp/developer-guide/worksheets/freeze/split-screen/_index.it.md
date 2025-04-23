---
title: Dividere lo schermo del foglio di lavoro Excel con C++
linktitle: Schermata divisa
type: docs
weight: 190
url: /it/cpp/how-to-split-screen-of-excel-worksheet
description: In questo articolo, imparerai come visualizzare alcune righe e/o colonne in pannelli separati dividendo il foglio di lavoro in due o quattro parti tramite la suddivisione programmata del foglio usando C++.
keywords: Congela le righe superiori, Congela la prima riga.
---

## **Introduzione**

In questo articolo, impareremo come visualizzare alcune righe e/o colonne in pannelli separati dividendo il foglio di lavoro in due o quattro parti. Quando si lavora con grandi set di dati, è necessario vedere alcune aree del stesso foglio contemporaneamente per confrontare diverse sottosezioni di dati. La funzione di divisione dello schermo può soddisfare le tue esigenze.

## **Come dividere lo schermo in Excel**
Per suddividere un foglio di lavoro in due o quattro parti, procedi come segue:

1. Seleziona la riga/colonna/cella prima della quale desideri posizionare la suddivisione.
2. Sulla scheda Visualizza, nel gruppo Finestre, fai clic sul pulsante Suddivisione.

**![Schermata divisa](Split-Screen.png)**

## **Suddividi il foglio di lavoro verticalmente sulle colonne**

Per separare due aree del foglio di calcolo verticalmente, seleziona la colonna a destra della colonna in cui desideri che appaia la suddivisione e fai clic sul pulsante Suddivisione in Excel.

È facile dividere verticalmente il foglio di lavoro in colonne tramite programmazione con Aspose.Cells for C++, basta selezionare una singola cella nella riga superiore come cella attiva, quindi
diviso con il metodo [**Worksheet.Split**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook.
    Workbook workbook(u"Book1.xlsx");

    // Get the first worksheet in the workbook.
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Sets C1 cell in the top row as the active cell.
    sheet.SetActiveCell(u"C1");

    // Split worksheet vertically on columns.
    sheet.Split();

    std::cout << "Worksheet processed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Suddividi il foglio di lavoro orizzontalmente sulle righe**
Per separare la finestra di Excel orizzontalmente, seleziona la riga sotto la riga in cui desideri che avvenga la suddivisione in Excel.

È facile dividere orizzontalmente il foglio di lavoro in righe tramite programmazione con Aspose.Cells for C++, basta selezionare una cella in una colonna sinistra come cella attiva, quindi
diviso con il metodo [**Worksheet.Split**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook and load an existing Excel file.
    Workbook workbook(u"Book1.xlsx");

    // Access the first worksheet in the workbook.
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Set the A6 cell in the left column as the active cell.
    sheet.SetActiveCell(u"A6");

    // Split the worksheet horizontally on rows.
    sheet.Split();

    // Save the modified workbook to a new file.
    workbook.Save(u"dest.xlsx");

    std::cout << "Workbook processed and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Dividi il foglio di lavoro in quattro parti.**
Per visualizzare contemporaneamente quattro diverse sezioni dello stesso foglio di lavoro, dividi lo schermo sia verticalmente che orizzontalmente in Excel.

È facile dividere verticalmente il foglio di lavoro in colonne tramite programmazione con Aspose.Cells for C++, basta selezionare una cella non nella prima riga e colonna come cella attiva, quindi
diviso con il metodo [**Worksheet.Split**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook.
    Workbook workbook(u"Book1.xlsx");

    // Get the first worksheet.
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Set E6 cell as the active cell.
    sheet.SetActiveCell(u"E6");

    // Split worksheet into four parts.
    sheet.Split();

    Aspose::Cells::Cleanup();
}
```

## **Come rimuovere la divisione**
Per rimuovere la divisione del foglio di lavoro, basta fare clic sul pulsante Dividi di nuovo.

Aspose.Cells for C++ fornisce un metodo [**Worksheet.RemoveSplit**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/) per rimuovere le impostazioni di suddivisione.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    Workbook workbook(u"Book1.xlsx");

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Remove split
    sheet.RemoveSplit();

    // Split worksheet into four parts
    sheet.Split();

    std::cout << "Worksheet split successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
