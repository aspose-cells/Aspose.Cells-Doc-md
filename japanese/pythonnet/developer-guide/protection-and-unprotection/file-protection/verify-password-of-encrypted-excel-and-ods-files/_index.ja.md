---
title: 暗号化されたファイルのパスワードを確認する
type: docs
weight: 10
url: /ja/python-net/verify-password-of-encrypted-excel-and-ods-files/
description: CShapeコードを使用して、暗号化されたExcel（xlsx、xlsb、xls、xlsm）およびOpen Office（ODS）ファイルのパスワードを検証してください。
---

{{% alert color="primary" %}}
Excel（xlsx、xlsb、xls、xlsm）およびOpen Office（ODS）ファイルがパスワードでロックされている場合、Asposeはファイルの特定のデータを解析せずに簡単なパスワード検証をサポートしています。
{{% /alert %}}

## **暗号化されたファイルのパスワードを確認します**

暗号化されたファイルのパスワードを確認するには、Aspose.Cells for Python via .NETが[**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/verify_password)メソッドを提供します。これらのメソッドは、ファイルストリームと検証したいパスワードの2つのパラメータを受け取ります。
以下のコードスニペットは、提供されたパスワードが有効かどうかを確認する[**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/verify_password)メソッドの使用を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-VerifyPassword-1.py" >}}


