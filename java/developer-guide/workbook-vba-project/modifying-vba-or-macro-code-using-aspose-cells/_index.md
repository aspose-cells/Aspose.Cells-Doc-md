---
title: Modifying VBA or Macro Code using Aspose.Cells
type: docs
weight: 90
url: /java/modifying-vba-or-macro-code-using-aspose-cells/
---

{{% alert color="primary" %}} 

You can modify VBA or Macro Code using Aspose.Cells. Aspose.Cells has added the following classes to read and modify the VBA project in the Excel file.

- VbaProject
- VbaModuleCollection
- VbaModule

This article will show you how to change the VBA or Macro Code inside the source Excel file using Aspose.Cells.

{{% /alert %}} 
#### **Example**
The following sample code loads the source Excel file which has a following VBA or Macro code inside it

{{< highlight java >}}

 Sub Button1_Click()

MsgBox "This is test message."

End Sub

{{< /highlight >}}

After the execution of Aspose.Cells sample code, the VBA or Macro code will be modified like this

{{< highlight java >}}

 Sub Button1_Click()

MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

You can download the [source Excel file](attachments/5276586/5472596.xlsm) and the [output Excel file](attachments/5276586/5472597.xlsm) from the given links.







{{< gist "aspose-cells" "87c05ec07dd1a65ac6fcdf2fa896b01e" "Examples-src-main-java-com-aspose-cells-examples-articles-ModifyVBAorMacroCode-ModifyVBAorMacroCode.java" >}}






