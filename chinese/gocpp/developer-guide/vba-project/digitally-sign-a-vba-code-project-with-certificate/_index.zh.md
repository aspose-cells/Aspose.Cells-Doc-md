---
title: 用数字证书为VBA代码项目数字签名（C++）
linktitle: 使用证书为VBA代码项目进行数字签名
type: docs
weight: 110
url: /zh/go-cpp/digitally-sign-a-vba-code-project-with-certificate/
description: 了解如何使用证书和Aspose.Cells for C++数字签名您的VBA代码项目。
---

{{% alert color="primary" %}} 

您可以使用Aspose.Cells及其[**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/go-cpp/vbaproject/sign/)方法对VBA代码项目进行数字签名。请按照以下步骤检查您的Excel文件是否已用证书进行数字签名。

- 点击**开发工具**标签中的**Visual Basic**以打开**Visual Basic for Applications IDE**。
- 在**Visual Basic for Applications IDE**中点击**工具** > **数字签名...**。

它将显示**数字签名表单**，显示文档是否已使用证书进行数字签名。

{{% /alert %}} 

## **用C++为VBA代码项目进行数字签名并使用证书**

以下示例代码演示如何使用[**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/go-cpp/vbaproject/sign/)方法。此示例代码的输入和输出文件都已列出。您可以使用任何Excel文件和任何证书测试此代码。

- [用于示例代码的源Excel文件](5115028.xlsm)
- [示例pfx文件](5115039.pfx)用于创建数字签名。请在计算机上安装它以运行此代码。其密码为1234。
- [示例代码生成的输出Excel文件](5115029.xlsm)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DigitallySignAVbaCodeProjectWithCertificate.go" >}}
