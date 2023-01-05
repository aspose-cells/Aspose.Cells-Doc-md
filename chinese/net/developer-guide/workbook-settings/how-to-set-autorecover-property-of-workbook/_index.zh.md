---
title: 如何设置工作簿的自动恢复属性
type: docs
weight: 220
url: /zh/net/how-to-set-autorecover-property-of-workbook/
---
{{% alert color="primary" %}}

您可以使用 Aspose.Cells 设置工作簿的自动恢复属性。该属性的默认值为**真的**.当你设置它**错误的**在工作簿上，Microsoft Excel 在该 Excel 文件上禁用自动恢复（自动保存）。

Aspose.Cells提供[**工作簿.设置.自动恢复**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/autorecover)属性来启用或禁用此选项。

{{% /alert %}}

下面的代码解释了如何使用[**工作簿.设置.自动恢复**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/autorecover)工作簿的属性。代码首先读取此属性的默认值，即**真的**，然后将其设置为**错误的**并保存工作簿。然后它再次读取工作簿并读取此属性的值**错误的**此时。

## C# 设置工作簿自动恢复属性的代码

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-SetAutoRecovery-SetAutoRecovery.cs" >}}

## **输出**

这是上述示例代码的控制台输出。

{{< highlight "java" >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}
