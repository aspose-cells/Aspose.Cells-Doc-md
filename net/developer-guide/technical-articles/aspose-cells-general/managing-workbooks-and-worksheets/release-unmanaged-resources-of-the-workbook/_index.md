---
title: Release Unmanaged Resources of the Workbook
type: docs
weight: 310
url: /net/release-unmanaged-resources-of-the-workbook/
---

{{% alert color="primary" %}} 

Aspose.Cells provides [Workbook.Dispose()](https://apireference.aspose.com/net/cells/aspose.cells/workbook/methods/dispose) method to release the unmanaged resources of the [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) object. The dispose pattern is used only for objects that access unmanaged resources, such as file and pipe handles, registry handles, wait handles or pointers to blocks of unmanaged memory. This is because the garbage collector is very efficient at reclaiming unused managed objects, but it is unable to reclaim unmanaged objects.

{{% /alert %}} 

[Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) object now implements the *System.IDisposable* interface which has a single method [Dispose()](https://apireference.aspose.com/net/cells/aspose.cells/workbook/methods/dispose). You can either directly call the [Workbook.Dispose()](https://apireference.aspose.com/net/cells/aspose.cells/workbook/methods/dispose) method or you can use the *Using* statement to call this method automatically.



{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ReleaseUnmanagedResources-ReleaseUnmanagedResourcesForWorkbooks.cs" >}}
