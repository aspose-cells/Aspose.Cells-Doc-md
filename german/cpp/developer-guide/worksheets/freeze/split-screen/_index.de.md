---
title: Excel Arbeitsblatt mit C++ in geteiltem Bildschirm anzeigen
linktitle: Bildschirm aufteilen
type: docs
weight: 190
url: /de/cpp/how-to-split-screen-of-excel-worksheet
description: In diesem Artikel lernen Sie, wie man bestimmte Zeilen und/oder Spalten in separaten Bereichen anzeigt, indem man das Arbeitsblatt programmatisch in zwei oder vier Teile aufteilt, mithilfe von C++.
keywords: Obere Zeile(n) einfrieren, obere Zeile einfrieren.
---

## **Einführung**

In diesem Artikel lernen wir, wie man bestimmte Zeilen und/oder Spalten in separaten Bereichen anzeigt, indem man das Arbeitsblatt in zwei oder vier Teile aufteilt. Bei großen Datensätzen müssen wir bestimmte Bereiche desselben Arbeitsblatts gleichzeitig sehen, um verschiedene Datensubsets zu vergleichen. Die Funktion zum Teilen des Bildschirms kann Ihre Anforderungen erfüllen.

## **Wie man den Bildschirm in Excel aufteilt**
Um ein Arbeitsblatt in zwei oder vier Teile aufzuteilen, führen Sie folgende Schritte aus:

1. Wählen Sie die Zeile/Spalte/Zelle aus, vor der Sie den Split platzieren möchten.
2. Klicken Sie im Register Ansicht auf der Registerkarte Fenster in der Gruppe Windows auf die Schaltfläche Split.

**![Bildschirm teilen](Split-Screen.png)**

## **Arbeitsblatt vertikal in Spalten teilen**

Um zwei Bereiche des Tabellenblatts vertikal zu trennen, wählen Sie die Spalte rechts von der Spalte aus, an der die Trennung erscheinen soll, und klicken Sie auf die Schaltfläche Split in Excel.

Es ist einfach, das Arbeitsblatt vertikal auf Spalten programmgesteuert mit Aspose.Cells for C++ zu teilen, wir müssen nur eine Zelle in der obersten Zeile als aktive Zelle auswählen.
mit der Methode [**Worksheet.Split**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/) teilen.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook.
    Workbook workbook(u"Book1.xlsx");

    // Get the first worksheet in the workbook.
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Sets C1 cell in the top row as the active cell.
    sheet.SetActiveCell(u"C1");

    // Split worksheet vertically on columns.
    sheet.Split();

    std::cout << "Worksheet processed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Arbeitsblatt horizontal in Zeilen teilen**
Um Ihr Excel-Fenster horizontal zu trennen, wählen Sie die Zeile unterhalb der Zeile, an der die Trennung in Excel erfolgen soll.

Es ist einfach, das Arbeitsblatt programmgesteuert horizontal auf Zeilen mit Aspose.Cells for C++ aufzuteilen, wir müssen nur eine Zelle in der linken Spalte als aktive Zelle auswählen, dann
mit der Methode [**Worksheet.Split**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/) teilen.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook and load an existing Excel file.
    Workbook workbook(u"Book1.xlsx");

    // Access the first worksheet in the workbook.
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Set the A6 cell in the left column as the active cell.
    sheet.SetActiveCell(u"A6");

    // Split the worksheet horizontally on rows.
    sheet.Split();

    // Save the modified workbook to a new file.
    workbook.Save(u"dest.xlsx");

    std::cout << "Workbook processed and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Arbeitsblatt in vier Teile teilen**
Um vier verschiedene Abschnitte desselben Arbeitsblatts gleichzeitig anzuzeigen, teilen Sie Ihren Bildschirm sowohl vertikal als auch horizontal in Excel.

Es ist einfach, das Arbeitsblatt programmgesteuert vertikal auf Spalten mit Aspose.Cells for C++ aufzuteilen, wir müssen nur eine Zelle auswählen, die nicht in der ersten Zeile und Spalte ist, als aktive Zelle, dann
mit der Methode [**Worksheet.Split**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/) teilen.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook.
    Workbook workbook(u"Book1.xlsx");

    // Get the first worksheet.
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Set E6 cell as the active cell.
    sheet.SetActiveCell(u"E6");

    // Split worksheet into four parts.
    sheet.Split();

    Aspose::Cells::Cleanup();
}
```

## **So entfernen Sie die Trennung**
Um die Trennung des Arbeitsblatts zu entfernen, klicken Sie einfach erneut auf die Schaltfläche Split.

Aspose.Cells for C++ bietet eine [**Worksheet.RemoveSplit**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/)-Methode zum Entfernen der Aufteilungseinstellung.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    Workbook workbook(u"Book1.xlsx");

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Remove split
    sheet.RemoveSplit();

    // Split worksheet into four parts
    sheet.Split();

    std::cout << "Worksheet split successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
