---
title: 在Excel中禁用兼容性检查程序
type: docs
weight: 270
url: /zh/java/disable-compatibility-checker-in-excel/
---

{{% alert color="primary" %}}

Microsoft Excel的兼容性检查程序在以较早的文件格式保存文件可能会导致功能问题或保真度丢失时会发出警告。兼容性检查程序是Microsoft Office Excel 2007、2010和2013的一个功能。

当您从Excel 2007或Excel 2010将工作簿保存在较早的版本中（Excel 97至Excel 2003），兼容性检查程序将扫描工作簿，以查看它是否包含较早版本不支持的功能。为了帮助您决定如何处理兼容性问题，兼容性检查程序显示带有选项的对话框。它还可用于创建有关工作簿中任何问题的报告，或者禁用该功能。

有时，您需要动态地禁用特定电子表格的兼容性检查程序。使用Aspose.Cells的API，您可以这样做，从而使用户在手动在Microsoft Excel中重新保存文件时，不会被兼容性检查程序的对话框所烦恼或困惑。

{{% /alert %}}

## **使用Microsoft Excel**

要在Microsoft Excel中禁用兼容性检查程序（例如Microsoft Excel 2007/2010）：

- （Excel 2007）在办公按钮上，单击**准备**，然后单击**运行兼容性检查**，然后清除**保存此工作簿时检查兼容性**选项。
- （Excel 2010和2013）在“文件”选项卡上，单击**信息**，然后单击**检查问题**，点击**检查兼容性**，最后清除**保存此工作簿时检查兼容性**选项。

## **使用Aspose.Cells API**

将[**WorkbookSettings.CheckComptiliblity**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckComptiliblity)属性设置为**False**以禁用Microsoft Excel的兼容性检查程序。

假设我们有一个模板XLS文件。当用户在MS Excel 2007/2010/2013中保存或重新保存它时，将显示兼容性检查程序的对话框，如下面的屏幕截图所示。

![todo:image_alt_text](disable-compatibility-checker-in-excel_1.png)

下面的代码展示如何使用Aspose.Cells for Java禁用兼容性检查器。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DisableCompatibilityChecker-DisableCompatibilityChecker.java" >}}
