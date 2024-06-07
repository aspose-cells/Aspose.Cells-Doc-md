---
title: 将Excel文件转换为与PDFA-1a兼容的PDF格式
type: docs
weight: 130
url: /zh/net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
---

## **可能的使用场景**

PDF/A是为文件长期保存而设计的PDF的独特品种。PDF/A是便携式文档格式（PDF）的一个符合ISO标准的版本，它是PDF的归档格式，它在PDF文件内嵌入了所有使用的字体。PDF/A通过禁止功能（如字体链接）和加密来限制PDF与PDF的不同。Aspose.Cells使您能够将Excel文件保存为PDF/A兼容的PDF文件（支持PdfA1a和PdfA1b）。本主题描述了如何将Excel工作簿保存为PDF/A兼容（PdfA1a）PDF文件。

## **将Excel文件转换为与PDFA-1a兼容的PDF格式**

开发人员可以使用**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**类为转换设置不同属性。设置**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**类的不同属性使您能够控制输出PDF的打印、字体、安全性和压缩设置。最重要的属性是**[PdfSaveOptions.Compliance](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance)**，它使您能够将Excel文件保存为PDF/A兼容的PDF文件。

以下示例代码解释了如何将Excel文件转换为与PDFA-1a兼容的PDF格式。请查看其[输出PDF](outputCompliancePdfA1a.pdf)，以及屏幕截图供参考。

## **截图**

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToPDFA_1a.cs" >}}
