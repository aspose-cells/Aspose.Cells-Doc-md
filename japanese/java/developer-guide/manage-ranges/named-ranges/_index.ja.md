---
title: 名前付き範囲
type: docs
weight: 40
url: /ja/java/named-ranges/
---

{{% alert color="primary" %}} 

通常、列と行のラベルは個々のセルを参照するために使用されます。セル、セルの範囲、数式、または定数値を表す記述的な名前を作成することができます。 **名前** という言葉は、セル、セルの範囲、数式、または定数値を表す文字列を指すことがあります。 範囲に名前を割り当てることによって、そのセルの範囲はその名前で参照することができます。 Sales!C20:C30 のような理解しにくい範囲を Products のような分かりやすい名前で参照するために使用します。 ラベルは、同じワークシート上のデータを参照する数式で使用できます。別のワークシート上の範囲を表す場合は、名前を使用できます。 *名前付き範囲は、Microsoft Excel の中でも、リストコントロール、ピボットテーブル、チャートなどのソース範囲として使用した場合に特に強力な機能の一つです。

{{% /alert %}} 
## **名前付き範囲の作成**
### **Microsoft Excel の使用**
Microsoft Excel を使用してセルまたはセルの範囲に名前を付ける手順を以下に示します。この方法は、Microsoft Office Excel 2003、Microsoft Excel 97、2000、および2002 に適用されます。

1. 名前を付けたいセル、セルの範囲を選択します。
1. フォーミュラバーの左端にある名前ボックスをクリックします。
1. セルに名前を入力します。
1. ENTER キーを押します。

{{% alert color="primary" %}} 

セルの内容を変更しているときにはセルに名前を付けることはできません。

{{% /alert %}} 
### **Aspose.Cellsの使用**
ここでは、Aspose.Cells API を使用してタスクを実行します。

Aspose.Cells は、Microsoft Excel ファイルを表す [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) クラスを提供します。 [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) クラスには、Excel ファイル内の各ワークシートにアクセスできる [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) を含みます。ワークシートは [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) クラスで表されます。 [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) クラスは [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) コレクションを提供します。

[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) コレクションのオーバーロードされた [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(java.lang.String,%20java.lang.String\)) メソッドを呼び出すことで、名前付き範囲を作成することができます。 [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(java.lang.String,%20java.lang.String\)) メソッドは、一般的なバージョンでは、以下のパラメータを取ります。

- 左上のセルの名前、範囲内の左上のセルの名前。
- 右下のセルの名前、範囲内の右下のセルの名前。

[createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(java.lang.String,%20java.lang.String\)) メソッドを呼び出すと、新しく作成された名前付き範囲が [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) クラスのインスタンスとして返されます。

次の例は、B4:G14 のセルの名前付き範囲を作成する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CreateNamedRangeofCells-CreateNamedRangeofCells.java" >}}
#### **スプレッドシートのすべての名前付き範囲にアクセスする**
[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) の [getNamedRanges](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getNamedRanges\(\)) メソッドを呼び出して、スプレッドシート内のすべての名前付き範囲にアクセスできます。 [getNamedRanges](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getNamedRanges\(\)) メソッドは、[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) 内のすべての名前付き範囲の配列を返します。

次の例は、ワークブック内のすべての名前付き範囲にアクセスする方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessAllNamedRanges-AccessAllNamedRanges.java" >}}
#### **特定の名前付き範囲にアクセスする**
[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) コレクションの [getRangeByName](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getRangeByName\(java.lang.String\)) メソッドを呼び出して、名前で指定した範囲にアクセスできます。 一般的な [getRangeByName](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getRangeByName\(java.lang.String\)) メソッドは、名前付き範囲の名前を取り、それを [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) クラスのインスタンスとして返します。

次の例は、名前で指定した範囲にアクセスする方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessSpecificNamedRange-AccessSpecificNamedRange.java" >}}
#### **名前付き範囲内のセルを識別する**
Aspose.Cells を使用すると、範囲内の個々のセルにデータを挿入することができます。 たとえば、セル A1:C4 の名前付き範囲があるとします。したがって、行列は 4 * 3 = 12 セルを作成し、個々の範囲セルは順番に配置されます。 Aspose.Cells は [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) クラスのいくつかの便利なプロパティを提供し、範囲内の個々のセルにアクセスするためのメソッドを提供します。

- [getFirstRow](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstRow) は、名前付き範囲内の最初の行のインデックスを返します。
- [getFirstColumn](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstColumn) は、名前付き範囲内の最初の列のインデックスを返します。

次の例では、指定された範囲のセルに値を入力する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-IdentifyCellsinNamedRange-IdentifyCellsinNamedRange.java" >}}
#### **名前付き範囲内のセルにデータを入力する**
Aspose.Cells を使用すると、範囲内の個々のセルにデータを挿入することができます。 たとえば、セル H1:J4 の名前付き範囲があるとします。したがって、行列は 4 * 3 = 12 セルを作成し、個々の範囲セルは順番に配置されます。 Aspose.Cells は [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) クラスの有用なプロパティを提供し、範囲内の個々のセルにアクセスするためのメソッドを提供します。

- [getFirstRow](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstRow) は、名前付き範囲内の最初の行のインデックスを返します。
- [getFirstColumn](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstColumn) は、名前付き範囲内の最初の列のインデックスを返します。

次の例では、指定された範囲のセルに値を入力する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-InputDataInCellsInRange-InputDataInCellsInRange.java" >}}
#### **範囲の書式設定...背景色とフォント属性のネームド レンジへの設定**
書式を適用するには、[Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) オブジェクトを定義してスタイル設定を指定し、[Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) オブジェクトに適用します。

次の例では、範囲に固体の塗りつぶし色（網掛け色）とフォント設定を設定する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormatRanges1-FormatRanges1.java" >}}
#### **範囲の書式設定...ネームド レンジにボーダーを追加**
単一のセルではなく、セルの範囲にボーダーを追加することができます。[Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) オブジェクトは、範囲のセルにボーダーを追加するために次のパラメータを取る [setOutlineBorders](https://reference.aspose.com/cells/java/com.aspose.cells/range#setOutlineBorders\(int,%20com.aspose.cells.Color\)) メソッドを提供します。

- borderStyle: ボーダーの種類、[CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType) 列挙型から選択します。
- borderColor: ボーダーの線の色、[Color](https://reference.aspose.com/cells/java/com.aspose.cells/Color) 列挙型から選択します。

次の例では、範囲にアウトラインボーダーを設定する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormatRanges2-FormatRanges2.java" >}}


上記のコードを実行した後の出力は、次のようになります: 

![todo:image_alt_text](named-ranges_1.png)
#### **指定された[Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) のセルにスタイルを適用する**
時には、[Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) のセルにスタイルを適用したいことがあります。その場合、範囲内のセルを反復処理し、[Cell.setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\)) メソッドを使用してセルにスタイルを適用します。

次の例では、[Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) のセルにスタイルを適用する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ConvertCellsAddresstoRangeorCellArea-ConvertCellsAddresstoRangeorCellArea.java" >}}
#### **ネームド レンジの削除**
Aspose.Cellsは、[NameCollection.RemoveAt()](https://reference.aspose.com/cells/java/com.aspose.cells/namecollection#removeAt\(int\)) メソッドを介して、ネームド レンジの名前を削除する機能を提供します。範囲の内容をクリアするには、[Cells.ClearRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#clearRange\(com.aspose.cells.CellArea\)) メソッドを使用します。
次の例では、ネームド レンジとその内容を削除する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-RemoveANamedRange-RemoveANamedRange.java" >}}


borderColors 
