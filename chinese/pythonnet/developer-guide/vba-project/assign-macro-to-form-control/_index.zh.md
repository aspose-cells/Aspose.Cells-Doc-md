---
title: 给窗体控件分配宏
type: docs
weight: 60
url: /zh/python-net/assign-macro-to-form-control/
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET允许您将宏代码指定给表单控件（如按钮）。请使用[**Shape.macro_name**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/macro_name)属性为工作簿中的表单控件分配新的宏代码。

{{% /alert %}}

以下示例代码创建一个新的工作簿，为一个表单按钮分配宏代码，并将输出保存为XLSM格式。一旦你在Microsoft Excel中打开输出的XLSM文件，你将看到以下宏代码。

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **在Python中为表单控件赋予宏**

以下是生成输出XLSM文件的示例代码

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-AssignMacroToFormControl-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
