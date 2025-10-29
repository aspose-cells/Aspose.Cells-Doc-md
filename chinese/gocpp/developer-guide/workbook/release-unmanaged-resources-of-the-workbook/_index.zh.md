---
title: 使用Golang via C++释放工作簿的非托管资源
linktitle: 释放工作簿的非托管资源
type: docs
weight: 310
url: /zh/go-cpp/release-unmanaged-resources-of-the-workbook/
description: 学习如何使用 Aspose.Cells 通过 C++ 在 Golang 中释放工作簿的未管理资源。
---

{{% alert color="primary" %}}

Aspose.Cells 提供 [**Workbook.Dispose()**](https://reference.aspose.com/cells/go-cpp/workbook/dispose/) 方法用于释放 [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) 对象的非托管资源。Dispose 模式仅用于访问非托管资源的对象，例如文件和管道句柄、注册表句柄、等待句柄或指向非托管内存块的指针。这是因为垃圾收集器在回收未使用的托管对象方面非常高效，但无法回收非托管对象。

{{% /alert %}}

[**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/)对象现在实现了*IDisposable*接口，它只有一个方法[**Dispose()**](https://reference.aspose.com/cells/go-cpp/workbook/dispose/)。你可以直接调用[**Workbook.Dispose()**](https://reference.aspose.com/cells/go-cpp/workbook/dispose/)方法，或者使用*Using*语句自动调用此方法。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReleaseUnmanagedResourcesOfTheWorkbook.go" >}}
