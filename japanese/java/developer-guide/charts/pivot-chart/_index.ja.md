---
title: Aspose.Cells を使用してピボットグラフを追加する方法
linktitle: ピボットチャート
type: docs
weight: 100
url: /ja/java/how-to-add-pivot-chart/
description: Aspose.Cells を使用してピボットグラフを追加する方法。
keywords: PivotChart
---
## ピボットグラフとは

Excel のピボットグラフは、ピボットテーブルから作成されたデータをグラフィカルに表現したものです。情報をグラフ形式で要約して表示することで、ユーザーはデータを動的に視覚化および分析できます。ピボットグラフはインタラクティブであり、データのさまざまな視点を表示するために簡単に変更できるため、Excel でのデータ分析とプレゼンテーションのための強力なツールになります。

##  Aspose.Cells を使用してピボットグラフを追加する方法
###  **ピボットテーブルの作成**

Aspose.Cells を使用してピボット テーブルを作成するには:

1. Cell オブジェクトの PutValue/setValue メソッドを使用して、ワークシートのセルにデータを追加します。すでにデータが入力されているテンプレート ファイルを使用することもできます。データはピボット テーブルのデータ ソースとして使用されます。
1. PivotTables コレクションの add メソッド (Worksheet オブジェクトにカプセル化されている) を呼び出して、ピボット テーブルをワークシートに追加します。
1. インデックスを渡すことにより、ピボットテーブル コレクションから新しいピボットテーブル オブジェクトにアクセスします。
1. PivotTable オブジェクトにカプセル化されたピボット テーブル オブジェクトのいずれかを使用して、テーブルを管理します。

コードサンプルを以下に示します。コードを実行すると、新しいファイル pivotTable_test.xls が生成されます。

**入力データ** 

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_1.png)

**出力ピボットテーブル**

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotTable-CreatePivotTable.java" >}}

###  **ピボットテーブルに基づいてピボットチャートを作成する**

Aspose.Cells を使用してピボット チャートを作成するには:

1. グラフを追加します。
1. スプレッドシート内の既存のピボット テーブルを参照するようにグラフの PivotSource を設定します。
1. 他の属性を設定します。

以下は、タスクを実行するためにコンポーネントによって使用されるコードです。コードを実行すると、新しいファイル pivotChart_test.xls が生成されます。

**ピボット チャート シート**

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotChartbasedonPivotTable-CreatePivotChartbasedonPivotTable.java" >}}

{{% alert color="primary" %}}

この記事では、Aspose.Cells を使用してピボット テーブルとピボット グラフを作成する方法を説明します。独自のシナリオでこれらの機能を使用するのに役立つことを願っています。

Aspose.Cells は、長年にわたる研究、設計、慎重なチューニングの恩恵を受けています。

ご質問、ご意見、ご提案をお待ちしております。[Aspose.Cells フォーラム](https://forum.aspose.com/c/cells/9)。迅速な対応を保証いたします。

{{% /alert %}}
