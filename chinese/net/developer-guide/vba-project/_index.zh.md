---
title: 管理启用 Excel 宏的工作簿的 VBA 代码。
linktitle: 宏观项目
type: docs
weight: 200
url: /zh/net/manage-vba-project/
description: 使用 Aspose.Cells 库添加 VBA 模块和修改 VBA 或宏。
---
## **在 C# 添加一个 VBA 模块**
{{% alert color="primary" %}}

Aspose.Cells 允许您使用 Aspose.Cells 添加新的 VBA 模块和宏代码。请使用[**工作簿.VbaProject.Modules.Add()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/add/index)在工作簿中添加新的 VBA 模块的方法

{{% /alert %}}

以下示例代码创建一个新工作簿并添加一个新的 VBA 模块和宏代码，并以 XLSM 格式保存输出。一次，您将在 Microsoft Excel 中打开输出 XLSM 文件并单击**开发人员 > Visual Basic**菜单命令，您将看到一个名为“TestModule”的模块，在其中，您将看到以下宏代码。

{{< highlight "java" >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

下面是使用 VBA 模块和宏代码生成输出 XLSM 文件的示例代码。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-AddVBAModuleOrCode-AddVBAModuleOrCode.cs" >}}

## **C#中修改VBA或宏**

{{% alert color="primary" %}} 

您可以使用 Aspose.Cells 修改 VBA 或宏代码。Aspose.Cells 添加了以下命名空间和类，以读取和修改 Excel 文件中的 VBA 项目。

- Aspose.Cells.Vba
- Vba项目
- Vba模块集合
- Vba模块

本文将向您展示如何使用 Aspose.Cells 更改源 Excel 文件中的 VBA 或宏代码。

{{% /alert %}} 

以下示例代码加载源 Excel 文件，其中包含以下 VBA 或宏代码

{{< highlight "java" >}}

 Sub Button1_Click()

    MsgBox "This is test message."

End Sub

{{< /highlight >}}

Aspose.Cells示例代码执行后，VBA或Macro代码会修改成这样

{{< highlight "java" >}}

 Sub Button1_Click()

    MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

您可以下载[源Excel文件](5112508.xlsm)和[输出Excel文件](5112511.xlsm)从给定的链接。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-ModifyingVBAOrMacroCode-ModifyingVBAOrMacroCode.cs" >}}

## **推进主题**
- [在工作簿中添加对 VBA 项目的库引用](/cells/zh/net/add-a-library-reference-to-vba-project-in-workbook/)
- [将宏分配给表单控件](/cells/zh/net/assign-macro-to-form-control/)
- [检查VBA代码的数字签名是否有效](/cells/zh/net/check-if-digital-signature-of-vba-code-is-valid/)
- [检查 VBA 代码是否已签名](/cells/zh/net/check-if-vba-code-is-signed/)
- [检查工作簿中的 VBA 项目是否已签名](/cells/zh/net/check-if-vba-project-in-a-workbook-is-signed/)
- [检查 VBA 项目是否受保护并锁定以供查看](/cells/zh/net/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [将 VBA 宏 UserForm DesignerStorage 从模板复制到目标工作簿](/cells/zh/net/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [使用证书对 VBA 代码项目进行数字签名](/cells/zh/net/digitally-sign-a-vba-code-project-with-certificate/)
- [将 VBA 证书导出到文件或流](/cells/zh/net/export-vba-certificate-to-file-or-stream/)
- [加载工作簿时筛选 VBA 项目](/cells/zh/net/filter-vba-project-while-loading-a-workbook/)
- [查看 VBA 项目是否受保护](/cells/zh/net/find-out-if-vba-project-is-protected/)
- [密码保护Excel工作簿的VBA项目](/cells/zh/net/password-protect-the-vba-project-of-excel-workbook/)

