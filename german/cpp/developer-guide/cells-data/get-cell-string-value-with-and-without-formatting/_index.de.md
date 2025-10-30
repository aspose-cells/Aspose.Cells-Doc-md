---
title: Cell String Wert mit und ohne Formatierung in C++ abrufen
linktitle: Cell String Wert abrufen
type: docs
weight: 240
url: /de/cpp/get-cell-string-value-with-and-without-formatting/
description: Lernen Sie, wie Sie den Cell String Wert mit und ohne Formatierung über die Aspose.Cells for C++ API abrufen.
keywords: Zellenzeichenfolgenwert mit und ohne Formatierung abrufen, Zellenzeichenfolgenwert mit und ohne Formatierung abrufen, Zellenzeichenfolgenwert mit und ohne Formatierung erhalten
---

{{% alert color="primary" %}}

Aspose.Cells bietet eine Methode [**Cell::GetStringValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/), um den String-Wert der Zelle mit oder ohne Formatierung zu erhalten. Angenommen, Sie haben eine Zelle mit dem Wert 0.012345 und haben sie so formatiert, dass nur zwei Dezimalstellen angezeigt werden. Es wird dann in Excel als 0.01 angezeigt. Sie können String-Werte sowohl als 0.01 als auch als 0.012345 mit der Methode [**Cell::GetStringValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/) abrufen. Diese Methode akzeptiert den Enum [**CellValueFormatStrategy**](https://reference.aspose.com/cells/cpp/aspose.cells/cellvalueformatstrategy/) als Parameter, der folgende Werte hat:

- CellValueFormatStrategy::CellStyle
- CellValueFormatStrategy::DisplayStyle
- CellValueFormatStrategy::DisplayString
- CellValueFormatStrategy::None

{{% /alert %}}

Der folgende Beispielcode erläutert die Verwendung der [**Cell::GetStringValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/)-Methode.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Put value inside the cell
    cell.PutValue(0.012345);

    // Format the cell to display 0.01 instead of 0.012345
    Style style = cell.GetStyle();
    style.SetNumber(2);
    cell.SetStyle(style);

    // Get string value as Cell Style
    U16String value = cell.GetStringValue(CellValueFormatStrategy::CellStyle);
    std::cout << value.ToUtf8() << std::endl;

    // Get string value without any formatting
    value = cell.GetStringValue(CellValueFormatStrategy::None);
    std::cout << value.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
