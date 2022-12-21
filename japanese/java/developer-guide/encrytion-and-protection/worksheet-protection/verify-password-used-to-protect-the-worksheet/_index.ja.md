---
title: ワークシートの保護に使用するパスワードの確認
type: docs
weight: 290
url: /ja/java/verify-password-used-to-protect-the-worksheet/
---
{{% alert color="primary" %}}

Aspose.Cells API により、[**保護**](https://reference.aspose.com/cells/java/com.aspose.cells/Protection)いくつかの便利なプロパティとメソッドを導入してクラスを作成します。そのような方法の 1 つは、[**パスワードを照合します**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#verifyPassword(java.lang.String)これにより、パスワードを文字列のインスタンスとして指定でき、ワークシートを保護するために同じパスワードが使用されているかどうかを確認できます。

{{% /alert %}}

## **ワークシートの保護に使用するパスワードの確認**

の[**Protection.verifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#verifyPassword(java.lang.String) ) メソッドが返す**真実**指定されたパスワードが、指定されたワークシートを保護するために使用されるパスワードと一致する場合、**間違い**指定したパスワードが一致しない場合。次のコードでは、[**Protection.verifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#verifyPassword(java.lang.String) ) メソッドと組み合わせて[**Protection.isProtectedWithPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#IsProtectedWithPassword)プロパティを使用してパスワード保護を検出し、パスワードを検証します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-VerifyPasswordtoProtectWorksheet-VerifyPasswordtoProtectWorksheet.java" >}}
