---
title: 用证书对VBA代码项目进行数字签名
type: docs
weight: 110
url: /zh/java/digitally-sign-a-vba-code-project-with-certificate/
---

{{% alert color="primary" %}}

您可以使用Aspose.Cells的[**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#sign(com.aspose.cells.DigitalSignature))方法对VBA代码项目进行数字签名。请按照以下步骤检查您的Excel文件是否用证书数字签名。

- 从**开发人员**选项卡中单击**Visual Basic**打开**Visual Basic for Applications IDE**
- 单击 **工具** > **数字签名...** 的 **Visual Basic for Applications IDE**

它将显示**数字签名表单**，显示文档是否使用证书进行了数字签名。

{{% /alert %}} 

## **使用C#对VBA代码项目进行数字签名**

以下示例代码说明了如何使用[**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#sign(com.aspose.cells.DigitalSignature))方法。这是示例代码的输入和输出文件。您可以使用任何Excel文件和任何证书来测试这段代码。

- [示例Excel文件](5115028.xlsm)用于示例代码。
- [示例pfx文件](5115039.pfx)用于创建数字签名。 请在计算机上安装它以运行此代码。 密码为1234。
- [输出的 Excel 文件](5115029.xlsm) 是由示例代码生成的。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ManagingVBAModules-DigitallySignVbaProjectWithCertificate.java" >}}
