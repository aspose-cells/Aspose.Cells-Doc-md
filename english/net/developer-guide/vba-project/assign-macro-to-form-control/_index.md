---
title: Assign Macro to Form Control
type: docs
weight: 60
url: /net/assign-macro-to-form-control/
---

{{% alert color="primary" %}}

Aspose.Cells allows you to assign a Macro Code to a Form Control like a Button. Please use the [**Shape.MarcoName**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/macroname) property to assign a new Macro Code to a Form Control inside the workbook.

{{% /alert %}}

The following sample code creates a new workbook, assign a Macro Code to a Form Button and saves the output in the XLSM format. Once, you will open the output XLSM file in Microsoft Excel you will see the following macro code.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **Assign Macro to Form Control in C#**

Here is the sample code to generate the output XLSM file with Macro Code.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-AssignMacroToFormControl-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}