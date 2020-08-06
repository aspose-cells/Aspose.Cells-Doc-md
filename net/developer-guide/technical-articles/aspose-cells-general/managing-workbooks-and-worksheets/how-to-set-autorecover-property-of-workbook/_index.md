---
title: How to set AutoRecover property of Workbook
type: docs
weight: 220
url: /net/how-to-set-autorecover-property-of-workbook/
---

{{% alert color="primary" %}} 

You can use Aspose.Cells to set AutoRecover property of workbook. The default value of this property is **true**. When you set it **false** on a workbook, Microsoft Excel disables Autorecover (Autosave) on that Excel file.

Aspose.Cells provides [Workbook.Settings.AutoRecover](https://apireference.aspose.com/net/cells/aspose.cells/workbooksettings/properties/autorecover) property to enable or disable this option.

{{% /alert %}} 

The following code explains how to use [Workbook.Settings.AutoRecover](https://apireference.aspose.com/net/cells/aspose.cells/workbooksettings/properties/autorecover) property of the workbook. The code first reads the default value of this property which is **true**, then it sets it as **false** and saves the workbook. Then it reads the workbook again and reads the value of this property which is **false** at this time.



{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-SetAutoRecovery-SetAutoRecovery.cs" >}}
## **Output**
Here is the console output of the above sample code.

{{< highlight java >}}

 AutoRecover: True

AutoRecover: False

{{< /highlight >}}
