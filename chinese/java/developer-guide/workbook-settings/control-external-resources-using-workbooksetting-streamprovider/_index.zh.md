---
title: 使用WorkbookSetting.StreamProvider控制外部资源
type: docs
weight: 10
url: /zh/java/control-external-resources-using-workbooksetting-streamprovider/
---

## **可能的使用场景**
有时，您的Excel文件中包含外部资源，例如链接的图像等。Aspose.Cells允许您通过[Workbook.Settings.StreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#StreamProvider)控制这些外部资源，该方法使用[IStreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)接口的实现。每当您尝试渲染包含外部资源（例如链接的图像）的工作表时，将调用[IStreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)接口的方法，从而使您能够针对您的外部资源采取适当的操作。
## **使用WorkbookSetting.StreamProvider控制外部资源**
以下示例代码解释了如何使用[Workbook.Settings.StreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#StreamProvider)。它加载包含链接图像的示例Excel文件61767877.xlsx。代码将链接图像替换为Aspose标志，并使用[SheetRender](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender)类将整个工作表呈现为单个图像。以下屏幕截图显示了示例Excel文件及其[呈现的输出图像61767874.png](61767874.png)供参考。如您所见，破损的链接图像已被替换为Aspose标志。

![todo:image_alt_text](control-external-resources-using-workbooksetting-streamprovider_1.png)
## **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookSettings-ControlExternalResourcesUsingWorkbookSetting_StreamProvider-1.java" >}}
