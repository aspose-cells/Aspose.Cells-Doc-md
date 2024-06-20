---
title: ピボットテーブルを挿入する
linktitle: ピボットテーブル
type: docs
weight: 160
url: /ja/net/create-pivot-table/
description: Excelスプレッドシートファイルのピボットテーブルを作成し、書式を設定する。
---

## **ピボットテーブルの作成**

Aspose.Cellsを使用してプログラムでスプレッドシートにピボットテーブルを追加することができます。

### **ピボットテーブルオブジェクトモデル**

Aspose.Cellsには、ピボットテーブルを作成し制御するための[**Aspose.Cells.Pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot)名前空間内の特別なクラスがあります。これらのクラスは、ピボットテーブルの構成要素である[**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)オブジェクトを作成および設定するために使用されます。オブジェクトには以下のものがあります:

- [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield)は、[**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)のフィールドを表します。
- [**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection)は、[**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)のすべての[**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield)オブジェクトのコレクションを表します。
- [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)は、ワークシート上のPivotTableを表します。
- [**PivotTableCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection)は、ワークシート上のすべての[**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)オブジェクトのコレクションを表します。

### **Aspose.Cellsを使用して簡単なピボットテーブルを作成する**

1. [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)オブジェクトの[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)メソッドを使用してワークシートにデータを追加します。
   このデータは、ピボットテーブルのデータソースとして使用されます。
1. ワークシートにピボットテーブルを追加するために、[**PivotTables**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection)コレクションの[**add**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/add/index)メソッドを呼び出します。このメソッドはWorksheetオブジェクトでカプセル化されています。
1. 新しい[**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)オブジェクトを[**PivotTables**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection)コレクションから取得します。このコレクションはPivotTableのインデックスを渡すことでアクセスできます。
1. ピボットテーブルを管理するために、上記で説明した[**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)のいずれかを使用します。

例のコードを実行すると、ワークシートにピボットテーブルが追加されます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-CreatePivotTable-1.cs" >}}

{{% alert color="primary" %}}

データソースとしてセル範囲を割り当てるときには、範囲は左上から右下に向かっている必要があります。例えば、「A1:C3」は有効ですが、「C3:A1」は無効です。

{{% /alert %}}

## **高度なトピック**
- [集約関数](/cells/ja/net/consolidation-function/)
- [ピボットテーブルのカスタムソート](/cells/ja/net/custom-sorting-in-pivot-table/)
- [ピボットテーブルのグローバリゼーション設定のカスタマイズ](/cells/ja/net/customize-globalization-settings-for-pivot-table/)
- [ピボットテーブルリボンの無効化](/cells/ja/net/disable-pivot-table-ribbons/)
- [親ピボットテーブルのネストされたピボットテーブルや子ピボットテーブルを見つけて更新する](/cells/ja/net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/)
- [ピボットテーブルの書式設定](/cells/ja/net/formatting-pivot-table/)
- [ピボットテーブルの外部接続データソースの取得](/cells/ja/net/get-external-connection-data-source-of-pivot-table/)
- [ピボットキャッシュレコードを解析してExcelファイルをロードする際の操作](/cells/ja/net/get-pivot-table-refresh-date-and-refresh-by-who-information/)
- [ピボットテーブル内のPivot Fieldをグループ化](/cells/ja/net/group-pivot-fields-in-the-pivot-table/)
- [Excelファイルをロードする際にPivotキャッシュレコードを解析する](/cells/ja/net/parsing-pivot-cached-records-while-loading-excel-file/)
- [ピボットテーブルの非表示およびデータのソート](/cells/ja/net/pivot-table-and-source-data/)
- [ピボットテーブルのデータを非表示にしたり並べ替えたり](/cells/ja/net/pivot-table-hide-and-sort-data/)
- [計算項目を持つピボットテーブルを更新および計算する](/cells/ja/net/refresh-and-calculate-pivot-table-having-calculated-items/)
- [レポートフィルタページオプションを表示](/cells/ja/net/save-pivot-table-in-ods-file/)
- [レポートフィルターページのオプションを表示](/cells/ja/net/show-report-filter-pages-option/)
- [行と列のフォーマット](/cells/ja/net/working-with-data-display-formats-of-datafield-in-pivot-table/)
