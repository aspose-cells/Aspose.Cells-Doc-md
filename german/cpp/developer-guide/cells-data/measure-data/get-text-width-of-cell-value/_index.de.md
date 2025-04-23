---
title: Textbreite des Zellwerts mit C++ ermitteln
linktitle: Textbreite des Zellenwerts erhalten
type: docs
weight: 50
url: /de/cpp/get-text-width-of-cell-value/
description: Lernen Sie, wie Sie die Textbreite des Zellwerts durch die API Aspose.Cells for C++ ermitteln.
keywords: Textbreite des Zellenwerts erhalten, Textbreite des Zellenwerts erhalten
---

## **Breite des Zellenwerts abrufen**

Manchmal müssen Entwickler die Breite des Zellwerts berechnen, um Daten in einem bestimmten Layout zu arrangieren. Aspose.Cells bietet die [**CellsHelper::GetTextWidth**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/gettextwidth/)-Methode, die Entwicklern ermöglicht, die Textbreite des Zellwerts zu ermitteln. Das folgende Beispiel zeigt, wie man [**CellsHelper::GetTextWidth**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/gettextwidth/) verwendet, um auf die Textbreite des Zellwerts zuzugreifen.

Die im folgenden Code-Ausschnitt verwendete Quelldatei ist zur Referenz angehängt.

[Quelldatei](96928090.xlsx)

## Beispielcode

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Directory path for source files
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook from the specified Excel file
    Workbook workbook(sourceDir + u"GetTextWidthSample.xlsx");

    // Calculate the text width for the string value of cell A1
    double textWidth = CellsHelper::GetTextWidth(workbook.GetWorksheets().Get(0).GetCells().Get(u"A1").GetStringValue(), workbook.GetDefaultStyle().GetFont(), 1);

    // Output the text width
    std::wcout << u"Text width: " << textWidth << std::endl;

    Aspose::Cells::Cleanup();
}
```
