---
title: 将 Excel 文件转换为符合 PDFA 1a 规范的 PDF 格式，使用 Golang 通过 C++
linktitle: 将Excel文件转换为与PDFA 1a兼容的PDF格式
type: docs
weight: 130
url: /zh/go-cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
description: 学习如何使用 Golang 通过 C++ 将 Excel 文件转换为符合 PDF/A 1a 标准的 PDF 格式，使用 Aspose.Cells。
---

## **可能的使用场景**

 PDF/A是一种特殊的PDF版本，旨在文件的长期保存。PDF/A是ISO标准化的PDF格式，它在PDF中嵌入了所有使用的字体以实现存档，且禁止某些功能，如字体链接（而非嵌入）和加密。Aspose.Cells支持将Excel文件保存为符合PDF/A标准的PDF文件（支持PDF/A-1a、PDF/A-1b、PDF/A-2a、PDF/A-2b、PDF/A-2u、PDF/A-3a、PDF/A-2ab 和 PDF/A-3u）。本主题介绍如何将Excel工作簿保存为符合PDF/A（PDF/A-1a）标准的PDF文件。

## **将Excel文件转换为与PDF/A-1a兼容的PDF格式**

 开发者可以使用[**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/)类设置转换的不同属性。设置[**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/)类的不同属性，可以控制输出PDF的打印、字体、安全性和压缩设置。最重要的属性是[**PdfSaveOptions.GetCompliance()**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/getcompliance/)，它允许你将Excel文件保存为符合PDF/A标准的PDF文件。

以下示例代码解释了如何将Excel文件转换为与PDF/A-1a兼容的PDF格式。请参阅其[输出PDF](outputCompliancePdfA1a.pdf)以及屏幕截图作为参考。

## **屏幕截图**

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertExcelFileToPdfFormatCompatibleWithPdfa1a.go" >}}
