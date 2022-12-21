---
title: マージとアンマージ Cells
type: docs
weight: 140
url: /ja/java/merging-and-unmerging-cells/
---
{{% alert color="primary" %}}

すべての行または列に常に同じ数のセルが必要なわけではありません。たとえば、複数の列にまたがるセルにタイトルを入れたい場合があります。または、請求書を作成する場合は、合計の列を少なくしたい場合があります。 2 つ以上のセルから 1 つのセルを作成するには、それらをマージします。 Microsoft Excel では、ユーザーがセルを選択して結合し、スプレッドシートを自由に構成できます。

**Microsoft Excel の左側のセルとして書式設定されたセルの範囲を結合してから分割した結果** 

![todo:画像_代替_文章](merging-and-unmerging-cells_1.png)

Aspose.Cells はこの機能をサポートしており、ワークシート内のセルを結合することもできます。結合されたセルを結合解除または分割することもできます。結合セルのセル参照は、最初に選択した範囲の左上のセルの参照です。

セルが結合されると、左上のセルのデータのみが保持されることに注意してください。範囲内の他のセルにデータがある場合、そのデータは削除されます。

同様に、書式設定は参照セルに基づいているため、セルを結合すると、範囲内の左上のセルの書式設定が結合されたセルに適用されます。セルが分割されると、新しいセルは元の書式設定を保持します。

{{% /alert %}}

## **ワークシートで Cells をマージします。**

### **Microsoft エクセルを使う**

次の手順では、Microsoft Excel を使用してワークシート内のセルを結合する方法について説明します。

1. 必要なデータを範囲内の左上端のセルにコピーします。
1. 結合するセルを選択します。
1. 行または列のセルを結合してセルの内容を中央に配置するには、**マージして中央揃え**アイコン**書式設定**ツールバー。

### **Aspose.Cells を使用**

の[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)クラスには、タスクに役立つメソッドがいくつかあります。たとえば、メソッド[**マージ（）**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#merge(int,%20int,%20int,%20int)) は、指定されたセル範囲内の単一のセルにセルを結合します。

以下のコードを実行すると、次の出力が生成されます。

**セル (C6:E7) が結合されました** 

![todo:画像_代替_文章](merging-and-unmerging-cells_2.png)

#### **コード例**

次の例は、ワークシートのセル (C6:E7) を結合する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MergingCellsInWorksheet-MergingCellsInWorksheet.java" >}}

## **アンマージ (分割) マージ済み Cells**

### **Microsoft エクセルを使う**

次の手順では、Microsoft Excel を使用して結合セルを分割する方法について説明します。

1. 結合セルを選択します。
セルを結合すると、**マージして中央揃え**で選択されます**書式設定**ツールバー。
1. クリック**マージして中央揃え**上で**書式設定**ツールバー。

#### **Aspose.Cells を使用**

の[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)クラスには次の名前のメソッドがあります[**unMerge()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unMerge(int,%20int,%20int,%20int)) セルを元の状態に分割します。このメソッドは、結合されたセル範囲内のセルの参照を使用して、セルの結合を解除します。

#### **コード例**

次の例は、結合されたセル (C6) を分割する方法を示しています。この例では、前の例で作成したファイルを使用して、結合されたセルを分割します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UnMergingCellsInWorksheet-UnMergingCellsInWorksheet.java" >}}

## **関連記事**

- [結合セルの検索と分割](/cells/ja/java/detect-merged-cells-in-a-worksheet/).
- [Range.merge() および Range.unMerge() メソッドを使用してセル範囲を結合および分割する](/cells/ja/java/merge-or-unmerge-range-of-cells/).

