---
title: How to set AutoRecover property of Workbook with C++
linktitle: How to set AutoRecover property of Workbook
type: docs
weight: 220
url: /cpp/how-to-set-autorecover-property-of-workbook/
description: Learn how to enable or disable the AutoRecover property of a workbook using Aspose.Cells for C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

You can use Aspose.Cells to set the AutoRecover property of a workbook. The default value of this property is **true**. When you set it to **false** on a workbook, Microsoft Excel disables AutoRecover (autosave) for that Excel file.

Aspose.Cells provides the [**Workbook.GetAutoRecover()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getautorecover/) property to enable or disable this option.

{{% /alert %}}

The following code explains how to use the [**Workbook.GetAutoRecover()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getautorecover/) property of the workbook. The code first reads the default value of this property, which is **true**, then sets it to **false** and saves the workbook. It then reads the workbook again and obtains the value of this property, which is **false** at that time.

## C++ code to set the AutoRecover property of Workbook

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

    // Create workbook object
    Workbook workbook;

    // Read AutoRecover property
    std::cout << "AutoRecover: " << workbook.GetSettings().GetAutoRecover() << std::endl;

    // Set AutoRecover property to false
    workbook.GetSettings().SetAutoRecover(false);

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    // Read the saved workbook again
    Workbook workbook2(outDir + u"output_out.xlsx");

    // Read AutoRecover property
    std::cout << "AutoRecover: " << workbook2.GetSettings().GetAutoRecover() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Output**

Here is the console output of the above sample code.

{{< highlight cpp >}}
AutoRecover: True
AutoRecover: False
{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
