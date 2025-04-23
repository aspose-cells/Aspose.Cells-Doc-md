---
title: 如何设置工作簿的AutoRecover属性
type: docs
weight: 220
url: /zh/python-net/how-to-set-autorecover-property-of-workbook/
---

{{% alert color="primary" %}}

您可以使用 Aspose.Cells for Python via .NET 设置工作簿的自动恢复属性。该属性的默认值是 **true**。当将其设置为 **false** 时，Microsoft Excel 将在该 Excel 文件上禁用自动恢复（自动保存）。

Aspose.Cells for Python via .NET 提供 [**Workbook.settings.auto_recover**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/auto_recover) 属性以启用或禁用此选项。

{{% /alert %}}

以下代码说明了如何使用工作簿的 [**Workbook.settings.auto_recover**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/auto_recover) 属性。代码首先读取此属性的默认值（为 **true**），然后将其设为 **false** 并保存工作簿。接着再次读取工作簿，查看此属性的值，此时为 **false**。

## C#代码设置工作簿的AutoRecover属性

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "WorkbookSettings-SetAutoRecovery.py" >}}

## **输出**

这是上面示例代码的控制台输出。

{{< highlight java >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}

