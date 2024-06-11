---
title: 管理Excel宏启用的工作簿的VBA代码。
linktitle: 宏项目
type: docs
weight: 200
url: /zh/net/manage-vba-project/
description: 使用Aspose.Cells库添加VBA模块并修改VBA或宏。
---

## **在C#中添加VBA模块**
{{% alert color="primary" %}}

Aspose.Cells允许您使用Aspose.Cells添加新的VBA模块和宏代码。请使用[**Workbook.VbaProject.Modules.Add()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/add/index)方法在工作簿内添加新的VBA模块。

{{% /alert %}}

以下示例代码创建一个新工作簿，并添加一个新的VBA模块和宏代码，将输出保存为XLSM格式。一旦您打开输出的XLSM文件并单击“开发人员> Visual Basic”菜单命令，您将看到一个名为“TestModule”的模块，并在其中看到以下宏代码。

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

以下是生成带有VBA模块和宏代码的输出XLSM文件的示例代码。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-AddVBAModuleOrCode-AddVBAModuleOrCode.cs" >}}

## **在C#中修改VBA或宏代码**

{{% alert color="primary" %}} 

您可以使用Aspose.Cells修改VBA或宏代码。Aspose.Cells已添加以下名称空间和类来读取和修改Excel文件中的VBA项目。

- Aspose.Cells.Vba
- VbaProject
- VbaModuleCollection
- VbaModule

本文将向您展示如何使用Aspose.Cells更改源Excel文件中的VBA或宏代码。

{{% /alert %}} 

以下示例代码加载带有以下VBA或宏代码的源Excel文件

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is test message."

End Sub

{{< /highlight >}}

执行Aspose.Cells示例代码后，VBA或宏代码将被修改如下

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

您可以从以下链接下载[源Excel文件](5112508.xlsm)和[输出Excel文件](5112511.xlsm)。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-ModifyingVBAOrMacroCode-ModifyingVBAOrMacroCode.cs" >}}

## **高级主题**
- [在工作簿中添加对VBA项目的库引用](/cells/zh/net/add-a-library-reference-to-vba-project-in-workbook/)
- [将宏分配给窗体控件](/cells/zh/net/assign-macro-to-form-control/)
- [检查VBA代码的数字签名是否有效](/cells/zh/net/check-if-digital-signature-of-vba-code-is-valid/)
- [检查VBA代码是否已签名](/cells/zh/net/check-if-vba-code-is-signed/)
- [检查工作簿中的VBA项目是否已签名](/cells/zh/net/check-if-vba-project-in-a-workbook-is-signed/)
- [检查VBA项目是否受保护并锁定以供查看](/cells/zh/net/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [将VBA宏用户表单DesignerStorage从模板复制到目标工作簿](/cells/zh/net/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [使用证书对VBA代码项目进行数字签名](/cells/zh/net/digitally-sign-a-vba-code-project-with-certificate/)
- [将VBA证书导出到文件或流](/cells/zh/net/export-vba-certificate-to-file-or-stream/)
- [加载工作簿时过滤VBA项目](/cells/zh/net/filter-vba-project-while-loading-a-workbook/)
- [查找VBA项目是否受保护](/cells/zh/net/find-out-if-vba-project-is-protected/)
- [为Excel工作簿的VBA项目设置密码保护](/cells/zh/net/password-protect-the-vba-project-of-excel-workbook/)

