---
title: ワークシートを保護するために使用されたパスワードの検証
type: docs
weight: 370
url: /ja/net/verify-password-used-to-protect-the-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells の API は [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/protection) クラスを向上させ、いくつかの便利なプロパティとメソッドを導入しています。 そのようなメソッドの1つは、*string* のインスタンスとしてパスワードを指定し、[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) を保護すると同じパスワードが使用されたかを検証する [**VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/methods/verifypassword) です。

{{% /alert %}}

[**Protection.VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/methods/verifypassword) メソッドは、指定されたパスワードが指定されたワークシートを保護するために使用されたパスワードに一致する場合は **true** を返し、指定されたパスワードが一致しない場合は **false** を返します。 次のコード片は、パスワード保護を検出し、パスワードを検証するために [**Protection.VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/methods/verifypassword) メソッドと [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword) プロパティを組み合わせて使用します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-VerifyPasswordUsedToProtectWorksheets-VerifyPasswordUsedToProtectWorksheets.cs" >}}
