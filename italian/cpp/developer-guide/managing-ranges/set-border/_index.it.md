---
title: Imposta il bordo dell intervallo con C++
type: docs
weight: 600
url: /it/cpp/set-range-border/
description: Impara come impostare i bordi dell intervallo usando Aspose.Cells con C++.
---

## **Possibili Scenari di Utilizzo**
 Quando vuoi impostare il bordo di un Intervallo, non è necessario impostare ogni cella singolarmente. Puoi impostare il bordo sull'intervallo. Aspose.Cells offre questa funzionalità. Questo articolo fornisce un esempio di codice che utilizza Aspose.Cells per impostare il bordo dell'intervallo.

## **Imposta il bordo dell'intervallo in Excel**
Per impostare il bordo di un intervallo in Excel, puoi seguire questi passaggi:
1. Seleziona l'intervallo di celle a cui desideri applicare il bordo.
2. Nella scheda "Home" del menu, individua il gruppo "Carattere".
3. All'interno del gruppo "Carattere", fai clic sul pulsante a discesa "Bordi".
<br>
<img src="border.png" />
4. Scegli il tipo di bordo che desideri applicare dalle opzioni nel menu a discesa. Puoi scegliere tra stili di bordi predefiniti o personalizzare il tuo bordo.
5. Una volta selezionato lo stile di bordo desiderato, il bordo sarà applicato all'intervallo selezionato di celle.

## **Imposta il bordo dell'intervallo usando Aspose.Cells**
Questo esempio mostra come:

1. Crea un libro di lavoro.
2. Aggiungi dati alle celle nel primo foglio di lavoro.
3. Crea un [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range).
 4. Imposta il bordo interno dell'intervallo.
 5. Imposta il bordo esterno dell'intervallo.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new Workbook object
    Workbook workbook;

    // Obtain the reference of the newly added worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Setting the value to the cells
    Cell cell = cells.Get("A1");
    cell.PutValue(u"Fruit");
    cell = cells.Get("B1");
    cell.PutValue(u"Count");
    cell = cells.Get("C1");
    cell.PutValue(u"Price");

    cell = cells.Get("A2");
    cell.PutValue(u"Apple");
    cell = cells.Get("A3");
    cell.PutValue(u"Mango");
    cell = cells.Get("A4");
    cell.PutValue(u"Blackberry");
    cell = cells.Get("A5");
    cell.PutValue(u"Cherry");

    cell = cells.Get("B2");
    cell.PutValue(5);
    cell = cells.Get("B3");
    cell.PutValue(3);
    cell = cells.Get("B4");
    cell.PutValue(6);
    cell = cells.Get("B5");
    cell.PutValue(4);

    cell = cells.Get("C2");
    cell.PutValue(5);
    cell = cells.Get("C3");
    cell.PutValue(20);
    cell = cells.Get("C4");
    cell.PutValue(30);
    cell = cells.Get("C5");
    cell.PutValue(60);

    // Create a range (A1:C5)
    Range range = cells.CreateRange(u"A1", u"C5");

    // Set inner border of range
    CellsColor innerColor = workbook.CreateCellsColor();
    innerColor.SetColor(Color::Red());
    range.SetInsideBorders(BorderType::Vertical, CellBorderType::Thin, innerColor);
    innerColor.SetColor(Color::Green());
    range.SetInsideBorders(BorderType::Horizontal, CellBorderType::Thin, innerColor);

    // Set outer border of range
    CellsColor outerColor = workbook.CreateCellsColor();
    outerColor.SetColor(Color::Blue());
    range.SetOutlineBorders(CellBorderType::Thin, outerColor);

    // Save the Workbook
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```
