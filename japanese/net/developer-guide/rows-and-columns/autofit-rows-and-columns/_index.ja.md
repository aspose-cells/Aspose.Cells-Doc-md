---
title: 行と列の自動調整
type: docs
weight: 20
url: /ja/net/autofit-rows-and-columns/
---
{{% alert color="primary" %}}

Microsoft Excel では、内容に応じてセルの幅と高さを自動調整できます。この機能は Aspose.Cells からも利用できるため、開発者は実行時にセルのサイズを自動調整できます。

{{% /alert %}}

## **自動フィッティング**

Aspose.Cells は[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)Microsoft Excel ファイルを表すクラス。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Excel ファイル内の各ワークシートにアクセスできるコレクション。ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスには、ワークシートを管理するためのさまざまなプロパティとメソッドが用意されています。この記事では、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)行または列を自動調整するクラス。

### **行の自動調整 - シンプル**

行の幅と高さを自動サイズ変更する最も簡単な方法は、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス[**行の自動調整**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index)方法。の[**行の自動調整**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index)メソッドは、(サイズ変更する行の) 行インデックスをパラメーターとして受け取ります。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsandColumns-1.cs" >}}

### **Cells の範囲で行を自動調整**

行は多くの列で構成されています。 Aspose.Cells を使用すると、開発者は、オーバーロードされたバージョンの[**行の自動調整**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1)方法。次のパラメータを取ります。

- **行インデックス**、自動調整しようとしている行のインデックス。
- **最初の列のインデックス**、行の最初の列のインデックス。
- **最後の列のインデックス**、行の最後の列のインデックス。

の[**行の自動調整**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1)メソッドは、行内のすべての列の内容をチェックしてから、行を自動調整します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowinSpecificRange-1.cs" >}}

### **Cells の範囲で列を自動調整**

列は多くの行で構成されています。オーバーロードされたバージョンの[**列の自動調整**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1)次のパラメータを取るメソッド:

- **列インデックス**、自動調整しようとしている列のインデックス。
- **最初の行のインデックス**、列の最初の行のインデックス。
- **最後の行のインデックス**、列の最後の行のインデックス。

の[**列の自動調整**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1)メソッドは、列内のすべての行の内容をチェックしてから、列を自動調整します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitColumninSpecificRange-1.cs" >}}

### **マージされた Cells の行の自動調整**

 Aspose.Cells を使用すると、[**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) API. [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)クラスが提供する[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype)結合されたセルの行を自動調整するために使用できるプロパティ。[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype)受け入れる[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitmergedcellstype)次のメンバーを持つ列挙可能。

- なし: 結合されたセルを無視します。
- FirstLine: 最初の行の高さのみを拡張します。
- LastLine: 最後の行の高さのみを拡張します。
- EachLine: 各行の高さのみを拡張します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsforMergedCells-1.cs" >}}

{{% alert color="primary" %}}

オーバーロードされたバージョンの使用を試みることもできます[**AutoFitRows**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrows) & [**AutoFitColumns**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitcolumns)行/列の範囲とインスタンスを受け入れるメソッド[**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)選択した行/列を目的の行に自動調整します[**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)によると。

前述のメソッドのシグネチャは次のとおりです。

1.  AutoFitRows(int startRow, int endRow,[**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)オプション)
1. AutoFitColumns(int firstColumn, int lastColumn,[**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)オプション)

{{% /alert %}}

## **知っておくべき重要事項**

{{% alert color="primary" %}}

セルが結合されている場合、AutoFit メソッドは適用されません。これは、Microsoft Excel と同じ動作です。これは、オート フィルター API を使用して回避できます。さらに、セル内のテキストが折り返されている場合、[**列の自動調整**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1)メソッドも適用されません。もう 1 つ知っておく必要があるのは、*自動調整*方法は時間がかかります。したがって、アプリケーションの効率を確保するために、これらのメソッドをできるだけ呼び出さないようにする必要があります。

{{% /alert %}}

## **先行トピック**
- [マージされた Cells の行の自動調整](/cells/ja/net/autofit-rows-for-merged-cells/)
