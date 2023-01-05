---
title: Microsoft Excel ファイルのテーブルを作成して管理します。
linktitle: テーブル
type: docs
weight: 150
url: /ja/net/create-and-format-table/
description: Aspose.Cells ライブラリを使用して、Excel ファイルのテーブルを挿入、サイズ変更、編集、削除、フォーマットします。
---
## **テーブルの作成**

スプレッドシートの利点の 1 つは、電話番号リスト、タスク リスト、取引リスト、資産または負債のリストなど、さまざまな種類のリストを作成できることです。複数のユーザーが協力して、さまざまなリストを使用、作成、および維持できます。

Aspose.Cells は、リストの作成と管理をサポートしています。

### **リスト オブジェクトの利点**

データのリストを実際のリスト オブジェクトに変換すると、多くの利点があります。

- 新しい行と列が自動的に含まれます。
- リストの下部に合計行を簡単に追加して、SUM、AVERAGE、COUNT などを表示できます。
- 右側に追加された列は、List オブジェクトに自動的に組み込まれます。
- 行と列に基づくグラフは自動的に展開されます。
- 行と列に割り当てられた名前付き範囲は、自動的に展開されます。
- リストは、偶発的な行と列の削除から保護されています。

### **Microsoft Excel を使用してリスト オブジェクトを作成する**

- List オブジェクトを作成するためのデータ範囲の選択
- [リストの作成] ダイアログが表示されます。
- データの List オブジェクトを実装し、合計行を指定します (選択**データ**、 それから**リスト**、 に続く**合計行**).

### **Aspose.Cells API を使用**

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)、Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Excel ファイル内の各ワークシートにアクセスできるコレクション。

ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスには、ワークシートを管理するためのさまざまなプロパティとメソッドが用意されています。を作成するには[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)ワークシートでは、[**リストオブジェクト**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/listobjects)のコレクション プロパティ[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。各[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)実際には、[**ListObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection)クラスは、さらに[**追加**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection/methods/add/index)List オブジェクトを追加し、リストのセル範囲を指定するメソッド。

指定されたセル範囲に従って、List オブジェクトは Aspose.Cells によって作成されます。属性を使用します (たとえば、[**ShowTotals**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/showtotals), [**ListColumns**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/listcolumns)など）の[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)リストを制御するクラス。

以下の例では、同じものを作成しました[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)上記のセクションで Microsoft Excel を使用して作成したように、Aspose.Cells API を使用します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-CreatingListObject-1.cs" >}}

## **テーブルをフォーマットする**

関連するデータのグループを管理および分析するために、セルの範囲をリスト オブジェクト (Excel テーブルとも呼ばれます) に変換することができます。テーブルは、他の行や列のデータとは独立して管理される関連データを含む一連の行と列です。既定では、テーブルのすべての列のヘッダー行でフィルター処理が有効になっているため、リスト オブジェクト データをすばやくフィルター処理または並べ替えることができます。各合計行セルの集計関数のドロップダウン リストを提供するリスト オブジェクトに、合計行 (数値データの操作に役立つ集計関数の選択を提供するリスト内の特別な行) を追加できます。 Aspose.Cells は、リスト (またはテーブル) を作成および管理するためのオプションを提供します。

### **リスト オブジェクトの書式設定**

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)、Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Excel ファイル内の各ワークシートにアクセスできるコレクション。

ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスには、ワークシートを管理するためのさまざまなプロパティとメソッドが用意されています。を作成するには[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)ワークシートで、使用[**リストオブジェクト**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/listobjects)のコレクション プロパティ[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。各[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)実際には、[**ListObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection)クラスは、さらに[**追加**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection/methods/add/index)メソッドを使用して List オブジェクトを追加し、それが包含するセルの範囲を指定します。指定されたセル範囲に従って、[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)は Aspose.Cells によってワークシートに作成されます。属性を使用します (たとえば、[**表スタイルの種類**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/tablestyletype) ) の[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)クラスを使用して、要件に合わせてテーブルをフォーマットします。

以下の例では、サンプル データをワークシートに追加し、[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)それにデフォルトのスタイルを適用します。[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)スタイルは、Microsoft Excel 2007/2010 でサポートされています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-FormataListObject-1.cs" >}}

## **先行トピック**
- [テーブルを ODS に変換](/cells/ja/net/convert-table-to-ods/)
- [外部データ接続に関連するクエリ テーブルとリスト オブジェクトを検索する](/cells/ja/net/find-query-tables-and-list-objects-related-to-external-data-connections/)
- [クエリ テーブル データ ソースを使用したテーブルの読み取りと書き込み](/cells/ja/net/read-and-write-table-with-query-table-data-source/)
- [ワークシート内のテーブルまたはリスト オブジェクトのコメントを設定する](/cells/ja/net/set-the-comment-of-table-or-list-object-inside-the-worksheet/)
- [テーブルと範囲](/cells/ja/net/tables-and-ranges/)

