---
title: 行と列の自動調整
type: docs
weight: 20
url: /ja/net/autofit-rows-and-columns/
description: この記事では、行、列、結合されたセルの行、およびセル範囲内の行を Aspose.Cells for .NET API によって自動調整する方法を説明します。
keywords: Autofit rows, autofit columns, autofit row in a range of cells, autofit rows of merged cells
---
{{% alert color="primary" %}}

Microsoft Excel では、ユーザーは内容に応じてセルの幅と高さのサイズを自動調整できます。この機能は Aspose.Cells からも利用できるため、開発者は実行時にセルの寸法を自動調整できます。

{{% /alert %}}

##  **自動フィッティング**

Aspose.Cells は、[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)Microsoft Excel ファイルを表すクラス。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Excel ファイル内の各ワークシートへのアクセスを許可するコレクション。ワークシートは次のように表されます。[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスは、ワークシートを管理するための幅広いプロパティとメソッドを提供します。この記事では、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)行または列を自動調整するクラス。

###  **行の自動調整 - シンプル**

行の幅と高さを自動調整する最も簡単な方法は、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス[**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index)方法。の[**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index)このメソッドは、(サイズ変更される行の) 行インデックスをパラメータとして受け取ります。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsandColumns-1.cs" >}}

###  **Cellsの範囲で行を自動調整する方法**

行は多くの列で構成されます。 Aspose.Cells を使用すると、開発者は、オーバーロードされたバージョンの[**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1)方法。次のパラメータを受け取ります。

- *行インデックス**、自動調整される行のインデックス。
- *最初の列インデックス**、行の最初の列のインデックス。
- *最後の列のインデックス**、行の最後の列のインデックス。

の[**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1)このメソッドは、行内のすべての列の内容をチェックし、行を自動調整します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowinSpecificRange-1.cs" >}}

###  **Cellsの範囲で列を自動調整する方法**

列は多くの行で構成されます。オーバーロードされたバージョンの[**AutoFitColumn**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1)次のパラメータを取るメソッド:

- *列インデックス**、自動調整される列のインデックス。
- *最初の行インデックス**、列の最初の行のインデックス。
- *最終行インデックス**、列の最後の行のインデックス。

の[**AutoFitColumn**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1)このメソッドは、列内のすべての行の内容をチェックし、列を自動調整します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitColumninSpecificRange-1.cs" >}}

###  **結合された Cells の行を自動調整する方法**

Aspose.Cells を使用すると、[**AutoFitterオプション**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) API. [**AutoFitterオプション**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)クラスが提供する[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype)結合されたセルの行を自動調整するために使用できるプロパティ。[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype)受け入れる[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitmergedcellstype)以下のメンバーを持つ enumerable です。

- なし: 結合されたセルを無視します。
- FirstLine: 最初の行の高さのみを拡張します。
- LastLine: 最後の行の高さのみを拡張します。
- EachLine: 各行の高さのみを拡張します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsforMergedCells-1.cs" >}}

{{% alert color="primary" %}}

オーバーロードされたバージョンの使用を試みることもできます。[**AutoFitRows**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrows) & [**AutoFitColumns**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitcolumns)行/列の範囲とインスタンスを受け入れるメソッド[**AutoFitterオプション**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)選択した行/列を希望の値に自動調整します[**AutoFitterオプション**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)それに応じて。

前述のメソッドのシグネチャは次のとおりです。

1.  AutoFitRows(int startRow, int endRow,[**AutoFitterオプション**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)オプション）
1.  AutoFitColumns(int firstColumn, int lastColumn,[**AutoFitterオプション**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)オプション）

{{% /alert %}}

##  **知っておくべき重要なこと**

{{% alert color="primary" %}}

セルが結合される場合、AutoFit メソッドは適用されません。これは、Microsoft Excel と同じ動作です。自動フィルタ API を使用すると、この問題を回避できます。さらに、セル内のテキストが折り返されている場合、[**AutoFitColumn**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1)メソッドも適用されません。もう 1 つ知っておく必要があるのは、*自動フィット*方法には時間がかかります。したがって、アプリケーションの効率を確保するには、これらのメソッドをできるだけ頻繁に呼び出さないようにする必要があります。

{{% /alert %}}

##  **アドバンストトピック**
- [結合された Cells の行の自動調整](/cells/ja/net/autofit-rows-for-merged-cells/)
