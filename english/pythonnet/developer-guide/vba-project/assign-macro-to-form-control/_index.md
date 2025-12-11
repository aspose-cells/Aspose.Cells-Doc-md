---
title: Assign Macro to Form Control
type: docs
weight: 60
url: /python-net/assign-macro-to-form-control/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET allows you to assign a macro to a form control such as a button. Please use the [**Shape.macro_name**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/macro_name) property to assign a new macro to a form control inside the workbook.

{{% /alert %}}

The following sample code creates a new workbook, assigns a macro to a form button, and saves the output in the XLSM format. Once you open the output XLSM file in Microsoft Excel, you will see the following macro code.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **Assign Macro to Form Control in Python**

Here is the sample code to generate the output XLSM file with macro code.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-AssignMacroToFormControl-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
