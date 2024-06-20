---
title: アクセスおよび名前付き範囲のコピーを作成します
type: docs
weight: 200
url: /ja/python-net/create-access-and-copy-named-ranges/
description: Aspose.Cells for Python via .NET API を使用してアクセスおよび名前付き範囲の作成およびコピー方法を示します。
keywords: Python Excel ライブラリ、アクセスと名前付き範囲の作成、名前付き範囲の作成、名前付き範囲のコピー、スプレッドシート内のすべての名前付き範囲にアクセスする Python。
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

## **Aspose.Cells for Python Excel ライブラリを使用した名前付き範囲の作業**

ここでは、Aspose.Cells for Python via .NET API を使用してタスクを実行します。
Aspose.Cells for Python via .NETは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスには、Excelファイル内の各ワークシートにアクセスできる[**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/)コレクションが含まれています。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスは[**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)コレクションを提供します。

### **名前付き範囲の作成**

[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)コレクションのオーバーロードされた[**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range/#str-str)メソッドを呼び出すことで、名前付き範囲を作成することが可能です。通常、[**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range/#str-str)メソッドの一般的なバージョンは、以下のパラメータを取ります:

- 左上のセルの名前、範囲内の左上のセルの名前。
- 右下のセルの名前、範囲内の右下のセルの名前。

[**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range/#str-str)メソッドを呼び出すと、[**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range)クラスのインスタンスとして新しく作成された範囲が返されます。この[**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range)オブジェクトを使用して、名前付き範囲を構成します。たとえば、[**name**](https://reference.aspose.com/cells/python-net/aspose.cells/range/name)プロパティを使用して範囲の名前を設定します。次の例は、B4:G14を拡張するセルの名前付き範囲を作成する方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-CreateNamedRangeofCells-1.py" >}}

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-InputDataInCellsInRange-1.py" >}}

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-IdentifyCellsinNamedRange-1.py" >}}

### **名前付き範囲へのアクセス**

#### **特定の名前付き範囲にアクセスする**

指定された名前で範囲にアクセスするために、[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/)コレクションの[**get_range_by_name**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/get_range_by_name/#str)メソッドを呼び出します。典型的な[**get_range_by_name**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/get_range_by_name/#str)メソッドは、名前付き範囲の名前を取り、[**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range)クラスのインスタンスとして指定された名前付き範囲を返します。次の例は、名前で指定された範囲にアクセスする方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-AccessSpecificNamedRange-1.py" >}}

#### **スプレッドシート内のすべての名前付き範囲にアクセス**

[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/)コレクションの[**get_named_ranges**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/get_named_ranges/#)メソッドを呼び出して、スプレッドシート内のすべての名前付き範囲を取得します。[**get_named_ranges**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/get_named_ranges/#)メソッドは、[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/)コレクション内のすべての名前付き範囲の配列を返します。

次の例は、ワークブック内のすべての名前付き範囲にアクセスする方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-AccessAllNamedRanges-1.py" >}}

### **名前付き範囲をコピー**

Aspose.Cells for Python via .NETでは、セルの範囲をフォーマット付きで別の範囲にコピーするための[**Range.copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy/#aspose.cells.Range)メソッドが提供されます。

次の例では、ソース範囲のセルを別の名前付き範囲にコピーする方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-CopyNamedRanges-1.py" >}}
