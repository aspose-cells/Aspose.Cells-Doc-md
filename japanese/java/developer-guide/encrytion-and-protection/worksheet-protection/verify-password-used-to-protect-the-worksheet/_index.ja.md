---
title: ワークシートを保護するために使用されたパスワードの検証
type: docs
weight: 290
url: /ja/java/verify-password-used-to-protect-the-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells APIは、[**Protection**](https://reference.aspose.com/cells/java/com.aspose.cells/Protection)クラスを拡張し、いくつかの有用なプロパティやメソッドを導入しました。そのようなメソッドの1つが、文字列のインスタンスとしてパスワードを指定し、ワークシートを保護するために同じパスワードが使用されているかどうかを検証する[**verifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#verifyPassword(java.lang.String))です。

{{% /alert %}}

## **ワークシートを保護するために使用されたパスワードの検証**

[**Protection.verifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#verifyPassword(java.lang.String))メソッドは、指定されたパスワードが与えられたワークシートを保護するために使用されたパスワードと一致する場合は**true**を返し、与えられたパスワードが一致しない場合は**false**を返します。次のコードは、[**Protection.verifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#verifyPassword(java.lang.String))メソッドを使用してパスワード保護を検出し、パスワードを検証することを示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-VerifyPasswordtoProtectWorksheet-VerifyPasswordtoProtectWorksheet.java" >}}
