---
title: ワークシートがパスワードで保護されているかどうかを検出する
type: docs
weight: 360
url: /ja/python-net/detect-if-worksheet-is-password-protected/
---

{{% alert color="primary" %}}

ワークブックおよびワークシートは個別に保護可能です。例えば、スプレッドシートにはパスワード保護された複数のワークシートが含まれる場合もありますが、スプレッドシート自体は保護されていない場合もあります。Aspose.Cells for Python via .NET APIは、特定のワークシートがパスワード保護されているかどうかを検出する手段を提供します。この資料では、その使用方法について説明します。

{{% /alert %}}

Aspose.Cells for Python via .NETは、[**Protection.is_protected_with_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/is_protected_with_password) プロパティを公開しており、これによりワークシートがパスワード保護されているかどうかを確認できます。Boolean型の [**Protection.is_protected_with_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/is_protected_with_password) プロパティは、ワークシートがパスワード保護されていれば**true**を返し、そうでなければ**false**を返します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-CheckIfPasswordProtected.py" >}}

