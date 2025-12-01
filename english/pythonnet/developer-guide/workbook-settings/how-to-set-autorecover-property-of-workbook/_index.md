---
title: How to set AutoRecover property of Workbook
type: docs
weight: 220
url: /python-net/how-to-set-autorecover-property-of-workbook/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

You can use Aspose.Cells for Python via .NET to set AutoRecover property of workbook. The default value of this property is **true**. When you set it **false** on a workbook, Microsoft Excel disables AutoRecover (Autosave) on that Excel file.

Aspose.Cells for Python via .NET provides [**Workbook.settings.auto_recover**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/auto_recover) property to enable or disable this option.

{{% /alert %}}

The following code explains how to use  [**Workbook.settings.auto_recover**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/auto_recover) property of the workbook. The code first reads the default value of this property which is **true**, then it sets it as **false** and saves the workbook. Then it reads the workbook again and reads the value of this property which is **false** at this time.

## C# code to set the AutoRecover property of Workbook

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "WorkbookSettings-SetAutoRecovery.py" >}}

## **Output**

Here is the console output of the above sample code.

{{< highlight java >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}

{{< app/cells/assistant language="python-net" >}}
