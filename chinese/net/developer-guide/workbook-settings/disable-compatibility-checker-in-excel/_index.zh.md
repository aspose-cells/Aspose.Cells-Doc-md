---
title: 在Excel中禁用兼容性检查程序
type: docs
weight: 170
url: /zh/net/disable-compatibility-checker-in-excel/
description: 本文展示如何通过Aspose.Cells for .NET API禁用兼容性检查器。
keywords: C#禁用兼容性检查器，Excel中的C#禁用兼容性检查器，工作簿中禁用兼容性检查器。 
---

## 在C#中禁用Excel工作表中的兼容性检查器 

{{% alert color="primary" %}}

Microsoft Excel的兼容性检查器在将文件保存为较早文件格式时可能会出现功能问题或保真度丢失。 兼容性检查器是Microsoft Office Excel 2007和Microsoft Excel 2010的功能。

当您从Excel 2007或Excel 2010将工作簿保存在较早的版本中（Excel 97至Excel 2003），兼容性检查程序将扫描工作簿，以查看它是否包含较早版本不支持的功能。为了帮助您决定如何处理兼容性问题，兼容性检查程序显示带有选项的对话框。它还可用于创建有关工作簿中任何问题的报告，或者禁用该功能。

有时，您需要为特定电子表格禁用兼容性检查器。通过Aspose.Cells的API，您可以以编程方式执行此操作，使用户在手动在Microsoft Excel中重新保存文件时不会因兼容性检查器对话框的弹出而感到沮丧或困惑。

{{% /alert %}}

## **如何使用Microsoft Excel禁用兼容性检查器**

要在Microsoft Excel中禁用兼容性检查程序（例如Microsoft Excel 2007/2010）：

- （Excel 2007）在办公按钮上，单击**准备**，然后单击**运行兼容性检查**，然后清除**保存此工作簿时检查兼容性**选项。
- （Excel 2010）单击“文件”选项卡，然后单击**信息**，再单击“检查问题”，再单击“检查兼容性”，最后清除“保存此工作簿时检查兼容性”选项。

## **如何使用Aspose.Cells API禁用兼容性检查器**

将[**Workbook.Settings.CheckComptiliblity**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcompatibility)属性设置为**False**以禁用Microsoft Excel的兼容性检查程序。

### **代码示例**

以下代码示例展示如何使用Aspose.Cells for .NET禁用兼容性检查器。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DisableCompatibilityChecker-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
