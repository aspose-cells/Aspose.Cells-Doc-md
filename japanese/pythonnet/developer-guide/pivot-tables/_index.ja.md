---
title: ピボットテーブルの挿入
linktitle: ピボットテーブル
type: docs
weight: 160
url: /ja/python-net/create-pivot-table/
description: Aspose.Cells for Python via .NET を使用してピボット テーブルを作成し、書式設定します。
keywords: Create Pivot Table, Insert Pivot Table, Format Pivot Table.
---
##  **ピボットテーブルの作成**

Aspose.Cells for Python via .NET を使用して、プログラムでスプレッドシートにピボット テーブルを追加することができます。

###  **ピボットテーブルオブジェクトモデル**

Aspose.Cells for Python via .NET は、[**aspose.cells.pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/)ピボット テーブルの作成と制御に使用される名前空間。これらのクラスは、作成および設定するために使用されます。[**ピボットテーブル**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/)オブジェクト、ピボット テーブルの構成要素。オブジェクトは次のとおりです。

- [**ピボットフィールド**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/)内のフィールドを表します[**ピボットテーブル**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/).
- [**ピボットフィールドコレクション**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection)すべてのコレクションを表します[**ピボットフィールド**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield)内のオブジェクト[**ピボットテーブル**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable).
- [**ピボットテーブル**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable)ワークシート上のピボットテーブルを表します。
- [**ピボットテーブルコレクション**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection)すべてのコレクションを表します[**ピボットテーブル**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable)ワークシート上のオブジェクト。

###  **Aspose.Cells を使用した単純なピボット テーブルの作成**

1. を使用してワークシートにデータを追加します。[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)オブジェクトの[**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#str)方法。
このデータはピボット テーブルのデータ ソースとして使用されます。
1. を呼び出してピボット テーブルをワークシートに追加します。[**ピボットテーブル**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection)コレクションの[**追加**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/add/#str-str-str)メソッド。Worksheet オブジェクトにカプセル化されます。
1. 新しいものにアクセスする[**ピボットテーブル**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable)からのオブジェクト[**ピボットテーブル**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection)ピボットテーブル インデックスを渡すことによってコレクションを取得します。
1. のいずれかを使用してください[**ピボットテーブル**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable)ピボット テーブルを管理するためのオブジェクト (上で説明)。

サンプル コードを実行すると、ピボット テーブルがワークシートに追加されます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-CreatePivotTable-1.py" >}}

{{% alert color="primary" %}}

セル範囲をデータ ソースとして割り当てる場合、範囲は左上から右下までである必要があります。たとえば、「A1:C3」は有効ですが、「C3:A1」は無効です。

{{% /alert %}}

##  **アドバンストトピック**
- [集約機能](/cells/ja/python-net/consolidation-function/)
- [ピボットテーブルでのカスタム並べ替え](/cells/ja/python-net/custom-sorting-in-pivot-table/)
- [ピボットテーブルのグローバリゼーション設定をカスタマイズする](/cells/ja/python-net/customize-globalization-settings-for-pivot-table/)
- [ピボットテーブルのリボンを無効にする](/cells/ja/python-net/disable-pivot-table-ribbons/)
- [親ピボット テーブルのネストされたピボット テーブルまたは子ピボット テーブルを検索して更新する](/cells/ja/python-net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/)
- [ピボットテーブルの書式設定](/cells/ja/python-net/formatting-pivot-table/)
- [ピボットテーブルの外部接続データソースの取得](/cells/ja/python-net/get-external-connection-data-source-of-pivot-table/)
- [ピボットテーブルの更新日と更新者情報を取得する](/cells/ja/python-net/get-pivot-table-refresh-date-and-refresh-by-who-information/)
- [ピボット テーブルのグループ ピボット フィールド](/cells/ja/python-net/group-pivot-fields-in-the-pivot-table/)
- [Excel ファイルのロード中にピボットのキャッシュされたレコードを解析する](/cells/ja/python-net/parsing-pivot-cached-records-while-loading-excel-file/)
- [ピボットテーブルとソースデータ](/cells/ja/python-net/pivot-table-and-source-data/)
- [ピボットテーブルのデータの非表示と並べ替え](/cells/ja/python-net/pivot-table-hide-and-sort-data/)
- [計算項目を含むピボット テーブルを更新して計算する](/cells/ja/python-net/refresh-and-calculate-pivot-table-having-calculated-items/)
- [ピボットテーブルをODSファイルに保存](/cells/ja/python-net/save-pivot-table-in-ods-file/)
- [レポートフィルターページオプションを表示する](/cells/ja/python-net/show-report-filter-pages-option/)
- [ピボットテーブルのデータフィールドのデータ表示形式を操作する](/cells/ja/python-net/working-with-data-display-formats-of-datafield-in-pivot-table/)
