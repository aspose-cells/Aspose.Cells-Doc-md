---
title: 暗号化されたファイルのパスワードを確認する
type: docs
weight: 10
url: /ja/net/verify-password-of-encrypted-excel-and-ods-files/
description: CShapeコードを使用して、暗号化されたExcel（xlsx、xlsb、xls、xlsm）およびOpen Office（ODS）ファイルのパスワードを検証してください。
---

{{% alert color="primary" %}}
Excel（xlsx、xlsb、xls、xlsm）およびOpen Office（ODS）ファイルがパスワードでロックされている場合、Asposeはファイルの特定のデータを解析せずに簡単なパスワード検証をサポートしています。
{{% /alert %}}

## **暗号化されたファイルのパスワードを確認します**

Aspose.Cells for .NETは、暗号化されたファイルのパスワードを検証するための[**VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/verifypassword)メソッドを提供します。これらのメソッドは、ファイルストリームと検証する必要があるパスワードの2つのパラメータを受け入れます。
以下のコードスニペットは、提供されたパスワードが有効かどうかを確認する[**VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/verifypassword)メソッドの使用を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-VerifyPassword-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
