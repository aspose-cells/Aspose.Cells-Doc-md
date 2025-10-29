---
title: 在使用 C++ 通过 Golang 将 Excel 转换为 PDF 时渲染实线网格线
linktitle: 渲染实线网格线
type: docs
weight: 390
url: /zh/go-cpp/render-solid-gridline-while-converting-excel-to-pdf/
description: 学习如何在使用 C++ 通过 Golang 将 Excel 转换为 PDF 时渲染实线网格线，使用 Aspose.Cells。
---

为了兼容旧版本，Aspose.Cells在将Excel转换为PDF时默认渲染网格线为点线。然而，现代Excel现在将网格线渲染为实线。

通过 [PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/) 选项，Aspose.Cells 还可以将网格线渲染为实线。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RenderSolidGridlineWhileConvertingExcelToPdf.go" >}}
![solid-gridline.png](solid-gridline.png)
