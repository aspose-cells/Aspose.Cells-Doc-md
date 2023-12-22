---
title: X 軸とカテゴリ軸
description: 軸とカテゴリ軸を区別する方法については、Aspose.Cells for .NET で説明しています。ガイドは、それらの使用法とプロパティの違い、およびニーズに応じてそれらを構成する方法を理解するのに役立ちます。
keywords: Aspose.Cells for .NET, X axis, Category axis, difference, usage, properties, configuration.
type: docs
weight: 180
url: /ja/net/X-axis-vs-category-axis/
---
##  **考えられる使用シナリオ**
軸にはさまざまな種類があります。 Y 軸は値タイプの軸ですが、X 軸はカテゴリ タイプの軸または値タイプの軸にすることができます。値軸を使用すると、データは連続的に変化する数値データとして扱われ、数値に応じて変化する軸に沿った点にマーカーが配置されます。カテゴリ軸を使用すると、データは一連の非数値テキスト ラベルとして処理され、マーカーはシーケンス内の位置に従って軸に沿った点に配置されます。以下のサンプルは、値軸とカテゴリ軸の違いを示しています。
サンプルデータは次のとおりです。[サンプルテーブルファイル](sample.png)下に。最初の列には X 軸データが含まれており、カテゴリまたは値として扱うことができます。番号は等間隔ではなく、番号順に表示されていないことに注意してください。

![todo:image_alt_text](sample.png)
##  **Microsoft Excel のように X とカテゴリ軸を処理します**
このデータを 2 種類のグラフに表示します。1 つ目のグラフは値軸としての XY (散布) グラフ X、2 つ目のグラフはカテゴリ軸としての折れ線グラフ X です。

![todo:image_alt_text](compare.png)
##  **サンプルコード**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "X-axis-vs-category-axis.cs" >}}
