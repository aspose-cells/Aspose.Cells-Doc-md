---
title: 控制在将MS Excel工作簿渲染为PDF时加载外部资源
type: docs
weight: 40
url: /zh/java/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/
---

## **可能的使用场景**

您的Excel文件可能包含外部资源，例如链接的图像或对象。当您将Excel文件转换为PDF时，Aspose.Cells会检索这些外部资源并将它们渲染为PDF。但有时，您可能不希望加载这些外部资源，甚至希望对它们进行操作。您可以使用[**PdfSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#StreamProvider)来实现[**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)接口。

## **控制在将MS Excel工作簿渲染为PDF时加载外部资源**

以下样本代码解释了如何使用[**PdfSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#StreamProvider)来控制加载外部资源并对其进行操作。请查看代码中使用的[sample Excel file](50528353.xlsx)以及代码生成的[output PDF](50528354.pdf)。[屏幕截图](50528357.png)显示了如何将样本Excel文件中的[旧外部图像](50528356.png)替换为[新图像](50528355.png)。

![todo:image_alt_text](control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-ControlLoadingOfExternalResourcesInExcelToPDF.java" >}}
