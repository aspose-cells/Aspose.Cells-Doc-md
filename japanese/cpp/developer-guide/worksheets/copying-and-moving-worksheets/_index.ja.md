---
title: ワークシートのコピーと移動
type: docs
weight: 10
url: /ja/cpp/copying-and-moving-worksheets/
---

{{% alert color="primary" %}} 

時には、共通のフォーマットとデータを持つワークシートの数が必要です。たとえば、四半期予算で作業する場合、同じ列見出し、行見出し、数式を含むシートを持つワークブックを作成したいと思うかもしれません。これを行う方法があります：1つのシートを作成してからコピーすることです。

Aspose.Cellsは、ワークブック内またはワークブック間でのワークシートのコピーと移動をサポートしています。データ、フォーマット、テーブル、行列、チャート、画像、その他のオブジェクトを含むワークシートは、高い精度でコピーされます。

{{% /alert %}} 
## **Microsoft Excelでシートを移動またはコピーする**
Microsoft Excelのワークブック内またはワークブック間でのワークシートのコピーと移動に関わる手順は次のとおりです。

1. 別のワークブックにシートを移動またはコピーするには、シートを受け取るワークブックを開きます。
1. 移動またはコピーしたいシートを含むワークブックに切り替え、そのシートを選択します。
1. **編集**メニューで**シートの移動またはコピー**をクリックします。
1. **ブックへ**ダイアログボックスで、シートを受け取るワークブックをクリックします。
1. 選択したシートを新しいワークブックに移動またはコピーするには、**新しいブック**をクリックします。
1. **前のシート**ボックスで、移動またはコピーされたシートが挿入される前のシートをクリックします。
1. 移動ではなくシートをコピーする場合は、**コピーを作成**チェックボックスを選択します。
### **Aspose.Cellsを使用してワークブック内でワークシートをコピーする**
Aspose.Cellsは、[AddCopy()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/addcopy/) というオーバーロードされたメソッドを提供しており、これを使用してワークシートをコレクションに追加し、既存のワークシートからデータをコピーします。このメソッドの1つのバージョンは、ソースワークシートのインデックスをパラメーターとして取ります。もう1つのバージョンは、ソースワークシートの名前を取ります。次の例では、ワークブック内で既存のワークシートをコピーする方法が示されています。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-CopyingAndMovingWorksheets-CopyWorksheetsWithinWorkbook-new.cpp" >}}
### **ワークブック内でのワークシートの移動**
Aspose.Cellsは、[MoveTo()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/moveto/) というメソッドを提供しており、これを使用してワークブック内でワークシートを別の位置に移動できます。このメソッドは対象のワークシートのインデックスをパラメーターとして取ります。次の例では、ワークブック内でワークシートを別の位置に移動する方法が示されています。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-CopyingAndMovingWorksheets-MoveWorksheetsWithinWorkbook-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
