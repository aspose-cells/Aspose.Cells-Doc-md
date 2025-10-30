---
title: Gestisci la stringa HTML delle celle con C++
linktitle: Gestisci Stringa Html Celle
type: docs
weight: 600
url: /it/cpp/manage-cells-html-string/
description: Impara come gestire la stringa HTML delle celle tramite l API Aspose.Cells for C++.
keywords: Aggiungi una stringa HTML all interno della cella, Imposta la stringa HTML all interno della cella, Aggiungi una stringa HTML, Ottieni la stringa HTML della cella, Gestisci la stringa HTML delle celle
---

## **Possibili Scenari di Utilizzo**
Quando devi impostare dati stilizzati per una cella specifica, puoi assegnare una stringa HTML alla cella. Ovviamente, puoi anche ottenere la stringa HTML della cella. Aspose.Cells offre questa funzionalità. Aspose.Cells fornisce le seguenti proprietà e metodi per aiutarti a raggiungere i tuoi obiettivi.
- [**Cell::GetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/)
- [**Cell::SetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/sethtmlstring/)

## **Ottieni e imposta la stringa HTML usando Aspose.Cells**
Questo esempio mostra come:

1. Creare un workbook e aggiungere alcuni dati.
1. Ottenere la cella specifica nella prima scheda di lavoro.
1. Impostare una stringa HTML nella cella.
1. Ottenere la stringa HTML della cella.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a Workbook object
    Workbook workbook;

    // Obtain the reference of the newly added worksheet
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

    Cell c3 = cells.Get(u"C3");
    // Set HTML string for C3 cell
    c3.SetHtmlString(u"<b>test bold</b>");

    Cell c4 = cells.Get(u"C4");
    // Set HTML string for C4 cell
    c4.SetHtmlString(u"<i>test italic</i>");

    // Get the HTML string of specific cell
    std::cout << c3.GetHtmlString().ToUtf8() << std::endl;
    std::cout << c4.GetHtmlString().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## Output generato dal codice di esempio

Lo screenshot seguente mostra l'output del codice di esempio precedente.

![todo:image_alt_text](htmlstring.png)
{{< app/cells/assistant language="cpp" >}}
