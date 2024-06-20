---
title: Excel の範囲をコピーする
linktitle: 範囲をコピーする
type: docs
weight: 30
url: /ja/java/copy-ranges-of-Excel/
---

## **紹介**

Excel では、範囲を選択し、範囲をコピーし、その後、同じワークシート、他のワークシート、または他のファイルに特定のオプションで貼り付けることができます。

## **Aspose.Cells を使用して範囲をコピーする**

Aspose.Cellsは、範囲をコピーするいくつかのオーバーロード[Range.Copy](https://reference.aspose.com/cells/java/com.aspose.cells/range)メソッドを提供しています。
## **範囲をコピー**

ソース範囲、ターゲット範囲を作成し、その後、Range.Copy メソッドを使用してソース範囲をターゲット範囲にコピーします。

以下のコードを参照してください:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Copy-Range.java" >}}

## **オプションで範囲を貼り付ける**

Aspose.Cells は特定のタイプで範囲を貼り付ける機能をサポートしています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Paste-Range.java" >}}

## **範囲のデータのみをコピーします。**
次のコードのようにRange.CopyDataメソッドを使用してデータをコピーすることもできます:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Copy-Range-Data.java" >}}


