---
title: 如何设置工作簿的AutoRecover属性
type: docs
weight: 220
url: /zh/net/how-to-set-autorecover-property-of-workbook/
---

{{% alert color="primary" %}}

您可以使用Aspose.Cells来设置工作簿的AutoRecover属性。 该属性的默认值为**true**。 当您在工作簿上将其设置为**false**时，Microsoft Excel会禁用该Excel文件上的AutoRecover（自动保存）。

Aspose.Cells提供了[**Workbook.Settings.AutoRecover**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/autorecover)属性来启用或禁用此选项。

{{% /alert %}}

以下代码解释了如何使用工作簿的[**Workbook.Settings.AutoRecover**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/autorecover)属性。 代码首先读取该属性的默认值，该值为**true**，然后将其设置为**false**并保存工作簿。 然后再次读取工作簿并读取该属性的值，此时该值为**false**。

## C#代码设置工作簿的AutoRecover属性

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-SetAutoRecovery-SetAutoRecovery.cs" >}}

## **输出**

这是上面示例代码的控制台输出。

{{< highlight java >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
