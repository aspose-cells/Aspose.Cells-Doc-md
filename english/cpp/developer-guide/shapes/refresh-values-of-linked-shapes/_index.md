---
title: Refresh Values of Linked Shapes with C++
linktitle: Refresh Values of Linked Shapes
type: docs
weight: 3200
url: /cpp/refresh-values-of-linked-shapes/
description: Learn how to refresh values of linked shapes in Excel files using Aspose.Cells for C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Sometimes, you have a linked shape in your Excel file which is linked to some cell. In Microsoft Excel, changing the value of the linked cell also changes the value of the linked shape. This also works fine with Aspose.Cells if you want to save your workbook in XLS or XLSX format. However, if you want to save your workbook in PDF or HTML format, then you will have to call [**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/updateselectedvalue/) method to refresh the value of the linked shape.

{{% /alert %}}

## Example

The following screenshot shows the source Excel file used in the sample code below. It has a linked picture linked to cells A1 to E4. We will change the value of cell B4 with Aspose.Cells and then call [**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/updateselectedvalue/) method to refresh the value of the picture and save it in PDF format.

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)

You can download the [source Excel file](95584291.xlsx) and the [output PDF](95584292.pdf) from the given links.

### C++ code to refresh the values of linked shapes

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook from source file
    Workbook workbook(srcDir + u"sampleRefreshValueOfLinkedShapes.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Change the value of cell B4
    Cell cell = worksheet.GetCells().Get(u"B4");
    cell.PutValue(100);

    // Update the value of the Linked Picture which is linked to cell B4
    worksheet.GetShapes().UpdateSelectedValue();

    // Save the workbook in PDF format
    workbook.Save(outDir + u"outputRefreshValueOfLinkedShapes.pdf", SaveFormat::Pdf);

    std::cout << "Linked shapes value refreshed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
