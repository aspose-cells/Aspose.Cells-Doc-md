---
title: Get HTML5 String from Cell with C++
linktitle: Get HTML5 String from Cell
type: docs
weight: 90
url: /cpp/get-html5-string-from-cell/
description: Learn how to get an HTML5 string from a cell using Aspose.Cells for C++ API.
keywords: Get HTML5 string from Cell, Obtain HTML5 string from Cell, Manage HTML5 string of Cell
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Aspose.Cells returns the HTML string of a cell using the [**GetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/) method, which accepts a boolean parameter. If you pass **false** as a parameter, it returns normal HTML, but if you pass **true**, it returns an HTML5 string.

## **Get HTML5 String from Cell**

The following sample code creates a workbook object and adds some text in cell A1 of the first worksheet. It then gets the normal HTML and HTML5 strings from cell A1 using the [**GetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/) method and prints them on the console.

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

    // Access cell A1 and put some text inside it
    Cell cell = ws.GetCells().Get(u"A1");
    cell.PutValue(u"This is some text.");

    // Get the Normal and Html5 strings
    U16String strNormal = cell.GetHtmlString(false);
    U16String strHtml5 = cell.GetHtmlString(true);

    // Print the Normal and Html5 strings on console
    std::cout << "Normal:\r\n" << strNormal.ToUtf8() << std::endl;
    std::cout << std::endl;
    std::cout << "Html5:\r\n" << strHtml5.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Console Output**

{{< highlight html >}}

Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

HTML5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
