---
title: 使用证书对 VBA 代码项目进行数字签名
type: docs
weight: 110
url: /zh/java/digitally-sign-a-vba-code-project-with-certificate/
---
{{% alert color="primary" %}}

您可以使用 Aspose.Cells 及其代码对您的 VBA 代码项目进行数字签名[**工作簿.VbaProject.Sign()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#sign(com.aspose.cells.DigitalSignature)） 方法。请按照以下步骤检查您的 excel 文件是否使用证书进行了数字签名。

- 点击**视觉基础**来自**开发商**要打开的选项卡**Visual Basic for Applications 集成开发环境**
- 点击**工具** > **数字签名...**的**Visual Basic for Applications 集成开发环境**

它会显示**数字签名表**显示文档是否使用证书进行数字签名。

{{% /alert %}} 

## **使用 C# 中的证书对 VBA 代码项目进行数字签名**

下面的示例代码说明了如何使用[**工作簿.VbaProject.Sign()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#sign(com.aspose.cells.DigitalSignature)） 方法。以下是示例代码的输入和输出文件。您可以使用任何 excel 文件和任何证书来测试此代码。

- [源 Excel 文件](5115028.xlsm)在示例代码中使用。
- [示例 pfx 文件](5115039.pfx)创建数字签名。请在您的计算机上安装它以运行此代码。它的密码是1234。
- [输出Excel文件](5115029.xlsm)由示例代码生成。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ManagingVBAModules-DigitallySignVbaProjectWithCertificate.java" >}}
