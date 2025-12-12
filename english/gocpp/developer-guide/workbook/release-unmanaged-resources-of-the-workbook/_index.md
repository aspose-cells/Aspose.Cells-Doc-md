---  
title: Release Unmanaged Resources of the Workbook with Golang via C++  
linktitle: Release Unmanaged Resources of the Workbook  
type: docs  
weight: 310  
url: /go-cpp/release-unmanaged-resources-of-the-workbook/  
description: Learn how to release unmanaged resources of the Workbook using Aspose.Cells with Golang via C++.  
---  

{{% alert color="primary" %}}

Aspose.Cells provides the **Workbook.Dispose()** method to release the unmanaged resources of the [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) object. The Dispose pattern is used only for objects that access unmanaged resources, such as file and pipe handles, registry handles, wait handles, or pointers to blocks of unmanaged memory. This is because the garbage collector is very efficient at reclaiming unused managed objects, but it is unable to reclaim unmanaged objects.

{{% /alert %}}

The [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) object now implements the *IDisposable* interface, which has a single method **Dispose()**. You can either call the **Workbook.Dispose()** method directly, or use the *using* statement to have this method called automatically.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReleaseUnmanagedResourcesOfTheWorkbook.go" >}}