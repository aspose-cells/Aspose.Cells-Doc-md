---
title: Office Add Ins beim Konvertieren von Excel in PDF mit C++ rendern
linktitle: Office Add Ins beim Konvertieren von Excel in PDF rendern
type: docs
weight: 100
url: /de/cpp/render-office-add-ins-while-converting-excel-to-pdf/
description: Erfahren Sie, wie Sie Office Add Ins beim Konvertieren von Excel Dateien in PDF mit Aspose.Cells for C++ rendern.
---

## **Mögliche Verwendungsszenarien**

Früher konnte Aspose.Cells Office-Add-Ins nicht rendern, wenn eine Excel-Datei in PDF gespeichert wurde. Jetzt rendert Aspose.Cells es korrekt. Es ist nicht notwendig, eine spezielle Methode oder Eigenschaft zu verwenden, um Office-Add-Ins im Ausgabepdf zu rendern. Speichern Sie einfach Ihre Excel-Datei im PDF-Format, und es werden die Office-Add-Ins gerendert.

## **Office-Add-Ins beim Konvertieren von Excel in PDF anzeigen**

Das folgende Beispiel speichert die [Beispiel-Excel-Datei](60489769.xlsx), die Office-Add-Ins enthält. Bitte sehen Sie sich das [Ausgabe-PDF, das mit der früheren Version (z.B. 17.11) generiert wurde](60489770.pdf), und das [Ausgabe-PDF, das mit der neueren Version (z.B. 17.12 und später) erstellt wurde](60489771.pdf). Das Ausgabe-PDF der vorherigen Version ist Leer, während das neuere eine Office-Add-In anzeigt.

## **Beispielcode**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load the sample Excel file containing Office Add-Ins
    U16String inputFilePath = u"sampleRenderOfficeAdd-Ins.xlsx";
    Workbook wb(inputFilePath);

    // Save it to Pdf format with version appended to the output filename
    U16String outputFilePath = u"output-" + CellsHelper::GetVersion() + u".pdf";
    wb.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "File saved successfully: " << outputFilePath.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
