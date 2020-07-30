---
title : "Release Unmanaged Resources of the Workbook" 
description : "" 
weight : 20452 
toc : false
type: docs
url: /net/developerguide/technicalarticles/general/mngworkbooksandworksheets/release+unmanaged+resources+of+the+workbook/
---

# Aspose.Cells for .NET : Release Unmanaged Resources of the Workbook


Aspose.Cells provides [Workbook.Dispose()](https://apireference.aspose.com/net/cells/aspose.cells/workbook/methods/dispose) method to release the unmanaged resources of the [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) object. The dispose pattern is used only for objects that access unmanaged resources, such as file and pipe handles, registry handles, wait handles or pointers to blocks of unmanaged memory. This is because the garbage collector is very efficient at reclaiming unused managed objects, but it is unable to reclaim unmanaged objects.

[Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook)object now implements the *System.IDisposable* interface which has a single method [Dispose()](https://apireference.aspose.com/net/cells/aspose.cells/workbook/methods/dispose). You can either directly call the [Workbook.Dispose()](https://apireference.aspose.com/net/cells/aspose.cells/workbook/methods/dispose) method or you can use the *Using *statement to call this method automatically.

