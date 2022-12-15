---
title: 将 Excel 文件转换为与 PDFA-1a 兼容的 PDF 格式
type: docs
weight: 130
url: /zh/net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
---
## **可能的使用场景**

PDF/A 是 PDF 的一种独特风格，专为长期保存文档而设计。 PDF/A 是可移植文档格式 (PDF) 的 ISO 标准化版本，它是一种 PDF 存档格式，将文档中使用的所有字体嵌入到 PDF 文件中。 PDF/A 与 PDF 的不同之处在于禁止使用字体链接（与字体嵌入相对）和加密等功能。 Aspose.Cells 使您能够将 Excel 文件保存为 PDF/A 兼容的 PDF 文件（支持 PdfA1a 和 PdfA1b）。本主题介绍如何将 Excel 工作簿保存为 PDF/A 兼容 (PdfA1a) PDF 文件。

## **将 Excel 文件转换为与 PDFA-1a 兼容的 PDF 格式**

开发人员可以使用**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**类来为转换设置不同的属性。设置不同的属性**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**类使您可以控制输出 PDF 的打印、字体、安全和压缩设置。最重要的属性是**[PdfSaveOptions.Compliance](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance)**使您能够将 Excel 文件保存为 PDF/A 兼容的 PDF 文件。

以下示例代码解释了如何将 Excel 文件转换为与 PDFA-1a 兼容的 PDF 格式。请看其[输出PDF](outputCompliancePdfA1a.pdf)以及屏幕截图以供参考。

## **截屏**

![待办事项：图像_替代_文本](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToPDFA_1a.cs" >}}
