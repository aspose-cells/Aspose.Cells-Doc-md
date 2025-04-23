---
title: アクセスおよび名前付き範囲のコピーを作成します
type: docs
weight: 200
url: /ja/net/create-access-and-copy-named-ranges/
---

## **紹介**

通常、列や行ラベルは個々のセルを参照するために使用されます。セル、セル範囲、数式、または定数値を表す記述的な名前を作成することが可能です。**名前**という言葉は、セル、セル範囲、数式、または定数値を表す文字列を指すことがあります。範囲に名前を割り当てると、そのセル範囲はその名前で参照することができます。Sales!C20:C30のようなわかりにくい範囲を表すために理解しやすい名前、例えばProductsなどを使用してください。ラベルは、同じワークシート上のデータを参照する数式で使用できます。他のワークシート上の範囲を表す場合は、名前を使用できます。*名前付き範囲* は、特にリストコントロール、ピボットテーブル、チャートなどのソース範囲として使用されたときに、Microsoft Excelの最も強力な機能の一つです。

## **Microsoft Excelを使用した名前付き範囲の操作**

### **名前付き範囲を作成します**

次の手順では、**MS Excel**を使用してセルまたはセル範囲に名前を付ける方法について説明します。この方法は **Microsoft Office Excel 2003**、**Microsoft Excel 97**、**2000** および **2002** に適用されます。

1. 名前を付けたいセル、セルの範囲を選択します。
1. フォーミュラバーの左端にある**名前ボックス**をクリックします。
1. セルに名前を入力します。
1. ENTER キーを押します。

{{% alert color="primary" %}}

セルの内容を変更しているときにはセルに名前を付けることはできません。

{{% /alert %}}

## **Aspose.Cellsを使用した名前付き範囲の操作**

ここでは、Aspose.Cells API を使用してタスクを実行します。
Aspose.Cellsは、Microsoft Excelファイルを表すクラス、[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)を提供しています。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには、Excelファイル内の各ワークシートにアクセスできる[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)コレクションが含まれています。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスには[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクションが提供されています。

### **名前付き範囲の作成**

[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクションのオーバーロードされた[**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index)メソッドを呼び出すことで、名前付き範囲を作成することが可能です。通常、[**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/3)メソッドの一般的なバージョンは、以下のパラメータを取ります:

- 左上のセルの名前、範囲内の左上のセルの名前。
- 右下のセルの名前、範囲内の右下のセルの名前。

[**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/3)メソッドを呼び出すと、[**Range**](https://reference.aspose.com/cells/net/aspose.cells/range)クラスのインスタンスとして新しく作成された範囲が返されます。この[**Range**](https://reference.aspose.com/cells/net/aspose.cells/range)オブジェクトを使用して、名前付き範囲を構成します。たとえば、[**Name**](https://reference.aspose.com/cells/net/aspose.cells/range/properties/name)プロパティを使用して範囲の名前を設定します。次の例は、B4:G14を拡張するセルの名前付き範囲を作成する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CreateNamedRangeofCells-1.cs" >}}

### **名前付き範囲内のセルにデータを入力する**

範囲の個々のセルにデータを挿入できます。パターンに従って範囲の個々のセルにデータを挿入できます

- **C#**: Range[row,column]
- **VB**: Range(row,column)

A1:C4をスパンするセルの名前付き範囲があるとします。行列は4 * 3 = 12個のセルを作ります。個々の範囲セルは順次配置されています: 範囲[0,0]、範囲[0,1]、範囲[0,2]、範囲[1,0]、範囲[1,1]、範囲[1,2]、範囲[2,0]、範囲[2,1]、範囲[2,2]、範囲[3,0]、範囲[3,1]、範囲[3,2]。

範囲内のセルを特定するには、次のプロパティを使用します:

- FirstRowは、名前付き範囲内の最初の行のインデックスを返します。
- FirstColumnは、名前付き範囲内の最初の列のインデックスを返します。
- RowCountは、名前付き範囲内の総行数を返します。
- ColumnCountは、名前付き範囲内の総列数を返します。

次の例では、指定された範囲のセルに値を入力する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-InputDataInCellsInRange-1.cs" >}}

### **名前付き範囲内のセルを特定する**

範囲の個々のセルにデータを挿入できます。

- **C#**: Range[row,column]
- **VB**: Range(row,column)

A1:C4をスパンする名前付き範囲があるとします。行列は4 * 3 = 12個のセルを作ります。個々の範囲セルは順次配置されています: 範囲[0,0]、範囲[0,1]、範囲[0,2]、範囲[1,0]、範囲[1,1]、範囲[1,2]、範囲[2,0]、範囲[2,1]、範囲[2,2]、範囲[3,0]、範囲[3,1]、範囲[3,2]。

範囲内のセルを特定するには、次のプロパティを使用します:

- FirstRowは、名前付き範囲内の最初の行のインデックスを返します。
- FirstColumnは、名前付き範囲内の最初の列のインデックスを返します。
- RowCountは、名前付き範囲内の総行数を返します。
- ColumnCountは、名前付き範囲内の総列数を返します。

次の例では、指定された範囲のセルに値を入力する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-IdentifyCellsinNamedRange-1.cs" >}}

### **名前付き範囲へのアクセス**

#### **特定の名前付き範囲にアクセスする**

指定された名前で範囲にアクセスするために、[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)コレクションの[**GetRangeByName**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getrangebyname)メソッドを呼び出します。典型的な[**GetRangeByName**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getrangebyname)メソッドは、名前付き範囲の名前を取り、[**Range**](https://reference.aspose.com/cells/net/aspose.cells/range)クラスのインスタンスとして指定された名前付き範囲を返します。次の例は、名前で指定された範囲にアクセスする方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-AccessSpecificNamedRange-1.cs" >}}

#### **スプレッドシート内のすべての名前付き範囲にアクセス**

[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)コレクションの[**GetNamedRanges**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getnamedranges)メソッドを呼び出して、スプレッドシート内のすべての名前付き範囲を取得します。[**GetNamedRanges**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getnamedranges)メソッドは、[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)コレクション内のすべての名前付き範囲の配列を返します。

次の例は、ワークブック内のすべての名前付き範囲にアクセスする方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-AccessAllNamedRanges-1.cs" >}}

### **名前付き範囲をコピー**

Aspose.Cellsは、別の範囲にセルの書式付きでコピーするための[**Range.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/copy/index)メソッドを提供します。

次の例では、ソース範囲のセルを別の名前付き範囲にコピーする方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CopyNamedRanges-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
