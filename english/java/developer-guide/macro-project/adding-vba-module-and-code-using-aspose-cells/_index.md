---
title: Adding VBA Module and Code using Aspose.Cells
type: docs
weight: 20
url: /java/adding-vba-module-and-code-using-aspose-cells/
---

{{% alert color="primary" %}}

Aspose.Cells allows you to add a new VBA Module and Macro Code using Aspose.Cells. Please use the [**Workbook.getVbaProject().getModules().add(**)](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#add(com.aspose.cells.Worksheet)) method to add the new VBA Module inside the workbook

{{% /alert %}}

## **Adding VBA Module and Code using Aspose.Cells**

The following sample code creates a new workbook and adds a new VBA Module and Macro Code and saves the output in the XLSM format. Once, you will open the output XLSM file in Microsoft Excel and click the **Developer > Visual Basic** menu commands, you will see a module named "TestModule" and inside it, you will see the following macro code.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## Sample Code

Here is a sample code to generate the output XLSM file with VBA Module and Macro Code.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddVBAModuleAndCode-AddVBAModuleAndCode.java" >}}
{{< app/cells/assistant language="java" >}}