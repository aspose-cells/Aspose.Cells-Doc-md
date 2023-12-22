---
title: 結合と結合解除 Cells
description: Aspose.Cells は、セルの結合と結合解除をサポートする、スプレッドシート ファイルを操作するための .NET ライブラリです。この記事では、Aspose.Cells ライブラリを使用してセルを結合および結合解除する方法、および結合されたセルのスタイルをカスタマイズする方法を紹介します。
keywords: Aspose.Cells, NET library, spreadsheet, merge cells, unmerge cells, style settings, custom styles
type: docs
weight: 190
url: /ja/net/merging-and-unmerging-cells/
---
{{% alert color="primary" %}} 

Aspose.Cells はこの機能をサポートしており、ワークシート内のセルを結合することもできます。結合されたセルの結合を解除したり、分割したりすることもできます。結合されたセルのセル参照は、元の選択範囲の左上のセルの参照です。

{{% /alert %}} 
##  **導入**
すべての行または列に常に同じ数のセルが必要なわけではありません。たとえば、複数の列にまたがるセルにタイトルを入力したい場合があります。または、請求書を作成する場合は、合計の列を少なくしたい場合があります。 2 つ以上のセルから 1 つのセルを作成するには、セルを結合します。 Microsoft Excel を使用すると、ユーザーはファイルを選択して結合し、スプレッドシートを自由に構成できます。

{{% alert color="primary" %}} 

セルを結合すると、左上のセルのデータのみが保持されることに注意してください。範囲内の他のセルにデータがある場合、そのデータは削除されます。
同様に、書式設定は参照セルに基づいて行われるため、セルを結合すると、範囲内の左上のセルの書式設定が結合されたセルに適用されます。セルが分割されると、新しいセルは元の形式設定を維持します。

{{% /alert %}} 
##  **Cells をワークシートに結合する**
###  **Cells Excel での Cells の結合**
次の手順では、MS Excel を使用してワークシート内のセルを結合する方法を説明します。

1. 必要なデータを範囲内の左上端のセルにコピーします。
1. 結合するセルを選択します。
1. 行または列内のセルを結合し、セルの内容を中央揃えにするには、**結合して中央揃えにする**のアイコン**書式設定**ツールバー。
###  **Cells と Aspose.Cells の結合**
Aspose.Cells.Cells クラスには、タスクに役立つメソッドがいくつかあります。たとえば、Merge() メソッドは、指定された範囲内のセルを 1 つのセルに結合します。

次の例は、ワークシート内のセル (C6:E7) を結合する方法を示しています。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-MergingCellsInWorksheet.-1.cs" >}}
##  **結合解除 (分割) 結合済み Cells**
###  **Microsoft Excelの使用**
次の手順では、Microsoft Excel を使用して結合されたセルを分割する方法を説明します。

1. 結合されたセルを選択します。
セルが結合されると、**結合して中央揃えにする**で選択されています**書式設定**ツールバー。
1. クリック**結合して中央揃えにする**で**書式設定**ツールバー。
###  **Aspose.Cellsを使用する**
クラス Aspose.Cells.Cells には、セルを元の状態に分割する UnMerge() というメソッドがあります。このメソッドは、結合されたセル範囲内のセルの参照を使用してセルの結合を解除します。

次の例は、結合されたセル (C6) を分割する方法を示しています。この例では、前の例で作成したファイルを使用し、結合されたセルを分割します。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-UnMergingtheMergedCells-1.cs" >}}


##  **アドバンストトピック**
- [ワークシート内の結合された Cells の検出](/cells/ja/net/detect-merged-cells-in-a-worksheet/)
