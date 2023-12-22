---
title: チャートデータをフィルタリングする 3 つの方法
description: Aspose.Cells for .NET を使用して Excel でグラフをフィルタリングする方法を学びます。当社の包括的なガイドでは、グラフにフィルタを適用する方法、グラフ要素をカスタマイズする方法、より良い洞察と情報に基づいた意思決定を行うためのデータ分析ツールの使用方法を説明します。
keywords: Aspose.Cells for .NET, Filtering Charts in Excel, Data Analysis, Decision Making, Visualization.
type: docs
weight: 2210
url: /ja/net/filtering-charts-in-excel/
---
{{% alert color="primary" %}}

##  **1. シリーズをフィルタリングしてグラフをレンダリングする**

###  **Excel でグラフから系列をフィルターする手順**
Excel では、グラフから特定の系列をフィルタリングして除外し、フィルタリングされた系列がグラフに表示されないようにすることができます。元のチャートは次のとおりです。**図1**。ただし、**Testseries2 をフィルタリングすると、**および *Testseries4** の場合、チャートは *図 2** のように表示されます。

 Aspose.Cells でも同様の操作を実行できます。のために[サンプル](seriesFiltered.xlsx)フィルターで除外したい場合は、このようなファイル**テストシリーズ2**および *Testseries4** を使用すると、次のコードを実行できます。さらに、2 つのリストを維持します。1 つは ([Nシリーズ](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/nseries/)選択したすべてのシリーズと別の ([FilteredNSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/filteredSeries/)) フィルタリングされたシリーズを保存します。

お願いします**注記**コード内で設定すると、**chart.NSeries[0].IsFiltered = true;**、[NSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/nseries/) の最初の系列が削除されます[FilteredNSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/filteredSeries/) 内の適切な位置に配置されます。その後、以前の **NSeries[1]**がリストの新しい最初の項目となり、後続のすべてのシリーズが 1 つずつ前方に移動します。これは、*chart.NSeries[1].IsFiltered = true;** を実行すると、元の 3 番目の系列が事実上削除されることを意味します。これは混乱を招く可能性があるため、シリーズを末尾から先頭まで削除するコードの操作に従うことをお勧めします。

![todo:image_alt_text](Figure1.png)

![todo:image_alt_text](Figure2.png)

###  **サンプルコード**
次のサンプルコードは、[サンプル Excel ファイル](seriesFiltered.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "seriesFiltered.cs" >}}

##  **2. データをフィルタリングしてグラフを変更します。**

データのフィルター処理は、大量のデータを含むグラフ フィルターを処理する優れた方法です。データをフィルタリングすると、グラフが変わります。私たちが対処しなければならない問題の 1 つは、チャートが画面上に留まるようにすることです。フィルターすると非表示の行が表示され、場合によってはグラフがそれらの非表示の行に表示されることがあります。

![todo:image_alt_text](Figure3.png)

###  **データ フィルターを使用して Excel のグラフを変更する手順**

1. データ範囲内をクリックします。
 2.**データ**タブをクリックし、「フィルター」をクリックしてフィルターをオンにします。ヘッダー行にはドロップダウン矢印が表示されます。
 3. 次の場所に移動してグラフを作成します。**入れる**タブをクリックして縦棒グラフを選択します。
4. 次に、データのドロップダウン矢印を使用してデータをフィルタリングします。グラフフィルターは使用しないでください。

###  **サンプルコード**
次のサンプル コードは、Aspsoe.Cells を使用した同じ機能を示しています。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "DataFilters.cs" >}}

##  **3. テーブルを使用してデータをフィルターし、グラフを変更します。**

テーブルの使用は、範囲を使用する方法 2 に似ていますが、範囲よりもテーブルの方が利点があります。範囲をテーブルに変更してデータを追加すると、グラフが自動的に更新されます。範囲を指定する場合は、データ ソースを変更する必要があります。

###  **Excel で表としてフォーマットする**

データ内をクリックして使用します**CTRL + T**または、「ホーム」タブを使用します。**テーブルとしてフォーマットする**

![todo:image_alt_text](Figure4.png)

###  **サンプルコード**
次のサンプルコードは、[サンプル Excel ファイル](TableFilters.xlsx)は、Aspsoe.Cells を使用した同じ機能を示しています。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "TableFilters.cs" >}}