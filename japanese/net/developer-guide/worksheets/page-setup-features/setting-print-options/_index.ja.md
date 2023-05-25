---
title: 印刷オプションの設定
type: docs
weight: 40
url: /ja/net/setting-print-options/
description: この記事では、C#、API、および .NET ライブラリを使用して、Excel ワークシートのページ設定機能の印刷オプションをプログラムで設定する方法を説明します。印刷範囲、印刷タイトル、ページ順序を設定できます。
keywords: set excel print area c#, set exce print titles c#, set excel page order c#
---
{{% alert color="primary" %}}

Microsoft Excel のページ設定設定には、ユーザーがワークシート ページの印刷方法を制御できるようにするいくつかの印刷オプション (シート オプションとも呼ばれます) が用意されています。

{{% /alert %}}

##  **印刷オプションの設定**

これらの印刷オプションにより、ユーザーは次のことが可能になります。

- ワークシート上の特定の印刷領域を選択します。
- タイトルを印刷します。
- グリッド線を印刷します。
- 行/列の見出しを印刷します。
- ドラフト品質を実現します。
- コメントを印刷します。
- セルエラーを出力します。
- ページの順序を定義します。

 Aspose.Cells は、Microsoft Excel が提供するすべての印刷オプションをサポートしており、開発者は、Excel が提供するプロパティを使用して、ワークシートに対してこれらのオプションを簡単に構成できます。[**ページ設定**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)クラス。これらのプロパティがどのように使用されるかについては、以下で詳しく説明します。

###  **印刷範囲の設定**

デフォルトでは、印刷領域には、データを含むワークシートのすべての領域が組み込まれます。開発者は、ワークシートの特定の印刷領域を設定できます。

特定の印刷領域を選択するには、[**ページ設定**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)クラス'[**印刷領域**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printarea)財産。印刷領域を定義するセル範囲をこのプロパティに割り当てます。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintArea-1.cs" >}}

###  **印刷タイトルを設定する**

Aspose.Cells を使用すると、印刷されるワークシートのすべてのページで繰り返す行ヘッダーと列ヘッダーを指定できます。これを行うには、[**ページ設定**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)クラス'[**印刷タイトル列**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printtitlecolumns)と[**印刷タイトル行**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printtitlerows)プロパティ。

繰り返される行または列は、行番号または列番号を渡すことによって定義されます。たとえば、行は $1:$2 として定義され、列は $A:$B として定義されます。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintTitle-1.cs" >}}

###  **その他の印刷オプションを設定する**

の[**ページ設定**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)クラスは、次のように一般的な印刷オプションを設定するための他のプロパティもいくつか提供します。

- [**印刷グリッドライン**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printgridlines)グリッド線を印刷するかどうかを定義するブール型プロパティ。
- [**印刷見出し**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printheadings)行と列の見出しを印刷するかどうかを定義するブール型プロパティ。
- [**黒と白**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/blackandwhite)ワークシートを白黒モードで印刷するかどうかを定義するブール型プロパティ。
- [**印刷コメント**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments)印刷コメントをワークシート上に表示するか、ワークシートの最後に表示するかを定義します。
- [**ドラフトの印刷**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printdraft)グラフィックなしでシートを印刷するかどうかを定義するブール型プロパティ。
- [**印刷エラー**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors)セル エラーを表示、空白、ダッシュ、または N/A として印刷するかどうかを定義します。

設定するには、[**印刷コメント**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments)と[**印刷エラー**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors)プロパティ、Aspose.Cells には 2 つの列挙も提供されます。[**印刷コメントタイプ**](https://reference.aspose.com/cells/net/aspose.cells/printcommentstype)、 と[**印刷エラーの種類**](https://reference.aspose.com/cells/net/aspose.cells/printerrorstype)に割り当てられる事前定義された値が含まれています。[**印刷コメント**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments)と[**印刷エラー**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors)それぞれのプロパティ。

の事前定義された値は、[**印刷コメントタイプ**](https://reference.aspose.com/cells/net/aspose.cells/printcommentstype)列挙とその説明を以下に示します。

|**コメントの種類を印刷する**|**説明**|
| :- | :- |
|インプレイスで印刷|ワークシートに表示されているコメントを印刷するように指定します。|
|印刷なしコメント|コメントを印刷しないように指定します。|
|プリントシート終了|ワークシートの最後にコメントを印刷するように指定します。|

事前に定義された値は、[**印刷エラーの種類**](https://reference.aspose.com/cells/net/aspose.cells/printerrorstype)列挙とその説明を以下に示します。



|**印刷エラーの種類**|**説明**|
| :- | :- |
|印刷エラー空白|エラーを出力しないように指定します。|
|印刷エラーダッシュ|エラーを「--」として出力するように指定します。|
|表示された印刷エラー|エラーを表示どおりに印刷するように指定します。|
|印刷エラーNA|エラーを「#N/A」として出力するように指定します。|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-OtherPrintOptions-1.cs" >}}

###  **ページ順序の設定**

の[**ページ設定**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)クラスが提供するのは、[**注文**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/order)ワークシートの複数ページの印刷を命令するために使用されるプロパティ。ページの順序には次の 2 つの方法があります。

- **ダウンしてオーバー:**右側のページを印刷する前に、すべてのページを下に印刷します。
- **上に、そして下に:**下のページを印刷する前に、ページを左から右に印刷します。

 Aspose.Cells は列挙を提供します。[**印刷注文タイプ**](https://reference.aspose.com/cells/net/aspose.cells/printordertype)これには、事前定義された注文タイプがすべて含まれています。

の事前定義された値[**印刷注文タイプ**](https://reference.aspose.com/cells/net/aspose.cells/printordertype)列挙は以下にリストされています。

|**印刷注文の種類**|**説明**|
| :- | :- |
|ダウンザオーバー|印刷順序を「下」、「上」として表します。|
|オーバーザエンダウン|印刷順序を「上」、「下」として表します。|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPageOrder-1.cs" >}}
