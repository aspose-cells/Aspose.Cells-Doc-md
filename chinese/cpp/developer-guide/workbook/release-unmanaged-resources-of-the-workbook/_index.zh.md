---
title: 用C++释放工作簿的未管理资源
linktitle: 释放工作簿的非托管资源
type: docs
weight: 310
url: /zh/cpp/release-unmanaged-resources-of-the-workbook/
description: 学习如何使用Aspose.Cells和C++释放工作簿的未管理资源。
---

{{% alert color="primary" %}}

Aspose.Cells 提供 [**Workbook.Dispose()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/dispose/) 方法用于释放 [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) 对象的非托管资源。Dispose 模式仅用于访问非托管资源的对象，例如文件和管道句柄、注册表句柄、等待句柄或指向非托管内存块的指针。这是因为垃圾收集器在回收未使用的托管对象方面非常高效，但无法回收非托管对象。

{{% /alert %}}

[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)对象现在实现了*IDisposable*接口，它只有一个方法[**Dispose()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/dispose/)。你可以直接调用[**Workbook.Dispose()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/dispose/)方法，或者使用*Using*语句自动调用此方法。

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
