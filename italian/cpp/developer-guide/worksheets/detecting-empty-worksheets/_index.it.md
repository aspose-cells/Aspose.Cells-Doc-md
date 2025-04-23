---
title: Rilevamento di fogli di lavoro vuoti con C++
linktitle: Rilevamento di fogli di lavoro vuoti
type: docs
weight: 410
url: /it/cpp/detecting-empty-worksheets/
description: Questo articolo mostra codice che spiega come rilevare i fogli di lavoro vuoti nei workbook Excel in modo programmatico usando l API C++ con la libreria Aspose.Cells.
keywords: rileva foglio di lavoro vuoto c++, trova foglio di lavoro Excel vuoto c++
---

## **Controllare le celle popolate**

I fogli di lavoro possono avere uno o più celle popolate con valori, dove un valore può essere semplice (testo, numerico, data/ora) o una formula o un valore basato su formula. In tal caso, è facile rilevare se un determinato foglio di lavoro è vuoto o meno. Tutto ciò che bisogna controllare sono le proprietà [**Cells.MaxDataRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatarow/) o [**Cells.MaxDataColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatacolumn/). Se le proprietà sopra menzionate restituiscono valori zero o positivi, ciò significa che una o più celle sono state popolate. Tuttavia, se una di queste proprietà restituisce -1, ciò indica che nessuna delle celle è stata popolata nel foglio di lavoro dato.

{{% alert color="primary" %}}

Le collezioni di righe & colonne hanno indice zero-based, quindi una cella alla riga 0 & colonna 0 corrisponde alla prima cella nel foglio di lavoro, che è A1.

{{% /alert %}}

## **Controllare le celle inizializzate vuote**

Tutte le celle che hanno valori sono automaticamente inizializzate. Tuttavia, c'è la possibilità che un foglio di lavoro abbia celle solo con formattazione applicata. In tal caso, le proprietà [**Cells.MaxDataRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatarow/) o [**Cells.MaxDataColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatacolumn/) restituiranno -1, indicando l'assenza di valori popolati. Ma le celle inizializzate a causa della formattazione della cella non possono essere rilevate con questo metodo. Per verificare se un foglio di lavoro ha celle inizializzate vuote, è consigliabile usare il metodo `MoveNext` sull'enumeratore ottenuto dalla collettione [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Se il metodo `MoveNext` restituisce **true**, significa che ci sono una o più celle inizializzate nel foglio di lavoro.

## **Controllare le forme**

È possibile che un determinato foglio di lavoro non abbia celle popolate, tuttavia, potrebbe contenere forme e oggetti come controlli, grafici, immagini e così via. Se dobbiamo verificare se un foglio di lavoro contiene forme, possiamo farlo ispezionando la proprietà [**ShapeCollection.Count**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/getcount/). Un valore positivo indica la presenza di forme nel foglio di lavoro.

## **Esempio di programmazione**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create an instance of Workbook and load an existing spreadsheet
    Workbook book(srcDir + u"sample.xlsx");

    // Loop over all worksheets in the workbook
    WorksheetCollection sheets = book.GetWorksheets();
    for (int i = 0; i < sheets.GetCount(); i++)
    {
        Worksheet sheet = sheets.Get(i);

        // Check if worksheet has populated cells
        if (sheet.GetCells().GetMaxDataRow() != -1)
        {
            cout << sheet.GetName().ToUtf8() << " is not empty because one or more cells are populated" << endl;
        }
        // Check if worksheet has shapes
        else if (sheet.GetShapes().GetCount() > 0)
        {
            cout << sheet.GetName().ToUtf8() << " is not empty because there are one or more shapes" << endl;
        }
        // Check if worksheet has empty initialized cells
        else
        {
            Range range = sheet.GetCells().GetMaxDisplayRange();
            auto rangeIterator = range.GetEnumerator();
            if (rangeIterator.MoveNext())
            {
                cout << sheet.GetName().ToUtf8() << " is not empty because one or more cells are initialized" << endl;
            }
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
