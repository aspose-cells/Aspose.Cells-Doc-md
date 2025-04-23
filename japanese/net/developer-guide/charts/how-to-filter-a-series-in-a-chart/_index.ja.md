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

Aspose.Cellsでは、同様の操作を行うことができます。[サンプル](seriesFiltered.xlsx)ファイルのように、**Testseries2**と**Testseries4**をフィルタリングしたい場合、以下のコードを実行します。また、2つのリスト（[NSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/nseries/)）を保持し、すべての選択されたシリーズを格納するリストと、フィルター済みシリーズを格納するリストを作成します。

コード内で**chart.NSeries[0].IsFiltered = true;**と設定すると、[NSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/nseries/)の最初のシリーズが削除され、適切な位置に[FilteredNSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/filterednseries/)に置き換えられます。その後、**NSeries[1]**がリストの新しい最初のアイテムになり、次のシリーズは一つ前にシフトします。つまり、**chart.NSeries[1].IsFiltered = true;**を実行すると、もともとの3番目のシリーズが削除されます。混乱を避けるために、コードでは末尾から先頭に向かってシリーズを削除する操作を推奨します。

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
{{< app/cells/assistant language="csharp" >}}
