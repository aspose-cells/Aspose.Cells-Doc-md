---
title: Excelファイルのデータ管理
linktitle: Cells データ
type: docs
weight: 110
url: /ja/net/view-and-edit-excel-data/
description: この記事では、Aspose.Cells ライブラリを使用して Excel ファイルのデータを表示および編集する方法について説明します。
keywords: Aspose.Cells C# Manage data of Excel file, add data to Excel file, get data from excel file, How to Improve Efficiency of adding data, manage cells data, update cells data, get cells data, insert cells data
---
{{% alert color="primary" %}}

で[ワークシートの Cells へのアクセス](/cells/ja/net/accessing-cells-of-a-worksheet/)では、ワークシート内のセルにアクセスするための基本的なアプローチについて説明しました。この記事では、これらのアプローチの 1 つを使用して、さまざまな種類のデータをセルに追加します。

{{% /alert %}}

##  **Cellsにデータを追加する方法**

Aspose.Cells はクラスを提供します。[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)、これは Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Excel ファイル内の各ワークシートへのアクセスを許可するコレクション。ワークシートは次のように表されます。[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスが提供するのは[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクション。の各項目[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクションはオブジェクトを表します[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラス。

 Aspose.Cells を使用すると、開発者は、[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラス'[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)方法。 Aspose.Cells は、オーバーロードされたバージョンの[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)開発者がさまざまな種類のデータをセルに追加できるメソッド。これらのオーバーロードされたバージョンの使用[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)メソッドを使用すると、ブール値、文字列、倍精度浮動小数点数、整数、日付/時刻などの値をセルに追加できます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AddingDataToCells-1.cs" >}}

##  **効率を向上させる方法**

使用する場合[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)大量のデータをワークシートに配置する方法では、最初に行ごと、次に列ごとにセルに値を追加する必要があります。このアプローチにより、アプリケーションの効率が大幅に向上します。

##  **Cells からデータを取得する方法**

Aspose.Cells はクラスを提供します。[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)これは Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)ファイル内のワークシートへのアクセスを許可するコレクション。ワークシートは次のように表されます。[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスが提供するのは[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクション。の各項目[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクションはオブジェクトを表します[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラス。

の[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラスには、開発者がデータ型に応じてセルから値を取得できるようにするいくつかのプロパティが用意されています。これらのプロパティには次のものが含まれます。

- [**文字列値**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/stringvalue)セルの文字列値を返します。
- [**ダブルバリュー**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/doublevalue)セルの double 値を返します。
- [**ブール値**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/boolvalue)セルのブール値を返します。
- [**日付時刻値**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/datetimevalue)セルの日付/時刻値を返します。
- [**FloatValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/floatvalue): セルの浮動小数点値を返します。
- [**整数値**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/intvalue)セルの整数値を返します。

フィールドが入力されていない場合、次のセルが表示されます。[**ダブルバリュー**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/doublevalue)または[**FloatValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/floatvalue)例外をスローします。

セルに含まれるデータの種類は、[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラス'[**タイプ**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/type)財産。実際、[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラス'[**タイプ**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/type)プロパティは、[**CellValueType**](https://reference.aspose.com/cells/net/aspose.cells/cellvaluetype)事前定義された値が以下にリストされている列挙体。

|**Cell 値のタイプ**|**説明**|
| :- | :- |
|イズブール|セル値がブール値であることを指定します。|
|IsDateTime|セル値が日付/時刻であることを指定します。|
|無効である|空白のセルを表します。|
|数値です|セル値が数値であることを指定します。|
|文字列|セル値が文字列であることを指定します。|
|不明です|セル値が不明であることを指定します。|

上記の事前定義されたセル値のタイプを使用して、各セルに存在するデータのタイプと比較することもできます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-RetrievingDataFromCells-1.cs" >}}

{{% alert color="primary" %}}

ワークシートで作業しているときに、ユーザーはセルにさまざまな種類のデータを追加できます。これらのデータ型には、ブール値、整数、浮動小数点、テキスト、または日付/時刻値が含まれる場合があります。 Aspose.Cells を使用すると、データ型に応じてセルから適切な値を取得できます。

{{% /alert %}}

##  **アドバンストトピック**
- [ワークシートの Cells へのアクセス](/cells/ja/net/accessing-cells-of-a-worksheet/)
- [テキスト数値データを数値に変換](/cells/ja/net/convert-text-numeric-data-to-number/)
- [小計の作成](/cells/ja/net/creating-subtotals/)
- [データフィルタリング](/cells/ja/net/data-filtering/)
- [データの並べ替え](/cells/ja/net/sort-data-of-excel/)
- [データ検証](/cells/ja/net/data-validation/)
- [ワークシートからデータをエクスポート](/cells/ja/net/export-data-from-worksheet/)
- [データの検索または検索](/cells/ja/net/find-or-search-data/)
- [書式設定ありまたはなしで Cell 文字列値を取得する](/cells/ja/net/get-cell-string-value-with-and-without-formatting/)
- [Cell 内に HTML リッチ テキストを追加](/cells/ja/net/adding-html-rich-text-inside-the-cell/)
- [Excel または OpenOffice にハイパーリンクを挿入する](/cells/ja/net/insert-hyperlinks-to-excel/)
- [データをワークシートにインポート](/cells/ja/net/import-data-into-worksheet/)
- [列挙子の使用方法と使用場所](/cells/ja/net/how-and-where-to-use-enumerators/)
- [Cell 値の幅と高さをピクセル単位で測定します](/cells/ja/net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [複数のスレッドで同時に Cell 値を読み取る](/cells/ja/net/reading-cell-values-in-multiple-threads-simultaneously/)
- [セル名と行/列インデックス間の変換](/cells/ja/net/names-and-indices/)
- [最初に行ごとにデータを入力し、次に列ごとにデータを入力します](/cells/ja/net/populate-data-first-by-row-then-by-column/)
- [Cell 値または範囲の一重引用符プレフィックスを保持する](/cells/ja/net/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Cell のリッチ テキストの部分にアクセスして更新する](/cells/ja/net/access-and-update-the-portions-of-rich-text-of-cell/)



