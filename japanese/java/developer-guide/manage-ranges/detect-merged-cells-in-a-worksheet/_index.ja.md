---
title: ワークシートでマージされた Cells を検出する
type: docs
weight: 3000
url: /ja/java/detect-merged-cells-in-a-worksheet/
---
{{% alert color="primary" %}}

Microsoft Excel では、複数のセルを 1 つに結合できます。これは、複雑なテーブルを作成したり、複数の列にまたがる見出しを保持するセルを作成したりするためによく使用されます。

Aspose.Cells を使用すると、ワークシート内の結合されたセル領域を識別できます。それらをマージ解除することもできます。この記事では、Aspose.Cells を使用してタスクを実行するための最も単純なコード行を提供します。

この記事では、ワークシート内の結合セルを検索して結合解除する方法について簡潔に説明します。

{{% /alert %}}

## **デモンストレーション**

この例では、テンプレート Microsoft という Excel ファイルを使用します。**マージトライアル**Merge Trial とも呼ばれるシートにいくつかの結合されたセル領域があります。

**テンプレートファイル**

![todo:画像_代替_文章](detect-merged-cells-in-a-worksheet_1.png)

Aspose.Cells は[**Cells.getMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MergedCells)結合されたセル領域の ArrayList を取得するために使用されるメソッド。

以下のコードが実行されると、シートの内容がクリアされ、ファイルを再度保存する前にすべてのセル領域が結合解除されます。

**出力ファイル**

![todo:画像_代替_文章](detect-merged-cells-in-a-worksheet_2.png)

## **コード例**

次のサンプル コードを参照して、ワークシート内の結合されたセル領域を特定し、結合を解除する方法を見つけてください。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectMergedCells-DetectMergedCells.java" >}}

## **関連記事**

- [セルの結合と分割](/cells/ja/java/merging-and-unmerging-cells/).
