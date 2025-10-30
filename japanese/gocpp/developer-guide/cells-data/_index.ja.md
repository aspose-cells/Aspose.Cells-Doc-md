---
title: Golangを使用したC++経由でのExcelデータ管理
linktitle: セルのデータ
type: docs
weight: 110
url: /ja/go-cpp/view-and-edit-excel-data/
description: この記事は、Aspose.Cellsライブラリを使用してC++でExcelファイルのデータを表示・編集する方法について説明しています。
keywords: Aspose.Cells C++でExcelファイルのデータ管理、データの追加、取得、効率的なデータ追加、セルデータの管理、セルデータの更新、セルデータ取得、セル挿入方法
---

{{% alert color="primary" %}}

[ワークシートのセルへのアクセス](/cells/ja/cpp/accessing-cells-of-a-worksheet/)では、ワークシート内のセルにアクセスするための基本的なアプローチについて説明しました。この記事では、これらのアプローチの1つを使用して、異なる種類のデータをセルに追加します。

{{% /alert %}}

## **セルにデータを追加する方法**

Aspose.Cellsは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/)クラスには、Excelファイルの各ワークシートへのアクセスを可能にする[**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)コレクションが含まれています。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスは[**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクションを提供します。[**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクション内の各アイテムは[**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)クラスのオブジェクトを表します。

Aspose.Cellsでは、[**Cell**](https://reference.aspose.com/cells/go-cpp/cell/)クラスの[**PutValue**](https://reference.aspose.com/cells/go-cpp/cell/putvalue/)メソッドを呼び出すことで、ワークシートのセルにデータを追加できます。Aspose.Cellsは、[**PutValue**](https://reference.aspose.com/cells/go-cpp/cell/putvalue/)メソッドのオーバーロードバージョンを提供し、開発者は異なる種類のデータをセルに追加できます。これらの[**PutValue**](https://reference.aspose.com/cells/go-cpp/cell/putvalue/)メソッドのオーバーロードバージョンを使用することで、セルにブール値、文字列、倍精度浮動小数点数、整数、日付/時間などを追加することが可能です。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CellsData.go" >}}
## **効率を向上させる方法**

[**PutValue**](https://reference.aspose.com/cells/go-cpp/cell/putvalue_bool/)メソッドを使用してワークシートに大量のデータを追加する場合は、まず行ごとに、次に列ごとに値をセルに追加するべきです。このアプローチにより、アプリケーションの効率が大幅に向上します。

## **セルからデータを取得する方法**

Aspose.Cellsは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/)クラスには、ファイル内のワークシートへのアクセスを可能にする[**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)コレクションが含まれています。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスは[**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクションを提供します。[**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクション内の各アイテムは[**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)クラスのオブジェクトを表します。

[**Cell**](https://reference.aspose.com/cells/go-cpp/cell/)クラスには、それぞれのデータ型に応じてセルから値を取得するためのいくつかのプロパティが提供されています。

- [**StringValue**](https://reference.aspose.com/cells/go-cpp/cell/getstringvalue_cellvalueformatstrategy/)：セルの文字列値を返します。
- [**DoubleValue**](https://reference.aspose.com/cells/go-cpp/cell/getdoublevalue/)：セルの倍精度浮動小数点数値を返します。
- [**BoolValue**](https://reference.aspose.com/cells/go-cpp/cell/getboolvalue/)：セルのブール値を返します。
- [**DateTimeValue**](https://reference.aspose.com/cells/go-cpp/cell/getdatetimevalue/)：セルの日付/時刻値を返します。
- [**FloatValue**](https://reference.aspose.com/cells/go-cpp/cell/getfloatvalue/)：セルの浮動小数点数値を返します。
- [**IntValue**](https://reference.aspose.com/cells/go-cpp/cell/getintvalue/)：セルの整数値を返します。

フィールドが埋められていない場合、[**DoubleValue**](https://reference.aspose.com/cells/go-cpp/cell/getdoublevalue/)または[**FloatValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/)のセルは例外をスローします。

また、[**Cell**](https://reference.aspose.com/cells/go-cpp/cell/)クラスの[**Type**](https://reference.aspose.com/cells/go-cpp/cell/gettype/)プロパティを使用してセルに含まれるデータの型を確認することもできます。実際、[**Cell**](https://reference.aspose.com/cells/go-cpp/cell/)クラスの[**Type**](https://reference.aspose.com/cells/go-cpp/cell/gettype/)プロパティは、その前に定義された値がリストされた[**CellValueType**](https://reference.aspose.com/cells/cpp/aspose.cells/cellvaluetype/)列挙型に基づいています。

|**セル値の種類**|**説明**|
| :- | :- |
|IsBool|セルの値がブール型であることを指定します。|
|IsDateTime|セルの値が日付/時刻であることを指定します。|
|IsNull|空白セルを表します。|
|IsNumeric|セルの値が数値であることを指定します。|
|IsString|セルの値が文字列であることを指定します。|
|IsUnknown|セルの値が不明であることを指定します。|

上記の事前定義されたセル値タイプを使用して、各セルに存在するデータのTypeと比較することもできます。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CellsData-1.go" >}}
{{% alert color="primary" %}}

ワークシートで作業している間、ユーザーはセルに異なるタイプのデータを追加することがあります。これらのデータ型には、ブール値、整数、浮動小数点、テキスト、日付/時刻値が含まれる場合があります。Aspose.Cellsを使用すると、セルから適切な値をデータ型に応じて取得できます。

{{% /alert %}}

## **高度なトピック**
- [ワークシートのセルへのアクセス](/cells/ja/cpp/accessing-cells-of-a-worksheet/)
- [テキスト数値データを数値に変換](/cells/ja/cpp/convert-text-numeric-data-to-number/)
- [小計を作成する](/cells/ja/cpp/creating-subtotals/)
- [データのフィルタリング](/cells/ja/cpp/data-filtering/)
- [データのソート](/cells/ja/cpp/sort-data-of-excel/)
- [データの検証](/cells/ja/cpp/data-validation/)
- [データの検索](/cells/ja/cpp/find-or-search-data/)
- [書式設定ありおよびなしでセル文字列の値を取得](/cells/ja/cpp/get-cell-string-value-with-and-without-formatting/)
- [セル内に HTML リッチテキストを追加](/cells/ja/cpp/adding-html-rich-text-inside-the-cell/)
- [ExcelまたはOpenOfficeにハイパーリンクを挿入](/cells/ja/cpp/insert-hyperlinks-to-excel/)
- [列挙子の使用方法と場所](/cells/ja/cpp/how-and-where-to-use-enumerators/)
- [セル値の幅と高さをピクセル単位で計測](/cells/ja/cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [複数スレッドで同時にセル値を読み取る](/cells/ja/cpp/reading-cell-values-in-multiple-threads-simultaneously/)
- [セル名と行/列インデックスの変換](/cells/ja/cpp/names-and-indices/)
- [最初に行ごと、次に列ごとにデータを取得](/cells/ja/cpp/populate-data-first-by-row-then-by-column/)
- [セル値または範囲の先頭にシングルクォートのプレフィックスを保存](/cells/ja/cpp/preserve-single-quote-prefix-of-cell-value-or-range/)
- [セルのリッチテキストの部分にアクセスして更新](/cells/ja/cpp/access-and-update-the-portions-of-rich-text-of-cell/)
