---
title: Reusing Style Objects with C++
linktitle: Reusing Style Objects
description: In Aspose.Cells for C++, by creating and using reusable style objects, you can simplify style management and improve code efficiency. Our guide will help you leverage the advantages of reusable style objects and implement them in your application.
keywords: Aspose.Cells for C++, Reusing Style Objects, Style Management, Code Efficiency, Reusable Styles, Application Development, API Reference, Example Code, Download, Support.
type: docs
weight: 3000
url: /cpp/reusing-style-objects/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Reusing style objects can save memory and make a program faster.

{{% /alert %}}

To apply some formatting to a large range of cells in a worksheet:

1. Create a style object.  
2. Specify the attributes.  
3. Apply the style to the cells in the range.

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

    // Put the values inside the cells
    cell1.PutValue(u"Hello World!");
    cell2.PutValue(u"Hello World!!");

    // Save to PDF without setting PdfSaveOptions.IsFontSubstitutionCharGranularity
    workbook.Save(outDir + u"SampleOutput_out.xlsx");

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Because the **Cell.GetStyle**/**Cell.SetStyle** approach uses far less memory and is efficient, the older **Cell.Style** property, which consumed a lot of unnecessary memory, was removed with the release of Aspose.Cells 7.1.0.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
