---
title: Access and Modify the Display Label of the Linked Ole Object with C++
linktitle: Access and Modify the Display Label of the Linked Ole Object
type: docs
weight: 100
url: /cpp/access-and-modify-the-display-label-of-the-linked-ole-object/
description: Learn how to access and modify the display label of linked Ole Objects in Excel files using Aspose.Cells for C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Microsoft Excel allows you to change the display label of the OLE object as shown in the following screenshot. You can also access or modify the display label of the OLE object using Aspose.Cells APIs with the [**GetLabel()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getlabel/) and [**SetLabel(const U16String\& value)**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/setlabel/) methods.

![todo:image_alt_text](access-and-modify-the-display-label-of-the-linked-ole-object_1.png)

## **Access and Modify the Display Label of the Linked Ole Object**

Please see the following sample code; it loads the [sample Excel file](64716810.xlsx) that contains the OLE object. The code accesses the OLE object and changes its label from **Sample APIs** to **Aspose APIs**. The console output below shows the effect of the sample code on the sample Excel file for reference.

## **Sample Code**

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Load the sample Excel file
    U16String inputFilePath = u"sampleAccessAndModifyLabelOfOleObject.xlsx";
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first Ole Object
    OleObject oleObject = ws.GetOleObjects().Get(0);

    // Display the Label of the Ole Object
    std::cout << "Ole Object Label - Before: " << oleObject.GetLabel().ToUtf8() << std::endl;

    // Modify the Label of the Ole Object
    oleObject.SetLabel(u"Aspose APIs");

    // Save workbook to memory stream
    auto ms = wb.SaveToStream();

    // Set the workbook reference to null
    wb = Workbook();

    // Load workbook from memory stream
    wb = Workbook(ms);

    // Access first worksheet
    ws = wb.GetWorksheets().Get(0);

    // Access first Ole Object
    oleObject = ws.GetOleObjects().Get(0);

    // Display the Label of the Ole Object that has been modified earlier
    std::cout << "Ole Object Label - After: " << oleObject.GetLabel().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Console Output**

{{< highlight java >}}

Ole Object Label - Before: Sample APIs

Ole Object Label - After: Aspose APIs

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
