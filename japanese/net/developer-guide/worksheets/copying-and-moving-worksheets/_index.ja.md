---
title: ワークシートのコピーと移動
type: docs
weight: 10
url: /ja/net/copying-and-moving-worksheets/
description: この記事には、C# APIまたは.NETライブラリを使用して、Excelワークブック内およびワークブック間でプログラムでワークシートをコピーおよび移動する方法についてのサンプルコードと説明が含まれています。
keywords: ワークシートのコピーC#、ワークシートの移動C#
---

{{% alert color="primary" %}}

時には、共通のフォーマットとデータを持つワークシートの数が必要です。たとえば、四半期予算で作業する場合、同じ列見出し、行見出し、数式を含むシートを持つワークブックを作成したいと思うかもしれません。これを行う方法があります：1つのシートを作成してからコピーすることです。

Aspose.Cellsは、ブック内またはブック間でのワークシートのコピーおよび移動をサポートしています。データ、書式、テーブル、行列、チャート、画像、その他のオブジェクトが完全な状態でコピーされます。

{{% /alert %}}

## **Microsoft Excelでシートを移動またはコピーする**

Microsoft Excelでワークブック内またはワークブック間でワークシートをコピーおよび移動する手順は次のとおりです。

1. 別のワークブックにシートを移動またはコピーするには、シートを受け取るワークブックを開きます。
1. 移動またはコピーしたいシートを含むワークブックに切り替え、そのシートを選択します。
1. **編集**メニューで**シートの移動またはコピー**をクリックします。
1. **ブックへ**ダイアログボックスで、シートを受け取るワークブックをクリックします。
1. 選択したシートを新しいワークブックに移動またはコピーするには、**新しいブック**をクリックします。
1. **前のシート**ボックスで、移動またはコピーされたシートが挿入される前のシートをクリックします。
1. 移動ではなくシートをコピーする場合は、**コピーを作成**チェックボックスを選択します。

### **Aspose.Cellsを使用してワークブック内でワークシートをコピーする**

Aspose.Cellsは[**Aspose.Cells.WorksheetCollection.AddCopy()**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/addcopy/index)というオーバーロードされたメソッドを提供し、これはコレクションにワークシートを追加し、既存のワークシートからデータをコピーするために使用されます。メソッドの1つのバージョンは、ソースワークシートのインデックスをパラメーターとして取ります。もう1つのバージョンは、ソースワークシートの名前をパラメーターとして取ります。

次の例は、ブック内で既存のワークシートをコピーする方法を示しています。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-CopyWithinWorkbook-1.cs" >}}

### **ブック間でのワークシートのコピー**

Aspose.Cellsは、指定のワークシートからデータおよび書式を別のワークブック内または間の別のワークシートにコピーするために使用されるメソッド[**Aspose.Cells.Worksheet.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/copy/index)を提供します。このメソッドは、ソースワークシートオブジェクトをパラメータとして受け取ります。

次の例は、ワークブックから別のワークブックにワークシートをコピーする方法を示しています。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-CopyWorksheetsBetweenWorkbooks-1.cs" >}}

次の例は、ワークブックから別のワークブックにワークシートをコピーする方法を示しています。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-CopyWorksheetFromWorkbookToOther-1.cs" >}}

### **ワークブック内でのワークシートの移動**

Aspose.Cellsは、スプレッドシート内の別の場所にワークシートを移動するために使用されるメソッド[**Aspose.Cells.Worksheet.MoveTo()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/moveto)を提供します。このメソッドは、移動先のワークシートインデックスをパラメータとして受け取ります。

次の例は、ワークブック内でワークシートを別の場所に移動する方法を示しています。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-MoveWorksheet-1.cs" >}}
