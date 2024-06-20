---
title: 将Excel文件转换为与PDFA 1a兼容的PDF格式
type: docs
weight: 130
url: /zh/python-net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
description: 学习如何使用Aspose.Cells for Python via .NET API将Excel文件转换为与PDFA 1a兼容的PDF格式。
keywords: Python将Excel文件转换为与PDFA 1a兼容的PDF格式，PDFA 1a，PDFA 1b，PDF14，PDF15，PDF16，PDF17
---

## **可能的使用场景**

PDF/A是PDF的一个专门的版本，用于长期保存文档。 PDF/A是ISO标准化的便携式文档格式（PDF）的一个归档格式，它在PDF文件中嵌入了文档中使用的所有字体。 PDF/A通过禁止某些功能（例如与字体嵌入相对应的字体链接和加密）与PDF有所不同。 Aspose.Cells for Python via .NET使您能够将Excel文件保存为符合PDF/A标准的PDF文件（支持PdfA1a和PdfA1b）。本主题介绍了如何将Excel工作簿保存为符合PDF/A（PdfA1a）的PDF文件。

## **将Excel文件转换为与PDFA-1a兼容的PDF格式**

开发人员可以使用 [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/) 类为转换设置不同的属性。设置 [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/) 类的不同属性将使您能够控制输出 PDF 的打印、字体、安全和压缩设置。最重要的属性是 [**PdfSaveOptions.compliance**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/compliance/)，它使您能够将 Excel 文件保存为 PDF/A 兼容的 PDF 文件。

以下示例代码解释了如何将Excel文件转换为与PDFA-1a兼容的PDF格式。请参阅其[输出PDF](outputCompliancePdfA1a.pdf)以及参考的屏幕截图。

## **屏幕截图**

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ConvertExcelFileToPDFA_1a.py" >}}
