---
title : "How to set AutoRecover property of Workbook" 
description : "" 
weight : 20443 
toc : false
type: docs
url: /net/developerguide/technicalarticles/general/mngworkbooksandworksheets/how+to+set+autorecover+property+of+workbook/
---

# Aspose.Cells for .NET : How to set AutoRecover property of Workbook


You can use Aspose.Cells to set AutoRecover property of workbook. The default value of this property is **true**. When you set it **false** on a workbook, Microsoft Excel disables Autorecover (Autosave) on that Excel file.

Aspose.Cells provides [Workbook.Settings.AutoRecover](https://apireference.aspose.com/net/cells/aspose.cells/workbooksettings/properties/autorecover) property to enable or disable this option.

The following code explains how to use [Workbook.Settings.AutoRecover](https://apireference.aspose.com/net/cells/aspose.cells/workbooksettings/properties/autorecover) property of the workbook. The code first reads the default value of this property which is **true**, then it sets it as **false** and saves the workbook. Then it reads the workbook again and reads the value of this property which is **false** at this time.

## Output

Here is the console output of the above sample code.

{{< code lang="cs" >}}
AutoRecover: True
AutoRecover: False
{{< /code >}}

