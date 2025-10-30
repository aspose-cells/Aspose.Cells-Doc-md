---
title: ワークシートを保護するために使用されたパスワードの検証
type: docs
weight: 370
url: /ja/python-net/verify-password-used-to-protect-the-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET APIは、便利なプロパティとメソッドを導入して [**Protection**](https://reference.aspose.com/cells/python-net/aspose.cells/protection) クラスを強化しています。その一例として、[**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/verify_password)メソッドはパスワードを*文字列* 型のインスタンスとして指定し、同じパスワードが保護に使用されたかどうかを検証します。

{{% /alert %}}

[**Protection.verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/verify_password) メソッドは、指定されたパスワードが指定されたワークシートを保護するために使用されたパスワードに一致する場合は **true** を返し、指定されたパスワードが一致しない場合は **false** を返します。 次のコード片は、パスワード保護を検出し、パスワードを検証するために [**Protection.verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/verify_password) メソッドと [**Protection.is_protected_with_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/is_protected_with_password) プロパティを組み合わせて使用します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-VerifyPasswordUsedToProtectWorksheets.py" >}}

{{< app/cells/assistant language="python-net" >}}
