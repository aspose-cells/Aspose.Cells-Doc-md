---
title: Ottieni il valore stringa della cella con e senza formattazione con C++
linktitle: Ottieni il valore stringa della cella
type: docs
weight: 240
url: /it/cpp/get-cell-string-value-with-and-without-formatting/
description: Impara come ottenere il valore stringa della cella con e senza formattazione tramite l API Aspose.Cells for C++.
keywords: Ottieni il valore della stringa della cella con e senza formattazione, recuperare il valore della stringa della cella con e senza formattazione, ottenere il valore della stringa della cella con e senza formattazione
---

{{% alert color="primary" %}}

Aspose.Cells fornisce un metodo [**Cell::GetStringValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/) che può essere usato per ottenere il valore stringa della cella con o senza formattazione. Supponi di avere una cella con valore 0.012345 e di averla formattata per mostrare solo due decimali. Verrà visualizzata come 0.01 in Excel. Puoi recuperare i valori stringa come 0.01 e come 0.012345 usando il metodo [**Cell::GetStringValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/). Richiede l'enumerazione [**CellValueFormatStrategy**](https://reference.aspose.com/cells/cpp/aspose.cells/cellvalueformatstrategy/) con i seguenti valori:

- CellValueFormatStrategy::CellStyle
- CellValueFormatStrategy::DisplayStyle
- CellValueFormatStrategy::DisplayString
- CellValueFormatStrategy::None

{{% /alert %}}

Il seguente codice di esempio spiega l'uso del metodo [**Cell::GetStringValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/).

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
