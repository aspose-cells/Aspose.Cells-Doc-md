---
title: 印刷オプションの設定
type: docs
weight: 40
url: /ja/net/setting-print-options/
---
{{% alert color="primary" %}}

Microsoft Excel のページ設定には、ユーザーがワークシート ページの印刷方法を制御できるいくつかの印刷オプション (シート オプションとも呼ばれます) が用意されています。

{{% /alert %}}

## **印刷オプションの設定**

これらの印刷オプションにより、ユーザーは次のことができます。

- ワークシート上の特定の印刷領域を選択します。
- タイトルを印刷します。
- グリッド線を印刷します。
- 行/列の見出しを印刷します。
- ドラフト品質を実現します。
- コメントを印刷します。
- セル エラーを出力します。
- ページの順序を定義します。

 Aspose.Cells は、Microsoft Excel が提供するすべての印刷オプションをサポートし、開発者は、[**ページ設定**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)クラス。これらのプロパティがどのように使用されるかについては、以下で詳しく説明します。

### **印刷範囲の設定**

デフォルトでは、データを含むワークシートのすべての領域が印刷領域に組み込まれます。開発者は、ワークシートの特定の印刷領域を設定できます。

特定の印刷領域を選択するには、[**ページ設定**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)クラス'[**印刷エリア**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printarea)財産。印刷領域を定義するセル範囲をこのプロパティに割り当てます。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintArea-1.cs" >}}

### **印刷タイトルの設定**

Aspose.Cells を使用すると、印刷されたワークシートのすべてのページで行ヘッダーと列ヘッダーを繰り返すように指定できます。これを行うには、[**ページ設定**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)クラス'[**PrintTitleColumns**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printtitlecolumns)と[**PrintTitleRows**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printtitlerows)プロパティ。

繰り返される行または列は、行番号または列番号を渡すことによって定義されます。たとえば、行は $1:$2 として定義され、列は $A:$B として定義されます。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintTitle-1.cs" >}}

### **その他の印刷オプションの設定**

の[**ページ設定**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)クラスには、次のような一般的な印刷オプションを設定するためのその他のプロパティもいくつか用意されています。

- [**PrintGridlines**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printgridlines)グリッド線を印刷するかどうかを定義するブール型のプロパティ。
- [**印刷見出し**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printheadings)行と列の見出しを印刷するかどうかを定義するブール型のプロパティ。
- [**黒と白**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/blackandwhite)ワークシートを白黒モードで印刷するかどうかを定義するブール値のプロパティ。
- [**印刷コメント**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments): 印刷コメントをワークシートに表示するか、ワークシートの最後に表示するかを定義します。
- [**下書きを印刷**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printdraft)グラフィックなしでシートを印刷するかどうかを定義するブール値のプロパティ..
- [**印刷エラー**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors): セル エラーを表示、空白、ダッシュ、または N/A として出力するかどうかを定義します。

を設定するには[**印刷コメント**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments)と[**印刷エラー**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors)プロパティ、Aspose.Cells は 2 つの列挙も提供します。[**PrintCommentsType**](https://reference.aspose.com/cells/net/aspose.cells/printcommentstype) 、 と[**PrintErrorsType**](https://reference.aspose.com/cells/net/aspose.cells/printerrorstype)に割り当てられる定義済みの値が含まれています。[**印刷コメント**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments)と[**印刷エラー**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors)プロパティ。

の定義済みの値[**PrintCommentsType**](https://reference.aspose.com/cells/net/aspose.cells/printcommentstype)列挙は、その説明とともに以下にリストされています。

|**印刷コメントの種類**|**説明**|
|:- |:- |
|PrintInPlace|ワークシートに表示されているコメントを印刷するように指定します。|
|PrintNoComments|コメントを印刷しないように指定します。|
|PrintSheetEnd|ワークシートの最後にコメントを印刷するように指定します。|

の定義済みの値[**PrintErrorsType**](https://reference.aspose.com/cells/net/aspose.cells/printerrorstype)列挙は、その説明とともに以下にリストされています。



|**印刷エラーの種類**|**説明**|
|:- |:- |
|PrintErrorsBlank|エラーを出力しないように指定します。|
|PrintErrorsDash|エラーを「--」として出力するように指定します。|
|PrintErrorsDisplayed|エラーを表示どおりに印刷するように指定します。|
|印刷エラーNA|エラーを「#N/A」として出力するように指定します。|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-OtherPrintOptions-1.cs" >}}

### **ページの順序を設定する**

の[**ページ設定**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)クラスが提供する[**注文**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/order)ワークシートの複数ページの印刷を注文するために使用されるプロパティ。ページの順序には、次の 2 つの方法があります。

- **下から上へ：**右側のページを印刷する前に、すべてのページを下に印刷します。
- **オーバー・アンド・ダウン:**下のページを印刷する前に、ページを左から右に印刷します。

 Aspose.Cells は列挙を提供し、[**PrintOrderType**](https://reference.aspose.com/cells/net/aspose.cells/printordertype)定義済みの注文タイプがすべて含まれています。

の定義済みの値[**PrintOrderType**](https://reference.aspose.com/cells/net/aspose.cells/printordertype)以下に列挙します。

|**印刷注文の種類**|**説明**|
|:- |:- |
|ダウン・ザ・オーバー|印刷順序を下から上に表します。|
|オーバー・ザ・ダウン|印刷順序を上から下に表します。|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPageOrder-1.cs" >}}
