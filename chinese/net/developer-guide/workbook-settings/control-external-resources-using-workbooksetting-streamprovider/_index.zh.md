---
title: 使用WorkbookSetting.StreamProvider控制外部资源
type: docs
weight: 10
url: /zh/net/control-external-resources-using-workbooksetting-streamprovider/
---

## **可能的使用场景**

有时，您的Excel文件包含外部资源，例如链接的图片等。Aspose.Cells允许您使用[**Workbook.Settings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider)控制这些外部资源，该方法采用[**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)接口的实现。每当您尝试渲染包含外部资源（例如链接的图片）的工作表时，将调用[**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)接口的方法，从而使您能够针对外部资源采取适当的操作。

## **使用WorkbookSetting.StreamProvider控制外部资源**

以下示例代码说明了[**Workbook.Settings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider)的用法。它加载包含链接图像的[示例Excel文件](61767863.xlsx)。该代码将链接图像替换为[Aspose标志](61767862.png)，并使用[**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)类将整个工作表渲染为单个图像。以下屏幕截图显示了示例Excel文件及其[渲染输出图像](61767865.png)以供参考。正如您所看到的那样，破损的链接图像已被替换为Aspose标志。

![todo:image_alt_text](control-external-resources-using-workbooksetting-streamprovider_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-ControlExternalResourcesUsingWorkbookSetting_StreamProvider-1.cs" >}}
