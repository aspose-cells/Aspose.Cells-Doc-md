---
title: Erstellen von benannten Bereichen auf Arbeitsmappen und Arbeitsblatt Ebene mit C++
linktitle: Benannten Bereich
type: docs
weight: 40
url: /de/cpp/create-workbook-and-worksheet-scoped-named-ranges/
description: Lernen Sie, wie Sie mit C++ und Aspose.Cells benannte Bereiche auf Arbeitsmappen und Arbeitsblatt Ebene erstellen.
---

{{% alert color="primary" %}} 

Microsoft Excel ermöglicht es Benutzern, benannte Bereiche mit zwei verschiedenen Bereichen zu definieren: arbeitsmappe (auch als globaler Bereich bekannt) und tabellenblatt.

- Benannte Bereiche mit arbeitsmappenbereich können von jedem Arbeitsblatt innerhalb dieser Arbeitsmappe aus durch einfaches Verwenden ihres Namens aufgerufen werden.
- Auf tabellenblattbeschränkte benannte Bereiche werden mithilfe des Verweises auf das bestimmte Arbeitsblatt, in dem sie erstellt wurden, aufgerufen.

Aspose.Cells bietet dieselbe Funktionalität wie Microsoft Excel zum Hinzufügen von arbeitsmappe- und tabellenblattumfassenden benannten Bereichen. Beim Erstellen eines tabellenblattumfassenden benannten Bereichs sollte der Verweis auf das tabellenblatt im benannten Bereich verwendet werden, um ihn als tabellenblattumfassenden benannten Bereich zu kennzeichnen.

{{% /alert %}} 

## **Hinzufügen eines benannten Bereichs mit arbeitsmappenbereich**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    //Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create a new Workbook object
    Workbook workbook;

    // Get the first worksheet of the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get worksheet's cells collection
    Cells cells = sheet.GetCells();

    // Create a range of Cells from Cell A1 to C10
    Range workbookScope = cells.CreateRange(u"A1", u"C10");

    // Assign the name to workbook scope named range
    workbookScope.SetName(u"workbookScope");

    // Save the workbook
    workbook.Save(srcDir + u"WorkbookScope.out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Hinzufügen eines benannten Bereichs mit tabellenblattbereich**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create a new Workbook object
    Workbook workbook;

    // Get the first worksheet of the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get worksheet's cells collection
    Cells cells = sheet.GetCells();

    // Create a range of Cells
    Range localRange = cells.CreateRange(u"A1", u"C10");

    // Assign name to range with sheet reference
    localRange.SetName(u"Sheet1!local");

    // Save the workbook
    U16String outputFilePath = u"..\\Data\\02_OutputDirectory\\output.out.xls";
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Erweiterte Themen**
- [Zugriff erstellen und benannte Bereiche kopieren](/cells/de/cpp/create-access-and-copy-named-ranges/)
- [Benannte Bereiche formatieren und ändern](/cells/de/cpp/format-and-modify-named-ranges/)
- [Bereich mit externen Links abrufen](/cells/de/cpp/get-range-with-external-links/)
- [Implementierung nicht aufeinanderfolgender Bereiche](/cells/de/cpp/implementing-non-sequential-ranges/)

