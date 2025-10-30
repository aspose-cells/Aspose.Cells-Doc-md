---
title: ワークシートビュー
type: docs
weight: 40
url: /ja/cpp/worksheet-views/
---

## **ページブレークプレビュー**
すべてのワークシートは次の2つのモードで表示できます:

- 通常の表示。
- ページブレークプレビュー。

通常の表示はワークシートのデフォルトの表示方法です。ページブレークプレビューは、ワークシートを印刷時の表示として提供する編集ビューです。ページブレークプレビューでは、どのデータが各ページに表示されるかを表示し、印刷範囲やページブレークを調整できます。Aspose.Cellsを使用すると、通常の表示またはページブレークプレビューモードを有効にできます。
### **表示モードの制御**
Aspose.CellsはMicrosoft Excelファイルを表す[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) クラスを提供します。[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) クラスにはExcelファイル内の各ワークシートにアクセスを許可する[Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) コレクションが含まれています。

ワークシートは[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) クラスで表されます。[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) クラスは、ワークシートを管理するために使用されるさまざまなメソッドを提供します。通常の表示またはページブレークプレビューモードを有効にするには、[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) クラスの [SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/) メソッドを使用します。[IsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/ispagebreakpreview/) は真偽値を返すため、**true** または **false** の値のみを格納できます。
#### **通常の表示の有効化**
ワークシートを[SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/) メソッドを使用して **false** に設定することで、通常の表示に設定します。
#### **ページブレークプレビューの有効化**
ワークシートを[SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/) メソッドを使用して **true** に設定することで、任意のワークシートをページブレークプレビューに切り替えます。

以下に、[SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/) メソッドを使用してExcelファイルの最初のワークシートにページブレークプレビューモードを有効にする方法を示す完全な例があります。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-EnablingPageBreakPreview-new.cpp" >}}
## **ズームファクター**
### **Microsoft Excel の使用**
Microsoft Excel には、ワークシートのズームやスケーリング要素を設定する機能があります。この機能は、ユーザーがワークシートの内容を小さなビューまたは大きなビューで表示するのに役立ちます。ユーザーは、ズーム要素を任意の値に設定できます。
### **Aspose.Cells & ズーム要素**
Aspose.Cells は開発者がワークシートのズーム要素を設定することも可能です。Aspose.Cells は、Microsoft Excel ファイルを表す [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) クラスを提供しています。[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) クラスには、Excel ファイル内の各ワークシートにアクセスを可能にする [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) コレクションが含まれています。

ワークシートは [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) クラスで表されます。[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) クラスには、ワークシートを管理するための様々なメソッドが用意されています。ワークシートのズーム要素を設定するには、[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) クラスの [SetZoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/) メソッドを使用します。ズーム要素は、[SetZoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/) メソッドに数値（整数）値を割り当てることで設定されます。

以下に示す完全な例では、Excel ファイルの最初のワークシートのズーム要素を設定する方法を示しています。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-ZoomFactor-new.cpp" >}}
## **ウィンドウ枠の固定**
### **Microsoft Excel の使用**
ウィンドウ枠の固定は、Microsoft Excel が提供する機能です。枠を固定すると、ワークシートをスクロールしても表示され続けるデータを選択できます。
### **Aspose.Cells & ウィンドウ枠の固定**
Aspose.Cells では、開発者が実行時にワークシートにウィンドウ枠の固定を適用することも可能です。Aspose.Cells は、Microsoft Excel ファイルを表す [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) クラスを提供しています。[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) クラスには、Excel ファイル内の各ワークシートにアクセスを可能にする [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) コレクションが含まれています。

ワークシートは [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) クラスで表されます。[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) クラスには、ワークシートを管理するための様々なメソッドが用意されています。ウィンドウ枠を設定するには、[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) クラスの [FreezePanes](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) メソッドを呼び出します。[FreezePanes](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) メソッドは以下のパラメータを受け取ります：

- **行**、枠が開始するセルの行インデックス。
- **列**、枠が開始するセルの列インデックス。
- **固定行**、上部枠内に表示される行数。
- **固定列**、左部枠内に表示される列数。

以下に示す完全な例では、Excel ファイルの最初のワークシートの行と列（4 行目および 3 列目で表される C4 から開始し、行および列は 0 インデックスから開始されます）を固定するために [FreezePanes](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) メソッドを使用する方法を示しています。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-FreezePanes-new.cpp" >}}
## **画面の分割**
ワークシート内で二つの異なるビューを取得するには、画面を分割する必要があります。Microsoft Excel は、ワークシートのコピーを複数表示し、各パネで独立してスクロールできる非常に便利な機能を提供しています：画面の分割。

パネは同時に動作します。片方で変更を加えると、同時に他方にも変更が表示されます。Aspose.Cells は、ユーザーに対して画面の分割機能を提供しています。
### **画面の分割の適用と解除**
#### **画面の分割**
Aspose.Cells は、Microsoft Excel ファイルを表す [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) クラスを提供しています。[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) クラスは、Excel ファイルを管理するための様々なメソッドを提供しています。分割ビューを実装するには、[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) クラスの [Split](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/) メソッドを使用します。分割パネルを削除するには、[RemoveSplit](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/) メソッドを使用します。

例では、シンプルなテンプレート ファイルをロードして、最初のワークシートのセルに分割パネル機能を適用し、更新されたファイルを保存します。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-SplitPanes-new.cpp" >}}
#### **パネルの削除**
[RemoveSplit](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/) メソッドを使用してパネルを削除します。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-RemovingPanes-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
