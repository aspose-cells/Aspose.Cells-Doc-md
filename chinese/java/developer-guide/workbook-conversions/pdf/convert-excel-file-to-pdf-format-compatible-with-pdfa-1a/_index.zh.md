---
title: 将Excel文件转换为与PDFA-1a兼容的PDF格式
type: docs
weight: 80
url: /zh/java/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
---

## **可能的使用场景**

PDF/A是PDF的一个专门的版本，用于长期保存文档。PDF/A是PDF的一个经过ISO标准化的版本，是在PDF文件内嵌所有使用的字体的档案格式。PDF/A通过禁止某些特性（例如字体链接）和加密来与PDF区别开来。Aspose.Cells使您能够将Excel文件保存为符合PDF/A标准（PdfA1a和PdfA1b都受支持）的PDF文件。本主题描述了如何将Excel工作簿保存为符合PDF/A（PdfA1a）的PDF文件。

## **将Excel文件转换为与PDFA-1a兼容的PDF格式**

开发人员可以使用**[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)**类来为转换设置不同的属性。设置**[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)**类的不同属性可以让您控制输出PDF的打印、字体、安全和压缩设置。最重要的属性是**[PdfSaveOptions.Compliance](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#Compliance)**，它使您能够将Excel文件保存为符合PDF/A标准的PDF文件。

以下示例代码解释了如何将Excel文件转换为与PDFA-1a兼容的PDF格式。请参阅其[output PDF](outputCompliancePdfA1a.pdf)以及屏幕截图。

## **截图**

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToPDFA_1a.java" >}}
