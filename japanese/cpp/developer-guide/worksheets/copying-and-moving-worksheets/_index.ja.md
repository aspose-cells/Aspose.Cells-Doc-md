---
title: ワークシートのコピーと移動
type: docs
weight: 10
url: /ja/cpp/copying-and-moving-worksheets/
---
{{% alert color="primary" %}} 

場合によっては、共通の書式設定とデータを含む多数のワークシートが必要になることがあります。たとえば、四半期の予算を扱う場合は、同じ列見出し、行見出し、および数式を含むシートを含むワークブックを作成するとよいでしょう。これを行うには、シートを 1 つ作成してコピーするという方法があります。

Aspose.Cells は、ワークブック内またはワークブック間でのワークシートのコピーと移動をサポートしています。データ、書式設定、表、行列、グラフ、画像、その他のオブジェクトを備えたワークシートが、最高の精度でコピーされます。

{{% /alert %}} 
##  **Microsoft Excel を使用してシートを移動またはコピーする**
Microsoft Excel でワークブック内またはワークブック間でワークシートをコピーおよび移動する手順は次のとおりです。

1. シートを別のワークブックに移動またはコピーするには、シートを受け取るワークブックを開きます。
1. 移動またはコピーするシートを含むブックに切り替えて、シートを選択します。
1. で**編集**メニューで、*シートの移動またはコピー** をクリックします。
1. の中に**予約する**ダイアログで、ワークブックをクリックしてシートを受け取ります。
1. 選択したシートを新しいワークブックに移動またはコピーするには、*新しいブック** をクリックします。
1. の中に**ビフォーシート**ボックスで、移動またはコピーしたシートを挿入する前にあるシートをクリックします。
1. シートを移動する代わりにコピーするには、**コピーを作成する**チェックボックス。
###  **Aspose.Cells を使用してワークブック内のワークシートをコピーする**
Aspose.Cells はオーバーロードされたメソッドを提供します[AddCopy()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/addcopy/)これは、ワークシートをコレクションに追加し、既存のワークシートからデータをコピーするために使用されます。メソッドの 1 つのバージョンは、ソース ワークシートのインデックスをパラメータとして受け取ります。もう 1 つのバージョンでは、ソース ワークシートの名前が使用されます。次の例は、ワークブック内の既存のワークシートをコピーする方法を示しています。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-CopyingAndMovingWorksheets-CopyWorksheetsWithinWorkbook-new.cpp" >}}
###  **ワークブック内でワークシートを移動する**
Aspose.Cells が方法を提供します[MoveTo()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/moveto/)これは、ワークシートを同じスプレッドシート内の別の場所に移動するために使用されます。このメソッドはターゲット ワークシート インデックスをパラメータとして受け取ります。次の例は、ワークシートをワークブック内の別の場所に移動する方法を示しています。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-CopyingAndMovingWorksheets-MoveWorksheetsWithinWorkbook-new.cpp" >}}
