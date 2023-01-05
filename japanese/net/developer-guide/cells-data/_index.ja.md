---
title: Excelファイルのデータ管理。
linktitle: Cells データ
type: docs
weight: 110
url: /ja/net/view-and-edit-excel-data/
description: この記事では、Aspose.Cells ライブラリを使用して Excel ファイルのデータを表示および編集する方法について説明します。
---
{{% alert color="primary" %}}

の[ワークシートの Cells へのアクセス](/cells/ja/net/accessing-cells-of-a-worksheet/)では、ワークシート内のセルにアクセスするための基本的な方法について説明しました。この記事では、これらのアプローチの 1 つを使用して、さまざまな種類のデータをセルに追加します。

{{% /alert %}}

## **Cells にデータを追加する**

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)、Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Excel ファイル内の各ワークシートにアクセスできるコレクション。ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスは[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクション。の各項目[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクションはのオブジェクトを表します[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラス。

Aspose.Cells を使用すると、開発者は、[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラス'[**プットバリュー**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)方法。 Aspose.Cells は、[**プットバリュー**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)開発者がさまざまな種類のデータをセルに追加できるようにするメソッド。これらのオーバーロードされたバージョンの[**プットバリュー**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)メソッドを使用すると、ブール値、文字列、倍精度、整数、日付/時刻などの値をセルに追加できます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AddingDataToCells-1.cs" >}}

## **効率の向上**

使用する場合[**プットバリュー**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)メソッドを使用して大量のデータをワークシートに配置するには、最初に行ごと、次に列ごとにセルに値を追加する必要があります。このアプローチにより、アプリケーションの効率が大幅に向上します。

## **Cells からのデータの取得**

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)ファイル内のワークシートへのアクセスを許可するコレクション。ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスは[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクション。の各項目[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクションはのオブジェクトを表します[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラス。

の[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラスには、開発者がデータ型に従ってセルから値を取得できるいくつかのプロパティが用意されています。これらのプロパティは次のとおりです。

- [**文字列値**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/stringvalue)セルの文字列値を返します。
- [**DoubleValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/doublevalue): セルの double 値を返します。
- [**ブール値**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/boolvalue): セルのブール値を返します。
- [**日時値**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/datetimevalue): セルの日付/時刻の値を返します。
- [**浮動小数点値**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/floatvalue): セルの float 値を返します。
- [**IntValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/intvalue)セルの整数値を返します。

フィールドが入力されていない場合、[**DoubleValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/doublevalue)また[**浮動小数点値**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/floatvalue)例外をスローします。

セルに含まれるデータの種類は、[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラス'[**タイプ**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/type)財産。実際、[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラス'[**タイプ**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/type)プロパティはに基づいています[**CellValueType**](https://reference.aspose.com/cells/net/aspose.cells/cellvaluetype)定義済みの値が以下にリストされている列挙型:

|**Cell 値の種類**|**説明**|
|:- |:- |
|IsBool|セル値がブールであることを指定します。|
|IsDateTime|セル値が日付/時刻であることを指定します。|
|無効です|空白のセルを表します。|
|IsNumeric|セル値が数値であることを指定します。|
|IsString|セル値が文字列であることを指定します。|
|不明|セル値が不明であることを指定します。|

上記の事前定義されたセル値タイプを使用して、各セルに存在するデータのタイプと比較することもできます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-RetrievingDataFromCells-1.cs" >}}

{{% alert color="primary" %}}

ワークシートで作業している間、ユーザーはセルにさまざまな種類のデータを追加できます。これらのデータ型には、ブール、整数、浮動小数点、テキスト、または日付/時刻の値が含まれる場合があります。 Aspose.Cells を使用すると、データ型に従ってセルから適切な値を取得できます。

{{% /alert %}}

## **先行トピック**
- [ワークシートの Cells へのアクセス](/cells/ja/net/accessing-cells-of-a-worksheet/)
- [テキスト数値データを数値に変換する](/cells/ja/net/convert-text-numeric-data-to-number/)
- [小計の作成](/cells/ja/net/creating-subtotals/)
- [データフィルタリング](/cells/ja/net/data-filtering/)
- [データの並べ替え](/cells/ja/net/sort-data-of-excel/)
- [データ検証](/cells/ja/net/data-validation/)
- [ワークシートからデータをエクスポート](/cells/ja/net/export-data-from-worksheet/)
- [データの検索または検索](/cells/ja/net/find-or-search-data/)
- [書式設定あり/なしで Cell 文字列値を取得する](/cells/ja/net/get-cell-string-value-with-and-without-formatting/)
- [Cell 内に HTML リッチ テキストを追加する](/cells/ja/net/adding-html-rich-text-inside-the-cell/)
- [Excel または OpenOffice にハイパーリンクを挿入する](/cells/ja/net/insert-hyperlinks-to-excel/)
- [データをワークシートにインポート](/cells/ja/net/import-data-into-worksheet/)
- [列挙子を使用する方法と場所](/cells/ja/net/how-and-where-to-use-enumerators/)
- [Cell 値の幅と高さをピクセル単位で測定する](/cells/ja/net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [複数のスレッドで同時に Cell の値を読み取る](/cells/ja/net/reading-cell-values-in-multiple-threads-simultaneously/)
- [セル名と行/列インデックス間の変換](/cells/ja/net/names-and-indices/)
- [最初に行ごと、次に列ごとにデータを入力](/cells/ja/net/populate-data-first-by-row-then-by-column/)
- [Cell 値または範囲の一重引用符プレフィックスを保持](/cells/ja/net/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Cell のリッチ テキストの一部にアクセスして更新する](/cells/ja/net/access-and-update-the-portions-of-rich-text-of-cell/)



