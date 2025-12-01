---
title: Implementing Non-Sequential Ranges with C++
linktitle: Implementing Non-Sequential Ranges
type: docs
weight: 700
url: /cpp/implementing-non-sequential-ranges/
description: Learn how to create named ranges with non-adjacent cells using Aspose.Cells with C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

Normally, named ranges are rectangular with cells continuous and adjacent to each other. But sometimes, you may need to use a non-sequential cell range in which cells are not adjacent. Aspose.Cells supports creating a named range with non-adjacent cells.

{{% /alert %}} 

The code sample below shows how to create a named non-sequential range with Aspose.Cells for C++.

```c++
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

    // Create a new workbook
    Workbook workbook;

    // Adding a Name for non sequenced range
    int index = workbook.GetWorksheets().GetNames().Add(u"NonSequencedRange");

    // Get the added name
    Name name = workbook.GetWorksheets().GetNames().Get(index);

    // Creating a non sequence range of cells
    name.SetRefersTo(u"=Sheet1!$A$1:$B$3,Sheet1!$D$5:$E$6");

    // Save the workbook
    workbook.Save(outDir + u"Output.out.xlsx");

    std::cout << "Workbook saved successfully with non-sequenced range!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
