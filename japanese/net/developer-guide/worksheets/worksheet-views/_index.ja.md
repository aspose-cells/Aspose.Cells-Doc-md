---
title: ワークシートビュー
type: docs
weight: 40
url: /ja/net/worksheet-views/
description: この記事では、C#および.NET APIを使用して、Excelワークブックとワークシートのページ休止プレビューとやり取りする方法について説明します。分割ウィンドウ、固定ウィンドウ、およびズームファクターを操作します。 
---

## **ページブレークプレビュー**

すべてのワークシートは次の2つのモードで表示できます:

- 通常の表示。
- ページブレークプレビュー。

通常ビューはワークシートのデフォルトビューです。ページ休止プレビューは、ワークシートを印刷時の表示として編集するビューです。ページ休止プレビューでは、各ページに表示されるデータを表示して、印刷エリアとページ休止を調整できます。Aspose.Cellsを使用すると、通常ビューまたはページ休止プレビューモードを有効にできます。

### **表示モードの制御**

Aspose.Cellsは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには、Excelファイル内の各ワークシートにアクセスするための[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)コレクションが含まれています。

ワークシートは[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスには、ワークシートを管理するための多くのプロパティやメソッドが含まれています。通常またはページ休止プレビューモードを有効にするには、[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスの[**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview)プロパティを使用します。[**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview)はブールプロパティであり、**true** または **false** の値のいずれかを格納できるためです。

#### **通常の表示の有効化**

[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスの[**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview)プロパティを **false** に設定することで、ワークシートを通常ビューに設定します。

#### **ページブレークプレビューの有効化**

[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスの[**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview)プロパティを **true** に設定することで、任意のワークシートをページ休止プレビューに設定します。これにより、ワークシートが通常ビューからページ休止プレビューに切り替わります。

次の例は、[**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview)プロパティを使用してExcelファイルの最初のワークシートのページ休止プレビューモードを有効にする方法を示しています。

book1.xlsファイルは、[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスのインスタンスを作成して開きます。最初のワークシートのビューは、[**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview)プロパティを**true**に設定することでページ休止プレビューに切り替えます。変更されたファイルは、output.xlsとして保存されます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-PageBreakPreview-1.cs" >}}

## **ズームファクター**

### **Microsoft Excel の使用**

Microsoft Excel には、ワークシートのズームやスケーリング要素を設定する機能があります。この機能は、ユーザーがワークシートの内容を小さなビューまたは大きなビューで表示するのに役立ちます。ユーザーは、ズーム要素を任意の値に設定できます。

### **Aspose.Cells & ズーム要素**

Aspose.Cellsを使用すると、開発者はワークシートのズームファクタを設定できます。
Aspose.CellsはMicrosoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスを提供します。 [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには、Excelファイル内の各ワークシートにアクセスできる[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)コレクションが含まれています。

ワークシートは[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスで表されます。 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスには、ワークシートを管理するための多くのプロパティとメソッドが用意されています。ワークシートのズームファクタを設定するには、[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスの[**Zoom**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom)プロパティを使用します。ズームファクタは、[**Zoom**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom)プロパティに数値（整数）を割り当てることで設定されます。

以下に、Excelファイルの最初のワークシートのズームファクタを設定する方法を示す完全な例が示されています。

book1.xlsファイルは、[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスのインスタンスを作成することで開かれます。最初のワークシートのズームファクタは75に設定され、変更されたファイルはoutput.xlsとして保存されます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-ZoomFactor-1.cs" >}}

## **ウィンドウ枠の固定**

### **Microsoft Excel の使用**

ウィンドウ枠の固定は、Microsoft Excel が提供する機能です。枠を固定すると、ワークシートをスクロールしても表示され続けるデータを選択できます。

### **Aspose.Cells & ウィンドウ枠の固定**

Aspose.Cellsを使用すると、開発者は実行時にワークシートにウィンドウ枠を適用できます。

Aspose.CellsはMicrosoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスを提供します。 [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには、Excelファイル内の各ワークシートにアクセスできる[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)コレクションが含まれています。

ワークシートは[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスで表されます。 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスには、ワークシートを管理するための多くのプロパティとメソッドが提供されています。ウィンドウ枠を構成するには、Worksheetクラスの[**FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index)メソッドを呼び出します。 [**FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index)メソッドには、次のパラメータが指定されます:

- **行**、枠が開始するセルの行インデックス。
- **列**、枠が開始するセルの列インデックス。
- **固定行**、上部枠内に表示される行数。
- **固定列**、左部枠内に表示される列数。

book1.xlsファイルは、[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスのコンストラクタを呼び出してインスタンス化し、最初のワークシートでいくつかの行と列が固定されます。変更されたファイルはoutput.xlsとして保存されます。

以下に、Excelファイルの最初のワークシートの4行目および3列目（行と列は0から始まるインデックスで表される、C4から始まる）の行と列を固定する方法を示す完全な例が示されています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-FreezePanes-1.cs" >}}

## **画面の分割**

ワークシート内で二つの異なるビューを取得するには、画面を分割する必要があります。Microsoft Excel は、ワークシートのコピーを複数表示し、各パネで独立してスクロールできる非常に便利な機能を提供しています：画面の分割。

パネは同時に動作します。片方で変更を加えると、同時に他方にも変更が表示されます。Aspose.Cells は、ユーザーに対して画面の分割機能を提供しています。

### **画面の分割の適用と解除**

#### **画面の分割**

Aspose.CellsはMicrosoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスを提供します。 [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには、Excelファイルを管理するための多くのプロパティとメソッドが提供されます。分割ビューを実装するには、[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスの[**Split**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/split)を使用します。パネルを解除するには、[**RemoveSplit**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/removesplit)メソッドを使用します。

例では、シンプルなテンプレート ファイルをロードして、最初のワークシートのセルに分割パネル機能を適用し、更新されたファイルを保存します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-SplitPanes-1.cs" >}}

上記のコードを実行すると、生成されたファイルには分割ビューが表示されます。

#### **パネルの削除**

分割ペインを[**RemoveSplit**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/removesplit)メソッドを使用して削除します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-RemovePanes-1.cs" >}}

## **高度なトピック**
- [ワークシートでゼロの値の表示を非表示にする](/cells/ja/net/hiding-the-display-of-zero-values-in-the-worksheet/)
- [ワークシートタブの色を設定する](/cells/ja/net/set-worksheet-tab-color/)
- [グリッド線と行列見出しの表示と非表示](/cells/ja/net/show-and-hide-gridlines-and-row-column-headers/)
- [行と列、スクロールバーの表示と非表示](/cells/ja/net/show-and-hide-rows-columns-and-scroll-bars/)
- [ワークシートとタブの表示と非表示](/cells/ja/net/show-and-hide-worksheets-and-tabs/)
- [ワークシートで値の代わりに数式を表示する](/cells/ja/net/show-formulas-instead-of-values-in-a-worksheet/)
- [エラーチェックオプションを使用する](/cells/ja/net/use-error-checking-options/)

