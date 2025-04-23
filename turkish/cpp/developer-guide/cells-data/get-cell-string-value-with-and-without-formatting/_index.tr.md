---
title: C++ ile Hücre Dizisi Değeri ile Formatlama ve Formatlamadan Alma
linktitle: Hücre Dizisi Değeri Alma
type: docs
weight: 240
url: /tr/cpp/get-cell-string-value-with-and-without-formatting/
description: Aspose.Cells for C++ API kullanarak, Formatlama ve Formatlamadan Hücre Dizisi Değeri Alma yöntemlerini öğrenin.
keywords: Biçimlendirme ile ve biçimlendirme olmadan Hücre Dize Değeri Almayı, Biçimlendirme ile ve biçimlendirme olmadan Hücre Dize Değeri Almayı Kurtarma, Biçimlendirme ile ve biçimlendirme olmadan Hücre Dize Değeri Almayı Elde Etme
---

{{% alert color="primary" %}}

Aspose.Cells, hücrenin değerini ve nan herhangi bir biçimlendirme ile veya biçimlendirmeden almak için kullanılabilecek [**Cell::GetStringValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/) yöntemini sağlar. Diyelim ki, değeri 0.012345 olan bir hücreniz var ve sadece iki ondalık gösterilecek şekilde biçimlendirilmiş. Bu durumda, Excel'de 0.01 olarak görüntülenir. Hem 0.01 hem de 0.012345 şeklinde string değerleri `[**Cell::GetStringValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/)` yöntemi ile alabilirsiniz. Bu yöntem, aşağıdaki değerleri içeren `[**CellValueFormatStrategy**](https://reference.aspose.com/cells/cpp/aspose.cells/cellvalueformatstrategy/)` enum parametresi alır:

- CellValueFormatStrategy::CellStyle
- CellValueFormatStrategy::DisplayStyle
- CellValueFormatStrategy::DisplayString
- CellValueFormatStrategy::Hiçbiri

{{% /alert %}}

Aşağıdaki örnek kod, [**Cell::GetStringValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/) yönteminin kullanımını açıklar.

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
