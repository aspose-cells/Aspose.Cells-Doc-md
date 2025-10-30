---
title: データフィルタリング
type: docs
weight: 85
url: /ja/nodejs-cpp/data-filtering/
description: Aspose.Cells for Node.js via C++ APIを使用してデータフィルタを追加する方法を学びます。
keywords: フィルターの色による追加（Node.js via C++）、日付フィルターの追加（Node.js via C++）、数値フィルターの追加（Node.js via C++）、動的フィルターの追加（Node.js via C++）、テキストフィルターの追加（Node.js via C++）、包含によるカスタムフィルターの追加（Node.js via C++）、NotContainsによるカスタムフィルターの追加（Node.js via C++）、BeginsWithによるカスタムフィルターの追加（Node.js via C++）、EndsWithによるカスタムフィルターの追加（Node.js via C++）
---

{{% alert color="primary" %}}
Microsoft Excelはワークシートデータの自動フィルタリングの良い機能を提供しています。Aspose.CellsはMicrosoft Excelの自動フィルタ機能を完全にサポートしています。この記事では、Microsoft Excelでのこれらの機能の使用方法と、それらをAspose.Cells for Node.js via C++を使用してコーディングする方法を説明します。
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

### **Aspose.Cells for Node.js via C++を用いた自動フィルタ|**

Aspose.CellsはExcelファイルを表すWorkbookクラスを提供します。WorkbookクラスにはワークシートにアクセスできるWorksheetsコレクションが含まれています

ワークシートは、ワークシートクラスによって表されます。ワークシートクラスには、ワークシートを管理するための広範なプロパティとメソッドが含まれています。Autofilterを作成するには、ワークシートクラスのAutoFilterプロパティを使用します。AutoFilterプロパティはAutoFilterクラスのオブジェクトであり、ヘッダ行を構成するセル範囲を指定するRangeプロパティが提供されています。オートフィルタは、ヘッダ行を構成するセル範囲に適用されます。

各ワークシートで、1つのフィルタ範囲のみを指定できます。これはMicrosoft Excelによって制限されています。カスタムデータフィルタリングには、AutoFilter.Customメソッドを使用します。

以下の例では、Microsoft Excelで作成したのと同じAutoFilterをAspose.Cells for Node.js via C++を使用して作成しました。|

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter.js" >}}

#### **異なる種類のフィルタ**

Aspose.Cellsでは、カラーフィルタ、日付フィルタ、数値フィルタ、テキストフィルタ、ブランクフィルタ、およびノンブランクフィルタなど、さまざまな種類のフィルタを適用するための複数のオプションが提供されます。

##### **塗りつぶし色**

Aspose.Cellsでは、セルの塗りつぶし色プロパティに基づいてデータをフィルタリングするためのAddFillColorFilter関数が提供されています。以下の例では、シートの最初の列に異なる塗りつぶし色を持つテンプレートファイルを使用して色のフィルタリング機能をテストしています。サンプルファイルは以下からダウンロードできます

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-FillColor.js" >}}


##### **日付**

2018年1月のすべての日付を持つ行をフィルタリングするなど、さまざまなタイプの日時フィルターを実装できます。以下のサンプルコードは、AddDateFilter関数を使用してこのフィルターを示しています。サンプルファイルは以下にあります。

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Date.js" >}}


##### **動的日付**

時々動的なフィルタが必要な場合があります。例えば、年を問わず1月の日付を持つすべてのセル。この場合、DynamicFilter関数を使用します。以下のサンプルコードでこのフィルタを示しています。サンプルファイルは以下に示されています。

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-DynamicFilter.js" >}}


##### **番号**

Aspose.Cellsを使用して数値の範囲内のセルを選択するなど、カスタムフィルタを適用できます。以下の例では、Custom()関数を使用して数値をフィルタする方法を示しています。サンプルファイルは以下にあります

1. [Number.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Number.js" >}}


##### **テキスト**

列にテキストが含まれていて、特定のテキストを含むセルを選択したい場合、Filter()関数を使用できます。以下の例では、テンプレートファイルに国のリストがあり、特定の国名を含む行を選択します。以下のコードはテキストのフィルタリングを示しています。サンプルファイルは以下にあります。

1. [Text.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Text.js" >}}


##### **空欄**

テキストが含まれ、空白のセルを選択し、それらの行のみを選択するフィルタが必要な場合、MatchBlanks()関数を使用します。以下に、それを実証しているサンプルコードが示されています。サンプルファイルは以下に示されています。

1. [Blank.xlsx](72417324.xlsx)
1. [FilteredBlank.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Blanks.js" >}}


##### **非空白セル**

テキストを含むセルをフィルタする必要がある場合は、MatchNonBlanksフィルタ関数を使用します。以下のサンプルコードが示されています。サンプルファイルは以下に示されています。

1. [Blank.xlsx](72417324.xlsx)
1. [FilteredNonBlank.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-NonBlanks.js" >}}


##### **Contains カスタムフィルタ**

Excelは、特定の文字列を含む行をフィルタリングするなど、カスタムフィルターを提供しています。この機能はAspose.Cellsで利用可能で、以下ではサンプルファイルの名前をフィルタリングすることで、デモンストレーションしています。

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Custom-Contains.js" >}}


##### **NotContains カスタムフィルタ**

Excelは特定の文字列を含まない行をフィルタリングするカスタムフィルタを提供しています。この機能はAspose.Cellsで利用可能で、以下のサンプルファイル内の名前のフィルタリングにより実演しています。

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Custom-NotContains.js" >}}


##### **BeginsWith カスタムフィルタ**

Excelは特定の文字列で始まる行をフィルタリングするカスタムフィルタを提供しています。この機能はAspose.Cellsで利用可能で、以下のサンプルファイル内の名前のフィルタリングにより実演しています。

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Custom-BeginsWith.js" >}}


##### **EndsWith カスタムフィルタ**

Excel は特定の文字列で終わる行をフィルタするなど、カスタムフィルタを提供しています。この機能は Aspose.Cells で利用可能であり、以下で示されているサンプルファイル内の名前をフィルタリングしています。

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Custom-EndsWith.js" >}}


## **高度なトピック**
- [複雑な基準を満たすレコードを表示するMicrosoft Excelの高度なフィルタの適用](/cells/ja/nodejs-cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [オートフィルタの更新後の非表示行インデックスの取得](/cells/ja/nodejs-cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/)
{{< app/cells/assistant language="nodejs-cpp" >}}
