---
title: データフィルタリング
type: docs
weight: 85
url: /ja/net/data-filtering/
description: Aspose.Cells for .NET APIを使用してデータフィルタを追加する方法について学びます。
keywords: 色でフィルタを追加, 日付フィルタを追加, 数値フィルタを追加, 動的フィルタを追加, テキストフィルタを追加, Containsでカスタムフィルタを追加, NotContainsでカスタムフィルタを追加, BeginsWithでカスタムフィルタを追加, EndsWithでカスタムフィルタを追加
---

{{% alert color="primary" %}}

Microsoft Excelには、ワークシートデータの自動フィルタリングに役立つ機能がいくつかあります。Aspose.CellsはMicrosoft Excelの自動フィルタ機能を完全にサポートしています。この記事では、Microsoft Excelの機能の使用方法と、Aspose.Cellsを使用したコーディング方法について説明します。

{{% /alert %}}

## **データの自動フィルタリング**

自動フィルタリングは、リスト内で表示したいアイテムのみを素早く選択できる最も簡単な方法です。自動フィルタ機能により、リスト内のアイテムを特定の基準に従ってフィルタリングできます。テキスト、数値、または日付に基づいてフィルタリングできます。

### **Microsoft Excelの自動フィルタ**

Microsoft Excelで自動フィルタ機能を有効にするには：

1. ワークシート内の見出し行をクリックします。
1. **データ** メニューから、**フィルタ** を選択し、その後** 自動フィルタ** を選択します。

ワークシートに自動フィルタを適用すると、フィルタスイッチ（黒い矢印）が列見出しの右側に表示されます。

1. フィルタ矢印をクリックして、フィルタオプションのリストを表示します。

自動フィルタのオプションには次のものがあります:

|**オプション**|**説明**|
| :- | :- |
|All|リストのすべてのアイテムを一度に表示します。|
|Custom|含む/含まないなどのフィルター条件をカスタマイズします|
|Filter by Color|塗りつぶし色に基づくフィルター|
|Date Filters|日付に基づくさまざまな条件で行をフィルター|
|Number Filters|比較、平均、トップ10など、数値に関する異なるタイプのフィルタ。
|Text Filters|始まり、終わり、含むなどのさまざまなフィルター|
|Blanks/Non Blanks|これらのフィルターはテキストフィルター空白を通じて実装できます|

Microsoft Excelのユーザーは、これらのオプションを使用してワークシートデータを手動でフィルタリングします。

### **Aspose.CellsのAutofilter**

Aspose.CellsはExcelファイルを表すWorkbookクラスを提供します。WorkbookクラスにはワークシートにアクセスできるWorksheetsコレクションが含まれています

ワークシートは、ワークシートクラスによって表されます。ワークシートクラスには、ワークシートを管理するための広範なプロパティとメソッドが含まれています。Autofilterを作成するには、ワークシートクラスのAutoFilterプロパティを使用します。AutoFilterプロパティはAutoFilterクラスのオブジェクトであり、ヘッダ行を構成するセル範囲を指定するRangeプロパティが提供されています。オートフィルタは、ヘッダ行を構成するセル範囲に適用されます。

各ワークシートで、1つのフィルタ範囲のみを指定できます。これはMicrosoft Excelによって制限されています。カスタムデータフィルタリングには、AutoFilter.Customメソッドを使用します。

以下の例では、前述のMicrosoft Excelで作成したのと同じAutoFilterをAspose.Cellsを使用して作成しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterData-1.cs" >}}

#### **異なる種類のフィルタ**

Aspose.Cellsでは、カラーフィルタ、日付フィルタ、数値フィルタ、テキストフィルタ、ブランクフィルタ、およびノンブランクフィルタなど、さまざまな種類のフィルタを適用するための複数のオプションが提供されます。

##### **塗りつぶし色**

Aspose.Cellsでは、セルの塗りつぶし色プロパティに基づいてデータをフィルタリングするためのAddFillColorFilter関数が提供されています。以下の例では、シートの最初の列に異なる塗りつぶし色を持つテンプレートファイルを使用して色のフィルタリング機能をテストしています。サンプルファイルは以下からダウンロードできます

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterColor-1.cs" >}}

##### **日付**

AddDateFilter関数を使用して、2018年1月の日付を持つすべての行をフィルタリングするなど、異なる種類の日付フィルタを実装できます。以下のサンプルコードは、このフィルタを示しています。サンプルファイルは以下に示されています。

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterDate-1.cs" >}}

##### **動的日付**

時々動的なフィルタが必要な場合があります。例えば、年を問わず1月の日付を持つすべてのセル。この場合、DynamicFilter関数を使用します。以下のサンプルコードでこのフィルタを示しています。サンプルファイルは以下に示されています。

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterDynamicFilter-1.cs" >}}

##### **番号**

Aspose.Cellsを使用して数値の範囲内のセルを選択するなど、カスタムフィルタを適用できます。以下の例では、Custom()関数を使用して数値をフィルタする方法を示しています。サンプルファイルは以下にあります

1. [Number.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterNumber-1.cs" >}}

##### **テキスト**

テキストが含まれ、特定のテキストを含むセルを選択する場合は、Filter()関数を使用します。次の例では、国のリストを含むテンプレートファイルがあり、特定の国名を含む行を選択します。次のコードはテキストのフィルタリングを示しています。サンプルファイルは以下に示されています。

1. [Text.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterText-1.cs" >}}

##### **空欄**

テキストが含まれ、空白のセルを選択し、それらの行のみを選択するフィルタが必要な場合、MatchBlanks()関数を使用します。以下に、それを実証しているサンプルコードが示されています。サンプルファイルは以下に示されています。

1. [Blank.xlsx](72417324.xlsx)
1. [FilteredBlank.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterBlank-1.cs" >}}

##### **非空白セル**

テキストを含むセルをフィルタする必要がある場合は、MatchNonBlanksフィルタ関数を使用します。以下のサンプルコードが示されています。サンプルファイルは以下に示されています。

1. [Blank.xlsx](72417324.xlsx)
1. [FilteredNonBlank.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterNonBlank-1.cs" >}}

##### **Contains カスタムフィルタ**

Excelは、特定の文字列を含む行をフィルタリングするなど、カスタムフィルターを提供しています。この機能はAspose.Cellsで利用可能で、以下ではサンプルファイルの名前をフィルタリングすることで、デモンストレーションしています。

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterCustom-Contains-1.cs" >}}

##### **NotContains カスタムフィルタ**

Excel は特定の文字列を含まない行をフィルタするなど、カスタムフィルタを提供しています。この機能は Aspose.Cells で利用可能であり、以下で示されているサンプルファイル内の名前をフィルタリングしています。

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterCustom-NotContains-1.cs" >}}

##### **BeginsWith カスタムフィルタ**

Excel は特定の文字列で始まる行をフィルタするなど、カスタムフィルタを提供しています。この機能は Aspose.Cells で利用可能であり、以下で示されているサンプルファイル内の名前をフィルタリングしています。

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterBeginsWith-1.cs" >}}

##### **EndsWith カスタムフィルタ**

Excelは、特定の文字列で終わる行をフィルタリングするなど、カスタムフィルターを提供しています。この機能はAspose.Cellsで利用可能で、以下ではサンプルファイルの名前をフィルタリングすることで、デモンストレーションしています。

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterEndsWith-1.cs" >}}

## **高度なトピック**
- [複雑な基準を満たすレコードを表示するMicrosoft Excelの高度なフィルタの適用](/cells/ja/net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [オートフィルタの更新後の非表示行インデックスの取得](/cells/ja/net/get-all-hidden-rows-indices-after-refreshing-autofilter/)
{{< app/cells/assistant language="csharp" >}}
