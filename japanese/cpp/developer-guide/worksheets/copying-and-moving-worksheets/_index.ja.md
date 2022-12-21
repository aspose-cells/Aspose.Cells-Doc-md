---
title: ワークシートのコピーと移動
type: docs
weight: 10
url: /ja/cpp/copying-and-moving-worksheets/
---
{{% alert color="primary" %}} 

場合によっては、共通の書式設定とデータを含む多数のワークシートが必要になることがあります。たとえば、四半期ごとの予算を扱う場合、同じ列見出し、行見出し、および数式を含むシートを含むワークブックを作成できます。これを行う方法があります: 1 つのシートを作成し、それをコピーします。

Aspose.Cells は、ワークブック内またはワークブック間でのワークシートのコピーと移動をサポートしています。データ、書式設定、テーブル、マトリックス、グラフ、画像、その他のオブジェクトを含むワークシートは、最高の精度でコピーされます。

{{% /alert %}} 
## **Microsoft Excel を使用したシートの移動またはコピー**
Microsoft Excel でワークブック内またはワークブック間でワークシートをコピーおよび移動する手順は次のとおりです。

1. シートを別のブックに移動またはコピーするには、シートを受け取るブックを開きます。
1. 移動またはコピーするシートを含むブックに切り替えてから、シートを選択します。
1. 上で**編集**メニュー、クリック**シートの移動またはコピー**.
1. の中に**予約する**ダイアログで、ワークブックをクリックしてシートを受け取ります。
1. 選択したシートを新しいワークブックに移動またはコピーするには、**新しい本**.
1. の中に**シート前**ボックスで、移動またはコピーしたシートを挿入する前のシートをクリックします。
1. シートを移動する代わりにコピーするには、**コピーを作成する**チェックボックス。
### **Aspose.Cells のワークブック内でワークシートをコピーする**
Aspose.Cells はオーバーロードされたメソッドを提供します[AddCopy()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection#aa1e73c54ea19bb7aa0f9f197c2baa5ba)ワークシートをコレクションに追加し、既存のワークシートからデータをコピーするために使用されます。メソッドの 1 つのバージョンは、ソース ワークシートのインデックスをパラメーターとして受け取ります。もう一方のバージョンは、ソース ワークシートの名前を取ります。次の例は、ブック内の既存のワークシートをコピーする方法を示しています。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-CopyingAndMovingWorksheets-CopyWorksheetsWithinWorkbook.cpp" >}}
### **ワークブック内でワークシートを移動する**
Aspose.Cells はメソッドを提供します[へ引っ越す（）](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a240bf1d3d52ea8c8bfd54ffa320921b7)ワークシートを同じスプレッドシート内の別の場所に移動するために使用されます。このメソッドは、対象のワークシート インデックスをパラメーターとして受け取ります。次の例は、ワークシートをブック内の別の場所に移動する方法を示しています。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-CopyingAndMovingWorksheets-MoveWorksheetsWithinWorkbook.cpp" >}}
