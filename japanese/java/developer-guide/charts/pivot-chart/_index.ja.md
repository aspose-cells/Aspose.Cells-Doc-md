---
title: Aspose.Cellsを使用してピボットチャートを追加する方法
linktitle: ピボットチャート
type: docs
weight: 100
url: /ja/java/how-to-add-pivot-chart/
description: Aspose.Cellsを使用してピボットチャートを追加する方法。
keywords: PivotChart
---
## PivotChartとは

ExcelのPivotChartは、PivotTableから作成されたデータの視覚的な表現です。これにより、ユーザーは情報を要約してチャート形式で表示し、データをダイナミックに視覚化して分析することができます。PivotChartは対話型であり、データの異なる視点を簡単に表示するように修正できるため、Excelでのデータ分析とプレゼンテーションにおける強力なツールとなっています。

## Aspose.Cellsを使用してピボットチャートを追加する方法
### **ピボットテーブルの作成**

Aspose.Cellsを使用してピボットテーブルを作成するには:

1. CellオブジェクトのPutValue/setValueメソッドを使用してワークシートセルにデータを追加します。また、データがすでに入力されたテンプレートファイルを使用することもできます。これらのデータはピボットテーブルのデータソースとして使用されます。
1. PivotTablesコレクションのaddメソッド（Worksheetオブジェクトにカプセル化されています）を呼び出すことによって、ワークシートにピボットテーブルを追加します。
1. インデックスを渡してPivotTablesコレクションから新しいPivotTableオブジェクトにアクセスします。
1. PivotTableオブジェクトにカプセル化されたピボットテーブルのオブジェクトのいずれかを使用してテーブルを管理します。

下記のコードサンプルがあります。このコードを実行すると新しいファイル「pivotTable_test.xls」が生成されます。

**入力データ** 

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_1.png)

**出力のピボットテーブル**

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotTable-CreatePivotTable.java" >}}

### **ピボットテーブルを基にしたピボットチャートの作成**

Aspose.Cellsを使用してピボットチャートを作成するには:

1. チャートを追加します。
1. グラフのPivotSourceを、スプレッドシート内の既存のピボットテーブルを指すように設定します。
1. 他の属性を設定します。

以下は、コンポーネントがこのタスクを実行するために使用するコードです。このコードを実行すると、新しいファイル「pivotChart_test.xls」が生成されます。

ピボットチャートシート

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotChartbasedonPivotTable-CreatePivotChartbasedonPivotTable.java" >}}

{{% alert color="primary" %}}

この記事では、Aspose.Cellsを使用してピボットテーブルとピボットチャートを作成する方法を示しています。これにより、これらの機能を独自のシナリオで使用する際に役立つはずです。

Aspose.Cellsは、長年の研究、設計、そして注意深い調整の成果です。

[Aspose.Cellsフォーラム](https://forum.aspose.com/c/cells/9)でのお問い合わせ、コメント、提案を歓迎します。迅速な回答を保証します。

{{% /alert %}}
