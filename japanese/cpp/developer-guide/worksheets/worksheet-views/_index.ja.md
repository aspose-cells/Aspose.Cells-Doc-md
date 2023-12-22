---
title: ワークシートビュー
type: docs
weight: 40
url: /ja/cpp/worksheet-views/
---
##  **改ページプレビュー**
すべてのワークシートは 2 つのモードで表示できます。

- 通常のビュー。
- 改ページのプレビュー。

標準ビューはワークシートのデフォルトのビューです。改ページプレビューは、印刷するワークシートを表示する編集ビューです。改ページプレビューには、各ページにどのようなデータが含まれるかが表示されるため、印刷領域と改ページを調整できます。 Aspose.Cells を使用すると、開発者は通常のビュー モードまたは改ページ プレビュー モードを有効にすることができます。
###  **表示モードの制御**
Aspose.Cells はクラスを提供します[ワークブック](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)これは Microsoft Excel ファイルを表します。の[ワークブック](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスには[ワークシート](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)Excel ファイル内の各ワークシートへのアクセスを許可するコレクション。

ワークシートは次のように表されます。[ワークシート](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラス。の[ワークシート](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスは、ワークシートを管理するための幅広いメソッドを提供します。通常または改ページ プレビュー モードを有効にするには、[SetIsPageBreakプレビュー](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/)の方法[ワークシート](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラス。[IsPageBreakプレビュー](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/ispagebreakpreview/)ブール値を返します。これは、**真実**または**間違い**価値。
####  **通常表示を有効にする**
を設定してワークシートを通常表示に設定します。[SetIsPageBreakプレビュー](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/)の方法[ワークシート](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスを *false** に設定します。
####  **改ページプレビューを有効にする**
を設定して、任意のワークシートを改ページ プレビューに設定します。[SetIsPageBreakプレビュー](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/)の方法[ワークシート](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスを *true** に設定します。これにより、ワークシートが通常のビューから改ページ プレビューに切り替わります。

の使用方法を示す完全な例を以下に示します。[SetIsPageBreakプレビュー](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/)Excel ファイルの最初のワークシートの改ページ プレビュー モードを有効にするメソッド。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-EnablingPageBreakPreview-new.cpp" >}}
##  **ズーム倍率**
###  **Microsoft Excelの使用**
Microsoft Excel には、ユーザーがワークシートのズームまたは倍率を設定できる機能が用意されています。この機能は、ユーザーがワークシートの内容を小さいビューまたは大きいビューで表示するのに役立ちます。ユーザーはズーム率を任意の値に設定できます。
###  **Aspose.Cells & ズーム率**
Aspose.Cells を使用すると、開発者はワークシートのズーム率を設定することもできます。 Aspose.Cells はクラスを提供します[ワークブック](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)これは Microsoft Excel ファイルを表します。の[ワークブック](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスには[ワークシート](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)Excel ファイル内の各ワークシートへのアクセスを許可するコレクション。

ワークシートは次のように表されます。[ワークシート](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラス。の[ワークシート](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスは、ワークシートを管理するための幅広いメソッドを提供します。ワークシートのズーム率を設定するには、[ズーム設定](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/)の方法[ワークシート](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラス。ズーム率は、数値 (整数) を割り当てて設定します。[ズーム設定](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/)方法。

の使用方法を示す完全な例を以下に示します。[ズーム設定](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/)Excel ファイルの最初のワークシートのズーム率を設定するメソッド。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-ZoomFactor-new.cpp" >}}
##  **ペインの固定**
###  **Microsoft Excelの使用**
ペインの固定は、Microsoft Excel によって提供される機能です。ペインを固定すると、ワークシート内をスクロールするときに表示されたままにするデータを選択できます。
###  **Aspose.Cells & ペインを凍結**
Aspose.Cells を使用すると、開発者は実行時にフリーズ ペインをワークシートに適用することもできます。 Aspose.Cells はクラスを提供します[ワークブック](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)これは Microsoft Excel ファイルを表します。の[ワークブック](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスには[ワークシート](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)Excel ファイル内の各ワークシートへのアクセスを許可するコレクション。

ワークシートは次のように表されます。[ワークシート](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラス。の[ワークシート](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスは、ワークシートを管理するための幅広いメソッドを提供します。フリーズペインを設定するには、[フリーズペイン](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/)の方法[ワークシート](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラス。の[フリーズペイン](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/)メソッドは次のパラメータを受け取ります。

- *Row**、フリーズが開始されるセルの行インデックス。
- *Column**、フリーズが開始されるセルの列インデックス。
- *固定行**、上部ペインに表示される行の数。
- *固定列**、左ペインに表示される列の数

の使用方法を示す完全な例を以下に示します。[フリーズペイン](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/)Excel ファイルの最初のワークシートの行と列 (C4 から始まり、4 行目と 3 列目で表され、行と列はインデックス 0 から始まります) を固定するメソッドです。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-FreezePanes-new.cpp" >}}
##  **ペインの分割**
同じワークシート内で 2 つの異なるビューを表示するために画面を分割する必要がある場合は、ペインを分割します。 Microsoft Excel には、ワークシートの複数のコピーを表示したり、ワークシートの各ペインを個別にスクロールしたりできる、非常に便利な機能 (ペインの分割) が用意されています。

ペインは同時に動作します。一方に変更を加えると、その変更は同時にもう一方にも反映されます。 Aspose.Cells は、ユーザーに分割ペイン機能を提供します。
###  **分割ペインの適用と削除**
####  **ペインの分割**
Aspose.Cells はクラスを提供します[ワークブック](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)これは Microsoft Excel ファイルを表します。の[ワークブック](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスは、Excel ファイルを管理するための幅広いメソッドを提供します。分割ビューを実装するには、[スプリット](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/)の方法[ワークシート](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラス。分割ペインを削除するには、[削除分割](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/)方法。

この例では、単純なテンプレート ファイルをロードしてから、分割ペインの設定機能を最初のワークシートのセルに適用します。更新されたファイルが保存されます。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-SplitPanes-new.cpp" >}}
####  **ペインの削除**
分割ペインを削除するには、[削除分割](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/)方法。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-RemovingPanes-new.cpp" >}}
