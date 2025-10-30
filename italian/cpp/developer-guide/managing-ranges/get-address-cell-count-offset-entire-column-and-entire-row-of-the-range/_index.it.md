---
title: Ottieni l indirizzo, il conteggio delle celle, l offset, l intera colonna e l intera riga dell intervallo con C++
linktitle: Ottieni l indirizzo, il conteggio delle celle, l offset, l intera colonna e l intera riga dell intervallo
type: docs
weight: 330
url: /it/cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/
description: Impara come ottenere indirizzo, conteggio celle, offset, intera colonna e intera riga di un intervallo usando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**
Aspose.Cells fornisce l'oggetto `Range`, che ha vari metodi utili che facilitano il lavoro con gli intervalli Excel. Questo articolo illustra l'uso dei seguenti metodi o proprietà dell'oggetto `Range` :

- **Indirizzo**

  Ottiene l'indirizzo dell'intervallo.

- **Conteggio celle**

  Ottiene il conteggio totale delle celle nell'intervallo.

- **Spostamento**

  Ottiene un intervallo per offset.

- **Intera Colonna**

  Ottiene un oggetto `Range` che rappresenta l'intera colonna (o colonne) che contiene l'intervallo specificato.

- **Intera Riga**

  Ottiene un oggetto `Range` che rappresenta l'intera riga (o righe) che contiene l'intervallo specificato.

## **Ottieni indirizzo, conteggio celle, offset, intera colonna e intera riga dell'intervallo**
Il seguente esempio di codice spiega l'uso dei metodi e proprietà discussi sopra. Si prega di consultare l'output della console del codice di seguito come riferimento.

## **Codice di Esempio**
```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Create empty workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Create range A1:B3
    cout << "Creating Range A1:B3" << endl;
    Range rng = ws.GetCells().CreateRange(u"A1:B3");

    // Print range address and cell count
    cout << "Range Address: " << rng.GetAddress().ToUtf8() << endl;
    cout << "Range row Count: " << rng.GetRowCount() << endl;
    cout << "Range column Count: " << rng.GetColumnCount() << endl;

    // Formatting console output
    cout << "----------------------" << endl;
    cout << endl;

    // Create range A1
    cout << "Creating Range A1" << endl;
    rng = ws.GetCells().CreateRange(u"A1");

    // Print range offset, entire column and entire row
    cout << "Offset: " << rng.GetOffset(2, 2).GetAddress().ToUtf8() << endl;
    cout << "Entire Column: " << rng.GetEntireColumn().GetAddress().ToUtf8() << endl;
    cout << "Entire Row: " << rng.GetEntireRow().GetAddress().ToUtf8() << endl;

    // Formatting console output
    cout << "----------------------" << endl;
    cout << endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Output della console**
{{< highlight java >}}

Creating Range A1:B3

Range Address: A1:B3

Cell Count: 6

\----------------------

Creating Range A1

Offset: C3

Entire Column: A:A

Entire Row: 1:1

\----------------------

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
