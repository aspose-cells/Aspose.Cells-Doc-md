---
title: Come controllare la barra delle schede del foglio con C++
linktitle: Come controllare la barra delle schede del foglio
type: docs
weight: 600
url: /it/cpp/how-to-control-sheet-tab-bar/
description: Impara come controllare la barra delle schede del foglio tramite l API Aspose.Cells for C++.
keywords: Come controllare la barra delle schede del foglio, Operare la barra delle schede del foglio, Impostare la barra delle schede del foglio, Controllare la barra delle schede del foglio. 
---

## **Possibili Scenari di Utilizzo**
Quando hai bisogno di regolare l'aspetto della barra del foglio Excel, devi sapere come controllare la barra delle schede del foglio, come nasconderla o mostrarla, modificare la larghezza della barra, specificare la prima scheda visibile, e così via. Aspose.Cells supporta queste funzionalità. Aspose.Cells fornisce le seguenti proprietà e metodi per aiutarti a raggiungere i tuoi obiettivi.

- [**WorkbookSettings.GetShowTabs()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshowtabs/)
- [**WorkbookSettings.GetSheetTabBarWidth()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getsheettabbarwidth/)
- [**WorkbookSettings.GetFirstVisibleTab()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getfirstvisibletab/)

## **Come controllare la barra delle schede del foglio usando Aspose.Cells for C++**
Questo esempio mostra come:

1. Crea un libro di lavoro.
1. Aggiungi dati alle celle nel primo foglio di lavoro.
1. Visualizzare la scheda del foglio e impostare la larghezza della barra delle schede.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook object
    Workbook workbook;

    // Obtain the reference to the newly added worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Setting the value to the cells
    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Fruit");
    cell = cells.Get(u"B1");
    cell.PutValue(u"Count");
    cell = cells.Get(u"C1");
    cell.PutValue(u"Price");

    cell = cells.Get(u"A2");
    cell.PutValue(u"Apple");
    cell = cells.Get(u"A3");
    cell.PutValue(u"Mango");
    cell = cells.Get(u"A4");
    cell.PutValue(u"Blackberry");
    cell = cells.Get(u"A5");
    cell.PutValue(u"Cherry");

    // Display the sheet tab and set the width of the tab bar
    workbook.GetSettings().SetShowTabs(true);
    workbook.GetSettings().SetSheetTabBarWidth(150);

    // Save the workbook
    workbook.Save(u"out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Anteprima del file di risultato:
<br>
<image src="result.png" width="70%" />

