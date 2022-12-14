---
title: 将宏分配给表单控件
type: docs
weight: 60
url: /zh/net/assign-macro-to-form-control/
---
{{% alert color="primary" %}}

Aspose.Cells 允许您将宏代码分配给像按钮一样的表单控件。请使用[**形状.MarcoName**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/macroname)属性将新的宏代码分配给工作簿中的表单控件。

{{% /alert %}}

以下示例代码创建一个新工作簿，将宏代码分配给表单按钮，并以 XLSM 格式保存输出。一次，您将在 Microsoft Excel 中打开输出 XLSM 文件，您将看到以下宏代码。

{{< highlight "java" >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **在 C# 中将宏分配给表单控件**

下面是使用宏代码生成输出 XLSM 文件的示例代码。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-AssignMacroToFormControl-1.cs" >}}
