---
title: ワークシートの保護に使用するパスワードの確認
type: docs
weight: 370
url: /ja/net/verify-password-used-to-protect-the-worksheet/
---
{{% alert color="primary" %}}

Aspose.Cells API により、[**保護**](https://reference.aspose.com/cells/net/aspose.cells/protection)いくつかの便利なプロパティとメソッドを導入してクラスを作成します。そのような方法の 1 つは、[**パスワードを照合します**](https://reference.aspose.com/cells/net/aspose.cells/protection/methods/verifypassword)これにより、パスワードをインスタンスとして指定できます*ストリング*を保護するために同じパスワードが使用されているかどうかを確認します。[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet).

{{% /alert %}}

の[**Protection.VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/methods/verifypassword)メソッドが返す**真実**指定されたパスワードが、指定されたワークシートを保護するために使用されるパスワードと一致する場合、および**間違い**指定したパスワードが一致しない場合。次のコードでは、[**Protection.VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/methods/verifypassword)と組み合わせた方法[**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword)プロパティを使用してパスワード保護を検出し、パスワードを検証します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-VerifyPasswordUsedToProtectWorksheets-VerifyPasswordUsedToProtectWorksheets.cs" >}}
