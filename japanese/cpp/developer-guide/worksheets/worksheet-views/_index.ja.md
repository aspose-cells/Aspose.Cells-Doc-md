---
title: ワークシート ビュー
type: docs
weight: 40
url: /ja/cpp/worksheet-views/
---
## **改ページプレビュー**
すべてのワークシートは、次の 2 つのモードで表示できます。

- 通常のビュー。
- 改ページのプレビュー。

標準ビューは、ワークシートの既定のビューです。改ページ プレビューは、印刷時にワークシートを表示する編集ビューです。改ページのプレビューでは、各ページにどのようなデータが表示されるかが表示されるため、印刷範囲と改ページを調整できます。 Aspose.Cells を使用すると、開発者は通常のビューまたは改ページ プレビュー モードを有効にできます。
### **表示モードの制御**
Aspose.Cells はクラスを提供します[Iワークブック](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)Microsoft Excel ファイルを表します。の[Iワークブック](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)クラスには[ワークシート](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)Excel ファイル内の各ワークシートにアクセスできるコレクション。

ワークシートは、[Iワークシート](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)クラス。の[Iワークシート](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)クラスには、ワークシートを管理するためのさまざまなメソッドが用意されています。通常または改ページのプレビュー モードを有効にするには、[IsPageBreakPreview](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892)の方法[Iワークシート](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)クラス。[IsPageBreakPreview](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892) bool 値を返します。つまり、格納できるのは**真実**また**間違い**価値。
#### **通常表示を有効にする**
を設定して、ワークシートを通常のビューに設定します。[IsPageBreakPreview](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892)の方法[Iワークシート](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)クラスへ**間違い**.
#### **改ページプレビューを有効にする**
を設定して、任意のワークシートを改ページ プレビューに設定します。[IsPageBreakPreview](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892)の方法[Iワークシート](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)クラスへ**真実**.これにより、ワークシートが通常のビューから改ページ プレビューに切り替わります。

の使用方法を示す完全な例を以下に示します。[IsPageBreakPreview](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892)メソッドを使用して、Excel ファイルの最初のワークシートで改ページ プレビュー モードを有効にします。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-EnablingPageBreakPreview.cpp" >}}
## **ズーム倍率**
### **Microsoft エクセルを使う**
Microsoft Excel には、ユーザーがワークシートのズームまたは倍率を設定できる機能があります。この機能は、ユーザーがワークシートの内容を小さいビューまたは大きいビューで表示するのに役立ちます。ユーザーはズーム倍率を任意の値に設定できます。
### **Aspose.Cells & ズーム倍率**
Aspose.Cells では、開発者がワークシートのズーム率を設定することもできます。 Aspose.Cells はクラスを提供します[Iワークブック](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)Microsoft Excel ファイルを表します。の[Iワークブック](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)クラスには[ワークシート](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)Excel ファイル内の各ワークシートにアクセスできるコレクション。

ワークシートは、[Iワークシート](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)クラス。の[Iワークシート](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)クラスには、ワークシートを管理するためのさまざまなメソッドが用意されています。ワークシートのズーム倍率を設定するには、[ズーム](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ad94669a93a4324b3a4b7f9582df5b0ec)の方法[Iワークシート](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)クラス ズーム係数は、数値 (整数) 値を[ズーム](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ad94669a93a4324b3a4b7f9582df5b0ec)方法。

の使用方法を示す完全な例を以下に示します。[ズーム](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ad94669a93a4324b3a4b7f9582df5b0ec)メソッドを使用して、Excel ファイルの最初のワークシートの倍率を設定します。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-ZoomFactor.cpp" >}}
## **フリーズペイン**
### **Microsoft エクセルを使う**
フリーズ ウィンドウは、Microsoft Excel によって提供される機能です。ペインをフリーズすると、ワークシートをスクロールするときにデータを選択して表示したままにすることができます。
### **Aspose.Cells & フリーズペイン**
Aspose.Cells を使用すると、開発者は実行時にフリーズ ペインをワークシートに適用することもできます。 Aspose.Cells はクラスを提供します[Iワークブック](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)Microsoft Excel ファイルを表します。の[Iワークブック](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)クラスには[ワークシート](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)Excel ファイル内の各ワークシートにアクセスできるコレクション。

ワークシートは、[Iワークシート](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)クラス。の[Iワークシート](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)クラスには、ワークシートを管理するためのさまざまなメソッドが用意されています。フリーズ ペインを構成するには、[FreezePanes](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ac4f68dfe9ac219fb8de6d6824ec1aa22)の方法[Iワークシート](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)クラス。の[FreezePanes](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ac4f68dfe9ac219fb8de6d6824ec1aa22)メソッドは次のパラメータを取ります。

- **行**、フリーズが開始されるセルの行インデックス。
- **桁**、フリーズが開始されるセルの列インデックス。
- **凍結された行**、上部ペインに表示される行の数。
- **冷凍列**、左ペインに表示される列の数

の使用方法を示す完全な例を以下に示します。[FreezePanes](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ac4f68dfe9ac219fb8de6d6824ec1aa22)Excel ファイルの最初のワークシートの行と列 (C4 から始まり、4 行目と 3 列目で表され、行と列は 0 インデックスから始まります) を固定するメソッド。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-FreezePanes.cpp" >}}
## **ペインの分割**
同じワークシートに 2 つの異なるビューを表示するために画面を分割する必要がある場合は、ペインを分割します。 Microsoft Excel には、ワークシートの複数のコピーを表示したり、ワークシートの各ペインを個別にスクロールしたりできる非常に便利な機能、分割ペインがあります。

ペインは同時に機能します。一方を変更すると、同時に他方にも変更が反映されます。 Aspose.Cells は、ユーザーに分割ペイン機能を提供します。
### **分割ペインの適用と削除**
#### **ペインの分割**
Aspose.Cells はクラスを提供します[Iワークブック](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)Microsoft Excel ファイルを表します。の[Iワークブック](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)クラスは、Excel ファイルを管理するためのさまざまなメソッドを提供します。分割ビューを実装するには、[スプリット](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a0e581a3a9528a767c57008521ee02b6f)の方法[Iワークシート](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)クラス。分割ペインを削除するには、[削除スプリット](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a5b554108c91f686e906400c26248eee5)方法。

この例では、読み込まれた単純なテンプレート ファイルを使用し、分割ペインの設定機能が最初のワークシートのセルに適用されます。更新されたファイルが保存されます。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-SplitPanes.cpp" >}}
#### **ペインの削除**
を使用して分割ペインを削除します[削除スプリット](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a5b554108c91f686e906400c26248eee5)方法。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-RemovingPanes.cpp" >}}
