---
title: Steuerung der Blattregisterkarte mit C++
linktitle: Steuerung der Registerkartenleiste
type: docs
weight: 600
url: /de/cpp/how-to-control-sheet-tab-bar/
description: Erfahren Sie, wie Sie die Blattregisterkarte mithilfe der Aspose.Cells for C++ API steuern.
keywords: Wie man die Registerkartenleiste steuert, die Registerkartenleiste bedient, die Registerkartenleiste einstellt, die Registerkartenleiste steuert. 
---

## **Mögliche Verwendungsszenarien**
Wenn Sie die Anzeige der Excel-Tabellenleiste anpassen möchten, müssen Sie wissen, wie die Blattregisterkarte gesteuert wird, z. B. das Verbergen oder Anzeigen der Registerkarte, die Änderung der Breite der Registerkarte, die Festlegung des ersten sichtbaren Tabs usw. Aspose.Cells unterstützt diese Funktionen. Aspose.Cells stellt die folgenden Eigenschaften und Methoden bereit, um Ihre Ziele zu erreichen.

- [**WorkbookSettings.GetShowTabs()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshowtabs/)
- [**WorkbookSettings.GetSheetTabBarWidth()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getsheettabbarwidth/)
- [**WorkbookSettings.GetFirstVisibleTab()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getfirstvisibletab/)

## **Steuerung der Blattregisterkarte mit Aspose.Cells for C++**
Dieses Beispiel zeigt, wie Sie:

1. Ein Arbeitsbuch erstellen.
1. Daten zu Zellen im ersten Arbeitsblatt hinzufügen.
1. Zeigen Sie die Registerkarte an und legen Sie die Breite der Registerkartenleiste fest.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook object
    Workbook workbook;

    // Obtain the reference to the newly added worksheet
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

    // Display the sheet tab and set the width of the tab bar
    workbook.GetSettings().SetShowTabs(true);
    workbook.GetSettings().SetSheetTabBarWidth(150);

    // Save the workbook
    workbook.Save(u"out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Vorschau der Ergebnisdatei:
<br>
<image src="result.png" width="70%" />

