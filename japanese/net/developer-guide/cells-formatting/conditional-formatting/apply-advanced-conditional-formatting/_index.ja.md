---
title: 高度な条件付き書式を適用する
type: docs
weight: 70
url: /ja/net/apply-advanced-conditional-formatting/
---
{{% alert color="primary" %}} 

Microsoft Excel 2007 以降のバージョン (2010/2013/2016) には、条件付き書式の高度な機能がいくつか用意されています。たとえば、セルのシェーディング、境界線、色付きのアイコン、矢印、フラグ、フォントの書式設定などを適用できます。これは非常に洗練されています。

{{% /alert %}} 
## **高度な条件付き書式を Microsoft Excel ファイルに適用する**
条件付き書式は次のことができます。

- 単純な棒グラフをセルに埋め込むことで、影付きのデータ バーを追加して、基礎となる数値をグラフィカルに強調します。
- 範囲内の他のセルの値との関係に基づいて、カラー スケールでセルを自動的に陰影付けします。デフォルト設定では、最低値が赤でシェーディングされ、最高値が緑で上に移動します。
- カラー スケールと同様の方法でアイコン セットを使用しますが、セルに影を付けるのではなく、矢印や信号機などの小さなアイコンをセルに追加します。

Aspose.Cells は、実行時にセルの XLSX 形式で Microsoft Excel 2007 以降のバージョンによって提供される条件付き書式を完全にサポートします。この例では、IconSets、DataBars、Color Scales、TimePeriods、Top/Bottom、およびさまざまな属性セットを持つその他のルールを含む、高度な条件付き書式設定タイプの演習を示します。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConditionalFormatting-1.cs" >}}
### **Microsoft が選択した色を計算する Excel for ColorScale 条件付き書式設定**
Aspose.Cells では、テンプレート ファイルで ColorScale 条件付き書式が使用されている場合に、Microsoft Excel で選択された色を計算できます。 Microsoft Excel で選択された色を計算する方法については、以下のサンプル コードを参照してください。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ComputeColorChoosenByMSExcel-1.cs" >}}
