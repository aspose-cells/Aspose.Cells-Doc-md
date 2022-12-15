---
title: 使用 WorkbookSetting.StreamProvider 控制外部资源
type: docs
weight: 10
url: /zh/net/control-external-resources-using-workbooksetting-streamprovider/
---
## **可能的使用场景**

有时，您的 Excel 文件包含外部资源，例如链接图像等。Aspose.Cells 允许您使用以下命令控制这些外部资源[**工作簿.设置.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider)这需要实施[**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)界面。每当您尝试呈现包含外部资源（例如链接图像）的工作表时，[**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)接口将被调用，这将使您能够对外部资源采取适当的操作。

## **使用 WorkbookSetting.StreamProvider 控制外部资源**

下面的示例代码解释了[**工作簿.设置.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider) .它加载了[示例 Excel 文件](61767863.xlsx)包含链接图像。该代码将链接的图像替换为[Aspose 徽标](61767862.png)并使用将整个工作表渲染成单个图像[**图纸渲染**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)班级。以下屏幕截图显示了示例 Excel 文件及其[渲染输出图像](61767865.png)供参考。如您所见，损坏的链接图像已替换为 Aspose 徽标。

![待办事项：图像_替代_文本](control-external-resources-using-workbooksetting-streamprovider_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-ControlExternalResourcesUsingWorkbookSetting_StreamProvider-1.cs" >}}
