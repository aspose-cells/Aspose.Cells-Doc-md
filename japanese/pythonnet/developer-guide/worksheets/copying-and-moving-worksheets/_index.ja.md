---
title: ワークシートのコピーと移動
type: docs
weight: 10
url: /ja/python-net/copying-and-moving-worksheets/
description: この記事にはサンプルコードが含まれており、Aspose.Cells for Python via .NET APIを使ってエクセルブック内および複数のエクセルブック間でワークシートをプログラム的にコピー・移動する方法を説明しています。
keywords: Python Excelライブラリ、Pythonコピーシート、Python移動シート、Pythonワークブック間のシートコピー、Pythonワークブック内のシート移動、Pythonワークブック間のシートコピー、Pythonワークブック内のシートコピー。
---

{{% alert color="primary" %}}

時には、共通のフォーマットとデータを持つワークシートの数が必要です。たとえば、四半期予算で作業する場合、同じ列見出し、行見出し、数式を含むシートを持つワークブックを作成したいと思うかもしれません。これを行う方法があります：1つのシートを作成してからコピーすることです。

Aspose.Cells for Python via .NETは、ワークブック内または間でシートをコピー・移動することをサポートします。シート、データ、書式設定、テーブル、マトリックス、チャート、画像、その他のオブジェクトを、最大限の精度でコピーします。

{{% /alert %}}

## **Microsoft Excelを使用してシートを移動またはコピーする方法**

Microsoft Excelでワークブック内またはワークブック間でワークシートをコピーおよび移動する手順は次のとおりです。

1. 別のワークブックにシートを移動またはコピーするには、シートを受け取るワークブックを開きます。
1. 移動またはコピーしたいシートを含むワークブックに切り替え、そのシートを選択します。
1. **編集**メニューで**シートの移動またはコピー**をクリックします。
1. **ブックへ**ダイアログボックスで、シートを受け取るワークブックをクリックします。
1. 選択したシートを新しいワークブックに移動またはコピーするには、**新しいブック**をクリックします。
1. **前のシート**ボックスで、移動またはコピーされたシートが挿入される前のシートをクリックします。
1. 移動ではなくシートをコピーする場合は、**コピーを作成**チェックボックスを選択します。

## **Aspose.Cells for Python via .NETを使用してワークブック内でシートをコピーする方法**

Pyhton用Aspose.Cells via .NETは、コレクションにワークシートを追加し、既存のワークシートからデータをコピーするために使用されるオーバーロードされたメソッド[**Aspose.Cells.WorksheetCollection.add_copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/add_copy/#str)を提供します。 このメソッドの一つのバージョンは、ソースワークシートのインデックスをパラメータとして受け取ります。もう一つのバージョンは、ソースワークシートの名前を受け取ります。

次の例は、ブック内で既存のワークシートをコピーする方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-CopyWithinWorkbook-1.py" >}}

## **ワークブック間でワークシートをコピーする方法**

Pyhton用Aspose.Cells via .NETは、ソースワークシートから他のワークシートへデータと書式設定をコピーするためのメソッド[**Aspose.Cells.Worksheet.copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/copy/#aspose.cells.Worksheet)を提供します。このメソッドは、ソースワークシートのオブジェクトをパラメータとして受け取ります。

次の例は、ワークブックから別のワークブックにワークシートをコピーする方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-CopyWorksheetsBetweenWorkbooks-1.py" >}}

次の例は、ワークブックから別のワークブックにワークシートをコピーする方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-CopyWorksheetFromWorkbookToOther-1.py" >}}

## **ワークブック内でワークシートを移動する方法**

Pyhton用Aspose.Cells via .NETは、同じスプレッドシート内でワークシートを別の場所に移動させるために使用される[**Aspose.Cells.Worksheet.move_to()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/move_to/#int)メソッドを提供します。このメソッドは、ターゲットワークシートのインデックスをパラメータとして受け取ります。

次の例は、ワークブック内でワークシートを別の場所に移動する方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-MoveWorksheet-1.py" >}}
