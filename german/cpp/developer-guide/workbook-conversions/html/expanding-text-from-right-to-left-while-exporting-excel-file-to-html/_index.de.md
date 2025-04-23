---
title: Expansionstext von rechts nach links beim Exportieren von Excel Dateien nach HTML mit C++
linktitle: Text von rechts nach links erweitern, während Excel Datei in HTML exportiert wird
type: docs
weight: 60
url: /de/cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/
description: Lernen, wie man Text von rechts nach links beim Exportieren von Excel Dateien nach HTML mit Aspose.Cells for C++ erweitert.
---

{{% alert color="primary" %}} 

Aspose.Cells for C++ unterstützt jetzt das Erweitern von Text von rechts nach links beim Exportieren von Excel-Dateien nach HTML. Dieses Feature wurde seit Version v8.9.0.0 implementiert. Wenn Ihre Quell-Excel-Datei Text enthält, der von rechts nach links erweitert wird, exportiert Aspose.Cells diesen korrekt nach HTML.

{{% /alert %}} 

## **Text von rechts nach links erweitern, während Excel-Datei in HTML exportiert wird**

Der folgende Beispielcode wandelt die [Beispieldatei Excel](5115502.xlsx) in HTML um. Dieses Screenshot zeigt, wie die Excel-Datei in Microsoft Excel 2013 aussieht.

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_1.png)

Dieses Screenshot zeigt das [generierte HTML mit älterer Version](5115509).

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_2.png)

Dieses Screenshot zeigt das [generierte HTML mit neuerer Version](5115508).

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_3.png)

Wie in den Screenshots zu sehen ist, erweitert die neuere Version den rechtsbündigen Text korrekt nach links, genau wie Microsoft Excel.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load source excel file inside the workbook object
    Workbook wb(srcDir + u"sample.xlsx");

    // Save workbook in html format
    U16String outputPath = srcDir + u"ExpandTextFromRightToLeft_out_" + CellsHelper::GetVersion() + u".html";
    wb.Save(outputPath, SaveFormat::Html);

    std::cout << "Workbook saved successfully in HTML format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
