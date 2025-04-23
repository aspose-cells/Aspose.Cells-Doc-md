---
title: 印刷オプションの設定
type: docs
weight: 40
url: /ja/net/setting-print-options/
description: この記事では、C# API および .NET ライブラリを使用して Excel ワークシートページ設定機能の印刷オプションをプログラムで設定する方法を示します。印刷エリア、印刷タイトル、ページの順序を設定することができます。
keywords: C# で Excel の印刷エリアを設定する、C# で Excel の印刷タイトルを設定する、C# で Excel のページの順序を設定する
---

{{% alert color="primary" %}}

Microsoft Excel のページ設定設定には、ワークシートページが印刷される方法を制御するいくつかの印刷オプション (またはシートオプションとも呼ばれる) が含まれています。

{{% /alert %}}

## **印刷オプションの設定**

これらの印刷オプションにより、ユーザーは次のような操作を行うことができます:

- ワークシート上の特定の印刷範囲を選択する。
- タイトルを印刷する。
- グリッド線を印刷する。
- 行/列見出しを印刷します。
- 下書き品質を実現する。
- コメントを印刷する。
- セルエラーを印刷する。
- ページ順序を定義する。

Aspose.Cells は Microsoft Excel が提供するすべての印刷オプションをサポートしており、開発者は [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) クラスが提供するプロパティを使用してワークシートのこれらのオプションを簡単に構成することが可能です。これらのプロパティの使用方法については、以下で詳しく説明します。

### **印刷範囲の設定**

デフォルトでは、印刷エリアにはデータを含むワークシートのすべての領域が組み込まれます。開発者はワークシートの特定の印刷エリアを設定することができます。

特定の印刷エリアを選択するには、[**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) クラスの [**PrintArea**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printarea) プロパティを使用します。このプロパティに、印刷エリアを定義するセル範囲を割り当てます。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintArea-1.cs" >}}

### **印刷タイトルを設定する**

Aspose.Cells を使用すると、印刷されるワークシートのすべてのページで行および列見出しを繰り返し指定することが可能です。これを行うには、[**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) クラスの [**PrintTitleColumns**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printtitlecolumns) および [**PrintTitleRows**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printtitlerows) プロパティを使用します。

繰り返す行または列は、その行番号または列番号を渡すことで定義されます。たとえば、行は$1:$2と定義され、列は$A:$Bと定義されます。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintTitle-1.cs" >}}

### **その他の印刷オプションの設定**

[**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) クラスには、以下の一般的な印刷オプションを設定するためのいくつかの他のプロパティも提供されています:

- [**PrintGridlines**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printgridlines): グリッド線を印刷するかどうかを定義するブール型のプロパティ。
- [**PrintHeadings**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printheadings): 行および列見出しを印刷するかどうかを定義するブール型のプロパティ。
- [**BlackAndWhite**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/blackandwhite): ブラックアンドホワイトモードでワークシートを印刷するかどうかを定義するブールプロパティ。
- [**PrintComments**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments): ワークシート上に印刷コメントを表示するか、ワークシートの最後に表示するかを定義する。
- [**PrintDraft**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printdraft): グラフィックを排除してシートを印刷するかどうかを定義するブールプロパティ。
- [**PrintErrors**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors): 表示されるままのセルエラー、空白、ダッシュ、またはN/A として印刷するかを定義する。

Aspose.Cellsは、[**PrintComments**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments) と [**PrintErrors**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors) プロパティを設定するために、[**PrintCommentsType**](https://reference.aspose.com/cells/net/aspose.cells/printcommentstype) と [**PrintErrorsType**](https://reference.aspose.com/cells/net/aspose.cells/printerrorstype) という2つの列挙型を提供しています。これらの列挙型には、それぞれ [**PrintComments**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments) と [**PrintErrors**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors) プロパティに割り当てるための事前に定義された値が含まれています。

[**PrintCommentsType**](https://reference.aspose.com/cells/net/aspose.cells/printcommentstype) 列挙型の事前に定義された値は、以下にその説明とともにリストされています。

|**コメント印刷タイプ**|**説明**|
| :- | :- |
|PrintInPlace|: ワークシート上に表示されているコメントを印刷することを指定。
|PrintNoComments|: コメントを印刷しないことを指定。
|PrintSheetEnd|: ワークシートの最後にコメントを印刷することを指定。

[**PrintErrorsType**](https://reference.aspose.com/cells/net/aspose.cells/printerrorstype) 列挙型の事前に定義された値は、以下にその説明とともにリストされています。



|**エラー印刷タイプ**|**説明**|
| :- | :- |
|PrintErrorsBlank|: エラーを印刷しないことを指定。
|PrintErrorsDash|: エラーを "--" として印刷することを指定。
|PrintErrorsDisplayed|: 表示されているエラーを印刷することを指定。
|PrintErrorsNA|: エラーを "#N/A" として印刷することを指定。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-OtherPrintOptions-1.cs" >}}

### **ページ順の設定**

[**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) クラスは、ワークシートを印刷するための複数のページの順序を設定するために使用される [**Order**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/order) プロパティを提供します。ページを順に印刷するためには、次の2つの可能性があります。

- **Down then over:** 右側のページを印刷する前に、すべてのページを下に印刷します。
- **Over then down:** 下側のページを印刷する前に、左から右のページを印刷します。

Aspose.Cellsは、[**PrintOrderType**](https://reference.aspose.com/cells/net/aspose.cells/printordertype) という列挙型を提供し、すべての事前に定義された順序タイプが含まれています。

列挙型 [**PrintOrderType**](https://reference.aspose.com/cells/net/aspose.cells/printordertype) の事前に定義された値は、以下にその説明とともにリストされています。

|**印刷順序タイプ**|**説明**|
| :- | :- |
|DownThenOver|: 下に印刷してから右に印刷するよう指定。
|OverThenDown|: 左から右に印刷してから下に印刷するよう指定。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPageOrder-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
