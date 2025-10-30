---
title: ワークシートビュー
type: docs
weight: 40
url: /ja/python-net/worksheet-views/
description: この記事では、Aspose.Cells for Python via .NET APIを使用してExcelワークブックとワークシートのページ区切りプレビューを操作する方法について説明します。分割ペイン、固定ペイン、ズーム倍率の操作も含みます。 
keywords: Python Excelライブラリ、Pythonのページ区切りプレビュの設定方法、Pythonの通常ビューの有効化方法、ズーム率の設定方法、ペインの固定・解除方法、ペインの分割方法
---

## **ページブレークプレビュー**

すべてのワークシートは次の2つのモードで表示できます:

- 通常の表示。
- ページブレークプレビュー。

通常ビューはワークシートのデフォルトビューです。ページ区切りプレビューは、印刷されるときのワークシートの表示モードです。ページ区切りプレビューは、どのデータが各ページに収まるかを表示し、印刷範囲やページ区切りを調整できます。Aspose.Cells for Python via .NETを使用すると、開発者は通常ビューまたはページ区切りプレビューのモードを有効にできます。

### **表示モードの制御**

Aspose.Cells for Python via .NETは、**[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)**クラスを提供し、Microsoft Excelファイルを表します。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスには、Excelファイル内の各ワークシートにアクセスできる**[**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets)**コレクションが含まれています。

ワークシートは[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスには、ワークシートを管理するための多くのプロパティやメソッドが含まれています。通常またはページ休止プレビューモードを有効にするには、[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスの[**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview)プロパティを使用します。[**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview)はブールプロパティであり、**true** または **false** の値のいずれかを格納できるためです。

#### **通常の表示の有効化**

[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスの[**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview)プロパティを **false** に設定することで、ワークシートを通常ビューに設定します。

#### **ページブレークプレビューの有効化**

[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスの[**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview)プロパティを **true** に設定することで、任意のワークシートをページ休止プレビューに設定します。これにより、ワークシートが通常ビューからページ休止プレビューに切り替わります。

次の例は、[**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview)プロパティを使用してExcelファイルの最初のワークシートのページ休止プレビューモードを有効にする方法を示しています。

book1.xlsファイルは、[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスのインスタンスを作成して開きます。最初のワークシートのビューは、[**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview)プロパティを**true**に設定することでページ休止プレビューに切り替えます。変更されたファイルは、output.xlsとして保存されます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-PageBreakPreview-1.py" >}}

## **ズームファクター**

### **Microsoft Excel の使用**

Microsoft Excel には、ワークシートのズームやスケーリング要素を設定する機能があります。この機能は、ユーザーがワークシートの内容を小さなビューまたは大きなビューで表示するのに役立ちます。ユーザーは、ズーム要素を任意の値に設定できます。

### **Aspose.Cells & ズーム要素**

Aspose.Cellsを使用すると、開発者はワークシートのズームファクタを設定できます。
Aspose.CellsはMicrosoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスを提供します。 [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスには、Excelファイル内の各ワークシートにアクセスできる[**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets)コレクションが含まれています。

ワークシートは[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスで表されます。 [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスには、ワークシートを管理するための多くのプロパティとメソッドが用意されています。ワークシートのズームファクタを設定するには、[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスの[**zoom**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/zoom)プロパティを使用します。ズームファクタは、[**zoom**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/zoom)プロパティに数値（整数）を割り当てることで設定されます。

以下に、Excelファイルの最初のワークシートのズームファクタを設定する方法を示す完全な例が示されています。

book1.xlsファイルは、[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスのインスタンスを作成することで開かれます。最初のワークシートのズームファクタは75に設定され、変更されたファイルはoutput.xlsとして保存されます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-ZoomFactor-1.py" >}}

## **ウィンドウ枠の固定**

### **Microsoft Excel の使用**

ウィンドウ枠の固定は、Microsoft Excel が提供する機能です。枠を固定すると、ワークシートをスクロールしても表示され続けるデータを選択できます。

### **Aspose.Cells & ウィンドウ枠の固定**

Aspose.Cellsを使用すると、開発者は実行時にワークシートにウィンドウ枠を適用できます。

Aspose.CellsはMicrosoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスを提供します。 [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスには、Excelファイル内の各ワークシートにアクセスできる[**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets)コレクションが含まれています。

ワークシートは[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスで表されます。 [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスには、ワークシートを管理するための多くのプロパティとメソッドが提供されています。ウィンドウ枠を構成するには、Worksheetクラスの[**freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#int-int-int-int)メソッドを呼び出します。 [**freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#int-int-int-int)メソッドには、次のパラメータが指定されます:

- **row**：フリーズを開始するセルの行インデックス。
- **column**：フリーズを開始するセルの列インデックス。
- **frozen_rows**：上部ペインに表示される行数。
- **frozen_columns**：左側ペインに表示される列数。

book1.xlsファイルは、[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスのコンストラクタを呼び出してインスタンス化し、最初のワークシートでいくつかの行と列が固定されます。変更されたファイルはoutput.xlsとして保存されます。

以下に、Excelファイルの最初のワークシートの4行目および3列目（行と列は0から始まるインデックスで表される、C4から始まる）の行と列を固定する方法を示す完全な例が示されています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-FreezePanes-1.py" >}}

## **画面の分割**

ワークシート内で二つの異なるビューを取得するには、画面を分割する必要があります。Microsoft Excel は、ワークシートのコピーを複数表示し、各パネで独立してスクロールできる非常に便利な機能を提供しています：画面の分割。

パネは同時に動作します。片方で変更を加えると、同時に他方にも変更が表示されます。Aspose.Cells は、ユーザーに対して画面の分割機能を提供しています。

### **画面の分割の適用と解除**

#### **画面の分割**

Aspose.CellsはMicrosoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスを提供します。 [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスには、Excelファイルを管理するための多くのプロパティとメソッドが提供されます。分割ビューを実装するには、[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスの[**split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/split)を使用します。パネルを解除するには、[**remove_split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/remove_split)メソッドを使用します。

例では、シンプルなテンプレート ファイルをロードして、最初のワークシートのセルに分割パネル機能を適用し、更新されたファイルを保存します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-SplitPanes-1.py" >}}

上記のコードを実行すると、生成されたファイルには分割ビューが表示されます。

#### **パネルの削除**

分割ペインを[**remove_split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/remove_split)メソッドを使用して削除します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-RemovePanes-1.py" >}}

## **高度なトピック**
- [ワークシートでゼロの値の表示を非表示にする](/cells/ja/python-net/hiding-the-display-of-zero-values-in-the-worksheet/)
- [ワークシートタブの色を設定する](/cells/ja/python-net/set-worksheet-tab-color/)
- [グリッド線と行列見出しの表示と非表示](/cells/ja/python-net/show-and-hide-gridlines-and-row-column-headers/)
- [行と列、スクロールバーの表示と非表示](/cells/ja/python-net/show-and-hide-rows-columns-and-scroll-bars/)
- [ワークシートとタブの表示と非表示](/cells/ja/python-net/show-and-hide-worksheets-and-tabs/)
- [ワークシートで値の代わりに数式を表示する](/cells/ja/python-net/show-formulas-instead-of-values-in-a-worksheet/)
- [エラーチェックオプションを使用する](/cells/ja/python-net/use-error-checking-options/)

{{< app/cells/assistant language="python-net" >}}
