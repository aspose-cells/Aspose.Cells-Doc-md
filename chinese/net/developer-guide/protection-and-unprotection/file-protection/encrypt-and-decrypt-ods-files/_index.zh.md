---
title: 加密和解密ODS文件
type: docs
weight: 10
url: /zh/net/encrypt-and-decrypt-ods-files/
description: 使用Aspose.Cells for .Net对ODS文件进行密码保护和加密，这是一个纯.NET库。
---

{{% alert color="primary" %}}
OpenOffice.org是一个功能齐全的办公套件，支持对文件进行密码保护和加密。然而，加密的ODS文件只能在提供密码后才能在OpenOffice中打开。Excel无法打开加密的ODS文件，可能会弹出警告消息。与其他文件类型不同，加密选项不适用于ODS文件。 
Aspose.Cells允许对ODS文件进行加密和解密。解密的ODS文件可以同时在Excel和OpenOffice中打开。 
{{% /alert %}}

## **在OpenOffice Calc中加密**
1. 选择**另存为**并点击**加上密码保存**框。
1. 点击**保存**按钮。
1. 在打开密码窗口中的**输入打开文件的密码**和**确认密码**字段中键入所需的密码。 
1. 点击**确定**按钮以保存文件。

## **使用Aspose.Cells for .Net加密ODS文件**
要对ODS文件进行加密，加载文件并在保存之前将[**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password)值设置为实际密码。加密的输出ODS文件只能在OpenOffice中打开。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingODSFiles-1.cs" >}}

## **使用Aspose.Cells for .Net解密ODS文件**

要解密ODS文件，通过在[**LoadOptions.Password**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/password)中提供密码来加载文件。一旦文件加载完成，将[**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password)字符串设置为null。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-DecryptingODSFiles-1.cs" >}}
