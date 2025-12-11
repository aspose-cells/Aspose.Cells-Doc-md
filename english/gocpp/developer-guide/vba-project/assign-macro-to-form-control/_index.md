---
title: Assign Macro to Form Control with Golang via C++
linktitle: Assign Macro to Form Control
type: docs
weight: 60
url: /go-cpp/assign-macro-to-form-control/
description: Learn how to assign a macro code to a form control like a button using Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells allows you to assign a macro code to a form control like a button. Please use the [**Shape.GetMacroName()**](https://reference.aspose.com/cells/go-cpp/shape/getmacroname/) property to assign a new macro code to a form control inside the workbook.

{{% /alert %}}

The following sample code creates a new workbook, assigns a macro code to a form button, and saves the output in the XLSM format. Once you open the output XLSM file in Microsoft Excel, you will see the following macro code.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **Assign Macro to Form Control in C++**

Here is the sample code to generate the output XLSM file with a macro code.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AssignMacroToFormControl.go" >}}