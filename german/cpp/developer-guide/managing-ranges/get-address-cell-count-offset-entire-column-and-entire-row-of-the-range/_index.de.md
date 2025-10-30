---
title: Erhalten Sie Adresse, Zellanzahl, Offset, gesamte Spalte und gesamte Zeile des Bereichs mit C++
linktitle: Erhalten Sie Adresse, Zellanzahl, Offset, gesamte Spalte und gesamte Zeile des Bereichs
type: docs
weight: 330
url: /de/cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/
description: Erfahren Sie, wie Sie Adresse, Zellanzahl, Offset, gesamte Spalte und gesamte Zeile eines Bereichs mit Aspose.Cells for C++ ermitteln.
---

## **Mögliche Verwendungsszenarien**
Aspose.Cells stellt das `Range`-Objekt bereit, das verschiedene Hilfsmethoden bietet, die die Arbeit mit Excel-Bereichen erleichtern. Dieser Artikel zeigt die Nutzung der folgenden Methoden oder Eigenschaften des `Range`-Objekts:

- **Adresse**

  Ermittelt die Adresse des Bereichs.

- **Zellanzahl**

  Ermittelt die Gesamtzahl der Zellen im Bereich.

- **Versatz**

  Ermittelt einen Bereich anhand des Offsets.

- **Gesamte Spalte**

  Erzeugt ein `Range`-Objekt, das die gesamte Spalte (oder Spalten) repräsentiert, die den angegebenen Bereich enthält.

- **Gesamte Zeile**

  Erzeugt ein `Range`-Objekt, das die gesamte Zeile (oder Zeilen) repräsentiert, die den angegebenen Bereich enthält.

## **Adresse, Zellanzahl, Offset, gesamte Spalte und gesamte Zeile des Bereichs abrufen**
Der folgende Beispielcode erklärt die Verwendung der oben diskutierten Methoden und Eigenschaften. Bitte beachten Sie die Konsolenausgabe des unten angegebenen Codes zu Referenz.

## **Beispielcode**
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

## **Konsolenausgabe**
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
