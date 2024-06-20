---
title: ピボットテーブルを挿入する
linktitle: ピボットテーブル
type: docs
weight: 160
url: /ja/python-net/create-pivot-table/
description: Aspose.Cells for Python via .NETでピボットテーブルを作成し、書式を設定する。
keywords: ピボットテーブルを作成し、ピボットテーブルを挿入し、ピボットテーブルを書式設定します。
---

## **ピボットテーブルの作成**

Aspose.Cells for Python via .NETを使用して、プログラムでピボットテーブルをスプレッドシートに追加することが可能です。

### **ピボットテーブルオブジェクトモデル**

Aspose.Cells for Python via .NETでは、ピボットテーブルを作成および制御するために使用される特別なクラスのセットが提供されています。これらのクラスは、ピボットテーブルの構成要素である[**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/)オブジェクトを作成および制御するために使用されます。オブジェクトは次のとおりです:

- [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/)は、[**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/)のフィールドを表します。
- [**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection)は、[**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable)のすべての[**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield)オブジェクトのコレクションを表します。
- [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable)は、ワークシート上のPivotTableを表します。
- [**PivotTableCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection)は、ワークシート上のすべての[**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable)オブジェクトのコレクションを表します。

### **Aspose.Cellsを使用して簡単なピボットテーブルを作成する**

1. [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)オブジェクトの[**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#str)メソッドを使用してワークシートにデータを追加します。
   このデータは、ピボットテーブルのデータソースとして使用されます。
1. ワークシートにピボットテーブルを追加するために、[**PivotTables**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection)コレクションの[**add**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/add/#str-str-str)メソッドを呼び出します。このメソッドはWorksheetオブジェクトでカプセル化されています。
1. 新しい[**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable)オブジェクトを[**PivotTables**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection)コレクションから取得します。このコレクションはPivotTableのインデックスを渡すことでアクセスできます。
1. ピボットテーブルを管理するために、上記で説明した[**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable)のいずれかを使用します。

例のコードを実行すると、ワークシートにピボットテーブルが追加されます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-CreatePivotTable-1.py" >}}

{{% alert color="primary" %}}

データソースとしてセル範囲を割り当てるときには、範囲は左上から右下に向かっている必要があります。例えば、「A1:C3」は有効ですが、「C3:A1」は無効です。

{{% /alert %}}

## **高度なトピック**
- [集約関数](/cells/ja/python-net/consolidation-function/)
- [ピボットテーブルのカスタムソート](/cells/ja/python-net/custom-sorting-in-pivot-table/)
- [ピボットテーブルのグローバリゼーション設定のカスタマイズ](/cells/ja/python-net/customize-globalization-settings-for-pivot-table/)
- [ピボットテーブルリボンの無効化](/cells/ja/python-net/disable-pivot-table-ribbons/)
- [親ピボットテーブルのネストされたピボットテーブルや子ピボットテーブルを見つけて更新する](/cells/ja/python-net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/)
- [ピボットテーブルの書式設定](/cells/ja/python-net/formatting-pivot-table/)
- [ピボットテーブルの外部接続データソースの取得](/cells/ja/python-net/get-external-connection-data-source-of-pivot-table/)
- [ピボットキャッシュレコードを解析してExcelファイルをロードする際の操作](/cells/ja/python-net/get-pivot-table-refresh-date-and-refresh-by-who-information/)
- [ピボットテーブル内のPivot Fieldをグループ化](/cells/ja/python-net/group-pivot-fields-in-the-pivot-table/)
- [Excelファイルをロードする際にPivotキャッシュレコードを解析する](/cells/ja/python-net/parsing-pivot-cached-records-while-loading-excel-file/)
- [ピボットテーブルの非表示およびデータのソート](/cells/ja/python-net/pivot-table-and-source-data/)
- [ピボットテーブルのデータを非表示にしたり並べ替えたり](/cells/ja/python-net/pivot-table-hide-and-sort-data/)
- [計算項目を持つピボットテーブルを更新および計算する](/cells/ja/python-net/refresh-and-calculate-pivot-table-having-calculated-items/)
- [レポートフィルタページオプションを表示](/cells/ja/python-net/save-pivot-table-in-ods-file/)
- [レポートフィルターページのオプションを表示](/cells/ja/python-net/show-report-filter-pages-option/)
- [行と列のフォーマット](/cells/ja/python-net/working-with-data-display-formats-of-datafield-in-pivot-table/)
