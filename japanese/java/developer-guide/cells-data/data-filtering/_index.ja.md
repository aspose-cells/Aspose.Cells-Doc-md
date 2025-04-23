---
title: データフィルタリング
type: docs
weight: 60
url: /ja/java/data-filtering/
---

{{% alert color="primary" %}}

Microsoft Excelには、ワークシートデータの自動フィルタリングに役立つ機能がいくつかあります。Aspose.CellsはMicrosoft Excelの自動フィルタ機能を完全にサポートしています。この記事では、Microsoft Excelの機能の使用方法と、Aspose.Cellsを使用したコーディング方法について説明します。

{{% /alert %}}

## **データの自動フィルタリング**

自動フィルタリングは、リスト内で表示したいアイテムのみを素早く選択できる最も簡単な方法です。自動フィルタ機能により、リスト内のアイテムを特定の基準に従ってフィルタリングできます。テキスト、数値、または日付に基づいてフィルタリングできます。

### **Microsoft Excelの自動フィルタ**

Microsoft Excelで自動フィルタ機能を有効にするには：

1. ワークシート内の見出し行をクリックします。
1. **データ** メニューから **フィルタ** を選択し、次に **自動フィルタ** を選択します。

ワークシートに自動フィルタを適用すると、フィルタスイッチ（黒い矢印）が列見出しの右側に表示されます。

1. フィルタ矢印をクリックして、フィルタオプションのリストを表示します。

自動フィルタのオプションには次のものがあります:

|**オプション**|**説明**|
| :- | :- |
|All|リストのすべてのアイテムを一度に表示します。|
|Custom|含む/含まないなどのフィルター条件をカスタマイズします|
|Filter by Color|塗りつぶし色に基づくフィルター|
|Date Filters|日付に基づくさまざまな条件で行をフィルター|
|Number Filters|比較、平均、上位10などの数字に基づく異なるタイプのフィルタを適用します。
|Text Filters|始まり、終わり、含むなどのさまざまなフィルター|
|Blanks/Non Blanks|これらのフィルターはテキストフィルター空白を通じて実装できます|
Microsoft Excelのユーザーは、これらのオプションを使用してワークシートデータを手動でフィルタリングします。

### **Aspose.CellsのAutofilter**

Aspose.CellsはExcelファイルを表すクラス、[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)を提供します。[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスには、Excelファイルの各ワークシートにアクセスできる[**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)が含まれています。

ワークシートは[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスには、ワークシートを管理するための多くのプロパティとメソッドが含まれています。自動フィルタを作成するには、[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスの[**AutoFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter)プロパティを使用します。[**AutoFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter)プロパティは[**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#Range)プロパティを用いたヘッダ行を構成するセルの範囲を指定するための[**AutoFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter)クラスのオブジェクトになります。自動フィルタは、見出し行を構成するセルの範囲に適用されます。

各ワークシートで、1つのフィルタ範囲のみを指定できます。これはMicrosoft Excelによって制限されています。カスタムデータフィルタリングには、[**AutoFilter.Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#custom-int-int-java.lang.Object-)メソッドを使用してください。

以下の例では、前述のMicrosoft Excelで作成したのと同じAutoFilterをAspose.Cellsを使用して作成しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterData.java" >}}

#### **異なる種類のフィルタ**

Aspose.Cellsでは、カラーフィルタ、日付フィルタ、数値フィルタ、テキストフィルタ、ブランクフィルタ、およびノンブランクフィルタなど、さまざまな種類のフィルタを適用するための複数のオプションが提供されます。

##### **塗りつぶし色**

Aspose.Cellsは、セルの塗りつぶし色プロパティに基づいてデータをフィルタリングするための[**addFillColorFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#addFillColorFilter-int-int-com.aspose.cells.CellsColor-com.aspose.cells.CellsColor-)関数を提供します。以下の例では、シートの最初の列に異なる塗りつぶし色が含まれるテンプレートファイルを使用して、色のフィルタリング機能をテストしています。機能を確認するために以下のファイルをダウンロードできます。

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterColor.java" >}}

##### **日付**

1月2018年に日付が含まれるすべての行をフィルタリングするなど、さまざまな種類の日付フィルタが実装されることがあります。以下のサンプルコードでは、[**addDateFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#addDateFilter-int-int-int-int-int-int-int-int-)関数を使用してこのフィルタをデモンストレーションしています。この機能をテストするために以下のファイルを使用できます。

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterDate.java" >}}

##### **動的日付**

時には、年に関係なく1月に日付を持つセルに基づいて動的なフィルタが必要になります。この場合、以下のサンプルコードに示すように、[**DynamicFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#dynamicFilter-int-int-)関数が使用されます。この機能をテストするために以下のファイルを使用できます。

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterDynamicFilter.java" >}}

##### **番号**

Aspose.Cellsを使用してカスタムフィルタを適用することができます。指定された範囲内の数値を持つセルを選択するために[**custom()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#custom-int-int-java.lang.Object-)関数の使用例を以下に示します。サンプルファイルを以下のリンクからダウンロードできます。

1. [Number.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterNumber.java" >}}

##### **テキスト**

列にテキストが含まれ、特定のテキストを含むセルを選択する必要がある場合、[**filter()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#filter-int-java.lang.String-)関数を使用できます。以下の例では、テンプレートファイルに国のリストが含まれており、特定の国名を含む行が選択されるようになっています。以下のサンプルファイルを使用して、以下のコードによるテキストのフィルタリングをデモンストレーションしています。

1. [Text.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterText.java" >}}

##### **空欄**

列にはいくつかの空欄のセルが含まれており、空欄のセルのみを選択するためにフィルタが必要な場合、以下のサンプルコードに示すように、[**matchBlanks()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#matchBlanks-int-)関数を使用できます。サンプルファイルを以下のリンクからダウンロードできます。

1. [Blank.xlsx](72417324.xlsx)
1. [FilteredBlank.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterBlank.java" >}}

##### **非空白セル**

テキストを含むセルをフィルタする場合は、以下で示されているように [**MatchNonBlanks**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#matchNonBlanks-int-) フィルタ関数を使用します。サンプルファイルは以下のリンクからダウンロードできます。

1. [Blank.xlsx](72417324.xlsx)
1. [FilteredNonBlank.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterNonBlank.java" >}}

##### **Contains カスタムフィルタ**

Excel は特定の文字列を含む行をフィルタするなど、カスタムフィルタを提供しています。この機能は Aspose.Cells で利用可能であり、以下のサンプルファイル内の名前をフィルタリングして以下で示されています。サンプルファイルは以下のリンクからダウンロードできます。

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-Contains.java" >}}

##### **NotContains カスタムフィルタ**

Excel は特定の文字列を含まない行をフィルタするなど、カスタムフィルタを提供しています。この機能は Aspose.Cells で利用可能であり、以下で示されているサンプルファイル内の名前をフィルタリングしています。

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-NotContains.java" >}}

##### **BeginsWith カスタムフィルタ**

Excel は特定の文字列で始まる行をフィルタするなど、カスタムフィルタを提供しています。この機能は Aspose.Cells で利用可能であり、以下で示されているサンプルファイル内の名前をフィルタリングしています。

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-BeginsWith.java" >}}

##### **EndsWith カスタムフィルタ**

Excel は特定の文字列で終わる行をフィルタするなど、カスタムフィルタを提供しています。この機能は Aspose.Cells で利用可能であり、以下で示されているサンプルファイル内の名前をフィルタリングしています。

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-EndsWith.java" >}}

## **高度なトピック**
- [複雑な基準を満たすレコードを表示するMicrosoft Excelの高度なフィルタの適用](/cells/ja/java/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [オートフィルタの更新後の非表示行インデックスの取得](/cells/ja/java/get-all-hidden-rows-indices-after-refreshing-autofilter/)

{{< app/cells/assistant language="java" >}}
