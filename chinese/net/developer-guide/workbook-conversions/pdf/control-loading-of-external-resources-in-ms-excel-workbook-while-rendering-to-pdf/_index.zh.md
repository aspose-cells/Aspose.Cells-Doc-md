---
title: 在将MS Excel工作簿渲染为PDF时控制加载外部资源
type: docs
weight: 40
url: /zh/net/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/
---

## **可能的使用场景**

您的Excel文件可能包含外部资源，例如链接的图像或对象。当您将Excel文件转换为PDF时，Aspose.Cells会检索这些外部资源并将它们呈现为PDF。但有时，您不希望加载这些外部资源，并且更重要的是，您希望操纵它们。您可以使用[**WorkbookSettings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider)实现[**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)接口来实现这一点。

## **在将MS Excel工作簿渲染为PDF时控制加载外部资源**

以下示例代码解释了如何利用[**WorkbookSettings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider)来控制外部资源的加载并操纵它们。请查看代码中使用的[示例Excel文件](50528322.xlsx)以及代码生成的[输出PDF](50528325.pdf)。[屏幕截图](50528326.png)显示了如何在示例Excel文件中的[旧外部图像](50528324.png)被替换为[新图像](50528323.png)的输出PDF。

![todo:image_alt_text](control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-ControlLoadingOfExternalResourcesInExcelToPDF-1.cs" >}}
