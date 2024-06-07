---
title: 将Excel文件转换为与PDFA-1a兼容的PDF格式
type: docs
weight: 130
url: /zh/python-net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
description: 了解如何使用Aspose.Cells for Python通过.NET API将Excel文件转换为与PDFA-1a兼容的PDF格式
keywords: Python将Excel文件转换为与PDFA-1a兼容的PDF格式，PDFA-1a，PDFA-1b，PDF14，PDF15，PDF16，PDF17
---

## **可能的使用场景**

PDFA是PDF的一种专用版本，旨在长期保存文档。PDFA是PDF的ISO标准化版本，是PDF的存档格式，将文档中使用的所有字体嵌入PDF文件中。 PDFA通过禁止某些功能（例如与字体嵌入相对应的字体链接和加密）与PDF不同。Aspose.Cells for Python通过.NET使您能够将Excel文件保存为符合PDFA标准的PDFA兼容PDF文件（支持PdfA1a和PdfA1b）。本主题描述了如何将Excel工作簿保存为符合PDFA标准（PdfA1a）的PDF文件。

## **将Excel文件转换为与PDFA-1a兼容的PDF格式**

开发人员可以使用**[PdfSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/)**类为转换设置不同属性。设置**[PdfSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/)**类的不同属性使您可以控制输出PDF的打印、字体、安全性和压缩设置。最重要的属性是**[PdfSaveOptions.compliance](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/compliance/)**，它使您能够将Excel文件保存为符合PDFA标准的PDF文件。

以下示例代码解释了如何将Excel文件转换为与PDFA-1a兼容的PDF格式。请查看其[输出PDF](outputCompliancePdfA1a.pdf)，以及屏幕截图供参考。

## **截图**

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ConvertExcelFileToPDFA_1a.py" >}}
