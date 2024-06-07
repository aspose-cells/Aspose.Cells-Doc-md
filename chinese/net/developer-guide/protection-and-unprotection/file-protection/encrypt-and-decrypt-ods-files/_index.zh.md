---
title: 加密和解密ODS文件
type: docs
weight: 10
url: /zh/net/encrypt-and-decrypt-ods-files/
description: 使用 Aspose.Cells for .Net 可以纯粹使用网络库密码保护和加密ODS文件。
---

{{% alert color="primary" %}}
OpenOffice.org 是一款功能齐全的办公套件，支持对文件进行密码保护和加密。但是，加密的ODS文件只能在提供密码后由OpenOffice打开。Excel无法打开加密的ODS文件，可能会出现警告消息。与其他文件类型不同，加密选项不适用于ODS文件。 
Aspose.Cells 允许加密和解密ODS文件。解密后的ODS文件可以在Excel和OpenOffice中打开。 
{{% /alert %}}

## **使用OpenOffice Calc进行加密**
1. 选择 **另存为** 并点击 **另存时使用密码** 框。
1. 点击**保存**按钮。
1. 在打开的“设置密码”窗口的“输入密码以打开”和“确认密码”字段中输入所需的密码。 
1. 单击**确定**按钮以保存文件。

## **使用Aspose.Cells for .Net对ODS文件进行加密**
要对ODS文件进行加密，请加载文件并在保存之前将[**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password)值设置为实际密码。输出的加密ODS文件只能在OpenOffice中打开。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingODSFiles-1.cs" >}}

## **使用Aspose.Cells for .Net对ODS文件进行解密**

要解密 ODS 文件，请提供密码加载文件到 [**LoadOptions.Password**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/password)。一旦文件加载完成，将 [**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) 字符串设置为 null。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-DecryptingODSFiles-1.cs" >}}
