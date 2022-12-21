---
title: 名前付き範囲
type: docs
weight: 40
url: /ja/java/named-ranges/
---
{{% alert color="primary" %}} 

通常、列と行のラベルは、個々のセルを参照するために使用されます。セル、セルの範囲、数式、または定数値を表すわかりやすい名前を作成できます。言葉**名前**セル、セル範囲、数式、または定数値を表す文字列を参照できます。範囲に名前を割り当てるということは、そのセル範囲をその名前で参照できることを意味します。 Sales!C20:C30 などのわかりにくい範囲を参照するには、Products などのわかりやすい名前を使用します。ラベルは、同じワークシートのデータを参照する数式で使用できます。別のワークシートで範囲を表したい場合は、名前を使用できます。 *名前付き範囲は、Microsoft Excel の最も強力な機能の 1 つであり、特にリスト コントロール、ピボット テーブル、グラフなどのソース範囲として使用される場合に有効です。

{{% /alert %}} 
## **名前付き範囲の作成**
### **Microsoft エクセルを使う**
次の手順では、Microsoft Excel を使用してセルまたはセル範囲に名前を付ける方法について説明します。この方法は、Microsoft Office Excel 2003、Microsoft Excel 97、2000、および 2002 に適用されます。

1. 名前を付けるセル、セル範囲を選択します。
1. 数式バーの左端にある名前ボックスをクリックします。
1. セルの名前を入力します。
1. ENTER を押します。

{{% alert color="primary" %}} 

セルの内容を変更している間は、セルに名前を付けることはできません。

{{% /alert %}} 
### **Aspose.Cells を使用**
ここでは、Aspose.Cells API を使用してタスクを実行します。

Aspose.Cells はクラスを提供し、[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)、Microsoft Excel ファイルを表します。の[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスには[ワークシート コレクション](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)これにより、Excel ファイル内の各ワークシートにアクセスできます。ワークシートは、[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラス。の[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスは[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクション。

オーバーロードされたを呼び出すことで、名前付き範囲を作成できます[createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(java.lang.String,%20java.lang.String\) ) の方法[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクション。の典型的なバージョン[createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(java.lang.String,%20java.lang.String\)メソッドは、次のパラメーターを取ります。

- 左上のセルの名前、範囲内の左上のセルの名前。
- 右下のセルの名前、範囲内の右下のセルの名前。

とき[createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(java.lang.String,%20java.lang.String\) メソッドが呼び出されると、新しく作成された名前付き範囲が のインスタンスとして返されます。[範囲](https://reference.aspose.com/cells/java/com.aspose.cells/range)クラス。

次の例は、B4:G14 を超えるセルの名前付き範囲を作成する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CreateNamedRangeofCells-CreateNamedRangeofCells.java" >}}
#### **スプレッドシート内のすべての名前付き範囲へのアクセス**
電話する[getNamedRanges](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getNamedRanges\(\) ) の方法[ワークシート コレクション](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)スプレッドシート内のすべての名前付き範囲を取得します。の[getNamedRanges](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getNamedRanges\(\) メソッドは、[ワークシート コレクション](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection).

次の例は、ブック内のすべての名前付き範囲にアクセスする方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessAllNamedRanges-AccessAllNamedRanges.java" >}}
#### **特定の名前付き範囲へのアクセス**
電話する[ワークシート コレクション](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)コレクションの[getRangeByName](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getRangeByName\(java.lang.String\) ) メソッドを使用して、指定された範囲を名前で取得します。典型的な[getRangeByName](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getRangeByName\(java.lang.String\) メソッドは名前付き範囲の名前を受け取り、指定された名前付き範囲を[範囲](https://reference.aspose.com/cells/java/com.aspose.cells/range)クラス。

次の例は、指定された範囲に名前でアクセスする方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessSpecificNamedRange-AccessSpecificNamedRange.java" >}}
#### **名前付き範囲で Cells を特定する**
Aspose.Cells を使用すると、範囲の個々のセルにデータを挿入できます。セルの名前付き範囲、つまり A1:C4 があるとします。したがって、マトリックスは 4 * 3 = 12 個のセルを作成し、個々の範囲セルは順番に配置されます。 Aspose.Cells は、範囲内の個々のセルにアクセスするための [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) クラスの便利なプロパティを提供します。範囲内のセルを識別するには、次の方法を使用できます。

- [getFirstRow](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstRow)名前付き範囲の最初の行のインデックスを返します。
- [getFirstColumn](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstColumn)名前付き範囲の最初の列のインデックスを返します。

次の例は、指定した範囲のセルに値を入力する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-IdentifyCellsinNamedRange-IdentifyCellsinNamedRange.java" >}}
#### **名前付き範囲の Cells にデータを入力します**
Aspose.Cells を使用すると、範囲の個々のセルにデータを挿入できます。 H1:J4 などの名前付きセル範囲があるとします。したがって、マトリックスは 4 * 3 = 12 個のセルを作成し、個々の範囲セルは順番に配置されます。 Aspose.Cells は、範囲内の個々のセルにアクセスするための [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) クラスの便利なプロパティを提供します。次のプロパティを使用して、範囲内のセルを識別できます。

- [getFirstRow](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstRow)名前付き範囲の最初の行のインデックスを返します。
- [getFirstColumn](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstColumn)名前付き範囲の最初の列のインデックスを返します。

次の例は、指定した範囲のセルに値を入力する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-InputDataInCellsInRange-InputDataInCellsInRange.java" >}}
#### **範囲の書式設定...名前付き範囲への背景色とフォント属性の設定**
フォーマットを適用するには、[スタイル](https://reference.aspose.com/cells/java/com.aspose.cells/style)スタイル設定を指定して適用するオブジェクト[範囲](https://reference.aspose.com/cells/java/com.aspose.cells/range)物体。

次の例は、フォント設定で塗りつぶしの単色 (シェーディング カラー) を範囲に設定する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormatRanges1-FormatRanges1.java" >}}
#### **範囲の書式設定...名前付き範囲に境界線を追加する**
 つのセルだけでなく、セル範囲に罫線を追加することもできます。の[範囲](https://reference.aspose.com/cells/java/com.aspose.cells/range)オブジェクトは[setOutlineBorders](https://reference.aspose.com/cells/java/com.aspose.cells/range#setOutlineBorders\(int,%20com.aspose.cells.Color\)メソッドは、次のパラメーターを使用して、セル範囲に境界線を追加します。

-  borderStyle: から選択された境界線のタイプ[CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType)列挙。
- borderColor: から選択された境界線の線の色[色](https://reference.aspose.com/cells/java/com.aspose.cells/Color)列挙。

次の例は、アウトラインの境界線を範囲に設定する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormatRanges2-FormatRanges2.java" >}}


上記のコードを実行すると、次の出力が生成されます。

![todo:画像_代替_文章](named-ranges_1.png)
#### **範囲内のセルにスタイルを適用する**
セルにスタイルを適用したい場合があります。[範囲](https://reference.aspose.com/cells/java/com.aspose.cells/range) .このために、範囲内のセルを反復処理して、[Cell.setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\)) メソッドを使用してセルにスタイルを適用します。

次の例は、Range 内のセルにスタイルを適用する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ConvertCellsAddresstoRangeorCellArea-ConvertCellsAddresstoRangeorCellArea.java" >}}
#### **名前付き範囲を削除する**
Aspose.Cells は[NameCollection.RemoveAt()](https://reference.aspose.com/cells/java/com.aspose.cells/namecollection#removeAt\(int\) ) メソッドを使用して、範囲の名前を消去します。範囲の内容をクリアするには、次を使用します[Cells.ClearRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#clearRange\(com.aspose.cells.CellArea\)） 方法。
次の例は、名前付き範囲とその内容を削除する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-RemoveANamedRange-RemoveANamedRange.java" >}}


ボーダーカラー
