---
title: 在 Excel 中禁用兼容性检查器
type: docs
weight: 270
url: /zh/java/disable-compatibility-checker-in-excel/
---
{{% alert color="primary" %}}

Microsoft 以较早的文件格式保存文件时，Excel 的兼容性检查器会标记保存文件可能会导致功能问题或保真度丢失。兼容性检查器是 Microsoft Office Excel 2007、2010 和 2013 的一项功能。

当您从 Excel 2007 或 Excel 2010 将工作簿保存为早期版本（从 Excel 97 到 Excel 2003）时，兼容性检查器会扫描工作簿以查看它是否包含早期版本不支持的功能。为了帮助您决定如何处理兼容性问题，兼容性检查器会显示带有选项的对话框。它还可用于创建有关工作簿中任何问题的报告，或禁用该功能。

有时，您需要禁用特定电子表格的兼容性检查器。使用 Aspose.Cells' API，您可以动态执行此操作，这样用户在手动将文件重新保存到 Microsoft Excel 中时，不会因弹出的兼容性检查器对话框而感到沮丧或困惑。

{{% /alert %}}

## **使用 Microsoft Excel**

要禁用 Microsoft Excel 中的兼容性检查器（例如 Microsoft Excel 2007/2010）：

-  (Excel 2007) 在 Office 按钮上，单击**准备**， 然后**运行兼容性检查器**，然后清除**保存此工作簿时检查兼容性**选项。
- （Excel 2010 和 2013）在文件选项卡上，单击**信息**， 然后**检查问题** ， 点击**检查兼容性**，最后，清除**保存此工作簿时检查兼容性**选项。

## **使用 Aspose.Cells API**

设置[**工作簿设置.检查兼容性**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckComptiliblity)财产给**错误的**禁用 Microsoft Excel 的兼容性检查器。

假设我们有一个模板 XLS 文件。当用户在 MS Excel 2007/2010/2013 中保存或重新保存它时，将显示兼容性检查器对话框，如下面的屏幕截图所示。

![待办事项：图像_替代_文本](disable-compatibility-checker-in-excel_1.png)

以下代码显示了如何使用 Aspose.Cells for Java 禁用兼容性检查器。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DisableCompatibilityChecker-DisableCompatibilityChecker.java" >}}
