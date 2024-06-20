---
title: Excelファイルのデータ管理
linktitle: セルのデータ
type: docs
weight: 110
url: /ja/python-net/view-and-edit-excel-data/
description: この記事では、Aspose.Cells for Python via .NETライブラリを使用してExcelファイルのデータを表示および編集する方法について説明します。
keywords: Python Excelライブラリ、Aspose.Cells for Python Excelファイルのデータ管理、PythonでExcelファイルにデータを追加、PythonでExcelファイルからデータを取得する、Pythonでデータを追加する方法、Pythonでセルのデータを管理する方法、Pythonでセルのデータを更新する方法、Pythonでセルのデータを取得する方法、Pythonでセルのデータを挿入する方法。
---

{{% alert color="primary" %}}

Worksheetのセルへのアクセスについては、[ワークシートセルへのアクセス](/cells/ja/python-net/accessing-cells-of-a-worksheet/)で基本的なアプローチについて説明しました。この記事ではこれらのアプローチの1つを使用して、セルにさまざまな種類のデータを追加します。

{{% /alert %}}

## **セルにデータを追加する方法**

Aspose.Cells for Python via .NETは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスには[**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/)コレクションが含まれており、Excelファイルの各ワークシートにアクセスできます。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスには[**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/)コレクションがあります。[**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/)コレクションの各アイテムは[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)クラスのオブジェクトを表します。

Aspose.Cells for Python via .NETでは、[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)クラスの[**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#bool)メソッドを呼び出すことで、ワークシートのセルにデータを追加することができます。Aspose.Cells for Python via .NETには、異なる種類のデータをセルに追加できる[**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#int)メソッドのオーバーロードバージョンが用意されています。これらの[**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#int)メソッドのオーバーロードバージョンを使用することで、ブール値、文字列、倍精度浮動小数点数、整数、日付/時刻などをセルに追加することが可能です。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-AddingDataToCells-1.py" >}}

## **効率を向上させる方法**

[**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#int)メソッドを使用してワークシートに大量のデータを追加する場合は、まず行ごとに、次に列ごとに値をセルに追加するべきです。このアプローチにより、アプリケーションの効率が大幅に向上します。

## **セルからデータを取得する方法**

Aspose.Cells for Python via .NETは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスには[**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/)コレクションが含まれており、ファイル内のワークシートにアクセスできます。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスには[**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/)コレクションがあります。[**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/)コレクションの各アイテムは[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)クラスのオブジェクトを表します。

[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)クラスには、それぞれのデータ型に応じてセルから値を取得するためのいくつかのプロパティが提供されています。

- [**string_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/string_value/)：セルの文字列値を返します。
- [**double_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/double_value/)：セルの倍精度浮動小数点数値を返します。
- [**bool_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/bool_value/)：セルのブール値を返します。
- [**date_time_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/date_time_value/)：セルの日付/時刻値を返します。
- [**float_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/float_value/)：セルの浮動小数点数値を返します。
- [**int_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/int_value/)：セルの整数値を返します。

フィールドが埋められていない場合、[**double_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/double_value/)または[**float_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/float_value/)のセルは例外をスローします。

また、[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)クラスの[**type**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/type/)プロパティを使用してセルに含まれるデータの型を確認することもできます。実際、[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)クラスの[**type**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/type/)プロパティは、その前に定義された値がリストされた[**CellValueType**](https://reference.aspose.com/cells/python-net/aspose.cells/cellvaluetype)列挙型に基づいています。

|**セル値の種類**|**説明**|
| :- | :- |
|IS_BOOL|はセルの値がブール値であることを指定します。
|IS_DATE_TIME|はセルの値が日付/時刻であることを指定します。
|IS_NULL|は空白のセルを表します。
|IS_NUMERIC|はセルの値が数値であることを指定します。
|IS_STRING|セルの値が文字列であることを指定します。
|IS_ERROR|セルの値がエラー値であることを指定します。
|IS_UNKNOWN|セルの値が不明であることを指定します。

上記の事前定義されたセル値タイプを使用して、各セルに存在するデータのTypeと比較することもできます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-RetrievingDataFromCells-1.py" >}}

{{% alert color="primary" %}}

ワークシートで作業をしている間に、ユーザーはセルに異なるタイプのデータを追加する場合があります。これらのデータタイプには、ブール値、整数、浮動小数点、テキスト、日付/時刻値が含まれる場合があります。Aspose.Cells for Python via .NETを使用すると、セルの適切な値をデータタイプに応じて取得できます。

{{% /alert %}}

## **高度なトピック**
- [ワークシートのセルへのアクセス](/cells/ja/python-net/accessing-cells-of-a-worksheet/)
- [テキスト数値データを数値に変換](/cells/ja/python-net/convert-text-numeric-data-to-number/)
- [小計を作成する](/cells/ja/python-net/creating-subtotals/)
- [データのフィルタリング](/cells/ja/python-net/data-filtering/)
- [データのソート](/cells/ja/python-net/sort-data-of-excel/)
- [データの検証](/cells/ja/python-net/data-validation/)
- [書式設定ありおよびなしでセル文字列の値を取得](/cells/ja/python-net/get-cell-string-value-with-format-strategy/)
- [セル内に HTML リッチテキストを追加](/cells/ja/python-net/adding-html-rich-text-inside-the-cell/)
- [データの検索](/cells/ja/python-net/find-or-search-data/)
- [ExcelまたはOpenOfficeにハイパーリンクを挿入](/cells/ja/python-net/insert-hyperlinks-to-excel/)
- [セル値の幅と高さをピクセル単位で計測](/cells/ja/python-net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [セル名と行/列インデックスの変換](/cells/ja/python-net/names-and-indices/)
- [最初に行ごと、次に列ごとにデータを取得](/cells/ja/python-net/populate-data-first-by-row-then-by-column/)
- [セル値または範囲の先頭にシングルクォートのプレフィックスを保存](/cells/ja/python-net/preserve-single-quote-prefix-of-cell-value-or-range/)
- [セルのリッチテキストの部分にアクセスして更新](/cells/ja/python-net/access-and-update-the-portions-of-rich-text-of-cell/)
