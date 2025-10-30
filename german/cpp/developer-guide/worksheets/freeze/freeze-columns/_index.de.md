---
title: Erfasse die erste(n) Spalte(n) in einem Excel Arbeitsblatt mit C++
linktitle: Spalten fixieren
type: docs
weight: 190
url: /de/cpp/how-to-freeze-columns-of-excel-worksheet
description: In diesem Artikel lernst du, wie man mit der C++ Bibliothek und Aspose.Cells die linken Spalten von Excel Arbeitsblättern programmatisch einfriert.
keywords: Linke Spalten einfrieren, Erste Spalten einfrieren, Spalte(n) sperren
---

## **Einführung**

In diesem Artikel lernen wir, wie man die linke(n) Spalte(n) einfriert. Wenn du große Datenmengen in einer Zeile hast und nicht in der Lage bist, die linken Spalten beim horizontalen Scrollen des Arbeitsblatts zu sehen. Du kannst die erste(n) Spalte(n) einfrieren und sperren, sodass du den gefrorenen Bereich auch beim Scrollen des restlichen Daten sichtbar behältst. So kannst du die Überschriften in den linken Spalten leicht sehen.

## **Spalten in Excel einfrieren**

**![Linke Spalte(n) in Excel einfrieren](freeze-columns.png)**

1. Wenn du die linke(n) Spalte(n) einfrieren möchtest, wähle zuerst die Spalte unter der Spalte, die eingefroren werden soll.
2. Klicken Sie auf Ansicht > Fenster einfrieren.
3. Klicke im Dropdown-Menü auf 'Erste Spalte einfrieren'.
4. Wenn du nach unten scrollst, ist die erste Spalte immer im linken Ansichtsbereich.

**![Gefrorene Spalte](frozen-columns.png)**

Wie du sehen kannst, ist die erste Spalte eingefroren, die erste Spalte bleibt beim horizontalen Scrollen immer an der Spitze des Sichtbereichs fixiert.

Festlegen der Spalten, damit Sie Ihre langen Daten anzeigen können, ohne die erste Spalte im Blick zu behalten.

## **Spalten mit Aspose.Cells for C++ einfrieren**
Das Einfrieren der ersten Spalte(n) mit Aspose.Cells for C++ ist einfach. 
Bitte verwenden Sie die Methode [**Worksheet.FreezePanes**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/), um die Spalte(n) an der ausgewählten Spalte einzufrieren.
1. Erstellen Sie eine Arbeitsmappe, um die Datei zu öffnen oder eine leere Datei zu erstellen.
2. Die erste Spalte mit der Worksheet.FreezePanes() Methode einfrieren.
3. Die Datei speichern.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    Workbook workbook(u"Freeze.xlsx");

    // Freezing panes at the second column
    workbook.GetWorksheets().Get(0).FreezePanes(u"B1", 0, 1);

    // Saving the file
    workbook.Save(u"frozen.xlsx");

    std::cout << "Panes frozen successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Anbei [Beispielquelle Excel-Datei](Freeze.xlsx).
{{< app/cells/assistant language="cpp" >}}
