---
title: Release Unmanaged Resources of the Workbook with Golang via C++
linktitle: Release Unmanaged Resources of the Workbook
type: docs
weight: 310
url: /go-cpp/release-unmanaged-resources-of-the-workbook/
description: Learn how to release unmanaged resources of the Workbook using Aspose.Cells with Golang via C++.
---

{{% alert color="primary" %}}

Aspose.Cells provides [**Workbook.Dispose()**](https://reference.aspose.com/cells/go-cpp/workbook/dispose/) method to release the unmanaged resources of the [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) object. The dispose pattern is used only for objects that access unmanaged resources, such as file and pipe handles, registry handles, wait handles or pointers to blocks of unmanaged memory. This is because the garbage collector is very efficient at reclaiming unused managed objects, but it is unable to reclaim unmanaged objects.

{{% /alert %}}

[**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) object now implements the *IDisposable* interface which has a single method [**Dispose()**](https://reference.aspose.com/cells/go-cpp/workbook/dispose/). You can either directly call the [**Workbook.Dispose()**](https://reference.aspose.com/cells/go-cpp/workbook/dispose/) method or you can use the *Using* statement to call this method automatically.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReleaseUnmanagedResourcesOfTheWorkbook.go" >}}