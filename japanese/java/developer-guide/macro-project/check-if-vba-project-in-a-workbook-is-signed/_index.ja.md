---
title: ワークブック内の VBA プロジェクトが署名されているかどうかを確認する
type: docs
weight: 40
url: /ja/java/check-if-vba-project-in-a-workbook-is-signed/
---
{{% alert color="primary" %}}

Microsoft Excel を使用して、VBA プロジェクトが署名されているかどうかを確認できます。**ツール > デジタル署名...**メニューコマンド。同様に、Aspose.Cells を使用してプログラムで確認できます。[**Workbook.getVbaProject().isSigned()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsSigned)方法。

{{% /alert %}}

## **ワークブック内の VBA プロジェクトが署名されているかどうかを確認する**

次のコードは、ワークブックを読み込み、その VBA プロジェクトが次の方法で署名されているかどうかを確認します。[**Workbook.getVbaProject().isSigned()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsSigned)財産。物件が戻ってくる**真実**プロジェクトが署名されている場合、それ以外の場合は返されます**間違い**.

## サンプルコード

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckVbaProjectSigned-CheckVbaProjectSigned.java" >}}
