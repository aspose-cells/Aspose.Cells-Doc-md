---
title: ワークシート内の結合セルを検出
type: docs
weight: 3000
url: /ja/java/detect-merged-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

Microsoft Excelでは、複数のセルを1つに結合することができます。これは、複雑なテーブルを作成したり、複数の列にまたがる見出しを作成したりするためによく使用されます。

Aspose.Cellsを使用してワークシート内の結合セル領域を特定できます。また、それらを結合解除することもできます。この記事では、Aspose.Cellsを使用してタスクを実行するための最も簡単なコード行を提供しています。

この記事では、ワークシート内の結合されたセルを検出してから結合を解除する手順の簡潔な説明を提供します。

{{% /alert %}}

## **デモンストレーション**

この例では、**MergeTrial**というテンプレートのMicrosoft Excelファイルを使用しています。そのシートには複数の結合セル領域も含まれています。

**テンプレートファイル**

![todo:image_alt_text](detect-merged-cells-in-a-worksheet_1.png)

Aspose.Cellsは、すべての結合セルを取得するために使用される[**Cells.getMergedCells()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells/#getMergedCells--)メソッドを提供します。

下記のコードを実行すると、シートの内容をクリアし、すべてのセル領域のマージを解除してファイルを再保存します。

出力ファイル

![todo:image_alt_text](detect-merged-cells-in-a-worksheet_2.png)

## **コード例**

ワークシート内の結合されたセル領域を特定し、それらを解除する方法を見つけるために、以下のサンプルコードを参照してください。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectMergedCells-DetectMergedCells.java" >}}

## **関連記事**

- [セルを結合および分割](/cells/ja/java/merging-and-unmerging-cells/)。
