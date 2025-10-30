---
title: Obere Zeile(n) der Excel Arbeitsmappe mit C++ einfrieren
linktitle: Zeilen einfrieren
type: docs
weight: 190
url: /de/cpp/how-to-freeze-rows-of-excel-worksheet
description: In diesem Artikel lernen Sie, wie man die oberen Zeilen von Excel Arbeitsblättern programmatisch mit C++ Bibliothek und Aspose.Cells API einfriert.
keywords: Obere Zeile(n) einfrieren, obere Zeile einfrieren.
---

## **Einführung**

In diesem Artikel lernen wir, wie man die oberen Zeilen einfriert. Wenn Sie eine große Datenmenge unter einer gemeinsamen Überschrift haben, können Sie die Überschrift beim Scrollen nach unten im Arbeitsblatt nicht sehen. Sie können obere Zeile(n) einfrieren, sodass Sie diesen eingefrorenen Bereich auch beim Scrollen durch den Rest der Daten sehen können. Überschriften in den oberen Zeilen sind leicht sichtbar.

## **Zeilen in Excel einfrieren**

**![Oberste Zeile(n) in Excel einfrieren](Freeze-Rows.png)**

1. Wenn Sie die oberen Zeile(n) einfrieren möchten, wählen Sie zuerst die Zeile unter der zu frierenden Zeile aus.
2. Klicken Sie auf Ansicht > Fenster einfrieren.
3. Wählen Sie im Dropdown-Menü "Oberste Zeile einfrieren" aus.
4. Wenn Sie nach unten scrollen, befindet sich die erste Zeile immer im oberen Sichtbereich.

**![Gefrorene Zeile](Frozen-Row.png)**

Wie Sie sehen können, ist die 1. Zeile eingefroren, und die erste Zeile bleibt beim Herunterscrollen immer oben im Blickfeld.

Zeilen einfrieren ermöglicht es Ihnen, Ihre großen Daten zu betrachten, ohne den Zeilenlabel aus den Augen zu verlieren.

## **Zeilen mit Aspose.Cells for C++ einfrieren**
Das Einfrieren der Zeile(n) mit Aspose.Cells for C++ ist einfach. 
Bitte verwenden Sie die [**Worksheet.FreezePanes**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) Methode, um die Zeile(n) an der ausgewählten Zeile einzufrieren.
1. Erstellen Sie eine Arbeitsmappe, um die Datei zu öffnen oder eine leere Datei zu erstellen.
2. Die erste Zeile mit der Worksheet.FreezePanes() Methode einfrieren.
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

    // Freezing panes at the cell B2
    workbook.GetWorksheets().Get(0).FreezePanes(u"A2", 1, 0);

    // Saving the file
    workbook.Save(u"frozen.xlsx");

    std::cout << "Panes frozen successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Angehängte [Beispielquelle für Excel-Datei](../Freeze.xlsx).
{{< app/cells/assistant language="cpp" >}}
