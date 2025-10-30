---
title: Excelファイルのデータ管理
linktitle: セルのデータ
type: docs
weight: 110
url: /ja/nodejs-cpp/view-and-edit-excel-data/
description: この文章では、Node.jsとC++を使ったAspose.CellsライブラリによるExcelファイルのデータ表示と編集方法について説明します。
keywords: Aspose.Cells Node.jsをC++で使用し、Excelファイルのデータを管理、追加、取得し、データ追加の効率化やセルデータの管理・更新を行う方法
---

{{% alert color="primary" %}}

[ワークシートのセルにアクセス](/cells/ja/nodejs-cpp/accessing-cells-of-a-worksheet/)では、セルにアクセスする基本的なアプローチについて説明しました。この中の一つを使い、さまざまなタイプのデータをセルに追加しています。

{{% /alert %}}

## **セルにデータを追加する方法**

Aspose.Cells for Node.js via C++は、Microsoft Excelファイルを表すクラス[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)を提供します。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスには、Excelファイル内の各ワークシートにアクセス可能な[**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)コレクションが含まれます。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスは[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)コレクションを提供し、その[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)コレクションの各アイテムは[**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)クラスのオブジェクトを表します。

Aspose.Cellsでは、[**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)クラスの[**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-)メソッドを呼び出すことで、ワークシートのセルにデータを追加可能です。Aspose.Cellsは、[**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-)メソッドのオーバーロード版を提供しており、さまざまな種類のデータ（ブール値、文字列、倍精度浮動小数点、整数、日時など）をセルに追加できます。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-AddDataToCells.js" >}}


## **効率を向上させる方法**

大量のデータをシートに配置する場合は、まず行ごとに値を追加し、その後列に追加すると効率が大幅に向上します。

## **セルからデータを取得する方法**

Aspose.Cells for Node.js via C++は、Microsoft Excelファイルを表すクラス[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)を提供します。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスは、ファイル内のワークシートにアクセスできる[**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)コレクションを含みます。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスは[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)コレクションを提供します。その[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)コレクションの各アイテムは、[**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)クラスのオブジェクトを表します。

[**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)クラスは、データタイプに応じたセルの値を取得するいくつかのプロパティを提供します。これらのプロパティには：

- [**getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--): セルの文字列値を返します。
- [**getDoubleValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDoubleValue--): セルの倍精度値を返します。
- [**getBoolValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getBoolValue--): セルのブール値を返します。
- [**getDateTimeValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDateTimeValue--): セルの日時値を返します。
- [**getFloatValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFloatValue--): セルの浮動小数点値を返します。
- [**getIntValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getIntValue--): セルの整数値を返します。

フィールドが入力されていない場合、[**getDoubleValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDoubleValue--)または[**getFloatValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFloatValue--)を持つセルは例外をスローします。

セルに含まれるデータタイプは、[**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)クラスの[**getType()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getType--)メソッドを使用しても確認できます。実際、[**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)クラスの[**getType()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getType--)メソッドは、以下にリストされた事前定義済みの値を持つ[**CellValueType**](https://reference.aspose.com/cells/nodejs-cpp/cellvaluetype)列挙体に基づいています：

|**セル値の種類**|**説明**|
| :- | :- |
|IsBool|セルの値がブール型であることを指定します。|
|IsDateTime|セルの値が日付/時刻であることを指定します。|
|IsNull|空白セルを表します。|
|IsNumeric|セルの値が数値であることを指定します。|
|IsString|セルの値が文字列であることを指定します。|
|IsUnknown|セルの値が不明であることを指定します。|

上記の事前定義されたセル値タイプを使用して、各セルに存在するデータのTypeと比較することもできます。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-RetrieveDataFromCells.js" >}}


{{% alert color="primary" %}}

Worksheetの操作中に、ユーザーはセルにさまざまな種類のデータを追加することがあります。これらのデータタイプには、ブール値、整数、浮動小数点、テキスト、または日時値が含まれる場合があります。Aspose.Cellsを使用すると、それぞれのデータタイプに応じた適切な値をセルから取得できます。

{{% /alert %}}

## **高度なトピック**
- [ワークシートのセルへのアクセス](/cells/ja/nodejs-cpp/accessing-cells-of-a-worksheet/)
- [テキスト数値データを数値に変換](/cells/ja/nodejs-cpp/convert-text-numeric-data-to-number/)
- [小計を作成する](/cells/ja/nodejs-cpp/creating-subtotals/)
- [データのフィルタリング](/cells/ja/nodejs-cpp/data-filtering/)
- [データのソート](/cells/ja/nodejs-cpp/sort-data-of-excel/)
- [データの検証](/cells/ja/nodejs-cpp/data-validation/)
- [データの検索](/cells/ja/nodejs-cpp/find-or-search-data/)
- [書式設定ありおよびなしでセル文字列の値を取得](/cells/ja/nodejs-cpp/get-cell-string-value-with-and-without-formatting/)
- [セル内に HTML リッチテキストを追加](/cells/ja/nodejs-cpp/adding-html-rich-text-inside-the-cell/)
- [ExcelまたはOpenOfficeにハイパーリンクを挿入](/cells/ja/nodejs-cpp/insert-hyperlinks-to-excel/)
- [列挙子の使用方法と場所](/cells/ja/nodejs-cpp/how-and-where-to-use-enumerators/)
- [セル値の幅と高さをピクセル単位で計測](/cells/ja/nodejs-cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [複数スレッドで同時にセル値を読み取る](/cells/ja/nodejs-cpp/reading-cell-values-in-multiple-threads-simultaneously/)
- [セル名と行/列インデックスの変換](/cells/ja/nodejs-cpp/names-and-indices/)
- [最初に行ごと、次に列ごとにデータを取得](/cells/ja/nodejs-cpp/populate-data-first-by-row-then-by-column/)
- [セル値または範囲の先頭にシングルクォートのプレフィックスを保存](/cells/ja/nodejs-cpp/preserve-single-quote-prefix-of-cell-value-or-range/)
- [セルのリッチテキストの部分にアクセスして更新](/cells/ja/nodejs-cpp/access-and-update-the-portions-of-rich-text-of-cell/)
{{< app/cells/assistant language="nodejs-cpp" >}}
