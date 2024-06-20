---
title: Aspose.Cellsを使用してピボットチャートを追加する方法
linktitle: ピボットチャート
type: docs
weight: 100
url: /ja/net/how-to-add-pivot-chart/
description: Aspose.Cellsを使用してピボットチャートを追加する方法。
keywords: PivotChart
---
## PivotChartとは

ExcelのPivotChartは、PivotTableから作成されたデータの視覚的な表現です。これにより、ユーザーは情報を要約してチャート形式で表示し、データをダイナミックに視覚化して分析することができます。PivotChartは対話型であり、データの異なる視点を簡単に表示するように修正できるため、Excelでのデータ分析とプレゼンテーションにおける強力なツールとなっています。

## Aspose.Cellsを使用してピボットチャートを追加する方法

### **ピボットテーブルの追加**

Aspose.Cellsを使用してピボットテーブルを作成するには:

1. CellオブジェクトのPutValue/setValueメソッドを使用してワークシートセルにデータを追加します。また、データがすでに入力されたテンプレートファイルを使用することもできます。これらのデータはピボットテーブルのデータソースとして使用されます。
1. PivotTablesコレクションのaddメソッド（Worksheetオブジェクトにカプセル化されています）を呼び出すことによって、ワークシートにピボットテーブルを追加します。
1. ピボットテーブルの新しいPivotTableオブジェクトにアクセスするには、そのインデックスを渡してPivotTablesコレクションからアクセスします。#PivotTableオブジェクトにカプセル化されているピボットテーブルオブジェクトを使用して、テーブルを管理します。

以下にコード例を示します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotTable-1.cs" >}}

### **ピボットチャートの追加**

Aspose.Cellsを使用してPivotChartを作成するには:

1. チャートを追加します。
1. グラフのPivotSourceを、スプレッドシート内の既存のピボットテーブルを指すように設定します。
1. 他の属性を設定します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotChart-1.cs" >}}

