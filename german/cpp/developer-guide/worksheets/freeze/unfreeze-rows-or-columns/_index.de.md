---
title: Zeilen oder Spalten in Excel Arbeitsblättern mit C++ entsperren
linktitle: Fenster fixieren
type: docs
weight: 190
url: /de/cpp/unfreeze-rows-or-columns-of-excel-worksheet
description: In diesem Artikel lernen Sie, wie Sie Zeilen, Spalten oder Fenster in Excel Arbeitsblättern programmgesteuert mithilfe der Aspose.Cells for C++ API entsperren.
keywords: Fenster, Zeilen, Spalten oder Paneele entsperren.
---

## **Einführung**

In diesem Artikel lernen wir, wie man Zeilen, Spalten und Paneele in Excel-Arbeitsblättern entsperrt. Wenn Arbeitsblätter in Excel-Dateien gefroren sind, möchten wir manchmal das Arbeitsblatt entsperren oder eingefrorene Zeilen, Spalten oder Paneele anpassen.

## **In Excel**

1. Klicken Sie auf die **Ansicht**-Registerkarte > **Fenster einfrieren** > **Fenster entsperren**.

**![Fenster nicht fixieren in Excel](Unfreeze-Panes.png)**

## **Zeilen, Spalten oder Paneele mit Aspose.Cells for C++ entsperren**
Das Entsperren von Paneelen mit Aspose.Cells for C++ ist einfach. Verwenden Sie die [**Worksheet.UnFreezePanes**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/unfreezepanes/)-Methode, um Paneele zu entsperren.

1. Erstellen Sie ein `Workbook`-Objekt, um die eingefrorene Datei zu öffnen.
2. Entsperren Sie Paneele mit der Methode `Worksheet.UnFreezePanes()`.
3. Die Datei speichern.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    U16String inputFilePath(u"Frozen.xlsx");
    Workbook workbook(inputFilePath);

    // Unfreeze panes in the first worksheet
    workbook.GetWorksheets().Get(0).UnFreezePanes();

    // Save the modified workbook
    U16String outputFilePath(u"Unfrozen.xlsx");
    workbook.Save(outputFilePath);

    std::cout << "Panes unfrozen successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Angehängte [Beispiel-Excel-Quelldatei](Frozen.xlsx).
{{< app/cells/assistant language="cpp" >}}
