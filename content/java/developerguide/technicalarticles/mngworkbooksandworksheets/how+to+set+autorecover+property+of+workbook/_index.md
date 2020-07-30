---
title : "How to set AutoRecover property of Workbook" 
description : "" 
weight : 16430 
toc : false
type: docs
url: /java/developerguide/technicalarticles/mngworkbooksandworksheets/how+to+set+autorecover+property+of+workbook/
---

# Aspose.Cells for Java : How to set AutoRecover property of Workbook


You can use Aspose.Cells to set AutoRecover property of workbook. The default value of this property is **true**. When you set it **false** on a workbook, Microsoft Excel disables Autorecover (Autosave) on that Excel file.

Aspose.Cells provides [Workbook.getSettings().setAutoRecover()](https://apireference.aspose.com/java/cells/com.aspose.cells/workbooksettings#AutoRecover) property to enable or disable this option.

#### Example

The following code explains how to use [Workbook.getSettings().setAutoRecover()](https://apireference.aspose.com/java/cells/com.aspose.cells/workbooksettings#AutoRecover) property of the workbook. The code first reads the default value of this property which is **true**, then it sets it as **false** and saves the workbook. Then it reads the workbook again and reads the value of this property which is false at this time.


#### Output

Here is the console output of the above sample code.

{{< code lang="cs" >}}
AutoRecover: true
AutoRecover: false
{{< /code >}}

