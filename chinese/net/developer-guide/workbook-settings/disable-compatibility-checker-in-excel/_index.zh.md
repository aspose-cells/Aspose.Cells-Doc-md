---
title: 在 Excel 中禁用兼容性检查器
type: docs
weight: 170
url: /zh/net/disable-compatibility-checker-in-excel/
description: 本文介绍如何通过 Aspose.Cells for .NET API 禁用兼容性检查器。
keywords: C# 禁用兼容性检查器，Excel 中禁用兼容性检查器，禁用工作簿中的兼容性检查器。 
---

## 在C#中禁用Excel工作表中的兼容性检查器 

{{% alert color="primary" %}}

Microsoft Excel的兼容性检查器会在保存文件为较早的文件格式可能导致功能问题或丢失精度时发出警告。兼容性检查器是Microsoft Office Excel 2007和Microsoft Excel 2010的一个功能。

当您从Excel 2007或Excel 2010中保存一个工作簿到Excel 97至Excel 2003之前的版本时，兼容性检查器会扫描工作簿，看看它是否包含早期版本不支持的功能。为了帮助您做出关于如何处理兼容性问题的决定，兼容性检查器会显示带有选项的对话框。它还可以用于创建有关工作簿中任何问题的报告，或者禁用该功能。

有时，您需要为特定电子表格禁用兼容性检查器。使用Aspose.Cells的API，您可以通过编程方式做到这一点，以便当用户手动在Microsoft Excel中重新保存文件时，不会因为兼容性检查器对话框的弹出而感到沮丧或困惑。

{{% /alert %}}

## **如何使用Microsoft Excel禁用兼容性检查器**

要在Microsoft Excel中禁用兼容性检查器（例如Microsoft Excel 2007/2010）：

-（Excel 2007）单击“Office”按钮，选择**准备**，然后选择**运行兼容性检查器**，最后取消选中“保存此工作簿时检查兼容性”的选项。
-（Excel 2010）点击“文件”选项卡，选择**信息**，然后选择**检查问题**，点击**检查兼容性**，最后取消选中“保存此工作簿时检查兼容性”的选项。

## **如何使用Aspose.Cells API禁用兼容性检查器**

将[**Workbook.Settings.CheckComptiliblity**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcompatibility)属性设置为**False**即可禁用Microsoft Excel的兼容性检查器。

### **代码示例**

以下代码示例演示了如何使用Aspose.Cells for .NET禁用兼容性检查器。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DisableCompatibilityChecker-1.cs" >}}
