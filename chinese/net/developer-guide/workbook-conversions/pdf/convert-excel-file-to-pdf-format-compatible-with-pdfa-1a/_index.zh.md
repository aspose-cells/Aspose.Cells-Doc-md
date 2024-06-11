---
title: 将Excel文件转换为与PDFA-1a兼容的PDF格式
type: docs
weight: 130
url: /zh/net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
---

## **可能的使用场景**

PDF/A是PDF的一种独特变体，旨在长期保存文件。PDF/A是PDF的ISO标准化版本，它是PDF的归档格式，将文档中使用的所有字体嵌入到PDF文件中。PDF/A与PDF不同之处在于禁止某些功能，例如字体链接（而不是字体嵌入）和加密。Aspose.Cells可以使您将Excel文件保存为PDF/A兼容的PDF文件（支持PdfA1a和PdfA1b）。本主题介绍了将Excel工作簿保存为PDF/A兼容（PdfA1a）的PDF文件的方法。

## **将Excel文件转换为与PDFA-1a兼容的PDF格式**

开发人员可以使用 **[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** 类来设置转换的不同属性。设置**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**类的不同属性可以让您控制输出PDF的打印、字体、安全和压缩设置。最重要的属性是**[PdfSaveOptions.Compliance](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance)**，它使您能够将Excel文件保存为PDF/A兼容的PDF文件。

以下示例代码解释了如何将Excel文件转换为与PDFA-1a兼容的PDF格式。请参阅其[输出PDF](outputCompliancePdfA1a.pdf)以及参考的屏幕截图。

## **屏幕截图**

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToPDFA_1a.cs" >}}
