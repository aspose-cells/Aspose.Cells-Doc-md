---
title: 渲染到 PDF 时控制 MS Excel 工作簿中外部资源的加载
type: docs
weight: 40
url: /zh/net/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/
---
## **可能的使用场景**

您的 Excel 文件可能包含外部资源，例如链接的图像或对象。当您将 Excel 文件转换为 PDF 时，Aspose.Cells 会检索这些外部资源并将它们呈现给 PDF。但有时，您不想加载这些外部资源，不仅如此，您还想操作它们。您可以使用[**工作簿设置.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider)它实现了[**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)界面。

## **渲染到 PDF 时控制 MS Excel 工作簿中外部资源的加载**

下面的示例代码解释了如何使用[**工作簿设置.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider)控制外部资源的加载和操作。请检查[示例 Excel 文件](50528322.xlsx)在代码中使用[输出 PDF](50528325.pdf)由代码生成。这[截屏](50528326.png)展示了如何[旧的外部图像](50528324.png)示例 Excel 文件中的替换为[新图片](50528323.png)在输出 PDF 中。

![待办事项：图片_替代_文本](control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-ControlLoadingOfExternalResourcesInExcelToPDF-1.cs" >}}
