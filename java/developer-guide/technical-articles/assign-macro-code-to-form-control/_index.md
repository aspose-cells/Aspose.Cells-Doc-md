---
title: Assign Macro Code to Form Control
type: docs
weight: 400
url: /java/assign-macro-code-to-form-control/
---

{{% alert color="primary" %}} 

Aspose.Cells allows you to assign a Macro Code to a Form Control like a Button. Please use the [ShapeCollection.addShape()](https://apireference.aspose.com/java/cells/com.aspose.cells/shapecollection#addShape\(int,%20int,%20int,%20int,%20int,%20int,%20int\)) method to assign a new Macro Code to a Form Control inside the workbook.

{{% /alert %}} 
#### **Assigning Macro Code to Form Control using Aspose.Cells**
The following sample code creates a new workbook, assign a Macro Code to a Form Buttom and saves the output in the XLSM format. Once, you will open the output XLSM file in Microsoft Excel you will see the following macro code.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

Here is a sample code to generate the output XLSM file with Macro Code.

{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Examples-src-main-java-com-aspose-cells-examples-articles-AssignMacroToFormControl-AssignMacroToFormControl.java" >}}
