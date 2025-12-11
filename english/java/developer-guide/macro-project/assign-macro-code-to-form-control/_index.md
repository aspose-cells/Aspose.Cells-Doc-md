---
title: Assign Macro Code to Form Control
type: docs
weight: 400
url: /java/assign-macro-code-to-form-control/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

Aspose.Cells allows you to assign a Macro Code to a Form Control like a Button. Please use the [ShapeCollection.addShape()](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape-int-int-int-int-int-int-int-) method to assign a new Macro Code to a Form Control inside the workbook.

{{% /alert %}} 
## **Assigning Macro Code to Form Control using Aspose.Cells**
The following sample code creates a new workbook, assigns a Macro Code to a Form Button, and saves the output in the XLSM format. Once you open the output XLSM file in Microsoft Excel, you will see the following macro code.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

Here is a sample code to generate the output XLSM file with Macro Code.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AssignMacroToFormControl-AssignMacroToFormControl.java" >}}
{{< app/cells/assistant language="java" >}}
