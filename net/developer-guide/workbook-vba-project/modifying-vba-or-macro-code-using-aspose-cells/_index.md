---
title: Modifying VBA or Macro Code using Aspose.Cells
type: docs
weight: 40
url: /net/modifying-vba-or-macro-code-using-aspose-cells/
---

{{% alert color="primary" %}} 

You can modify VBA or Macro Code using Aspose.Cells. Aspose.Cells has added the following namespace and classes to read and modify the VBA project in the Excel file.

- Aspose.Cells.Vba
- VbaProject
- VbaModuleCollection
- VbaModule

This article will show you how to change the VBA or Macro Code inside the source Excel file using Aspose.Cells.

{{% /alert %}} 

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

You can download the [source Excel file](5112508.xlsm) and the [output Excel file](5112511.xlsm) from the given links.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-ModifyingVBAOrMacroCode-ModifyingVBAOrMacroCode.cs" >}}
