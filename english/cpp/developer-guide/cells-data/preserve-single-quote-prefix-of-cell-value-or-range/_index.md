---
title: Preserve Single Quote Prefix of Cell Value or Range with C++
linktitle: Preserve Single Quote Prefix of Cell Value or Range
type: docs
weight: 310
url: /cpp/preserve-single-quote-prefix-of-cell-value-or-range/
description: Learn how to preserve the single‑quote prefix of a cell value or range through the Aspose.Cells for C++ API.
keywords: Preserve Single Quote Prefix of Cell Value or Range, Hide leading apostrophe or single quote mark, Show leading apostrophe or single quote mark
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

When you put a value inside a cell that has a leading apostrophe or single‑quote mark, Microsoft Excel hides it, but when you select the cell, it displays the leading apostrophe or single quote in the formula bar, as shown in the following screenshot.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells also hides the leading apostrophe or single quote like Microsoft Excel, but it sets the [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/) property to **true** for that cell. If you set an empty style for the cell, then [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/) becomes **false** again. To deal with this situation, Aspose.Cells provides the [**StyleFlag.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/getquoteprefix/) property. When it is set to **false**, [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/) is not updated at all and its previous value is preserved. This means that if the old value of the [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/) property was **true**, it will remain **true**; if the old value was **false**, it will remain **false**.

## **Preserve Single Quote Prefix of Cell Value or Range**

The following sample code demonstrates the usage of the [**StyleFlag.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/getquoteprefix/) property as described above. Please read the comments inside the code and see the console output for more help.

## **Sample Code**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell A1
    Cell cell = ws.GetCells().Get(u"A1");

    // Put some text in the cell; it does not have a leading single quote
    cell.PutValue(u"Text");

    // Access style of cell A1
    Style st = cell.GetStyle();

    // Print the value of Style.QuotePrefix of cell A1
    std::cout << "Quote Prefix of Cell A1: " << st.GetQuotePrefix() << std::endl;

    // Put some text in the cell; it has a leading single quote
    cell.PutValue(u"'Text");

    // Access style of cell A1
    st = cell.GetStyle();

    // Print the value of Style.QuotePrefix of cell A1
    std::cout << "Quote Prefix of Cell A1: " << st.GetQuotePrefix() << std::endl;

    // Print information about StyleFlag.QuotePrefix property
    std::cout << std::endl;
    std::cout << "When StyleFlag.QuotePrefix is false, it means do not update the value of Cell.Style.QuotePrefix." << std::endl;
    std::cout << "Similarly, when StyleFlag.QuotePrefix is true, it means update the value of Cell.Style.QuotePrefix." << std::endl;
    std::cout << std::endl;

    // Create an empty style
    st = wb.CreateStyle();

    // Create style flag – set StyleFlag.QuotePrefix to false
    // It means we do not want to update the Style.QuotePrefix property of cell A1's style.
    StyleFlag flag;
    flag.SetQuotePrefix(false);

    // Create a range consisting of the single cell A1
    Range rng = ws.GetCells().CreateRange(u"A1");

    // Apply the style to the range
    rng.ApplyStyle(st, flag);

    // Access the style of cell A1
    st = cell.GetStyle();

    // Print the value of Style.QuotePrefix of cell A1
    // It will print true because we have not updated the Style.QuotePrefix property of cell A1's style.
    std::cout << "Quote Prefix of Cell A1: " << st.GetQuotePrefix() << std::endl;

    // Create another empty style
    st = wb.CreateStyle();

    // Create style flag – set StyleFlag.QuotePrefix to true
    // It means we want to update the Style.QuotePrefix property of cell A1's style.
    flag.SetQuotePrefix(true);

    // Apply the style to the range
    rng.ApplyStyle(st, flag);

    // Access the style of cell A1
    st = cell.GetStyle();

    // Print the value of Style.QuotePrefix of cell A1
    // It will print false because we have updated the Style.QuotePrefix property of cell A1's style.
    std::cout << "Quote Prefix of Cell A1: " << st.GetQuotePrefix() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Console Output**

{{< highlight java >}}
Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False
{{< /highlight >}}

{{< app/cells/assistant language="cpp" >}}
