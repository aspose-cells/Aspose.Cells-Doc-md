---
title: 将宏代码分配给窗体控件
type: docs
weight: 400
url: /zh/java/assign-macro-code-to-form-control/
---

{{% alert color="primary" %}} 

Aspose.Cells允许您将宏代码分配给按钮等形式控件。请使用[ShapeCollection.addShape()](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape\(int,%20int,%20int,%20int,%20int,%20int,%20int\))方法将新的宏代码分配给工作簿内的形式控件。

{{% /alert %}} 
## **使用Aspose.Cells--将宏代码分配给表单控件**
以下示例代码创建一个新的工作簿，为一个表单按钮指定宏代码，并将输出保存为XLSM格式。一旦您在Microsoft Excel中打开输出的XLSM文件，您将看到以下宏代码。

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

以下是一个生成XLSM输出文件与宏代码的示例代码。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AssignMacroToFormControl-AssignMacroToFormControl.java" >}}
