---
title: Implementierung nicht sequenzieller Bereiche mit C++
linktitle: Implementieren von nicht sequentiellen Bereich
type: docs
weight: 700
url: /de/cpp/implementing-non-sequential-ranges/
description: Erfahren Sie, wie Sie benannte Bereiche mit nicht angrenzenden Zellen mit Aspose.Cells und C++ erstellen.
---

{{% alert color="primary" %}} 

Normalerweise sind benannte Bereiche rechteckig mit zusammenhängenden und benachbarten Zellen. Manchmal müssen Sie jedoch einen nicht-sequenziellen Zellenbereich verwenden, bei dem die Zellen nicht benachbart sind. Aspose.Cells unterstützt die Erstellung eines benannten Bereichs mit nicht benachbarten Zellen.

{{% /alert %}} 

Der untenstehende Code zeigt, wie man einen nicht-sequenziellen benannten Bereich mit Aspose.Cells for C++ erstellt.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Adding a Name for non sequenced range
    int index = workbook.GetWorksheets().GetNames().Add(u"NonSequencedRange");

    // Get the added name
    Name name = workbook.GetWorksheets().GetNames().Get(index);

    // Creating a non sequence range of cells
    name.SetRefersTo(u"=Sheet1!$A$1:$B$3,Sheet1!$D$5:$E$6");

    // Save the workbook
    workbook.Save(outDir + u"Output.out.xlsx");

    std::cout << "Workbook saved successfully with non-sequenced range!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
