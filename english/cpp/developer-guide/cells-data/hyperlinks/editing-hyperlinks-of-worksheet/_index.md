---
title: Editing Hyperlinks of Worksheet with C++
linktitle: Editing Hyperlinks of Worksheet
type: docs
weight: 330
url: /cpp/editing-hyperlinks-of-worksheet/
description: Learn how to edit hyperlinks of Worksheet through the Aspose.Cells for C++ API.
keywords: Edit Hyperlinks, Edit Hyperlinks of Worksheet, Edit hyperlink of Cell, Access all the hyperlinks of the worksheet
---

{{% alert color="primary" %}}

Aspose.Cells allows you to access all the hyperlinks of the worksheet using the [**GetHyperlinks()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gethyperlinks/) collection. You can access each hyperlink from this collection one by one and edit its properties.

{{% /alert %}}

The following sample code accesses all the hyperlinks of the worksheet and changes their [**GetAddress()**](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/getaddress/) property to the Aspose website.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook from input file
    Workbook workbook(srcDir + u"Sample.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Iterate through all hyperlinks in the worksheet
    for (int32_t i = 0; i < worksheet.GetHyperlinks().GetCount(); i++)
    {
        Hyperlink hl = worksheet.GetHyperlinks().Get(i);
        hl.SetAddress(u"http://www.aspose.com");
    }

    // Save the modified workbook to the output file
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Hyperlinks updated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```