---
title: 使用WorkbookSetting.StreamProvider控制外部资源
type: docs
weight: 10
url: /zh/java/control-external-resources-using-workbooksetting-streamprovider/
---

## **可能的使用场景**
有时，您的Excel文件包含外部资源，例如链接的图像等。Aspose.Cells允许您使用Workbook.Settings.StreamProvider控制这些外部资源，该方法接受IStreamProvider接口的实现。每当您尝试呈现包含外部资源的工作表时，将调用IStreamProvider接口的方法，这将使您能够针对外部资源采取适当的操作。
## **使用WorkbookSetting.StreamProvider控制外部资源**
以下示例代码解释了如何使用Workbook.Settings.StreamProvider。它加载包含链接图像的样本Excel文件。代码将链接图像替换为Aspose Logo，并使用SheetRender类将整个工作表呈现为单个图像。以下屏幕截图显示了示例Excel文件及其渲染输出图像供参考。正如您所见，损坏的链接图像已替换为Aspose Logo。

![todo:image_alt_text](control-external-resources-using-workbooksetting-streamprovider_1.png)
## **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookSettings-ControlExternalResourcesUsingWorkbookSetting_StreamProvider-1.java" >}}
