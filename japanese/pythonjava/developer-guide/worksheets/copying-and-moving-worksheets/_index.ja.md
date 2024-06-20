---
title: ワークシートのコピーと移動
type: docs
weight: 20
url: /ja/python-java/copying-and-moving-worksheets/
---

{{% alert color="primary" %}} 

時には、共通のフォーマットとデータを持つワークシートの数が必要です。たとえば、四半期予算で作業する場合、同じ列見出し、行見出し、数式を含むシートを持つワークブックを作成したいと思うかもしれません。これを行う方法があります：1つのシートを作成してからコピーすることです。

Aspose.Cellsは、ワークブック内またはワークブック間でワークシートをコピーおよび移動する機能をサポートしています。データ、書式、テーブル、行列、グラフ、画像、その他のオブジェクトを含む完全なワークシートが、最高の精度でコピーされます。

{{% /alert %}} 
## **Microsoft Excelでシートを移動またはコピーする**
ワークブックでワークシートをコピーおよび移動する手順は次のとおりです。

1. シートを受け取るワークブックを開きます。
1. 移動またはコピーしたいシートを含むワークブックに切り替え、そのシートを選択します。
1. **編集**メニューで、**シートの移動またはコピー**をクリックします。
1. 別のブックのボックスで、シートを受け取るブックをクリックしてください。
1. 選択したシートを新しいワークブックに移動またはコピーするには、**新しいブック**をクリックします。
1. **シートの前**ボックスで、移動またはコピーされるシートの前にクリックします。
1. 移動ではなくコピーする場合は、**コピーの作成**チェックボックスを選択します。
### **ブック内でのワークシートのコピー**
Aspose.Cellsは、既存のワークシートをコピーするために使用される[WorksheetCollection.addCopy()](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#addCopy\(int\))メソッドのオーバーロードされたバージョンを提供しています。メソッドの1つのバージョンは、ソースワークシートのインデックスをパラメータとして取ります。もう1つのバージョンは、ソースワークシートの名前をパラメータとして取ります。

次の例は、ブック内で既存のワークシートをコピーする方法を示しています。



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-CopyWithinWorkbook.py" >}}
### **ブック間でのワークシートのコピー**
Aspose.Cellsは、ワークシートを他のワークブックにコピーするために使用される[Worksheet.copy()](https://reference.aspose.com/cells/python/asposecells.api/worksheet#copy\(com.aspose.cells.Worksheet\))メソッドを提供しています。このメソッドは、ソースワークシートオブジェクトをパラメータとして取ります。

次の例は、ワークブックから別のワークブックにワークシートをコピーする方法を示しています。



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-CopyWorksheetsBetweenWorkbooks.py" >}}
### **ワークブック内でのワークシートの移動**
Aspose.Cellsは、ワークシートをスプレッドシート内の別の場所に移動するために使用される[Worksheet.moveTo()](https://reference.aspose.com/cells/python/asposecells.api/worksheet#moveTo\(int\))メソッドを提供しています。

次の例は、ワークブック内でワークシートを別の場所に移動する方法を示しています。



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-MoveWorksheet.py" >}}
