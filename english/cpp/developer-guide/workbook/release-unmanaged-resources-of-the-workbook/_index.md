---
title: Release Unmanaged Resources of the Workbook with C++
linktitle: Release Unmanaged Resources of the Workbook
type: docs
weight: 310
url: /cpp/release-unmanaged-resources-of-the-workbook/
description: Learn how to release unmanaged resources of the Workbook using Aspose.Cells with C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells provides [**Workbook.Dispose()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/dispose/) method to release the unmanaged resources of the [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) object. The dispose pattern is used only for objects that access unmanaged resources, such as file and pipe handles, registry handles, wait handles, or pointers to blocks of unmanaged memory. This is because the garbage collector is very efficient at reclaiming unused managed objects, but it is unable to reclaim unmanaged objects.

{{% /alert %}}

[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) object now implements the *IDisposable* interface which has a single method [**Dispose()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/dispose/). You can either call the [**Workbook.Dispose()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/dispose/) method directly, or you can use the *using* statement to call this method automatically.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook wb1;

    // Call Dispose method
    wb1.Dispose();

    // Call Dispose method via RAII (Resource Acquisition Is Initialization)
    {
        Workbook wb2;
        // Any other code goes here
    } // wb2 is automatically disposed when it goes out of scope

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
