---
title: 暗号化ファイルのパスワードを確認する
type: docs
weight: 10
url: /ja/java/verify-password-of-encrypted-excel-and-ods-files/
description: Java コードを使用して、暗号化された Excel (xlsx、xlsb、xls、xlsm) および Open Office (ODS) ファイルのパスワードを確認します。
---
{{% alert color="primary" %}}
Excel (xlsx、xlsb、xls、xlsm) および Open Office (ODS) ファイルがパスワードでロックされている場合、Aspose.Cells for Java は、ファイルの特定のデータを解析することなく、単純なパスワード検証をサポートします。
{{% /alert %}}

## **暗号化されたファイルのパスワードを確認する**

暗号化されたファイルのパスワードを確認するには、Aspose.Cells for Java を指定します。[**パスワードを照合します**](https://reference.aspose.com/cells/java/com.aspose.cells/fileformatutil#verifyPassword(java.io.InputStream,%20java.lang.String)) 方法。このメソッドは、検証が必要なファイル ストリームとパスワードの 2 つのパラメーターを受け入れます。
次のコード スニペットは、[**パスワードを照合します**](https://reference.aspose.com/cells/java/com.aspose.cells/fileformatutil#verifyPassword(java.io.InputStream,%20java.lang.String)) メソッドを使用して、提供されたパスワードが有効かどうかを確認します。

### **サンプルコード:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-VerifyPassword-1.java" >}}

