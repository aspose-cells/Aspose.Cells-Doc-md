---
title: 番号設定
description: Aspose.Cells は、さまざまなセル番号設定をサポートするスプレッドシート ファイルを操作するための .NET ライブラリです。この記事では、ユーザーが必要に応じてスプレッドシートの数値形式を調整できるように、Aspose.Cells ライブラリを使用してセルの数値設定を管理する方法を紹介します。
keywords: Aspose.Cells, .NET library, electronic spreadsheet, cell number settings, formatting, management, Formats of Numbers and Dates
type: docs
weight: 10
url: /ja/net/cells-number-settings/
---
##  **Numbersと日付の表示形式を設定する方法**

Microsoft Excel の非常に強力な機能は、数値や日付の表示形式をユーザーが設定できることです。数値データを使用して、小数、通貨、パーセンテージ、分数、会計上の値などのさまざまな値を表すことができることはわかっています。これらの数値はすべて、それが表す情報の種類に応じて異なる形式で表示されます。同様に、日付や時刻を表示できる形式は数多くあります。
Aspose.Cells はこの機能をサポートしており、開発者は数値または日付の表示形式を設定できます。

###  **Microsoft Excel で表示形式を設定する方法**

Microsoft Excel で表示形式を設定するには:

1. 任意のセルを右クリックします。
1. *形式 Cells** を選択します。任意の種類の値の表示形式を設定するためのダイアログが表示されます。

ダイアログの左側には、次のような値のカテゴリが多数あります。**一般**、**数値**、**通貨**、**会計**、**日付**、**時刻**、**パーセント、**など。Aspose.Cells はこれらの表示形式をすべてサポートしています。

Aspose.Cells はクラスを提供します。[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)これは Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Excel ファイル内の各ワークシートへのアクセスを許可するコレクション。ワークシートは次のように表されます。[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスが提供するのは[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクション。の各項目[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクションはオブジェクトを表します[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラス。

 Aspose.Cellsが提供します[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle)そして[**スタイルの設定**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle)のためのメソッド[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラス。これらのメソッドは、セルの書式設定を取得および設定するために使用されます。の[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)クラスは、数値と日付の表示形式を処理するための便利なプロパティをいくつか提供します。

###  **組み込みの数値形式の使用方法**

Aspose.Cells は、数値と日付の表示形式を構成するためのいくつかの組み込み数値形式を提供します。これらの組み込みの数値形式は、[**番号**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number)の財産[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)物体。すべての組み込み数値形式には、一意の数値が与えられます。開発者は、任意の数値を[**番号**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number)の財産[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)表示形式を適用するオブジェクト。このアプローチは高速です。 Aspose.Cells でサポートされる組み込みの数値形式を以下に示します。

|**価値**|**タイプ**|**フォーマット文字列**|
| :- | :- | :- |
|0|General|一般的な|
|1|Decimal|0|
|2|Decimal|0.00|
|3|Decimal|# ,##0
|
|4|Decimal|# ,##0.00
|
|5|Currency|$#,##0;$-#,##0|
|6|Currency|$#,##0;[赤]$-#,##0|
|7|Currency|$#,##0.00;$-#,##0.00|
|8|Currency|$#,##0.00;[レッド]$-#,##0.00|
|9|Percentage|0%|
|10|Percentage|0.00%|
|11|Scientific|0.00E+00|
|12|Fraction|#  ?/?
|
|13|Fraction|#  */*
|
|14|Date|月/日/yyyy|
|15|Date|うーん、うん|
|16|Date|うーん|
|17|Date|うーん、うん|
|18|Time|時:分 午前/午後|
|19|Time|時:mm:s 午前/午後|
|20|Time|ふーむ|
|21|Time|時:mm:ss|
|22|Time|m/d/yy 時:mm|
|37|Currency|# ,##0;-#,##0
|
|38|Currency|# ,##0;[赤]-#,##0
|
|39|Currency|# ,##0.00;-#,##0.00
|
|40|Currency|# ,##0.00;[赤]-#,##0.00
|
|41|Accounting|_ * #,##0_ ;_ * "_ ;_ @_|
|42|Accounting|_ $* #,##0_ ;_ $* "_ ;_ @_|
|43|Accounting|_ * #,##0.00_ ;_ * "??_ ;_ @_|
|44|Accounting|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|
|45|Time|mm:ss|
|46|Time|時:mm:ss|
|47|Time|mm:ss.0|
|48|Scientific|## 0.0E+00
|
|49|Text|@|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SettingDisplayFormats-UsingBuiltInNumberFormats-1.cs" >}}

###  **カスタム数値形式の使用方法**

表示形式を設定するための独自のカスタマイズされた形式文字列を定義するには、[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)オブジェクトの[**カスタム**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom)財産。このアプローチは、プリセット形式を使用するほど高速ではありませんが、より柔軟です。


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SettingDisplayFormats-UsingCustomNumber-1.cs" >}}

{{% alert color="primary" %}}

を使用する場合は、[**カスタム**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom)数値形式を設定するプロパティ。以前の形式は、[**番号**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number)プロパティはオーバーライドされ、その逆も同様です。

{{% /alert %}}

##  **アドバンストトピック**
- [Style.Custom プロパティを設定するときにカスタム数値形式を確認する](/cells/ja/net/check-custom-number-format-when-setting-style-custom-property/)
- [サポートされている数値形式のリスト](/cells/ja/net/list-of-supported-number-formats/)
- [カスタム日付形式パターン g および ge mm dd をレンダリングする](/cells/ja/net/render-custom-date-format-pattern-g-and-ge-mm-dd/)
- [ワークブックのカスタム数値の小数点およびグループ区切り文字を指定する](/cells/ja/net/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [DBNum カスタム パターン形式の指定](/cells/ja/net/specifying-dbnum-custom-pattern-formatting/)
