---
title: 将Excel文件转换为与PDFA-1a兼容的PDF格式
type: docs
weight: 80
url: /zh/java/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
---

## **可能的使用场景**

PDF/A是PDF的一个专用变体，用于长期保存文件。PDF/A是PDF的ISO标准化版本，是在文档中嵌入使用的所有字体的存档格式的PDF。PDF/A通过禁止一些特性（例如字体链接而非字体嵌入）和加密，与PDF不同。Aspose.Cells使您能够将Excel文件保存为PDF/A兼容的PDF文件（PdfA1a和PdfA1b都受支持）。

## **将 Excel 文件转换为兼容 PDFA-1a 格式的 PDF**

开发人员可以使用**[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)**类为转换设置不同属性。设置**[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)**类的不同属性能够控制输出PDF的打印、字体、安全和压缩设置。最重要的属性是**[PdfSaveOptions.Compliance](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#Compliance)**，它使您能将Excel文件保存为PDF/A兼容的PDF文件。

以下样本代码解释了将Excel文件转换为与PDFA-1a兼容的PDF格式。请参阅其[output PDF](outputCompliancePdfA1a.pdf)以及参考用的屏幕截图。

## **屏幕截图**

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToPDFA_1a.java" >}}
