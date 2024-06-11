---
title: 给窗体控件分配宏
type: docs
weight: 60
url: /zh/net/assign-macro-to-form-control/
---

{{% alert color="primary" %}}

Aspose.Cells允许您向按钮等窗体控件分配宏代码。请使用[**Shape.MarcoName**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/macroname)属性将新的宏代码分配给工作簿内的窗体控件。

{{% /alert %}}

以下示例代码创建一个新的工作簿，为一个表单按钮分配宏代码，并将输出保存为XLSM格式。一旦你在Microsoft Excel中打开输出的XLSM文件，你将看到以下宏代码。

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **在C#中为表单控件分配宏**

以下是生成输出XLSM文件的示例代码

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-AssignMacroToFormControl-1.cs" >}}
