---
title: Bereiche mit C++ verwalten
linktitle: Bereiche
type: docs
weight: 105
url: /de/cpp/managing-ranges/
description: Erfahren, wie man Bereiche in Excel Dateien mit Aspose.Cells und C++ verwaltet, einschließlich Erstellen, Bearbeiten und Formatieren.
---

## **Einführung**

In Excel kann man mit einer Mausauswahlbox mehrere Zellen auswählen, die Auswahl der Zellen wird als "Bereich" bezeichnet.

Sie können beispielsweise in Zelle "A1" von Excel mit der linken Maustaste klicken und dann zu Zelle "C4" ziehen. Der ausgewählte rechteckige Bereich kann auch leicht als Objekt erstellt werden, indem Sie Aspose.Cells verwenden.

So erstellen Sie einen Bereich, fügen Werte ein, setzen Stil und führen weitere Operationen am "Bereich"-Objekt durch.

## **Bereiche verwalten mit Aspose.Cells**

Aspose.Cells bietet eine Klasse [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) enthält eine [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)-Sammlung, die den Zugriff auf jede Arbeitsmappe in einer Excel-Datei ermöglicht. Eine Arbeitsmappe wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) bietet eine [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-Sammlung.

### **Bereich erstellen**

Wenn Sie einen rechteckigen Bereich erstellen möchten, der über A1:C4 reicht, können Sie den folgenden Code verwenden:

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook
    Workbook workbook;

    // Get Cells from the first worksheet
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Create a Range from A1 to C4
    Range range = cells.CreateRange(u"A1:C4");

    Aspose::Cells::Cleanup();
}
```

### **Wert in die Zellen des Bereichs eingeben**

Angenommen, Sie haben einen Zellenbereich, der sich über A1:C4 erstreckt. Die Matrix umfasst 4 * 3 = 12 Zellen. Die einzelnen Bereichszellen sind sequenziell angeordnet: Bereich[0,0], Bereich[0,1], Bereich[0,2], Bereich[1,0], Bereich[1,1], Bereich[1,2], Bereich[2,0], Bereich[2,1], Bereich[2,2], Bereich[3,0], Bereich[3,1], Bereich[3,2].

Das folgende Beispiel zeigt, wie man einige Werte in die Zellen des Bereichs eingibt.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook
    Workbook workbook;

    // Get Cells from the first worksheet
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Create a Range from A1 to C4
    Range range = cells.CreateRange(u"A1:C4");

    // Put values in specific cells
    range.Get(0, 0).PutValue(u"A1");
    range.Get(0, 1).PutValue(u"B1");
    range.Get(0, 2).PutValue(u"C1");
    range.Get(3, 0).PutValue(u"A4");
    range.Get(3, 1).PutValue(u"B4");
    range.Get(3, 2).PutValue(u"C4");

    // Save the Workbook
    workbook.Save(u"RangeValueTest.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Stellen Sie den Stil der Zellen des Bereichs ein**

Das folgende Beispiel zeigt, wie man den Stil der Zellen des Bereichs festlegt.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook
    Workbook workbook;

    // Get Cells
    WorksheetCollection sheets = workbook.GetWorksheets();
    Cells cells = sheets.Get(0).GetCells();

    // Create Range
    Range range = cells.CreateRange(u"A1:C4");

    // Put value
    range.Get(0, 0).PutValue(u"A1");
    range.Get(3, 2).PutValue(u"C4");

    // Set Style
    Style style00 = workbook.CreateStyle();
    style00.SetPattern(BackgroundType::Solid);
    style00.SetForegroundColor(Color::Red());
    range.Get(0, 0).SetStyle(style00);

    Style style32 = workbook.CreateStyle();
    style32.SetPattern(BackgroundType::HorizontalStripe);
    style32.SetForegroundColor(Color::Green());
    range.Get(3, 2).SetStyle(style32);

    // Save the Workbook
    workbook.Save(u"RangeStyleTest.xlsx");

    std::cout << "Workbook saved successfully with range styles applied!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Aktuelles Gebiet des Bereichs erhalten**

CurrentRegion ist eine Eigenschaft, die ein Range-Objekt zurückgibt, das die aktuelle Region darstellt. 

Die aktuelle Region ist ein Bereich, der durch eine beliebige Kombination von leeren Zeilen und leeren Spalten begrenzt ist. Schreibgeschützt.

In Excel können Sie den Bereich "CurrentRegion" wie folgt erhalten:
1. Wählen Sie einen Bereich (Range1) mit dem Mausfeld aus.
2. Klicken Sie auf "Start - Bearbeiten - Suchen & Auswählen - Gehe zu - Besonderes - Aktuelle Region", oder verwenden Sie "Strg+Umschalt+*", dann sehen Sie, dass Excel automatisch einen Bereich (Range2) auswählt. Jetzt haben Sie es geschafft, Range2 ist die CurrentRegion von Range1.

Mit Aspose.Cells können Sie die Eigenschaft "Range.CurrentRegion" verwenden, um dieselbe Funktion auszuführen.

Bitte laden Sie die folgende Testdatei herunter, öffnen Sie sie in Excel, wählen Sie einen Bereich "A1:D7" mit dem Mausfeld aus, klicken Sie dann "Strg+Umschalt+*", dann sehen Sie, dass der Bereich "A1:C3" ausgewählt ist.

[current_region.xlsx](current_region.xlsx)

Führen Sie jetzt bitte das folgende Beispiel aus, sehen Sie, wie es in Aspose.Cells funktioniert:

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook
    Workbook workbook(u"current_region.xlsx");

    // Get Cells from the first worksheet
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Create a Range from A1 to D7
    Range src = cells.CreateRange(u"A1:D7");

    // Get the CurrentRegion of the created range
    Range A1C3 = src.GetCurrentRegion();

    Aspose::Cells::Cleanup();
}
```


## **Erweiterte Themen**
- [Autofüllbereich der Excel-Datei](/cells/de/cpp/autofill-ranges/)
- [Bereiche von Excel kopieren](/cells/de/cpp/copy-ranges-of-Excel/)
- [Nur Datenbereich kopieren](/cells/de/cpp/copy-range-data-only/)
- [Datenbereich mit Stil kopieren](/cells/de/cpp/copy-range-data-with-style/)
- [Nur Bereichsstil kopieren](/cells/de/cpp/copy-range-style-only/)
- [Union Range erstellen](/cells/de/cpp/create-union-range/)
- [Bereich ausschneiden und einfügen](/cells/de/cpp/cut-and-paste-cells/)
- [Bereiche löschen](/cells/de/cpp/delete-ranges-from-Excel/)
- [Adresse, Zellenanzahl, Versatz, Gesamte Spalte und Gesamte Zeile des Bereichs abrufen](/cells/de/cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [Bereiche einfügen](/cells/de/cpp/insert-ranges-to-Excel/)
- [Zellbereich zusammenführen oder trennen](/cells/de/cpp/merge-or-unmerge-range-of-cells/)
- [Bereich von Zellen in einem Arbeitsblatt verschieben](/cells/de/cpp/move-range-of-cells-in-a-worksheet/)
- [Arbeitsbuch- und arbeitsblattübergreifende benannte Bereiche erstellen](/cells/de/cpp/create-workbook-and-worksheet-scoped-named-ranges/)
- [Suchen und Ersetzen von Daten in einem Bereich](/cells/de/cpp/search-and-replace-data-in-a-range/)
{{< app/cells/assistant language="cpp" >}}
