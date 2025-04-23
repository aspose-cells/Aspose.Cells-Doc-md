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
ピボットチャートは、ピボットテーブルのデータを視覚的に表現したものです。ピボットチャートは、要約の概要、分析、探索、および提示のための方法を提供します。主な特徴と側面は以下の通りです：

1. 動的データ表現：ピボットチャートは、ピボットテーブルの変更に応じて自動的に更新されます。フィールドの追加や削除により、ピボットチャートもそれに応じて更新されます。

1. インタラクティブ：ピボットチャートはインタラクティブで、フィルタリング、並べ替え、詳細表示が可能です。これにより、データセットのさまざまな側面を簡単に探索できます。

1. 柔軟なレイアウト：ユーザーはフィールドをドラッグアンドドロップしてピボットチャートのレイアウトを変更でき、データの視覚化に柔軟性を持たせることができます。

1. 様々なチャートタイプ：棒グラフ、折れ線グラフ、円グラフなど、さまざまなタイプのチャートで作成可能です。データの性質や洞察したい内容に応じて選択します。

1. 要約：ピボットチャートは大量のデータを要約し、合計値、平均値、カウント、その他の統計情報を表示できます。

1. フィルタリング：特定の条件を満たすデータのみを表示するフィルタリング機能もあります。

<br>
ピボットチャートは、ビジネスインテリジェンスやデータ分析によく使われ、複雑なデータセットの明確で簡潔なビジュアル概要を提供します。データ駆動の意思決定に強力なツールです。

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
{{< app/cells/assistant language="java" >}}
