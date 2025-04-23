---
title: Wiederverwendung von Style Objekten mit C++
linktitle: Wiederverwendung von Style Objekten
description: In Aspose.Cells for C++ schafft die Erstellung und Verwendung wiederverwendbarer Style Objekte eine Vereinfachung der Stilverwaltung und verbessert die Code Effizienz. Unser Leitfaden hilft, die Vorteile wiederverwendbarer Style Objekte zu nutzen und sie in Ihrer Anwendung zu implementieren.
keywords: Aspose.Cells for C++, Wiederverwendung von Style Objekten, Stilverwaltung, Code Effizienz, Wiederverwendbare Stile, Anwendungsentwicklung, API Referenz, Beispielcode, Download, Support.
type: docs
weight: 3000
url: /de/cpp/reusing-style-objects/
---

{{% alert color="primary" %}}

Die Wiederverwendung von Style-Objekten kann Speicherplatz sparen und ein Programm schneller machen.

{{% /alert %}}

Um einige Formatierungen auf einen großen Zellenbereich in einem Arbeitsblatt anzuwenden:

1. Erstellen Sie ein Style-Objekt.
1. Geben Sie die Attribute an.
1. Wenden Sie den Style auf die Zellen im Bereich an.

```cpp
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

    // Create workbook object
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cells
    Cell cell1 = worksheet.GetCells().Get(u"A1");
    Cell cell2 = worksheet.GetCells().Get(u"B1");

    // Set the styles of both cells to Times New Roman
    Style styleObject = workbook.CreateStyle();
    styleObject.GetFont().SetColor(Color::Red());
    styleObject.GetFont().SetName(u"Times New Roman");
    cell1.SetStyle(styleObject);
    cell2.SetStyle(styleObject);

    // Put the values inside the cell
    cell1.PutValue(u"Hello World!");
    cell2.PutValue(u"Hello World!!");

    // Save to Pdf without setting PdfSaveOptions.IsFontSubstitutionCharGranularity
    workbook.Save(outDir + u"SampleOutput_out.xlsx");

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Da der Ansatz [**Cell.GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/)/[**Cell.SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) viel weniger Speicherplatz verbraucht und effizient ist, wurde die ältere Cell.Style-Eigenschaft, die unnötig viel Speicherplatz verbrauchte, mit der Veröffentlichung von Aspose.Cells 7.1.0 entfernt.

{{% /alert %}}
