---
title: Microsoft Excelファイルのテーブルを作成および管理する
linktitle: テーブル
type: docs
weight: 150
url: /ja/net/create-and-format-table/
description: Aspose.Cellsライブラリを使用して、Microsoft Excelファイルのテーブルの挿入、サイズ変更、編集、削除、フォーマットを行う。
---

## **テーブルの作成**

スプレッドシートの利点の1つは、電話リスト、タスクリスト、取引のリスト、資産リスト、負債リストなど、さまざまなタイプのリストを作成できることです。複数のユーザーが協力して、さまざまなリストを利用、作成、維持することができます。

Aspose.Cellsはリストの作成と管理をサポートしています。

### **リストオブジェクトの利点**

実際のリストオブジェクトにデータのリストを変換するときの利点はいくつかあります。

- 新しい行や列が自動的に含まれます。
- リストの最下部に合計、平均、カウントなどを表示するために総合行を簡単に追加できます。
- 右に追加された列は自動的にリストオブジェクトに取り込まれます。
- 行と列に基づくチャートは自動的に拡張されます。
- 行と列に割り当てられた名前付き範囲は自動的に拡張されます。
- リストは誤って行や列が削除されないように保護されています。

### **Microsoft Excelを使用してリストオブジェクトを作成する**

リストオブジェクトを作成するためのデータ範囲を選択
- これはリスト作成ダイアログを表示します。
- データオブジェクトを実装し、合計行を指定します（**データ**、**リスト**、**合計行**の順に選択）。

### **Aspose.Cells APIを使用する**

Aspose.Cellsは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスを提供します。 [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには、Excelファイルの各ワークシートにアクセスできる[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)コレクションが含まれています。

ワークシートは[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) クラスはワークシートの管理に幅広いプロパティとメソッドを提供します。ワークシートに[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) を作成するには、[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) クラスの[**ListObjects**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/listobjects) コレクションプロパティを使用します。それぞれの[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) は実際には[**ListObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection) クラスのオブジェクトであり、さらにリストオブジェクトを追加し、リストに含まれるセルの範囲を指定する[**Add**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection/methods/add/index) メソッドを提供しています。

Aspose.Cellsによって指定されたセル範囲に基づいて、リストオブジェクトが作成されます。 [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) クラスの属性（例：[**ShowTotals**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/showtotals)、[**ListColumns**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/listcolumns)など）を使用して、リストを制御します。

以下の例では、上のセクションでMicrosoft Excelを使用して作成したものと同じ[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)をAspose.Cells APIを使用して作成しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-CreatingListObject-1.cs" >}}

## **表の書式設定**

関連するデータのグループを管理および分析するには、セル範囲をリストオブジェクト（またはExcelテーブルとも呼ばれる）に変換することができます。 テーブルは、他の行や列のデータから独立して管理される関連データを含む行と列のシリーズです。 テーブルの各列には、ヘッダー行でフィルタリングが有効になっており、リストオブジェクトデータを迅速にフィルタリングまたは並べ替えることができます。 リストオブジェクトには特別な行（数値データで作業するために有用な集計関数の選択を提供するリスト内の特別な行）を追加することができます。 Aspose.Cellsには、リスト（またはテーブル）の作成と管理のためのオプションが用意されています。

### **リストオブジェクトの書式設定**

Aspose.Cellsは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスを提供します。 [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには、Excelファイルの各ワークシートにアクセスできる[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)コレクションが含まれています。

ワークシートは [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) クラスはワークシートの管理に幅広いプロパティとメソッドを提供します。ワークシートに[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) を作成するには、[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) クラスの[**ListObjects**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/listobjects) コレクションプロパティを使用します。それぞれの[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) は実際には[**ListObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection) クラスのオブジェクトであり、さらにリストオブジェクトを追加し、それが含むべきセルの範囲を指定する[**Add**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection/methods/add/index) メソッドを提供しています。指定されたセル範囲に基づいて、Aspose.Cellsによってワークシートに [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) が作成されます。 [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) クラスの属性（例：[**TableStyleType**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/tablestyletype)）を使用して、テーブルの形式をあなたの要件に合わせます。

以下の例では、ワークシートにサンプルデータを追加し、[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)を追加し、デフォルトのスタイルを適用します。マイクロソフトエクセル2007/2010で[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)のスタイルがサポートされています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-FormataListObject-1.cs" >}}

## **高度なトピック**
- [テーブルをODSに変換する](/cells/ja/net/convert-table-to-ods/)
- [外部データ接続に関連するクエリテーブルとリストオブジェクトを見つける](/cells/ja/net/find-query-tables-and-list-objects-related-to-external-data-connections/)
- [クエリテーブルデータソースを持つテーブルの読み書き](/cells/ja/net/read-and-write-table-with-query-table-data-source/)
- [ワークシート内のテーブルまたはリストオブジェクトのコメントを設定してください](/cells/ja/net/set-the-comment-of-table-or-list-object-inside-the-worksheet/)
- [表と範囲](/cells/ja/net/tables-and-ranges/)

{{< app/cells/assistant language="csharp" >}}
