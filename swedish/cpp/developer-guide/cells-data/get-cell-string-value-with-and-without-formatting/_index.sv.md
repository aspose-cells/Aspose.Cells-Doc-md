---
title: Hämta cellsträngvärde med och utan formatering med C++
linktitle: Hämta cellsträngvärde
type: docs
weight: 240
url: /sv/cpp/get-cell-string-value-with-and-without-formatting/
description: Lär dig att hämta cellsträngvärde med och utan formatering via API Aspose.Cells for C++.
keywords: Hämta cellsträngvärde med och utan formatering, hämta cellsträngvärde med och utan formatering, erhåll cellsträngvärde med och utan formatering
---

{{% alert color="primary" %}}

Aspose.Cells tillhandahåller en metod [**Cell::GetStringValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/) som kan användas för att få cellens strängvärde med eller utan formatering. Anta att du har en cell med värdet 0,012345 och att du har formaterat den för att bara visa två decimaler. Den kommer då att visas som 0,01 i Excel. Du kan hämta strängvärden både som 0,01 och som 0,012345 med hjälp av [**Cell::GetStringValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/)-metoden. Den tar [**CellValueFormatStrategy**](https://reference.aspose.com/cells/cpp/aspose.cells/cellvalueformatstrategy/) enum som parameter, som har följande värden:

- CellValueFormatStrategy::CellStyle
- CellValueFormatStrategy::DisplayStyle
- CellValueFormatStrategy::DisplayString
- CellValueFormatStrategy::None

{{% /alert %}}

Följande exempelkod förklarar användningen av [**Cell::GetStringValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/) metoden.

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
