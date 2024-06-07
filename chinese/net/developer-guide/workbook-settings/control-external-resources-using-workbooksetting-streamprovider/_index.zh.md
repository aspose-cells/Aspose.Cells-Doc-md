---
title: 使用WorkbookSetting.StreamProvider控制外部资源
type: docs
weight: 10
url: /zh/net/control-external-resources-using-workbooksetting-streamprovider/
---

## **可能的使用场景**

有时候，您的 Excel 文件包含外部资源，如链接的图像等。Aspose.Cells 允许您使用[**Workbook.Settings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider)来控制这些外部资源，该方法需要实现[**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)接口。每当您尝试呈现包含外部资源的工作表时，例如链接的图像时，将调用[**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)接口的方法，这将使您能够为外部资源采取适当的操作。

## **使用WorkbookSetting.StreamProvider控制外部资源**

以下示例代码解释了[**Workbook.Settings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider)的用法。它加载了包含链接图像的[示例 Excel 文件](61767863.xlsx)。代码将链接图像替换为[Aspose Logo](61767862.png)，并使用[**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)类将整个工作表呈现为单个图像。以下屏幕截图显示了示例 Excel 文件及其[渲染的输出图像](61767865.png)供参考。正如您所见，已将断开的链接图像替换为Aspose Logo。

![todo:image_alt_text](control-external-resources-using-workbooksetting-streamprovider_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-ControlExternalResourcesUsingWorkbookSetting_StreamProvider-1.cs" >}}
