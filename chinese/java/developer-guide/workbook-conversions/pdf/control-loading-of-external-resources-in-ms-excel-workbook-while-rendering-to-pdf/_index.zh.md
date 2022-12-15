---
title: 在呈现为 PDF 时控制 MS Excel 工作簿中外部资源的加载
type: docs
weight: 40
url: /zh/java/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/
---
## **可能的使用场景**

您的 Excel 文件可能包含外部资源，例如链接的图像或对象。当您将 Excel 文件转换为 PDF 时，Aspose.Cells 会检索这些外部资源并将它们呈现为 PDF。但有时，您不想加载这些外部资源，更甚于您想要操作它们。您可以使用[**PdfSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#StreamProvider)它实现了[**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)界面。

## **在呈现为 PDF 时控制 MS Excel 工作簿中外部资源的加载**

下面的示例代码解释了如何使用[**PdfSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#StreamProvider)控制外部资源的加载和操作。请检查[示例 Excel 文件](50528353.xlsx)在代码中使用[输出PDF](50528354.pdf)由代码生成。这[截屏](50528357.png)展示了如何[旧的外部图像](50528356.png)示例 Excel 文件中的替换为[新图片](50528355.png)在输出 PDF 中。

![待办事项：图像_替代_文本](control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-ControlLoadingOfExternalResourcesInExcelToPDF.java" >}}
