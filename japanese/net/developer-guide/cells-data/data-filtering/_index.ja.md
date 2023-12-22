---
title: データフィルタリング
type: docs
weight: 85
url: /ja/net/data-filtering/
description: Aspose.Cells for .NET API を使用してデータ フィルターを追加する方法を学習します。
keywords: Add Filter by Color, Add Date Filters, Add Number Filters, Add Dynamic Filter, Add Text Filters, Add custom filter with Contains, Add custom filter with NotContains, Add custom filter with BeginsWith, Add custom filter with EndsWith
---
{{% alert color="primary" %}}

Microsoft Excel には、ワークシート データを自動フィルターする優れた機能がいくつか用意されています。 Aspose.Cells は Microsoft Excel のオートフィルター機能を完全にサポートしています。この記事では、Microsoft Excel の機能の使い方と、Aspose.Cells を使用したコーディング方法について説明します。

{{% /alert %}}

##  **オートフィルターデータ**

オートフィルタリングは、ワークシートからリストに表示する項目のみを選択する最も簡単な方法です。オートフィルター機能を使用すると、ユーザーは設定された基準に従ってリスト内の項目をフィルターできます。テキスト、数値、または日付に基づいてフィルターします。

###  **Microsoft Excel のオートフィルター**

Microsoft Excel でオートフィルター機能を有効にするには:

1. ワークシートの見出し行をクリックします。
1. から**データ**メニュー、選択**フィルター**そして*オートフィルター**。

ワークシートにオートフィルターを適用すると、列見出しの右側にフィルター スイッチ (黒い矢印) が表示されます。

1. フィルタの矢印をクリックすると、フィルタ オプションのリストが表示されます。

オートフィルター オプションの一部は次のとおりです。

|**オプション**|**説明**|
| :- | :- |
|全て|リスト内のすべての項目を 1 回表示します。|
|カスタム|含む/含まないなどのフィルター条件をカスタマイズする|
|色でフィルターする|塗りつぶされた色に基づいてフィルタリングします|
|日付フィルター|日付のさまざまな基準に基づいて行をフィルタリングします|
|数値フィルター|比較、平均、トップ 10 などの数値に関するさまざまな種類のフィルター。|
|テキストフィルター|で始まる、で終わる、を含むなどのさまざまなフィルター|
|空白/空白以外|これらのフィルターは、Text Filter Blank を通じて実装できます。|

ユーザーは、これらのオプションを使用して、Microsoft Excel のワークシート データを手動でフィルターします。

###  **Aspose.Cells のオートフィルター**

Aspose.Cells は、Excel ファイルを表すクラス Workbook を提供します。 Workbook クラスには、Excel ファイル内の各ワークシートへのアクセスを可能にする Worksheets コレクションが含まれています。

ワークシートは Worksheet クラスによって表されます。 Worksheet クラスは、ワークシートを管理するための幅広いプロパティとメソッドを提供します。オートフィルターを作成するには、Worksheet クラスの AutoFilter プロパティを使用します。 AutoFilter プロパティは AutoFilter クラスのオブジェクトであり、見出し行を構成するセルの範囲を指定する Range プロパティを提供します。オートフィルターは、見出し行であるセル範囲に適用されます。

各ワークシートで指定できるフィルター範囲は 1 つだけです。これは Microsoft Excel によって制限されます。カスタム データ フィルタリングの場合は、AutoFilter.Custom メソッドを使用します。

以下の例では、上のセクションで Microsoft Excel を使用して作成したのと同じオートフィルターを Aspose.Cells を使用して作成しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterData-1.cs" >}}

####  **さまざまな種類のフィルター**

Aspose.Cells には、カラー フィルター、日付フィルター、数値フィルター、テキスト フィルター、空白フィルター、空白なしフィルターなど、さまざまな種類のフィルターを適用するための複数のオプションが用意されています。

#####  **塗りつぶしの色**

Aspose.Cells は、セルの塗りつぶしの色プロパティに基づいてデータをフィルター処理する関数 AddFillColorFilter を提供します。以下に示す例では、シートの最初の列に異なる塗りつぶしの色を持つテンプレート ファイルを使用して、カラー フィルタリング機能をテストします。サンプルファイルは以下のリンクからダウンロードできます。

1. [ColoredCells.xlsx](72417315.xlsx)
1. [FilteredColoredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterColor-1.cs" >}}

#####  **日付**

2018 年 1 月の日付を持つすべての行をフィルターするなど、さまざまなタイプの日付フィルターを実装できます。次のサンプル コードは、AddDateFilter 関数を使用したこのフィルターを示しています。サンプルファイルを以下に示します。

1. [日付.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterDate-1.cs" >}}

#####  **動的日付**

すべてのセルが年に関係なく 1 月の日付を持つなど、日付に基づいた動的フィルターが必要になる場合があります。この場合、DynamicFilter 関数は次のサンプル コードのように使用されます。サンプルファイルを以下に示します。

1. [日付.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterDynamicFilter-1.cs" >}}

#####  **番号**

カスタム フィルターは、特定の範囲内の数値を持つセルを選択するのと同様に、Aspose.Cells を使用して適用できます。次の例は、Custom() 関数を使用して数値をフィルタリングする方法を示しています。サンプルファイルを以下に示します。

1. [Number.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterNumber-1.cs" >}}

#####  **文章**

列にテキストが含まれており、特定のテキストを含むセルを選択する場合は、Filter() 関数を使用できます。次の例では、テンプレート ファイルに国のリストが含まれており、特定の国名を含む行が選択されます。次のコードは、テキストのフィルタリングを示しています。サンプルファイルを以下に示します。

1. [テキスト.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterText-1.cs" >}}

#####  **ブランク**

列に空白セルがほとんどないようなテキストが含まれており、空白セルが存在する行のみを選択するためにフィルタが必要な場合は、以下に示すように MatchBlanks() 関数を使用できます。サンプルファイルを以下に示します。

1. [空白の.xlsx](72417324.xlsx)
1. [FilteredBlank.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterBlank-1.cs" >}}

#####  **空白以外**

テキストを含むセルをフィルタリングする場合は、以下に示すように MatchNonBlanks フィルタ関数を使用します。サンプルファイルを以下に示します。

1. [空白の.xlsx](72417324.xlsx)
1. [FilteredNonBlank.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterNonBlank-1.cs" >}}

#####  **次を含むカスタム フィルター**

Excel には、特定の文字列を含むフィルター行などのカスタム フィルターが用意されています。この機能は Aspose.Cells で利用可能であり、サンプル ファイル内の名前をフィルタリングすることによって以下に示されています。サンプルファイルを以下に示します。

1. [ソースサンプル国名.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSample CountryNames.xlsx](outSourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterCustom-Contains-1.cs" >}}

#####  **NotContains を使用したカスタム フィルター**

Excel には、特定の文字列を含まないフィルター行などのカスタム フィルターが用意されています。この機能は Aspose.Cells で利用可能であり、以下に示すサンプル ファイル内の名前をフィルタリングすることによって以下に示されます。

1. [ソースサンプル国名.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterCustom-NotContains-1.cs" >}}

#####  **BeginsWith を使用したカスタム フィルター**

Excel には、特定の文字列で始まるフィルター行などのカスタム フィルターが用意されています。この機能は Aspose.Cells で利用可能であり、以下に示すサンプル ファイル内の名前をフィルタリングすることによって以下に示されます。

1. [ソースサンプル国名.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterBeginsWith-1.cs" >}}

#####  **EndsWith を使用したカスタム フィルター**

Excel には、特定の文字列で終わるフィルター行などのカスタム フィルターが用意されています。この機能は Aspose.Cells で利用可能であり、以下に示すサンプル ファイル内の名前をフィルタリングすることによって以下に示されます。

1. [ソースサンプル国名.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterEndsWith-1.cs" >}}

##  **アドバンストトピック**
- [Microsoft Excel の高度なフィルターを適用して、複雑な基準を満たすレコードを表示する](/cells/ja/net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [オートフィルターを更新した後にすべての非表示の行インデックスを取得する](/cells/ja/net/get-all-hidden-rows-indices-after-refreshing-autofilter/)
