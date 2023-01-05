---
title: 加密和解密 ODS 个文件
type: docs
weight: 10
url: /zh/net/encrypt-and-decrypt-ods-files/
description: 使用 Aspose.Cells for .Net 密码保护和加密 ODS 文件，这是一个纯网络库。
---
{{% alert color="primary" %}}
OpenOffice.org 是一个功能齐全的办公套件，支持密码保护和加密文件。然而加密的ODS文件只有在提供密码后才能被OpenOffice打开。 Excel 无法打开加密的 ODS 文件，可能会引发警告消息。与其他文件类型不同，加密选项不适用于 ODS 文件。
 Aspose.Cells 允许加密和解密 ODS 文件。解密后的ODS文件可以在Excel和OpenOffice中打开，
{{% /alert %}}

## **使用 OpenOffice Calc 加密**
1. 选择**另存为**并点击**用密码保存**盒子。
1. 点击**救球**按钮。
1. 在两者中输入您想要的密码**输入密码打开**和**确认密码**打开的“设置密码”窗口中的字段。
1. 点击**好的**按钮保存文件。

## **使用 .Net 的 Aspose.Cells 加密 ODS 文件**
要加密 ODS 文件，加载文件并设置[**工作簿设置.密码**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password)在保存之前将值设置为实际密码。输出的加密文件ODS只能在OpenOffice中打开。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingODSFiles-1.cs" >}}

## **使用 .Net 的 Aspose.Cells 解密 ODS 文件**

要解密 ODS 文件，请通过在[**加载选项.密码**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/password).加载文件后，设置[**工作簿设置.密码**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password)字符串为空。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-DecryptingODSFiles-1.cs" >}}
