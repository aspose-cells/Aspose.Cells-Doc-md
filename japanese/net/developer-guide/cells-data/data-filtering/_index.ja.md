---
title: データフィルタリング
type: docs
weight: 85
url: /ja/net/data-filtering/
---
{{% alert color="primary" %}}

Microsoft Excel には、ワークシート データを自動フィルター処理する優れた機能がいくつか用意されています。 Aspose.Cells は Microsoft Excel のオートフィルター機能を完全にサポートします。この記事では、Microsoft Excel の機能を使用する方法と、Aspose.Cells を使用してそれらをコーディングする方法について説明します。

{{% /alert %}}

## **データのオートフィルター**

オートフィルターは、ワークシートからリストに表示する項目のみを選択する最も簡単な方法です。オートフィルター機能を使用すると、ユーザーは設定された基準に従ってリスト内のアイテムをフィルター処理できます。テキスト、数値、または日付に基づいてフィルタリングします。

### **Microsoft Excel のオートフィルター**

Microsoft Excel でオートフィルター機能を有効にするには:

1. ワークシートの見出し行をクリックします。
1. から**データ**メニュー、選択**フィルター**その後**オートフィルター**.

ワークシートにオートフィルターを適用すると、列見出しの右側にフィルター スイッチ (黒い矢印) が表示されます。

1. フィルタの矢印をクリックして、フィルタ オプションのリストを表示します。

オートフィルタ オプションの一部は次のとおりです。

|**オプション**|**説明**|
|:- |:- |
|全て|リスト内のすべてのアイテムを 1 回表示します。|
|カスタム|含む/含まないなどのフィルター基準をカスタマイズする|
|色でフィルター|塗りつぶし色に基づくフィルター|
|日付フィルター|日付のさまざまな基準に基づいて行をフィルター処理します|
|数値フィルター|比較、平均、上位 10 などの数値に対するさまざまなタイプのフィルター。|
|テキスト フィルター|で始まる、終わる、含むなどのさまざまなフィルター、|
|ブランクス/ノンブランクス|これらのフィルターは、Text Filter Blank を使用して実装できます。|

ユーザーは、これらのオプションを使用して、Microsoft Excel でワークシート データを手動でフィルター処理します。

### **Aspose.Cells のオートフィルター**

Aspose.Cells は、Excel ファイルを表すクラス Workbook を提供します。 Workbook クラスには、Excel ファイル内の各ワークシートへのアクセスを可能にする Worksheets コレクションが含まれています。

ワークシートは Worksheet クラスによって表されます。 Worksheet クラスは、ワークシートを管理するためのさまざまなプロパティとメソッドを提供します。オートフィルターを作成するには、Worksheet クラスの AutoFilter プロパティを使用します。 AutoFilter プロパティは、見出し行を構成するセルの範囲を指定するための Range プロパティを提供する AutoFilter クラスのオブジェクトです。見出し行であるセル範囲にオートフィルターが適用されます。

各ワークシートでは、1 つのフィルター範囲のみを指定できます。これは、Microsoft Excel によって制限されます。カスタム データ フィルタリングには、AutoFilter.Custom メソッドを使用します。

以下の例では、上記のセクションで Microsoft Excel を使用して作成したのと同じ AutoFilter を Aspose.Cells を使用して作成しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterData-1.cs" >}}

#### **さまざまな種類のフィルター**

Aspose.Cells には、カラー フィルター、日付フィルター、数値フィルター、テキスト フィルター、空白フィルター、なし空白フィルターなど、さまざまな種類のフィルターを適用する複数のオプションが用意されています。

##### **塗りつぶしの色**

Aspose.Cells は、関数 AddFillColorFilter を提供して、セルの塗りつぶしの色のプロパティに基づいてデータをフィルター処理します。以下の例では、シートの最初の列に異なる塗りつぶし色を持つテンプレート ファイルを使用して、カラー フィルタリング機能をテストしています。サンプルファイルは以下のリンクからダウンロードできます。

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColoredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterColor-1.cs" >}}

##### **日にち**

2018 年 1 月の日付を持つすべての行をフィルタリングするなど、さまざまなタイプの日付フィルターを実装できます。次のサンプル コードは、AddDateFilter 関数を使用したこのフィルターを示しています。サンプルファイルを以下に示します。

1. [日付.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterDate-1.cs" >}}

##### **動的日付**

年に関係なく 1 月の日付を持つすべてのセルのように、日付に基づく動的フィルターが必要になる場合があります。この場合、次のサンプル コードに示すように DynamicFilter 関数が使用されます。サンプルファイルを以下に示します。

1. [日付.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterDynamicFilter-1.cs" >}}

##### **番号**

カスタム フィルターは、Aspose.Cells を使用して、特定の範囲内の数値を持つセルを選択するように適用できます。次の例は、 Custom() 関数を使用して数値をフィルタリングする方法を示しています。サンプルファイルを以下に示します。

1. [数値.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterNumber-1.cs" >}}

##### **文章**

列にテキストが含まれており、特定のテキストを含むセルを選択する場合は、Filter() 関数を使用できます。次の例では、テンプレート ファイルに国のリストが含まれており、特定の国名を含む行が選択されます。次のコードは、テキストのフィルタリングを示しています。サンプルファイルを以下に示します。

1. [テキスト.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterText-1.cs" >}}

##### **ブランクス**

列に空白のセルがほとんどないようなテキストが含まれており、空白のセルが存在する行のみを選択するためにフィルターが必要な場合は、以下に示すように MatchBlanks() 関数を使用できます。サンプルファイルを以下に示します。

1. [空白.xlsx](72417324.xlsx)
1. [FilteredBlank.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterBlank-1.cs" >}}

##### **非ブランク**

テキストを含むセルをフィルター処理する場合は、以下に示すように MatchNonBlanks フィルター関数を使用します。サンプルファイルを以下に示します。

1. [空白.xlsx](72417324.xlsx)
1. [FilteredNonBlank.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterNonBlank-1.cs" >}}

##### **含むカスタム フィルター**

Excel には、特定の文字列を含むフィルター行などのカスタム フィルターが用意されています。この機能は Aspose.Cells で利用可能で、サンプル ファイル内の名前をフィルタリングすることによって以下に示されています。サンプルファイルを以下に示します。

1. [sourceSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterCustom-Contains-1.cs" >}}

##### **NotContains を使用したカスタム フィルター**

Excel には、特定の文字列を含まないフィルター行などのカスタム フィルターが用意されています。この機能は Aspose.Cells で利用可能で、以下のサンプル ファイルで名前をフィルタリングすることによって以下に示されています。

1. [sourceSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterCustom-NotContains-1.cs" >}}

##### **BeginsWith を使用したカスタム フィルター**

Excel には、特定の文字列で始まるフィルター行などのカスタム フィルターが用意されています。この機能は Aspose.Cells で利用可能で、以下のサンプル ファイルで名前をフィルタリングすることによって以下に示されています。

1. [sourceSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterBeginsWith-1.cs" >}}

##### **EndsWith を使用したカスタム フィルター**

Excel には、特定の文字列で終わるフィルター行などのカスタム フィルターが用意されています。この機能は Aspose.Cells で利用可能で、以下のサンプル ファイルで名前をフィルタリングすることによって以下に示されています。

1. [sourceSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterEndsWith-1.cs" >}}

## **先行トピック**
- [Microsoft Excel の高度なフィルターを適用して、複雑な基準を満たすレコードを表示する](/cells/ja/net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [オートフィルターを更新した後にすべての非表示の行インデックスを取得する](/cells/ja/net/get-all-hidden-rows-indices-after-refreshing-autofilter/)
