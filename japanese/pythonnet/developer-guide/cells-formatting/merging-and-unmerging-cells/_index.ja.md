---
title: セルの結合と解除
description: Aspose.Cellsは、セルの結合と解除をサポートするPythonライブラリです。この資料では、Aspose.Cells for Python via .NETライブラリを使用したセルの結合と解除方法、および結合セルのスタイルのカスタマイズ方法について紹介します。
keywords: Aspose.Cells for Python via .NET、.NETライブラリ、スプレッドシート、セルの結合と分割、スタイル設定、カスタムスタイル
type: docs
weight: 190
url: /ja/python-net/merging-and-unmerging-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells for Python via .NETはこの機能をサポートし、ワークシート内のセルを結合することも可能です。結合解除や分割も行えます。結合されたセルのセル参照は、元の選択範囲の左上セルの参照です。

{{% /alert %}} 
## **紹介**
すべての行や列に常に同じ数のセルを必ずしも欲しいわけではありません。 たとえば、複数の列にまたがるタイトルを置きたい場合があります。 または、請求書を作成する場合、合計に対して少ない列を望むことがあります。 セルを1つに結合してみてください。 Microsoft Excelは、ユーザーがファイルを選択して自分の望むようにスプレッドシートの構造を結合できます。

{{% alert color="primary" %}} 

セルを結合すると、結合範囲の左上のセルのデータのみが保持されます。 範囲内の他のセルにデータがある場合、このデータは削除されます。
同様に、書式設定は結合されたセルに適用される範囲の左上のセルに基づいており、セルを結合すると、結合されたセルに元の書式設定が適用されます。 セルが分割されると、新しいセルは元の書式設定を維持します。

{{% /alert %}} 
## **ワークシート内でセルを結合する**
### **Microsoft Excelでセルを結合する**
以下の手順では、MS Excelを使用してワークシート内のセルを結合する方法について説明します。

1. 範囲内で左上のセルにデータをコピーします。
1. 結合したいセルを選択します。
1. 行または列内のセルを結合してセルの内容を中央に配置するには、**書式設定**ツールバーの**結合して中央配置**アイコンをクリックします。

### **Aspose.Cells for Python via .NETを使ったセルの結合**
Aspose.Cells.Cellsクラスには、そのようなタスクに便利なメソッドがいくつかあります。 たとえば、メソッドMerge()は指定された範囲内でセルを1つのセルに結合します。

以下の例は、ワークシート内のセル(C6:E7)を結合する方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-MergingCellsInWorksheet.-1.py" >}}

## **結合されたセルの結合解除（分割）**
### **Microsoft Excel の使用**
以下の手順では、Microsoft Excelを使用して結合されたセルを分割する方法について説明します。

1. 結合されたセルを選択します。セルが結合されている場合、**整列して中央揃え**が**書式設定**ツールバーで選択されます。
1. **書式設定**ツールバーで**結合して中央配置**をクリックします。

### **Aspose.Cells for Python via .NETを使用して**
Aspose.Cells.Cellsクラスには、セルの参照を使用して結合されたセルを元の状態に分割するメソッドUnMerge()があります。 このメソッドは、結合されたセルの範囲内のセルの参照を使用してセルを分割します。

以下の例は、結合されたセル(C6)を分割する方法を示しています。 この例では、前の例で作成されたファイルを使用し、結合されたセルを分割しています。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-UnMergingtheMergedCells-1.py" >}}


## **高度なトピック**
- [ワークシート内の結合セルを検出する](/cells/ja/python-net/detect-merged-cells-in-a-worksheet/)

{{< app/cells/assistant language="python-net" >}}
