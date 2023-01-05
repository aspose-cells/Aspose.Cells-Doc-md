---
title: ワークシートのコピーと移動
type: docs
weight: 20
url: /ja/python-java/copying-and-moving-worksheets/
---
{{% alert color="primary" %}} 

場合によっては、共通の書式設定とデータを含む多数のワークシートが必要になることがあります。たとえば、四半期ごとの予算を扱う場合、同じ列見出し、行見出し、および数式を含むシートを含むワークブックを作成できます。これを行う方法があります: 1 つのシートを作成し、それをコピーします。

Aspose.Cells は、ワークブック内またはワークブック間でのワークシートのコピーと移動をサポートしています。データ、フォーマット、テーブル、マトリックス、グラフ、画像、その他のオブジェクトを含むワークシートは、最高の精度でコピーされます。

{{% /alert %}} 
## **Microsoft Excel を使用したシートの移動またはコピー**
ワークブック内またはワークブック間でワークシートをコピーおよび移動する手順は次のとおりです。

1. シートを受け取るブックを開きます。
1. 移動またはコピーするシートを含むブックに切り替えてから、シートを選択します。
1. 上で**編集**メニュー、クリック**シートの移動またはコピー**.
1. [To book] ボックスで、ワークブックをクリックしてシートを受け取ります。
1. 選択したシートを新しいワークブックに移動またはコピーするには、**新しい本**.
1. の中に**シート前**ボックスで、移動またはコピーしたシートを挿入する前のシートをクリックします。
1. シートを移動する代わりにコピーするには、**コピーを作成する**チェックボックス。
### **ワークブック内でワークシートをコピーする**
Aspose.Cells はオーバーロードされた[WorksheetCollection.addCopy()](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#addCopy\(int\)既存のワークシートをコピーするために使用されるメソッド。メソッドの 1 つのバージョンは、ソース ワークシートのインデックスをパラメーターとして受け取ります。もう一方のバージョンは、ソース ワークシートの名前を取ります。

次の例は、ブック内の既存のワークシートをコピーする方法を示しています。



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-CopyWithinWorkbook.py" >}}
### **ワークブック間でワークシートをコピーする**
Aspose.Cells は[Worksheet.copy()](https://reference.aspose.com/cells/python/asposecells.api/worksheet#copy\(com.aspose.cells.Worksheet\)) ワークシートを他のワークブックにコピーするために使用されるメソッド。このメソッドは、ソース ワークシート オブジェクトをパラメーターとして受け取ります。

次の例は、あるブックから別のブックにワークシートをコピーする方法を示しています。



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-CopyWorksheetsBetweenWorkbooks.py" >}}
### **ワークブック内でワークシートを移動する**
Aspose.Cells は[Worksheet.moveTo()](https://reference.aspose.com/cells/python/asposecells.api/worksheet#moveTo\(int\)) メソッドを使用して、ワークシートを同じスプレッドシート内の別の場所に移動します。

次の例は、ワークシートをブック内の別の場所に移動する方法を示しています。



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-MoveWorksheet.py" >}}
