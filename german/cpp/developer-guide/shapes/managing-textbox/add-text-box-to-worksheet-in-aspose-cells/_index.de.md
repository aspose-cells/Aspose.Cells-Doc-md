---
title: Wie man ein Textfeld mit C++ zum Arbeitsblatt hinzufügt/eingibt
linktitle: Fügen Sie eine Textbox in ein Arbeitsblatt ein
type: docs
weight: 10
url: /de/cpp/add-text-box-to-worksheet-in-aspose-cells/
description: Wie man in Aspose.Cells mit C++ ein Textfeld zum Arbeitsblatt hinzufügt/eingibt.
keywords: Textfeld hinzufügen/einfügen Textfeld Arbeitsblatt Excel Aspose
---

## Fügen Sie ein Textfeld in das Arbeitsblatt in Excel ein

In den Excel-Programmen (Version 07 und höher) gibt es zwei Stellen, an denen Sie Textfelder einfügen können. Einmal in "Einfügen-Formen", dann auf der rechten Seite des oberen Menüs unter der Option "Einfügen".

### Methode Eins:

![1](1.png)

### Methode Zwei:

![2](2.png)

## Wie man erstellt

Sie können Textfelder mit horizontal oder vertikal ausgerichtetem Text erstellen.

- Wählen Sie die entsprechende Option (horizontal oder vertikal)
- Klicken Sie links auf die Seite
- Halten Sie die linke Taste gedrückt und ziehen Sie eine Entfernung auf der Seite
- Lassen Sie die linke Taste los

Nun haben Sie ein Textfeld.

## Fügen Sie ein Textfeld in das Arbeitsblatt in Aspose.Cells ein

Wenn Sie eine große Anzahl von Textfeldern in das Arbeitsblatt einfügen müssen, ist die manuelle Einfügung offensichtlich problematisch. Wenn Sie dies stört, wird dieses Dokument Ihnen sicherlich helfen. [Aspose.Cells](https://products.aspose.com/cells/) bietet eine API, mit der Sie einfache Masseninserts in Ihrem Code durchführen können.

Der folgende Beispielcode erstellt ein Textfeld.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create an object of the Workbook class
    Workbook workbook;

    // Access first worksheet from the collection
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Add the TextBox to the worksheet
    sheet.GetTextBoxes().Add(6, 10, 100, 200);

    // Save the workbook with the text box
    workbook.Save(outDir + u"result.xlsx", SaveFormat::Xlsx);

    std::cout << "Text box added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Sie erhalten eine Datei, die der [Ergebnisdatei](result.xlsx) ähnlich ist. In der Datei werden Sie Folgendes sehen:

![](52449.png)
