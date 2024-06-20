---
title: 高度な条件付き書式の適用
description: C#でAspose.Cellsライブラリを使用して、高度な条件付き書式を適用する方法について説明します。これらの基準を調整することで、セルの外観と表示に対するより多くの制御が可能です。
keywords: Aspose.Cells, 高度な条件付き書式, C#, 条件付き, 書式
type: docs
weight: 70
url: /ja/net/apply-advanced-conditional-formatting/
---

{{% alert color="primary" %}} 

Microsoft Excel 2007およびそれ以降のバージョン（2010/2013/2016）では、条件付き書式の高度な機能が提供されています。たとえば、セルのシェーディング、境界線、カラー アイコン、矢印、フラグ、フォントの書式などが適用でき、かなり洗練されたものになっています。

{{% /alert %}} 
## **Microsoft Excelファイルに高度な条件付き書式を適用する**
条件付き書式を適用することで:

- シェーディングされたデータバーを追加して、単純な棒グラフをセルに埋め込むことで、基になる数値を視覚的に強調できます。
- セルの色が他のセルの値との関係に基づいて自動的に色分けされます。デフォルトの設定では、最小値が赤で、最大値が緑になります。
- カラースケールではなくアイコンセットを使用し、セルに小さな矢印や信号機などのアイコンを追加します。

Aspose.Cellsは、実行時にMicrosoft Excel 2007およびそれ以降のバージョンでXLSX形式で提供されるセルの条件付き書式を完全にサポートしています。この例では、アイコンセット、データバー、カラースケール、時間帯、最上位/最下位などの異なる属性セットでの高度な条件付き書式タイプの演習を示します。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConditionalFormatting-1.cs" >}}
### **Microsoft ExcelがColorScale条件付き書式を使用した場合に選択された色をAspose.Cellsで計算する**
Aspose.Cellsを使用すると、テンプレートファイルでColorScale条件付き書式が使用された場合に、Microsoft Excelによって選択された色を計算できます。以下のサンプルコードを参照して、Microsoft Excelによって選択された色を計算する方法を学んでください。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ComputeColorChoosenByMSExcel-1.cs" >}}
