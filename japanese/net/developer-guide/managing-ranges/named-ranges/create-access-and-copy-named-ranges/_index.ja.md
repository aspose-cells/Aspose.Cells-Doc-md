---
title: アクセスの作成と名前付き範囲のコピー
type: docs
weight: 200
url: /ja/net/create-access-and-copy-named-ranges/
---
## **序章**

通常、列と行のラベルは個々のセルを参照して使用されます。セル、セルの範囲、数式、または定数値を表すわかりやすい名前を作成できます。言葉**名前**セル、セル範囲、数式、または定数値を表す文字列を参照できます。範囲に名前を割り当てるということは、そのセル範囲をその名前で参照できることを意味します。 Sales!C20:C30 などのわかりにくい範囲を参照するには、Products などのわかりやすい名前を使用します。ラベルは、同じワークシートのデータを参照する数式で使用できます。別のワークシートで範囲を表したい場合は、名前を使用できます。 *名前付き範囲は、Microsoft Excel の最も強力な機能の 1 つであり、特にリスト コントロール、ピボット テーブル、グラフなどのソース範囲として使用される場合に有効です。

## **Microsoft Excel を使用した名前付き範囲の操作**

### **名前付き範囲の作成**

次の手順では、セルまたはセル範囲に名前を付ける方法について説明します。**MS エクセル**.この方法が適用されるのは**Microsoft オフィス エクセル 2003**, **Microsoft エクセル97**, **2000**と**2002**.

1. 名前を付けるセル、セル範囲を選択します。
1. クリック**ネームボックス**数式バーの左端にあります。
1. セルの名前を入力します。
1. ENTER を押します。

{{% alert color="primary" %}}

セルの内容を変更している間は、セルに名前を付けることはできません。

{{% /alert %}}

## **Aspose.Cells を使用した名前付き範囲の操作**

ここでは、Aspose.Cells API を使用してタスクを実行します。
Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Excel ファイル内の各ワークシートにアクセスできるコレクション。ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスは[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクション。

### **名前付き範囲の作成**

オーバーロードされたを呼び出すことで、名前付き範囲を作成できます[**作成範囲**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index)の方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクション。の典型的なバージョン[**作成範囲**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/3)メソッドは次のパラメータを取ります。

- 左上のセルの名前、範囲内の左上のセルの名前。
- 右下のセルの名前、範囲内の右下のセルの名前。

とき[**作成範囲**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/3)メソッドが呼び出されると、新しく作成された範囲を[**範囲**](https://reference.aspose.com/cells/net/aspose.cells/range)クラス。これを使って[**範囲**](https://reference.aspose.com/cells/net/aspose.cells/range)名前付き範囲を構成するオブジェクト。たとえば、次を使用して範囲の名前を設定します。[**名前**](https://reference.aspose.com/cells/net/aspose.cells/range/properties/name)財産。次の例は、B4:G14 を超えるセルの名前付き範囲を作成する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CreateNamedRangeofCells-1.cs" >}}

### **名前付き範囲の Cells にデータを入力します**

パターンに従って範囲の個々のセルにデータを挿入できます

- **C#**範囲[行,列]
- **VB**: 範囲(行、列)

A1:C4 にまたがる名前付きセル範囲があるとします。行列は 4 * 3 = 12 個のセルを作成します。個々の範囲セルは順番に配置されます: Range[0,0]、Range[0,1]、Range[0,2]、Range[1,0]、Range[1,1]、Range[1,2]、範囲[2,0]、範囲[2,1]、範囲[2,2]、範囲[3,0]、範囲[3,1]、範囲[3,2]。

次のプロパティを使用して、範囲内のセルを識別します。

- FirstRow は、名前付き範囲の最初の行のインデックスを返します。
- FirstColumn は、名前付き範囲の最初の列のインデックスを返します。
- RowCount は、指定された範囲内の行の総数を返します。
- ColumnCount は、名前付き範囲内の列の総数を返します。

次の例は、指定した範囲のセルに値を入力する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-InputDataInCellsInRange-1.cs" >}}

### **名前付き範囲で Cells を特定します**

パターンに従って、範囲の個々のセルにデータを挿入できます。

- **C#**範囲[行,列]
- **VB**: 範囲(行、列)

A1:C4 にまたがる名前付き範囲がある場合。行列は 4 * 3 = 12 個のセルを作成します。個々の範囲セルは順番に配置されます: Range[0,0]、Range[0,1]、Range[0,2]、Range[1,0]、Range[1,1]、Range[1,2]、範囲[2,0]、範囲[2,1]、範囲[2,2]、範囲[3,0]、範囲[3,1]、範囲[3,2]。

次のプロパティを使用して、範囲内のセルを識別します。

- FirstRow は、名前付き範囲の最初の行のインデックスを返します。
- FirstColumn は、名前付き範囲の最初の列のインデックスを返します。
- RowCount は、指定された範囲内の行の総数を返します。
- ColumnCount は、名前付き範囲内の列の総数を返します。

次の例は、指定した範囲のセルに値を入力する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-IdentifyCellsinNamedRange-1.cs" >}}

### **名前付き範囲へのアクセス**

#### **特定の名前付き範囲へのアクセス**

電話する[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)コレクションの[**GetRangeByName**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getrangebyname)指定した名前で範囲を取得するメソッド。典型的な[**GetRangeByName**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getrangebyname)メソッドは名前付き範囲の名前を受け取り、指定された名前付き範囲を[**範囲**](https://reference.aspose.com/cells/net/aspose.cells/range)クラス。次の例は、指定された範囲に名前でアクセスする方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-AccessSpecificNamedRange-1.cs" >}}

#### **スプレッドシート内のすべての名前付き範囲へのアクセス**

電話する[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)コレクションの[**GetNamedRanges**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getnamedranges)メソッドを使用して、スプレッドシート内のすべての名前付き範囲を取得します。の[**GetNamedRanges**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getnamedranges)メソッドは、すべての名前範囲の配列を返します[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)コレクション。

次の例は、ブック内のすべての名前付き範囲にアクセスする方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-AccessAllNamedRanges-1.cs" >}}

### **名前付き範囲をコピー**

Aspose.Cells提供[**範囲.コピー()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/copy/index)書式設定されたセルの範囲を別の範囲にコピーするメソッド。

次の例は、セルのソース範囲を別の名前付き範囲にコピーする方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CopyNamedRanges-1.cs" >}}
