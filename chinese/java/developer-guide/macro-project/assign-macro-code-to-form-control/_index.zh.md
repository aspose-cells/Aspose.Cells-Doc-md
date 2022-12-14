---
title: 将宏代码分配给表单控件
type: docs
weight: 400
url: /zh/java/assign-macro-code-to-form-control/
---
{{% alert color="primary" %}} 

Aspose.Cells 允许您将宏代码分配给像按钮一样的表单控件。请使用[ShapeCollection.addShape()](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape\(int,%20int,%20int,%20int,%20int,%20int,%20int\)) 方法将新的宏代码分配给工作簿中的表单控件。

{{% /alert %}} 
## **使用 Aspose.Cells 将宏代码分配给表单控件**
以下示例代码创建一个新工作簿，将宏代码分配给表单按钮并以 XLSM 格式保存输出。一次，您将在 Microsoft Excel 中打开输出 XLSM 文件，您将看到以下宏代码。

{{< highlight "java" >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

以下是使用宏代码生成输出 XLSM 文件的示例代码。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AssignMacroToFormControl-AssignMacroToFormControl.java" >}}
