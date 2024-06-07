---
title: 在 Excel 中禁用兼容性检查器
type: docs
weight: 270
url: /zh/java/disable-compatibility-checker-in-excel/
---

{{% alert color="primary" %}}

Microsoft Excel在将文件保存为较早文件格式时，会标记兼容性检查器，警告您保存文件可能会导致功能问题或保真度的丢失。兼容性检查器是Microsoft Office Excel 2007、2010和2013的功能。

当您从Excel 2007或Excel 2010中保存一个工作簿到Excel 97至Excel 2003之前的版本时，兼容性检查器会扫描工作簿，看看它是否包含早期版本不支持的功能。为了帮助您做出关于如何处理兼容性问题的决定，兼容性检查器会显示带有选项的对话框。它还可以用于创建有关工作簿中任何问题的报告，或者禁用该功能。

有时，您需要动态地禁用特定电子表格的兼容性检查器。使用Aspose.Cells的API，您可以这样做，以便当用户手动在Microsoft Excel中重新保存文件时，他们不会因为兼容性检查器对话框的弹出而感到沮丧或困惑。

{{% /alert %}}

## **使用Microsoft Excel**

要在Microsoft Excel中禁用兼容性检查器（例如Microsoft Excel 2007/2010）：

-（Excel 2007）单击“Office”按钮，选择**准备**，然后选择**运行兼容性检查器**，最后取消选中“保存此工作簿时检查兼容性”的选项。
- (Excel 2010 & 2013) 在**文件**选项卡上，单击**信息**，然后单击**检查问题**，单击**检查兼容性**，最后清除**保存此工作簿时检查兼容性**选项。

## **使用Aspose.Cells的API**

将[**WorkbookSettings.CheckComptiliblity**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckComptiliblity)属性设置为**False**即可禁用Microsoft Excel的兼容性检查器。

假设我们有一个模板XLS文件。当用户在MS Excel 2007/2010/2013中保存或重新保存文件时，会显示兼容性检查器对话框，如下方截图所示。

![todo:image_alt_text](disable-compatibility-checker-in-excel_1.png)

以下代码显示了如何使用Aspose.Cells for Java禁用兼容性检查器。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DisableCompatibilityChecker-DisableCompatibilityChecker.java" >}}
