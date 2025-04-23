---
title: ワークシートのコピーと移動
type: docs
weight: 20
url: /ja/java/copying-and-moving-worksheets/
---

{{% alert color="primary" %}}

時には、共通のフォーマットとデータを持つワークシートの数が必要です。たとえば、四半期予算で作業する場合、同じ列見出し、行見出し、数式を含むシートを持つワークブックを作成したいと思うかもしれません。これを行う方法があります：1つのシートを作成してからコピーすることです。

Aspose.Cellsは、ブック内またはブック間でのワークシートのコピーおよび移動をサポートしています。データ、書式、テーブル、行列、チャート、画像、その他のオブジェクトが完全な状態でコピーされます。

{{% /alert %}}

## **Microsoft Excelでシートを移動またはコピーする**

ブック内またはブック間でのワークシートのコピーおよび移動の手順は次のとおりです。

1. 別のワークブックにシートを移動またはコピーするには、シートを受け取るワークブックを開きます。
1. 移動またはコピーしたいシートを含むワークブックに切り替え、そのシートを選択します。
1. **編集**メニューで**シートの移動またはコピー**をクリックします。
1. 別のブックのボックスで、シートを受け取るブックをクリックしてください。
1. 選択したシートを新しいブックに移動またはコピーするには、**新しいブック**をクリックしてください。
1. **前のシート**ボックスで、移動またはコピーされたシートが挿入される前のシートをクリックします。
1. 移動ではなくシートをコピーする場合は、**コピーを作成**チェックボックスを選択します。

## **ブック内でのワークシートのコピー**

Aspose.Cellsは[**WorksheetCollection.addCopy()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#addCopy-int-)というオーバーロードされたメソッドを提供し、これはコレクションにワークシートを追加し、既存のワークシートからデータをコピーするために使用されます。メソッドの1つのバージョンは、ソースワークシートのインデックスをパラメーターとして取ります。もう1つのバージョンは、ソースワークシートの名前をパラメーターとして取ります。

次の例は、ブック内で既存のワークシートをコピーする方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CopyWithinWorkbook-CopyWithinWorkbook.java" >}}

## **ブック間でのワークシートのコピー**

Aspose.Cellsは[**Worksheet.copy()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#copy-com.aspose.cells.Worksheet-)というメソッドを提供し、これはソースのワークシートオブジェクトをパラメーターとして使用して、ブック内またはブック間で別のワークシートにデータと書式をコピーするために使用されます。

次の例は、ワークブックから別のワークブックにワークシートをコピーする方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CopyWorksheetsBetweenWorkbooks-CopyWorksheetsBetweenWorkbooks.java" >}}

次の例は、ワークブックから別のワークブックにワークシートをコピーする方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CopyWorksheetFromWorkbookToOther-CopyWorksheetFromWorkbookToOther.java" >}}

## **ワークブック内でのワークシートの移動**

Aspose.Cellsは[**Worksheet.moveTo()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#moveTo-int-)というメソッドを提供し、これは同じスプレッドシート内でワークシートを別の場所に移動するために使用されます。

次の例は、ワークブック内でワークシートを別の場所に移動する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-MoveWorksheet-MoveWorksheet.java" >}}
{{< app/cells/assistant language="java" >}}
