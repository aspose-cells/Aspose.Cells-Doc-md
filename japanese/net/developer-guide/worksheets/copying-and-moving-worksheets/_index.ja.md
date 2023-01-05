---
title: ワークシートのコピーと移動
type: docs
weight: 10
url: /ja/net/copying-and-moving-worksheets/
---
{{% alert color="primary" %}}

場合によっては、共通の書式設定とデータを含む多数のワークシートが必要になることがあります。たとえば、四半期ごとの予算を扱う場合、同じ列見出し、行見出し、および数式を含むシートを含むワークブックを作成できます。これを行う方法があります: 1 つのシートを作成し、それをコピーします。

Aspose.Cells は、ワークブック内またはワークブック間でのワークシートのコピーと移動をサポートしています。データ、フォーマット、テーブル、マトリックス、チャート、画像、その他のオブジェクトを備えたワークシートは、最高の精度でコピーされます。

{{% /alert %}}

## **Microsoft Excel を使用したシートの移動またはコピー**

以下は、Microsoft Excel のワークブック内またはワークブック間でワークシートをコピーおよび移動するための手順です。

1. シートを別のブックに移動またはコピーするには、シートを受け取るブックを開きます。
1. 移動またはコピーするシートを含むブックに切り替えてから、シートを選択します。
1. 上で**編集**メニュー、クリック**シートの移動またはコピー**.
1. の中に**予約する**ダイアログで、ワークブックをクリックしてシートを受け取ります。
1. 選択したシートを新しいワークブックに移動またはコピーするには、**新しい本**.
1. の中に**シート前**ボックスで、移動またはコピーしたシートを挿入する前のシートをクリックします。
1. シートを移動する代わりにコピーするには、**コピーを作成する**チェックボックス。

### **Aspose.Cells のワークブック内でワークシートをコピーする**

Aspose.Cells はオーバーロードされたメソッドを提供し、[**Aspose.Cells.WorksheetCollection.AddCopy()**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/addcopy/index)、ワークシートをコレクションに追加し、既存のワークシートからデータをコピーするために使用されます。メソッドの 1 つのバージョンは、ソース ワークシートのインデックスをパラメーターとして受け取ります。もう一方のバージョンは、ソース ワークシートの名前を取ります。

次の例は、ブック内の既存のワークシートをコピーする方法を示しています。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-CopyWithinWorkbook-1.cs" >}}

### **ワークブック間でワークシートをコピーする**

Aspose.Cells はメソッドを提供し、[**Aspose.Cells.ワークシート.コピー()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/copy/index)ワークブック内またはワークブック間でソース ワークシートから別のワークシートにデータと書式をコピーするために使用されます。このメソッドは、ソース ワークシート オブジェクトをパラメーターとして受け取ります。

次の例は、あるブックから別のブックにワークシートをコピーする方法を示しています。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-CopyWorksheetsBetweenWorkbooks-1.cs" >}}

次の例は、あるブックから別のブックにワークシートをコピーする方法を示しています。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-CopyWorksheetFromWorkbookToOther-1.cs" >}}

### **ワークブック内でワークシートを移動する**

Aspose.Cells はメソッドを提供します[**Aspose.Cells.Worksheet.MoveTo()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/moveto)ワークシートを同じスプレッドシート内の別の場所に移動するために使用されます。このメソッドは、対象のワークシート インデックスをパラメーターとして受け取ります。

次の例は、ワークシートをブック内の別の場所に移動する方法を示しています。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-MoveWorksheet-1.cs" >}}
