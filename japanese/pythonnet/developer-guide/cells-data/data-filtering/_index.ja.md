---
title: データフィルタリング
type: docs
weight: 85
url: /ja/python-net/data-filtering/
description: Aspose.Cells for Python via .NET API を使用してデータフィルタを追加する方法を学びます。
keywords: Python Excel Library、Python Add Filter by Color、Python Add Date Filters、Python Add Number Filters、Python Add Dynamic Filter、Python Add Text Filters、Python Add custom filter with Contains、Python Add custom filter with NotContains、Python Add custom filter with BeginsWith、Python Add custom filter with EndsWith
---

{{% alert color="primary" %}}

Microsoft Excelにはワークシートデータの自動フィルタリング機能があります。Aspose.Cells for Python via .NETは、Microsoft Excelの自動フィルタ機能を完全にサポートしています。この記事では、Microsoft Excelの機能の使用方法と、Aspose.Cells for Python via .NETを使用したコーディング方法について説明します。

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
|All|Show all items in the list once.|
|Custom|Customize filter criteria like contains/not contains|
|Filter by Color|Filters based on filled color|
|Date Filters|Filters rows based on different criteria on date|
|Number Filters|比較、平均、トップ10など、数値に関する異なるタイプのフィルタ。
|Text Filters|Different filters like begins with, ends with, contains etc,|
|Blanks/Non Blanks|These filters can be implemented through Text Filter Blank|

Microsoft Excelのユーザーは、これらのオプションを使用してワークシートデータを手動でフィルタリングします。

### **Aspose.Cells for Python Excel LibraryでAutofilterを使用します。**

Aspose.Cells for Python via .NETには、Excelファイルを表すWorkbookクラスがあります。Workbookクラスには、Excelファイル内の各ワークシートにアクセスできるWorksheetsコレクションが含まれています。

ワークシートは、ワークシートクラスによって表されます。ワークシートクラスには、ワークシートを管理するための広範なプロパティとメソッドが含まれています。Autofilterを作成するには、ワークシートクラスのAutoFilterプロパティを使用します。AutoFilterプロパティはAutoFilterクラスのオブジェクトであり、ヘッダ行を構成するセル範囲を指定するRangeプロパティが提供されています。オートフィルタは、ヘッダ行を構成するセル範囲に適用されます。

各ワークシートで、1つのフィルタ範囲のみを指定できます。これはMicrosoft Excelによって制限されています。カスタムデータフィルタリングには、AutoFilter.Customメソッドを使用します。

以下の例では、Microsoft Excelで作成したものと同じAutoFilterをAspose.Cells for Python via .NETを使用して作成しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-AutofilterData-1.py" >}}

#### **異なる種類のフィルタ**

Aspose.Cells for Python via .NETには、色フィルタ、日付フィルタ、数値フィルタ、テキストフィルタ、空フィルタ、空でないフィルタなど、異なるタイプのフィルタを適用するための複数のオプションが提供されています。

##### **塗りつぶし色**

Aspose.Cells for Python via .NETには、セルの塗りつぶし色プロパティに基づいてデータをフィルタリングするAddFillColorFilter関数があります。以下の例では、シートの最初の列に異なる塗りつぶし色が含まれたテンプレートファイルを使用して、色フィルタリング機能をテストしています。サンプルファイルは以下のリンクからダウンロードできます。

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterColor-1.py" >}}

##### **日付**

AddDateFilter関数を使用して、2018年1月の日付を持つすべての行をフィルタリングするなど、異なる種類の日付フィルタを実装できます。以下のサンプルコードは、このフィルタを示しています。サンプルファイルは以下に示されています。

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterDate-1.py" >}}

##### **動的日付**

時々動的なフィルタが必要な場合があります。例えば、年を問わず1月の日付を持つすべてのセル。この場合、DynamicFilter関数を使用します。以下のサンプルコードでこのフィルタを示しています。サンプルファイルは以下に示されています。

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterDynamicFilter-1.py" >}}

##### **番号**

Aspose.Cells for Python via .NETを使用して、指定された範囲内の数値を持つセルを選択するなど、カスタムフィルタを適用できます。以下の例は、Custom()関数を使用して数値をフィルタリングする方法を示しています。サンプルファイルは以下に示されています。

1. [Number.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterNumber-1.py" >}}

##### **テキスト**

テキストが含まれ、特定のテキストを含むセルを選択する場合は、Filter()関数を使用します。次の例では、国のリストを含むテンプレートファイルがあり、特定の国名を含む行を選択します。次のコードはテキストのフィルタリングを示しています。サンプルファイルは以下に示されています。

1. [Text.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterText-1.py" >}}

##### **空欄**

テキストが含まれ、空白のセルを選択し、それらの行のみを選択するフィルタが必要な場合、MatchBlanks()関数を使用します。以下に、それを実証しているサンプルコードが示されています。サンプルファイルは以下に示されています。

1. [Blank.xlsx](72417324.xlsx)
1. [FilteredBlank.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterBlank-1.py" >}}

##### **非空白セル**

テキストを含むセルをフィルタする必要がある場合は、MatchNonBlanksフィルタ関数を使用します。以下のサンプルコードが示されています。サンプルファイルは以下に示されています。

1. [Blank.xlsx](72417324.xlsx)
1. [FilteredNonBlank.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterNonBlank-1.py" >}}

##### **Contains カスタムフィルタ**

Excelは特定の文字列を含む行をフィルタリングするなど、カスタムフィルタを提供しています。この機能はAspose.Cells for Python via .NETで利用可能であり、下のサンプルファイルの名前をフィルタリングすることで示されています。サンプルファイルは以下に示します。

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterCustom-Contains-1.py" >}}

##### **NotContains カスタムフィルタ**

Excelは特定の文字列を含まない行をフィルタリングするなど、カスタムフィルタを提供しています。この機能はAspose.Cells for Python via .NETで利用可能であり、下のサンプルファイルの名前をフィルタリングすることで示されています。

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterCustom-NotContains-1.py" >}}

##### **BeginsWith カスタムフィルタ**

Excelは特定の文字列で始まる行をフィルタリングするなど、カスタムフィルタを提供しています。この機能はAspose.Cells for Python via .NETで利用可能であり、下のサンプルファイルの名前をフィルタリングすることで示されています。

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-AutofilterBeginsWith-1.py" >}}

##### **EndsWith カスタムフィルタ**

Excelは特定の文字列で終わる行をフィルタリングするなど、カスタムフィルタを提供しています。この機能はAspose.Cells for Python via .NETで利用可能であり、下のサンプルファイルの名前をフィルタリングすることで示されています。

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-AutofilterEndsWith-1.py" >}}

## **高度なトピック**
- [複雑な基準を満たすレコードを表示するMicrosoft Excelの高度なフィルタの適用](/cells/ja/python-net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [オートフィルタの更新後の非表示行インデックスの取得](/cells/ja/python-net/get-all-hidden-rows-indices-after-refreshing-autofilter/)
