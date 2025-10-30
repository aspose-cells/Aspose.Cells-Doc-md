---
title: Benutzerdefinierte Papiergröße des Arbeitsblatts für die Wiedergabe mit C++ implementieren
linktitle: Benutzerdefinierte Papiergröße des Arbeitsblatts für die Darstellung implementieren
type: docs
weight: 70
url: /de/cpp/implement-custom-paper-size-of-worksheet-for-rendering/
description: Dieser Artikel erklärt, wie Sie die C++ API verwenden, um die benutzerdefinierte Papiergröße Ihrer gewünschten Arbeitsblätter beim programmgesteuerten Rendern einer Excel Datei in das PDF Format festzulegen.
keywords: Benutzerdefinierte Papiergröße beim Rendern von Excel nach PDF mit C++ festlegen
---

## **Mögliche Verwendungsszenarien**

Es steht keine direkte Option zur Verfügung, um benutzerdefinierte Papiergrößen in MS Excel zu erstellen; jedoch können Sie beim Rendern von Excel-Dateien in das PDF-Format die Papiergröße Ihrer gewünschten Arbeitsblätter anpassen. Dieses Dokument erklärt, wie Sie die Papiergröße eines Arbeitsblatts mit Aspose.Cells-APIs festlegen können.

## **Benutzerdefinierte Papiergröße des Arbeitsblatts für die Darstellung implementieren**

Aspose.Cells ermöglicht es Ihnen, die gewünschte Papiergröße des Arbeitsblatts festzulegen. Sie können die [**CustomPaperSize**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/custompapersize/)-Methode der [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/)-Klasse verwenden, um eine benutzerdefinierte Seitengröße anzugeben. Der folgende Beispielcode zeigt, wie Sie eine benutzerdefinierte Papiergröße für das erste Arbeitsblatt im Arbeitsbuch festlegen. Bitte beachten Sie auch das [Ausgabe-PDF](45056028.pdf), das mit dem folgenden Code zur Referenz erstellt wurde.

## **Screenshot**

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)

## **Beispielcode**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create workbook object
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Set custom paper size in unit of inches
    ws.GetPageSetup().CustomPaperSize(6, 4);

    // Access cell B4
    Cell b4 = ws.GetCells().Get("B4");

    // Add the message in cell B4
    b4.PutValue(u"Pdf Page Dimensions: 6.00 x 4.00 in");

    // Save the workbook in pdf format
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    wb.Save(outputDir + u"outputCustomPaperSize.pdf");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
