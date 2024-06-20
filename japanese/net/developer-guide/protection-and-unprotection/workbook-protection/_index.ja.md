---
title: ブック構造の保護と保護解除
type: docs
weight: 40
url: /ja/net/protect-and-unprotect-workbook-structure/
description: CSharpコードを使用してExcelファイルのブック構造を保護および保護解除
---


{{% alert color="primary" %}}
他のユーザーによる隠しワークシートの表示、追加、移動、削除、または非表示、およびワークシートの名前の変更を防ぐために、Excelブックの構造をパスワードで保護できます。
{{% /alert %}}


## **MS Excelでのブック構造の保護と保護解除**

**![ブック構造の保護と保護解除](protect-and-unprotect-workbook-structure.png)**

1. **レビュー > ブックの保護** をクリックします。
1. **パスワードボックス** にパスワードを入力します。
1. **OK** を選択し、パスワードを再入力して確認し、その後再度 **OK** を選択します。


## **Aspose.Cell for .Netを使用してブック構造を保護**
Excelファイルのワークシートの構造を保護するためには、次の簡単なコード行のみが必要です。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Example-Protect-Workbook-Structure.cs" >}}

## **Aspose.Cell for .Netを使用してブック構造を保護解除**
Aspose.Cells APIを使用してワークブック構造を保護解除するのは簡単です。正しいパスワードが必要です。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Example-Unprotect-Workbook-Structure.cs" >}}

{{% alert color="primary" %}}
注意：正しいパスワードが必要です。
{{% /alert %}}
