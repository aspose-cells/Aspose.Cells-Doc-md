---
title: 用Golang通过C++将宏分配给表单控件
linktitle: 给窗体控件分配宏
type: docs
weight: 60
url: /zh/go-cpp/assign-macro-to-form-control/
description: 学习如何使用Aspose.Cells for C++将宏代码分配给按钮等表单控件。
---

{{% alert color="primary" %}}

Aspose.Cells允许您向按钮等窗体控件分配宏代码。请使用[**Shape.GetMacroName()**](https://reference.aspose.com/cells/go-cpp/shape/getmacroname/)属性将新的宏代码分配给工作簿内的窗体控件。

{{% /alert %}}

以下示例创建一个新工作簿，将宏代码分配给表单按钮，并以XLSM格式保存。当在Microsoft Excel中打开该文件时，将看到如下宏代码。

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **在C++中将宏分配给表单控件**

以下是生成输出XLSM文件的示例代码

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AssignMacroToFormControl.go" >}}
