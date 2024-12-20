---
title: How to set AutoRecover property of Workbook
type: docs
weight: 160
url: /java/how-to-set-autorecover-property-of-workbook/
---

{{% alert color="primary" %}}

You can use Aspose.Cells to set AutoRecover property of workbook. The default value of this property is **true**. When you set it **false** on a workbook, Microsoft Excel disables Autorecover (Autosave) on that Excel file.

Aspose.Cells provides [**Workbook.getSettings().setAutoRecover()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#AutoRecover) property to enable or disable this option.

{{% /alert %}}

## Java code to set AutoRecover property of Workbook

The following code explains how to use [**Workbook.getSettings().setAutoRecover()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#AutoRecover) property of the workbook. The code first reads the default value of this property which is **true**, then it sets it as **false** and saves the workbook. Then it reads the workbook again and reads the value of this property which is false at this time.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetAutoRecoverProperty-SetAutoRecoverProperty.java" >}}

## Output generated by sample code

Here is the console output of the above sample code.

{{< highlight java >}}

AutoRecover: true

AutoRecover: false

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}