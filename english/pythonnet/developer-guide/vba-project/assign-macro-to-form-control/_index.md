---
title: Assign Macro to Form Control
type: docs
weight: 60
url: /python-net/assign-macro-to-form-control/
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET allows you to assign a Macro Code to a Form Control like a Button. Please use the [**Shape.macro_name**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/macro_name) property to assign a new Macro Code to a Form Control inside the workbook.

{{% /alert %}}

The following sample code creates a new workbook, assign a Macro Code to a Form Button and saves the output in the XLSM format. Once, you will open the output XLSM file in Microsoft Excel you will see the following macro code.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **Assign Macro to Form Control in Python**

Here is the sample code to generate the output XLSM file with Macro Code.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-AssignMacroToFormControl-1.py" >}}
{{< app/cells/assistant language="python-net" >}}