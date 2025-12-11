---
title: Assign Macro to Form Control
type: docs
weight: 60
url: /net/assign-macro-to-form-control/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells allows you to assign a macro code to a Form Control like a button. Please use the [**Shape.MacroName**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/macroname) property to assign a new macro code to a Form Control inside the workbook.

{{% /alert %}}

The following sample code creates a new workbook, assigns a macro code to a Form button, and saves the output in the XLSM format. Once you open the output XLSM file in Microsoft Excel you will see the following macro code.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **Assign Macro to Form Control in C#**

Here is the sample code to generate the output XLSM file with macro code.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-AssignMacroToFormControl-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
