---
title: ワークシートのコピーと移動
type: docs
weight: 20
url: /ja/java/copying-and-moving-worksheets/
---
{{% alert color="primary" %}}

場合によっては、共通の書式設定とデータを含む多数のワークシートが必要になることがあります。たとえば、四半期ごとの予算を扱う場合、同じ列見出し、行見出し、および数式を含むシートを含むワークブックを作成できます。これを行う方法があります: 1 つのシートを作成し、それをコピーします。

Aspose.Cells は、ワークブック内またはワークブック間でのワークシートのコピーと移動をサポートしています。データ、フォーマット、テーブル、マトリックス、チャート、画像、その他のオブジェクトを備えたワークシートは、最高の精度でコピーされます。

{{% /alert %}}

## **Microsoft Excel を使用したシートの移動またはコピー**

以下は、ワークブック内またはワークブック間でワークシートをコピーおよび移動するための手順です。

1. シートを別のブックに移動またはコピーするには、シートを受け取るブックを開きます。
1. 移動またはコピーするシートを含むブックに切り替えてから、シートを選択します。
1. 上で**編集**メニュー、クリック**シートの移動またはコピー**.
1. [To book] ボックスで、ワークブックをクリックしてシートを受け取ります。
1. 選択したシートを新しいワークブックに移動またはコピーするには、**新しい本**.
1. の中に**シート前**ボックスで、移動またはコピーしたシートを挿入する前のシートをクリックします。
1. シートを移動する代わりにコピーするには、**コピーを作成する**チェックボックス。

## **ワークブック内でワークシートをコピーする**

Aspose.Cells はオーバーロードされたメソッドを提供し、[**WorksheetCollection.addCopy()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#addCopy(int))、ワークシートをコレクションに追加し、既存のワークシートからデータをコピーするために使用されます。メソッドの 1 つのバージョンは、ソース ワークシートのインデックスをパラメーターとして受け取ります。もう一方のバージョンは、ソース ワークシートの名前を取ります。

次の例は、ブック内の既存のワークシートをコピーする方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CopyWithinWorkbook-CopyWithinWorkbook.java" >}}

## **ワークブック間でワークシートをコピーする**

Aspose.Cells はメソッドを提供し、[**Worksheet.copy()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#copy(com.aspose.cells.Worksheet))、ソース ワークシートからワークブック内またはワークブック間でデータと書式設定を別のワークシートにコピーするために使用されます。このメソッドは、ソース ワークシート オブジェクトをパラメーターとして受け取ります。

次の例は、あるブックから別のブックにワークシートをコピーする方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CopyWorksheetsBetweenWorkbooks-CopyWorksheetsBetweenWorkbooks.java" >}}

次の例は、あるブックから別のブックにワークシートをコピーする方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CopyWorksheetFromWorkbookToOther-CopyWorksheetFromWorkbookToOther.java" >}}

## **ワークブック内でワークシートを移動する**

Aspose.Cells はメソッドを提供し、[**Worksheet.moveTo()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#moveTo(int))、ワークシートを同じスプレッドシート内の別の場所に移動するために使用されます。

次の例は、ワークシートをブック内の別の場所に移動する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-MoveWorksheet-MoveWorksheet.java" >}}
