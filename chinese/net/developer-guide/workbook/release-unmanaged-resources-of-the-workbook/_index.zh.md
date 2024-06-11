---
title: 释放工作簿的非托管资源
type: docs
weight: 310
url: /zh/net/release-unmanaged-resources-of-the-workbook/
---

{{% alert color="primary" %}}

Aspose.Cells 提供 [**Workbook.Dispose()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose) 方法用于释放 [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 对象的非托管资源。Dispose 模式仅用于访问非托管资源的对象，例如文件和管道句柄、注册表句柄、等待句柄或指向非托管内存块的指针。这是因为垃圾收集器在回收未使用的托管对象方面非常高效，但无法回收非托管对象。

{{% /alert %}}

[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)对象现在实现了*System.IDisposable*接口，该接口有一个方法[**Dispose()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose)。您可以直接调用[**Workbook.Dispose()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose)方法，也可以使用*Using*语句自动调用该方法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ReleaseUnmanagedResources-ReleaseUnmanagedResourcesForWorkbooks.cs" >}}
