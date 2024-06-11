---
title: 使用证书为VBA代码项目进行数字签名
type: docs
weight: 110
url: /zh/net/digitally-sign-a-vba-code-project-with-certificate/
---

{{% alert color="primary" %}}

您可以使用Aspose.Cells的[**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/methods/sign)方法为VBA代码项目进行数字签名。请按照以下步骤检查您的Excel文件是否使用证书进行了数字签名。

- 从“开发人员”选项卡中单击“Visual Basic”以打开“Visual Basic for Applications IDE”
- 在“Visual Basic for Applications IDE”中单击“工具” > “数字签名...”

将显示“数字签名表单”，显示文档是否已使用证书进行数字签名。

{{% /alert %}} 

## **使用C＃为VBA代码项目使用证书进行数字签名**

以下示例代码说明了如何使用[**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/methods/sign)方法。这是示例代码的输入和输出文件。您可以使用任何Excel文件和任何证书来测试此代码。

- [用于示例代码的源Excel文件](5115028.xlsm)
- [示例pfx文件](5115039.pfx)用于创建数字签名。请在计算机上安装它以运行此代码。其密码为1234。
- [示例代码生成的输出Excel文件](5115029.xlsm)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-DigitallySignVbaProjectWithCertificate-1.cs" >}}
