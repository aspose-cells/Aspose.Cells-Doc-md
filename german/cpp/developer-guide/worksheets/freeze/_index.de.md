---
title: Fenster in Excel Arbeitsblatt mit C++ einfrieren
linktitle: Fenster einfrieren
type: docs
weight: 190
url: /de/cpp/how-to-freeze-panes-of-excel-worksheet
description: In diesem Artikel lernen Sie, wie man die Fenster in Excel Arbeitsblättern mit programmgesteuert unter Verwendung der C++ Bibliothek und Aspose.Cells API einfriert.
keywords: Fenster einfrieren, Fenster fixieren.
---

## **Einführung**

In diesem Artikel lernen Sie, wie man Fenster einfriert. Wenn Sie große Datenmengen unter einer gemeinsamen Überschrift haben, können Sie die Überschrift beim Herunterscrollen im Arbeitsblatt nicht mehr sehen. Jedes Datensatz enthält viele Daten. Sie können Fenster einfrieren, sodass Sie den eingefrorenen Bereich auch beim Scrollen des restlichen Daten sehen können. Sie können Kopfzeilen in den oberen Zeilen oder den ersten Spalten leicht erkennen. Das Einfrieren und Aufheben des Einfrierens ändert nur die Ansicht der Daten, ohne die Daten selbst zu verändern.

## **In Excel**

**![Fenster einfrieren in Excel](Freeze-panes.png)**

1. Wenn Sie Fenster einfrieren möchten, Zeilen und Spalten einfrieren, wählen Sie zuerst eine Zelle (wie B2).
2. Klicken Sie auf Ansicht > Fenster einfrieren.
3. Im Dropdown-Menü klicken Sie auf Fenster einfrieren.
4. Wenn Sie nach unten oder nach rechts scrollen, sind die erste Zeile und die erste Spalte eingefroren.

**![Eingefrorene Fenster](Frozen-Panes.png)**

Wie Sie sehen können, sind die erste Zeile und Spalte A eingefroren, die zweite Zeile ist 32, und die zweite sichtbare Spalte ist D.

Fenster einfrieren ermöglicht das Anzeigen Ihrer großen Daten, ohne die Zeilen- oder Spaltenbeschriftungen im Blick zu behalten.

## **Fenster einfrieren mit Aspose.Cells for C++**
Das Einfrieren von Fenstern mit Aspose.Cells for C++ ist einfach. Bitte verwenden Sie die [**Worksheet.FreezePanes**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) Methode, um Fenster bei der ausgewählten Zelle einzufrieren.
1. Erstellen Sie eine Arbeitsmappe, um die Datei zu öffnen oder eine leere Datei zu erstellen.
2. Frieren Sie die Fenster mit der Methode `Worksheet.FreezePanes()` ein.
3. Die Datei speichern.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    U16String inputFilePath(u"Freeze.xlsx");
    Workbook workbook(inputFilePath);

    // Freeze panes at the cell B2
    WorksheetCollection sheets = workbook.GetWorksheets();
    sheets.Get(0).FreezePanes(u"B2", 1, 1);

    // Save the file
    U16String outputFilePath(u"frozen.xlsx");
    workbook.Save(outputFilePath);

    std::cout << "Panes frozen successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Anbei [Beispielquelle Excel-Datei](Freeze.xlsx).
