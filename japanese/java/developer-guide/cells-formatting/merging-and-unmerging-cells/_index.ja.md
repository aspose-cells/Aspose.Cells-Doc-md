---
title: セルの結合と解除
type: docs
weight: 140
url: /ja/java/merging-and-unmerging-cells/
---

{{% alert color="primary" %}}

すべての行や列に常に同じ数のセルを必要とするわけではありません。 たとえば、複数の列にまたがるタイトルを配置したい場合や、請求書を作成する場合には、合計用の少ない列を使用したい場合があります。 2つ以上のセルを1つのセルに結合して、それらをマージします。 Microsoft Excelを使用して、ユーザーはセルを選択してマージし、スプレッドシートを自分の希望の形に整理することができます。

**Microsoft Excelで選択されたセル範囲をマージしてから分割することで、左側のセルと同じ形式のセルになった結果** 

![todo:image_alt_text](merging-and-unmerging-cells_1.png)

Aspose.Cellsはこの機能をサポートし、ワークシートでセルを結合することもできます。 また、結合されたセルを分割することもできます。 結合されたセルのセルの参照は、元の選択範囲の左上のセルの参照です。

セルがマージされると、データは左上のセルにしか保持されません。 範囲内の他のセルにデータがある場合、そのデータは削除されます。

フォーマットも同様に、参照セルに基づいているため、セルを結合すると、範囲内の左上のセルの書式設定が結合されたセルに適用されます。セルが分割されると、新しいセルは元の書式設定を保持します。

{{% /alert %}}

## **ワークシート内のセルの結合。**

### **Microsoft Excel の使用**

Microsoft Excel を使用してワークシートでセルを結合する手順は以下の通りです。

1. 範囲内で左上のセルにデータをコピーします。
1. 結合したいセルを選択します。
1. 行または列内のセルを結合してセルの内容を中央に配置するには、**書式設定**ツールバーの**結合して中央配置**アイコンをクリックします。

### **Aspose.Cellsの使用**

タスクには [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) クラスに有用なメソッドがいくつかあります。例えば、メソッド [**merge()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#merge-int-int-int-int-) は、セルを特定のセル範囲内の単一のセルに結合します。

以下のコードを実行した後に生成される出力は次のとおりです。

**セル (C6:E7) が結合されました** 

![todo:image_alt_text](merging-and-unmerging-cells_2.png)

#### **コード例**

以下の例は、ワークシート内のセル(C6:E7)を結合する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MergingCellsInWorksheet-MergingCellsInWorksheet.java" >}}

## **結合されたセルの結合解除（分割）**

### **Microsoft Excel の使用**

以下の手順では、Microsoft Excelを使用して結合されたセルを分割する方法について説明します。

1. 結合されたセルを選択します。 
   セルが結合されている場合、**結合して中央配置**が**書式設定**ツールバーで選択されます。
1. **書式設定**ツールバーで**結合して中央配置**をクリックします。

#### **Aspose.Cellsの使用**

[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) クラス には、結合されたセルの参照を使用してセルを元の状態に戻すメソッド [**unMerge()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unMerge-int-int-int-int-) があります。このメソッドは、結合されたセル範囲内のセルを分割します。

#### **コード例**

以下の例は、結合されたセル(C6)を分割する方法を示しています。 この例では、前の例で作成されたファイルを使用し、結合されたセルを分割しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UnMergingCellsInWorksheet-UnMergingCellsInWorksheet.java" >}}

## **関連記事**

- [ワークシート内で結合されたセルを見つけて分割する](/cells/ja/java/detect-merged-cells-in-a-worksheet/)
- [Range.merge() および Range.unMerge() メソッドを使用してセル範囲の結合と分割](/cells/ja/java/merge-or-unmerge-range-of-cells/)

{{< app/cells/assistant language="java" >}}
