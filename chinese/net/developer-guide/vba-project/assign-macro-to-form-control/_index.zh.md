---
title: 为窗体控件分配宏
type: docs
weight: 60
url: /zh/net/assign-macro-to-form-control/
---

{{% alert color="primary" %}}

Aspose.Cells允许您为按钮等窗体控件分配宏代码。请使用[**Shape.MarcoName**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/macroname) 属性将新的宏代码分配给工作簿内的窗体控件。

{{% /alert %}}

以下示例代码创建一个新的工作簿，为窗体按钮分配一个宏代码，并以XLSM格式保存输出。一旦您在Microsoft Excel中打开输出的XLSM文件，您将看到以下宏代码。

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **在C#中为窗体控件分配宏**

以下是生成带有宏代码的输出XLSM文件的示例代码。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-AssignMacroToFormControl-1.cs" >}}
