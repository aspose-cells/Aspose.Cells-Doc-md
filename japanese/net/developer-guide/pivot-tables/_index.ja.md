---
title: ピボットテーブルを挿入
linktitle: ピボットテーブル
type: docs
weight: 160
url: /ja/net/create-pivot-table/
description: Excel スプレッドシート ファイルのピボット テーブルを作成してフォーマットします。
---
## **ピボット テーブルの作成**

Aspose.Cells を使用して、ピボット テーブルをプログラムでスプレッドシートに追加することができます。

### **ピボット テーブル オブジェクト モデル**

Aspose.Cells は、[**Aspose.Cells.Pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot)ピボット テーブルの作成と制御に使用される名前空間。これらのクラスは、作成および設定に使用されます[**ピボットテーブル**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)オブジェクト、ピボット テーブルのビルディング ブロック。オブジェクトは次のとおりです。

- [**ピボットフィールド**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield)のフィールドを表します[**ピボットテーブル**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**ピボットフィールド コレクション**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection)すべてのコレクションを表します[**ピボットフィールド**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield)のオブジェクト[**ピボットテーブル**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**ピボットテーブル**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)ワークシート上のピボットテーブルを表します。
- [**ピボットテーブル コレクション**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection)すべてのコレクションを表します[**ピボットテーブル**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)ワークシート上のオブジェクト。

### **Aspose.Cells を使用して簡単なピボット テーブルを作成する**

1. を使用してワークシートにデータを追加する[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)オブジェクトの[**プットバリュー**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)方法。
このデータは、ピボット テーブルのデータ ソースとして使用されます。
1. を呼び出して、ワークシートにピボット テーブルを追加します。[**ピボットテーブル**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection)コレクションの[**追加**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/add/index)Worksheet オブジェクトにカプセル化されているメソッド。
1. 新しい[**ピボットテーブル**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)からのオブジェクト[**ピボットテーブル**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection)ピボットテーブル インデックスを渡すことでコレクションを作成します。
1. のいずれかを使用します。[**ピボットテーブル**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)オブジェクト (上記で説明) を使用してピボット テーブルを管理します。

サンプル コードを実行すると、ワークシートにピボット テーブルが追加されます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-CreatePivotTable-1.cs" >}}

{{% alert color="primary" %}}

セルの範囲をデータ ソースとして割り当てる場合、範囲は左上から右下に移動する必要があります。たとえば、「A1:C3」は有効ですが、「C3:A1」は無効です。

{{% /alert %}}

## **先行トピック**
- [連結機能](/cells/ja/net/consolidation-function/)
- [ピボット テーブルでのカスタム並べ替え](/cells/ja/net/custom-sorting-in-pivot-table/)
- [ピボット テーブルのグローバリゼーション設定のカスタマイズ](/cells/ja/net/customize-globalization-settings-for-pivot-table/)
- [ピボット テーブル リボンを無効にする](/cells/ja/net/disable-pivot-table-ribbons/)
- [親ピボット テーブルのネストされたピボット テーブルまたは子ピボット テーブルを検索して更新する](/cells/ja/net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/)
- [ピボット テーブルの書式設定](/cells/ja/net/formatting-pivot-table/)
- [ピボット テーブルの外部接続データ ソースを取得する](/cells/ja/net/get-external-connection-data-source-of-pivot-table/)
- [ピボット テーブルの更新日を取得し、誰が情報を更新するか](/cells/ja/net/get-pivot-table-refresh-date-and-refresh-by-who-information/)
- [ピボット テーブルでピボット フィールドをグループ化する](/cells/ja/net/group-pivot-fields-in-the-pivot-table/)
- [Excel ファイルの読み込み中にピボット キャッシュ レコードを解析する](/cells/ja/net/parsing-pivot-cached-records-while-loading-excel-file/)
- [ピボット テーブルとソース データ](/cells/ja/net/pivot-table-and-source-data/)
- [ピボット テーブルのデータの非表示と並べ替え](/cells/ja/net/pivot-table-hide-and-sort-data/)
- [計算項目を含むピボット テーブルの更新と計算](/cells/ja/net/refresh-and-calculate-pivot-table-having-calculated-items/)
- [ピボット テーブルを ODS ファイルに保存する](/cells/ja/net/save-pivot-table-in-ods-file/)
- [レポート フィルター ページの表示オプション](/cells/ja/net/show-report-filter-pages-option/)
- [ピボット テーブルでの DataField のデータ表示形式の操作](/cells/ja/net/working-with-data-display-formats-of-datafield-in-pivot-table/)
