---
title: Microsoft Excelファイルのテーブルを作成および管理する
linktitle: テーブル
type: docs
weight: 150
url: /ja/python-net/create-and-format-table/
description: Aspose.Cellsライブラリを使用して、Microsoft Excelファイルのテーブルの挿入、サイズ変更、編集、削除、フォーマットを行う。
---

## **テーブルの作成**

スプレッドシートの利点の1つは、電話リスト、タスクリスト、取引のリスト、資産リスト、負債リストなど、さまざまなタイプのリストを作成できることです。複数のユーザーが協力して、さまざまなリストを利用、作成、維持することができます。

Aspose.Cells for Python via .NETはリストの作成と管理をサポートしています。

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

### **Aspose.Cells for Python via .NET APIの使用例**

Aspose.Cells for Python via .NETは、Microsoft Excelファイルを表すクラス[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)を提供します。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスには、Excelファイル内の各ワークシートにアクセスするためのコレクションが含まれています。

ワークシートは[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) クラスはワークシートの管理に幅広いプロパティとメソッドを提供します。ワークシートに[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) を作成するには、[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) クラスの[**list_objects**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/list_objects) コレクションプロパティを使用します。それぞれの[**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) は実際には[**add**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobjectcollection/add/#int-int-int-int-bool) クラスのオブジェクトであり、さらにリストオブジェクトを追加し、リストに含まれるセルの範囲を指定する[**add**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobjectcollection/add/#int-int-int-int-bool) メソッドを提供しています。

指定されたセル範囲に基づいて、List オブジェクトはAspose.Cells for Python via .NETによって作成されます。[**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject)クラスの属性（例：[**show_totals**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject/show_totals)、[**ListColumns**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject/list_columns)など）を使ってリストを制御してください。

以下の例では、前述のセクションと同様にMicrosoft Excelを使用して作成したのと同じ[**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject)をAspose.Cells for Python via .NET APIを用いて作成しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Tables-CreatingListObject-1.py" >}}

## **表の書式設定**

関連するデータのグループを管理および分析するために、セル範囲をリストオブジェクト（Excelテーブルとも呼ばれる）に変換できます。テーブルは、関連するデータを含む行と列の集合であり、他の行や列のデータと独立して管理されます。デフォルトでは、テーブルの各列のヘッダー行にフィルタリングが有効になっており、リストオブジェクトのデータを迅速にフィルタリングや並べ替えが可能です。合計行（数値データの操作に便利な集計関数の選択肢を提供する特殊な行）をリストオブジェクトに追加すると、それぞれの合計行セルにドロップダウンリストの集計関数が表示されます。Aspose.Cells for Python via .NETは、リスト（またはテーブル）の作成と管理のオプションを提供します。

### **リストオブジェクトの書式設定**

Aspose.Cells for Python via .NETは、Microsoft Excelファイルを表すクラス[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)を提供します。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスは、Excelファイル内の各ワークシートにアクセスできる[**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets)コレクションを含んでいます。

ワークシートは [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) クラスはワークシートの管理に幅広いプロパティとメソッドを提供します。ワークシートに[**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) を作成するには、[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) クラスの[**list_objects**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/list_objects) コレクションプロパティを使用します。それぞれの[**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) は実際には[**ListObjectCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobjectcollection) クラスのオブジェクトであり、さらにリストオブジェクトを追加し、それが含むべきセルの範囲を指定する[**add**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobjectcollection/add/#int-int-int-int-bool) メソッドを提供しています。指定されたセル範囲に基づいて、Aspose.Cellsによってワークシートに [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) が作成されます。 [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) クラスの属性（例：[**table_style_type**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject/table_style_type)）を使用して、テーブルの形式をあなたの要件に合わせます。

以下の例では、ワークシートにサンプルデータを追加し、[**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject)を追加し、デフォルトのスタイルを適用します。マイクロソフトエクセル2007/2010で[**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject)のスタイルがサポートされています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Tables-FormataListObject-1.py" >}}

## **高度なトピック**
- [テーブルをODSに変換する](/cells/ja/python-net/convert-table-to-ods/)
- [外部データ接続に関連するクエリテーブルとリストオブジェクトを見つける](/cells/ja/python-net/find-query-tables-and-list-objects-related-to-external-data-connections/)
- [クエリテーブルデータソースを持つテーブルの読み書き](/cells/ja/python-net/read-and-write-table-with-query-table-data-source/)
- [ワークシート内のテーブルまたはリストオブジェクトのコメントを設定してください](/cells/ja/python-net/set-the-comment-of-table-or-list-object-inside-the-worksheet/)
- [表と範囲](/cells/ja/python-net/tables-and-ranges/)


{{< app/cells/assistant language="python-net" >}}
