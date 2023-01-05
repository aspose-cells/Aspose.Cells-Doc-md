---
title: 在 Excel 中禁用兼容性检查器
type: docs
weight: 170
url: /zh/net/disable-compatibility-checker-in-excel/
keywords: c# excel disable compatibility checke
---
## 在 C# 中禁用 Excel 工作表中的兼容性检查器

{{% alert color="primary" %}}

Microsoft 以早期文件格式保存文件时，Excel 的兼容性检查器标记可能会导致功能问题或保真度丢失。兼容性检查器是 Microsoft Office Excel 2007 和 Microsoft Excel 2010 的一项功能。

当您从 Excel 2007 或 Excel 2010 将工作簿保存为早期版本（从 Excel 97 到 Excel 2003）时，兼容性检查器会扫描工作簿以查看它是否包含早期版本不支持的功能。为了帮助您决定如何处理兼容性问题，兼容性检查器会显示带有选项的对话框。它还可用于创建有关工作簿中任何问题的报告，或禁用该功能。

有时，您需要禁用特定电子表格的兼容性检查器。使用 Aspose.Cells' API，您可以以编程方式执行此操作，这样用户在手动将文件重新保存到 Microsoft Excel 中时，不会因弹出的兼容性检查器对话框而感到沮丧或困惑。

{{% /alert %}}

## **使用 Microsoft Excel**

要禁用 Microsoft Excel 中的兼容性检查器（例如 Microsoft Excel 2007/2010）：

-  (Excel 2007) 在 Office 按钮上，单击**准备**， 然后**运行兼容性检查器**，然后清除**保存此工作簿时检查兼容性**选项。
-  (Excel 2010) 在“文件”选项卡上，单击**信息**， 然后**检查问题** ， 点击**检查兼容性**，最后，清除**保存此工作簿时检查兼容性**选项。

## **使用 Aspose.Cells API**

设置[**工作簿.设置.检查兼容性**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcompatibility)财产给**错误的**禁用 Microsoft Excel 的兼容性检查器。

### **代码示例**

下面的代码示例显示了如何使用 Aspose.Cells for .NET 禁用兼容性检查器。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DisableCompatibilityChecker-1.cs" >}}
