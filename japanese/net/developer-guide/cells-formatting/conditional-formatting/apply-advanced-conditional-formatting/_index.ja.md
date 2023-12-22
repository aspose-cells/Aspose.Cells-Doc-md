---
title: 高度な条件付き書式設定を適用する
description: C# の Aspose.Cells ライブラリを使用して高度な条件付き書式設定を適用する方法。これらの基準を調整することで、セルの外観をより詳細に制御できるようになります。
keywords: Aspose.Cells, Advanced Conditional Formatting, C#, Conditional, Formatting
type: docs
weight: 70
url: /ja/net/apply-advanced-conditional-formatting/
---
{{% alert color="primary" %}} 

Microsoft Excel 2007 以降のバージョン (2010/2013/2016) には、条件付き書式設定の高度な機能がいくつか用意されています。たとえば、セルのシェーディング、境界線、色付きのアイコン、矢印、フラグ、フォントの書式設定などを適用でき、非常に洗練されています。

{{% /alert %}} 
##  **Microsoft Excel ファイルに高度な条件付き書式設定を適用する**
条件付き書式では次のことが可能です。

- 単純な棒グラフをセルに埋め込むことで、陰影付きのデータ バーを追加して、基礎となる数値を視覚的に強調します。
- 範囲内の他のセルの値との関係に基づいて、カラー スケールでセルを自動的にシェーディングします。デフォルト設定では、最小値が赤で表示され、最大値が緑で表示されます。
- カラー スケールと同様の方法でアイコン セットを使用しますが、セルをシェーディングするのではなく、矢印や信号機などの小さなアイコンをセルに追加します。

Aspose.Cells は、実行時にセル上で Microsoft Excel 2007 以降のバージョンの XLSX 形式で提供される条件付き書式設定を完全にサポートします。この例では、IconSet、DataBars、Color Scale、TimePeriods、Top/Bottom、およびさまざまな属性セットを持つその他のルールを含む、高度な条件付き書式設定タイプの演習を示します。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConditionalFormatting-1.cs" >}}
###  **ColorScale 条件付き書式設定用に Microsoft Excel で選択された色を計算する**
Aspose.Cells ColorScale 条件付き書式がテンプレート ファイルで使用されている場合、Microsoft Excel で選択された色を計算できます。 Microsoft Excel で選択された色を計算する方法については、以下のサンプル コードを参照してください。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ComputeColorChoosenByMSExcel-1.cs" >}}
