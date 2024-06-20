---
title: 暗号化されたファイルのパスワードを確認する
type: docs
weight: 10
url: /ja/java/verify-password-of-encrypted-excel-and-ods-files/
description: Excel（xlsx、xlsb、xls、xlsm）およびOpenOffice（ODS）ファイルのパスワードを検証するために、Javaコードを使用します。
---

{{% alert color="primary" %}}
Excel（xlsx、xlsb、xls、xlsm）およびOpenOffice（ODS）ファイルがパスワードでロックされている場合、Aspose.Cells for Javaはファイルの特定のデータを解析せずに簡単なパスワード検証をサポートしています。
{{% /alert %}}

## **暗号化されたファイルのパスワードを確認します**

暗号化されたファイルのパスワードを確認するために、Aspose.Cells for Javaは[**VerifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/fileformatutil#verifyPassword(java.io.InputStream,%20java.lang.String))メソッドを提供します。これにより、ファイルストリームと確認するパスワードの2つのパラメータを受け入れます。
以下のコードスニペットは、提供されたパスワードが有効かどうかを確認する[**VerifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/fileformatutil#verifyPassword(java.io.InputStream,%20java.lang.String))メソッドの使用を示しています。

### **サンプルコード:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-VerifyPassword-1.java" >}}

