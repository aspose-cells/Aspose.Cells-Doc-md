---
title: チャートデータのフィルタリングの3つの方法
description: Aspose.Cells for .NETを使用してExcelでチャートをフィルタリングする方法について学びます。当社の包括的なガイドが、チャートにフィルターを適用し、チャート要素をカスタマイズし、より良い洞察と情報に基づく意思決定を行うためのデータ分析ツールを示します。
keywords: Aspose.Cells for .NET、Excelでのチャートのフィルタリング、データ分析、意思決定、ビジュアライゼーション。
type: docs
weight: 2210
url: /ja/net/filtering-charts-in-excel/
---

{{% alert color="primary" %}}

## **1. チャートからシリーズをフィルタリングする**

### **Excelでチャートからシリーズをフィルタリングする手順**
Excelでは、特定のシリーズをチャートからフィルタリングして、フィルタリングされたシリーズをチャートに表示されないようにすることができます。元のチャートは**図1**に表示されます。ただし、**Testseries2**と**Testseries4**をフィルタリングすると、**図2**に示すようにチャートが表示されます。

Aspose.Cellsでは同様の操作を実行することができます。次のような[サンプル](seriesFiltered.xlsx)ファイルについて、例えば**Testseries2**と**Testseries4**をフィルタリングしたい場合、次のコードを実行できます。さらに、選択されたシリーズをすべて格納する[NSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/nseries/)リストと、フィルタリングされたシリーズを格納する[FilteredNSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/filteredSeries/)が2つあります。

コードで**chart.NSeries[0].IsFiltered = true;**を設定すると、[NSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/nseries/)の最初のシリーズが削除され、適切な位置に[FilteredNSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/filteredSeries/)に配置されます。その後、以前の**NSeries[1]**は新しい最初のアイテムとなり、その後ろの全てのシリーズは1つ前にシフトされます。つまり、次に**chart.NSeries[1].IsFiltered = true;**を実行すると、実質的に元の3番目のシリーズが削除されます。これは、混乱を招くことがあるため、コードで操作に従うことをお勧めします。

![todo:image_alt_text](Figure1.png)

![todo:image_alt_text](Figure2.png)

### **サンプルコード**
次のサンプルコードは、[サンプルExcelファイル](seriesFiltered.xlsx)を読み込みます。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "seriesFiltered.cs" >}}

## **2. データをフィルターし、グラフを変更します**

データをフィルターすることは、多くのデータを持つチャートのフィルターを処理する良い方法です。 データをフィルターすると、グラフが変わります。 対処する問題の1つは、チャートが画面に残るようにすることです。 データをフィルターすると、非表示の行が表示され、時々チャートがその非表示の行に含まれることがあります。

![todo:image_alt_text](Figure3.png)

### **Excelでチャートを変更するデータフィルターの使用手順**

1. データ範囲の内側をクリックします。
2. **データ** タブをクリックし、フィルターを選択してフィルターをオンにします。 ヘッダー行にはドロップダウン矢印が表示されます。
3. **挿入** タブに移動し、列のチャートを選択して、チャートを作成します。
4. 今、データをドロップダウン矢印を使用してフィルタリングします。 チャートフィルターは使用しないでください。

### **サンプルコード**
以下のサンプルコードは、Aspose.Cellsを使用して同じ機能を示しています。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "DataFilters.cs" >}}

## **3. テーブルを使用してデータをフィルターし、グラフを変更します**

テーブルを使用することは、範囲を使用する方法2と似ていますが、テーブルには範囲よりも優れた点があります。 テーブルに範囲を変更してデータを追加すると、チャートが自動的に更新されます。 範囲の場合、データソースを変更する必要があります。

### **Excelでテーブルとしてフォーマット**

データ内をクリックし、**CTRL + T** を使用するか、**ホーム** タブ、**テーブルの書式設定** を使用します。

![todo:image_alt_text](Figure4.png)

### **サンプルコード**
次のサンプルコードは、[サンプルExcelファイル](TableFilters.xlsx) を使用して、Aspose.Cellsを使用して同じ機能を示しています。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "TableFilters.cs" >}}
