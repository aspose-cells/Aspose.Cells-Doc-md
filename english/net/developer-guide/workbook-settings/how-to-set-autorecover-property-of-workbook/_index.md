---
title: How to set AutoRecover property of Workbook
type: docs
weight: 220
url: /net/how-to-set-autorecover-property-of-workbook/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

You can use Aspose.Cells to set the AutoRecover property of a workbook. The default value of this property is **true**. When you set it to **false** on a workbook, Microsoft Excel disables AutoRecover (Autosave) for that Excel file.

Aspose.Cells provides the [**Workbook.Settings.AutoRecover**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/autorecover) property to enable or disable this option.

{{% /alert %}}

The following code demonstrates how to use the [**Workbook.Settings.AutoRecover**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/autorecover) property of the workbook. The code first reads the default value of this property (which is **true**), then sets it to **false** and saves the workbook. It then reloads the workbook and reads the property value, which is now **false**.

## C# code to set the AutoRecover property of Workbook

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-SetAutoRecovery-SetAutoRecovery.cs" >}}

## **Output**

Here is the console output of the above sample code.

{{< highlight java >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
