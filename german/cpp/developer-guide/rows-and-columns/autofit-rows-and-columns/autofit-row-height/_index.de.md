---
title: Automatisches Anpassen der Zeilenhöhe beim Laden der Datei mit C++
linktitle: Automatische Anpassung der Zeilenhöhe beim Laden der Datei
type: docs
weight: 120
url: /de/cpp/autofit-row-height/
description: Erfahren Sie, wie man die Zeilenhöhe anpasst, wenn diese nicht manuell eingestellt wurde, mit Aspose.Cells und C++.
keywords: Automatische Anpassung der Zeilenhöhe beim Laden der Datei, passt automatisch die Zeilenhöhe beim Öffnen der Excel Datei an.
---

## **Mögliche Verwendungsszenarien**
Die Höhe der Zeile passt sich automatisch an die Schriftart des Inhalts an, aber wenn die Höhe der zwischengespeicherten Zeile nicht mit der Höhe des Inhalts in der Datei übereinstimmt, passt MS Excel beim Laden der Datei die Zeilenhöhe automatisch an, während Aspose.Cells dies zur Leistungssteigerung nicht automatisch macht. Wenn Sie das Programm von Aspose.Cells verwenden möchten, um die Zeilenhöhen beim Laden von Dateien automatisch anzupassen, können Sie das Ziel mit dem Parameter [LoadOptions.GetOnlyAuto()](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getonlyauto/) erreichen.

Bitte beachten Sie die folgenden Bilddaten. Wir können beobachten, dass die zwischengespeicherte Zeilenhöhe in Zeile 11 15 beträgt, aber Excel passt die Zeilenhöhe automatisch an, wenn die Datei geladen wird.
<br>
<img src="1.png" width=70% />

## **Anpassen der Zeilenhöhe mit Aspose.Cells**
Wenn Sie die Datei direkt laden und sie als PDF speichern, wird die Daten nicht vollständig in PDF angezeigt, weil die Zeilenhöhe des zwischengespeicherten Inhalts nur 15 beträgt.
<br>
<img src="2.png" width=70% />
<br>
Wenn Sie beim Laden der Datei den Parameter [LoadOptions.GetOnlyAuto()](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getonlyauto/) auf true setzen, passt Aspose.Cells die Zeilenhöhe automatisch an. Die angepasste Zeilenhöhe kann die Textanzeigeanforderungen effektiv erfüllen.
<br>
<img src="3.png" width=70% />

## **C++ Beispielcode**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Define the file path
    U16String filePath(u"..\\Data\\01_SourceDirectory\\");

    // Open an existing Excel file and save it as PDF
    {
        Workbook wb(filePath + u"sample.xlsx");
        wb.Save(filePath + u"out.pdf");
    }

    // Set load options for the second workbook
    LoadOptions loadOptions;
    {
        AutoFitterOptions autoFitterOptions;
        autoFitterOptions.SetOnlyAuto(true);
        loadOptions.SetAutoFitterOptions(autoFitterOptions);
    }

    // Open the existing Excel file with load options and save it as PDF
    {
        Workbook book(filePath + u"sample.xlsx", loadOptions);
        book.Save(filePath + u"out2.pdf");
    }

    std::cout << "PDF files created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
