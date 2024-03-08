---
title: Aspose.Cells を使用してピボットグラフを追加する方法
linktitle: ピボットチャート
type: docs
weight: 100
url: /ja/net/how-to-add-pivot-chart/
description: Aspose.Cells を使用してピボットグラフを追加する方法。
keywords: PivotChart
---
## ピボットグラフとは

Excel のピボットグラフは、ピボットテーブルから作成されたデータをグラフィカルに表現したものです。情報をグラフ形式で要約して表示することで、ユーザーはデータを動的に視覚化および分析できます。ピボットグラフはインタラクティブであり、データのさまざまな視点を表示するために簡単に変更できるため、Excel でのデータ分析とプレゼンテーションのための強力なツールになります。

##  Aspose.Cells を使用してピボットグラフを追加する方法

###  **ピボットテーブルの追加**

Aspose.Cells を使用してピボット テーブルを作成するには:

1. Cell オブジェクトの PutValue/setValue メソッドを使用して、ワークシートのセルにデータを追加します。すでにデータが入力されているテンプレート ファイルを使用することもできます。データはピボット テーブルのデータ ソースとして使用されます。
1. PivotTables コレクションの add メソッド (Worksheet オブジェクトにカプセル化されている) を呼び出して、ピボット テーブルをワークシートに追加します。
1. インデックスを渡すことにより、ピボットテーブル コレクションから新しいピボットテーブル オブジェクトにアクセスします。 # PivotTable オブジェクトにカプセル化されたピボット テーブル オブジェクトのいずれかを使用してテーブルを管理します。

コード例を以下に示します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotTable-1.cs" >}}

###  **ピボット チャートの追加**

Aspose.Cells を使用してピボットグラフを作成するには:

1. グラフを追加します。
1. スプレッドシート内の既存のピボット テーブルを参照するようにグラフの PivotSource を設定します。
1. 他の属性を設定します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotChart-1.cs" >}}

