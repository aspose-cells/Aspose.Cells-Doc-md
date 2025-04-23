---
title: 将Excel文件转换为与PDFA 1a兼容的PDF格式
type: docs
weight: 80
url: /zh/java/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
---

## **可能的使用场景**

PDF/A是PDF的一种独特类型，旨在长期保存文档。PDF/A是便携式文档格式（PDF）的ISO标准版本，它是PDF的档案格式，将文档中使用的所有字体嵌入PDF文件中。与PDF不同，PDF/A禁止了一些功能，如字体链接（与字体嵌入相对）和加密。Aspose.Cells使您能够将Excel文件保存为符合PDF/A标准的PDF文件（支持PDF/A-1a、PDF/A-1b、PDF/A-2a、PDF/A-2b、PDF/A-2u、PDF/A-3a、PDF/A-2ab和PDF/A-3u）。本主题描述了如何将Excel工作簿保存为符合PDF/A标准（PDF/A-1a）的PDF文件。

## **将Excel文件转换为与PDF/A-1a兼容的PDF格式**

开发人员可以使用 [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) 类为转换设置不同属性。设置 [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) 类的不同属性可控制输出 PDF 的打印、字体、安全和压缩设置。最重要的属性是 [PdfSaveOptions.Compliance**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#Compliance)，它使您能够将 Excel 文件保存为 PDF/A 兼容的 PDF 文件。

以下示例代码解释了如何将Excel文件转换为与PDF/A-1a兼容的PDF格式。请参阅其[输出PDF](outputCompliancePdfA1a.pdf)以及参考的屏幕截图。

## **屏幕截图**

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToPDFA_1a.java" >}}
{{< app/cells/assistant language="java" >}}
