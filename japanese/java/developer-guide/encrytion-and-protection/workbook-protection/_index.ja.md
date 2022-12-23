---
title: ブック構造の保護と保護解除
type: docs
weight: 40
url: /ja/java/protect-and-unprotect-workbook-structure/
description: Java コードを使用して Excel ファイルのワークブック構造を保護および保護解除します。
---
{{% alert color="primary" %}}
他のユーザーが非表示のワークシートを表示したり、ワークシートを追加、移動、削除、非表示にしたり、ワークシートの名前を変更したりできないようにするために、Excel ブックの構造をパスワードで保護できます。
{{% /alert %}}


## **MS Excel でワークブック構造を保護および保護解除する**

**![ワークブック構造の保護と保護解除](protect-and-unprotect-workbook-structure.png)**

1. クリック**レビュー > ブックの保護**.
1. にパスワードを入力してください**パスワードボックス**.
1. 選択する**わかった**、パスワードを再入力して確認し、**わかった**また。


## **Aspose.Cell for Java を使用してブック構造を保護する**
Excel ファイルのワークブック構造の保護を実装するには、次の単純なコード行のみが必要です。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Protect-Workbook-Structure.java" >}}

## **Aspose.Cell for Java を使用してブック構造の保護を解除する**
Aspose.Cells API を使用すると、ブック構造の保護を簡単に解除できます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Unprotect-Workbook-Structure.java" >}}
{{% alert color="primary" %}}
注: 正しいパスワードが必要です。
{{% /alert %}}