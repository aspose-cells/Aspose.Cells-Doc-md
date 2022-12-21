---
title: データフィルタリング
type: docs
weight: 60
url: /ja/java/data-filtering/
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

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)これは Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスには[**ワークシート コレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)これにより、Excel ファイル内の各ワークシートにアクセスできます。

ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスには、ワークシートを管理するためのさまざまなプロパティとメソッドが用意されています。オートフィルターを作成するには、[**オートフィルター**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter)のプロパティ[**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラス。の[**オートフィルター**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter)プロパティはのオブジェクトです[**オートフィルター**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter)を提供するクラス[**範囲**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#Range)見出し行を構成するセルの範囲を指定するためのプロパティ。見出し行であるセル範囲にオートフィルターが適用されます。

各ワークシートでは、1 つのフィルター範囲のみを指定できます。これは、Microsoft Excel によって制限されます。カスタム データ フィルタリングの場合は、[**AutoFilter.Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#custom(int,%20int,%20java.lang.Object)） 方法。

以下の例では、上記のセクションで Microsoft Excel を使用して作成したのと同じ AutoFilter を Aspose.Cells を使用して作成しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterData.java" >}}

#### **さまざまな種類のフィルター**

Aspose.Cells には、カラー フィルター、日付フィルター、数値フィルター、テキスト フィルター、空白フィルター、なし空白フィルターなど、さまざまな種類のフィルターを適用する複数のオプションが用意されています。

##### **塗りつぶしの色**

Aspose.Cells は機能を提供します[**addFillColorFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#addFillColorFilter(int,%20int,%20com.aspose.cells.CellsColor,%20com.aspose.cells.CellsColor)セルの塗りつぶしの色のプロパティに基づいてデータをフィルター処理します。以下の例では、シートの最初の列に異なる塗りつぶし色を持つテンプレート ファイルを使用して、カラー フィルタリング機能をテストしています。次のファイルをダウンロードして、機能を確認できます。

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColoredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterColor.java" >}}

##### **日にち**

2018 年 1 月の日付を持つすべての行をフィルタリングするなど、さまざまなタイプの日付フィルターを実装できます。[**addDateFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#addDateFilter(int,%20int,%20int,%20int,%20int,%20int,%20int,%20int)） 関数。この機能のテストには、次のファイルを使用できます。

1. [日付.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterDate.java" >}}

##### **動的日付**

年に関係なく 1 月の日付を持つすべてのセルのように、日付に基づく動的フィルターが必要になる場合があります。この場合、[**DynamicFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#dynamicFilter(int,%20int)) 関数は、次のサンプル コードで指定されているように使用されます。次のファイルをテストに使用できます。

1. [日付.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterDynamicFilter.java" >}}

##### **番号**

カスタム フィルターは、Aspose.Cells を使用して、特定の範囲内の数値を持つセルを選択するように適用できます。次の例は、の使用法を示しています[**習慣（）**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#custom(int,%20int,%20java.lang.Object)) 数値をフィルタリングする関数。サンプルファイルは以下のリンクからダウンロードできます。

1. [数値.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterNumber.java" >}}

##### **文章**

列にテキストが含まれ、特定のテキストを含むセルが選択される場合、[**フィルター（）**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#filter(int,%20java.lang.String))機能が使えます。次の例では、テンプレート ファイルに国のリストが含まれており、特定の国名を含む行が選択されます。次のコードは、以下のサンプル ファイルを使用してテキストをフィルタリングする方法を示しています。

1. [テキスト.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterText.java" >}}

##### **ブランクス**

列に空白のセルがほとんどないようなテキストが含まれており、空白のセルが存在する行のみを選択するためにフィルタが必要な場合、[**matchBlanks()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#matchBlanks(int)) 関数は、以下に示すように使用できます。サンプルファイルは以下のリンクからダウンロードできます。

1. [空白.xlsx](72417324.xlsx)
1. [FilteredBlank.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterBlank.java" >}}

##### **非ブランク**

テキストを含むセルをフィルタリングする場合は、[**MatchNonBlanks**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#matchNonBlanks(int)) 以下に示すようにフィルター関数。サンプルファイルは以下のリンクからダウンロードできます。

1. [空白.xlsx](72417324.xlsx)
1. [FilteredNonBlank.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterNonBlank.java" >}}

##### **含むカスタム フィルター**

Excel には、特定の文字列を含むフィルター行などのカスタム フィルターが用意されています。この機能は Aspose.Cells で利用可能で、サンプル ファイル内の名前をフィルタリングすることによって以下に示されています。サンプルファイルは以下のリンクからダウンロードできます。

1. [sourceSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-Contains.java" >}}

##### **NotContains を使用したカスタム フィルター**

Excel には、特定の文字列を含まないフィルター行などのカスタム フィルターが用意されています。この機能は Aspose.Cells で利用可能で、以下のサンプル ファイルで名前をフィルタリングすることによって以下に示されています。

1. [sourceSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-NotContains.java" >}}

##### **BeginsWith を使用したカスタム フィルター**

Excel には、特定の文字列で始まるフィルター行などのカスタム フィルターが用意されています。この機能は Aspose.Cells で利用可能で、以下のサンプル ファイルで名前をフィルタリングすることによって以下に示されています。

1. [sourceSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-BeginsWith.java" >}}

##### **EndsWith を使用したカスタム フィルター**

Excel には、特定の文字列で終わるフィルター行などのカスタム フィルターが用意されています。この機能は Aspose.Cells で利用可能で、以下のサンプル ファイルで名前をフィルタリングすることによって以下に示されています。

1. [sourceSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-EndsWith.java" >}}

## **先行トピック**
- [Microsoft Excel の高度なフィルターを適用して、複雑な基準を満たすレコードを表示する](/cells/ja/java/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [オートフィルターを更新した後にすべての非表示の行インデックスを取得する](/cells/ja/java/get-all-hidden-rows-indices-after-refreshing-autofilter/)

