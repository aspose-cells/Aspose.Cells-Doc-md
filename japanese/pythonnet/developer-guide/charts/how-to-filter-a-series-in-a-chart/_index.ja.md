---
title: チャートデータのフィルタリングの3つの方法
description: Aspose.Cells for Python via .NETを使用してExcelのチャートをフィルタリングする方法を学びます。包括的なガイドでは、チャートにフィルターを適用する方法、チャート要素をカスタマイズする方法、データ分析ツールを使用してより良い洞察と意思決定を行う方法を紹介します。
keywords: Aspose.Cells for Python via .NET、Excelでのチャートフィルタリング、データ分析、意思決定、可視化
type: docs
weight: 2210
url: /ja/python-net/filtering-charts-in-excel/
---

{{% alert color="primary" %}}

## **1. チャートからシリーズをフィルタリングする**

### **Excelでチャートからシリーズをフィルタリングする手順**
Excelでは、特定のシリーズをチャートからフィルタリングして、フィルタリングされたシリーズをチャートに表示されないようにすることができます。元のチャートは**図1**に表示されます。ただし、**Testseries2**と**Testseries4**をフィルタリングすると、**図2**に示すようにチャートが表示されます。

Aspose.Cells for Python via .NETでは、同様の操作を行うことができます。例として[サンプル](seriesFiltered.xlsx)のファイルの場合、**Testseries2**と**Testseries4**を除外したい場合、次のコードを実行します。さらに、二つのリストを保持します：一つはすべての選択された系列を格納する（[n_series](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/n_series/)）、もう一つはフィルタリングされた系列を格納する（[filtered_n_series](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/filtered_n_series/)）。

コード内で**chart.nSeries[0].is_filtered = TRUE;**と設定すると、最初の系列が[n_series](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/n_series/)から除去され、[filtered_n_series](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/filtered_n_series/)に適切に配置されます。その後、次の系列**nSeries[1]**がリストの新しい最初のアイテムとなり、すべての系列が一つずつ前にシフトします。つまり、もし**chart.nSeries[1].is_filtered = TRUE;**を実行すると、元の第3系列を除去します。この操作は混乱を招くこともあるため、コード内の操作は、末尾から先頭へ削除する方法を推奨します。

![todo:image_alt_text](Figure1.png)

![todo:image_alt_text](Figure2.png)

### **サンプルコード**
次のサンプルコードは、[サンプルExcelファイル](seriesFiltered.xlsx)を読み込みます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-seriesFiltered.py" >}}

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-DataFilters.py" >}}

## **3. テーブルを使用してデータをフィルターし、グラフを変更します**

テーブルを使用することは、範囲を使用する方法2と似ていますが、テーブルには範囲よりも優れた点があります。 テーブルに範囲を変更してデータを追加すると、チャートが自動的に更新されます。 範囲の場合、データソースを変更する必要があります。

### **Excelでテーブルとしてフォーマット**

データ内をクリックし、**CTRL + T** を使用するか、**ホーム** タブ、**テーブルの書式設定** を使用します。

![todo:image_alt_text](Figure4.png)

### **サンプルコード**
次のサンプルコードは、[サンプルExcelファイル](TableFilters.xlsx) を使用して、Aspose.Cellsを使用して同じ機能を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-TableFilters.py" >}}
