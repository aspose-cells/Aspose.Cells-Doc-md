---
title: ページ設定機能
type: docs
weight: 40
url: /ja/java/page-setup-features/
---
場合によっては、印刷を制御するためにワークシートのページ設定を構成する必要があります。これらのページ設定の設定には、さまざまなオプションがあります。

**ページ オプション** 

![todo:画像_代替_文章](page-setup-features_1.png)

ページ設定オプションは、Aspose.Cells で完全にサポートされています。この記事では、Aspose.Cells でページ オプションを設定する方法について説明します。

## **ページ オプションの設定**

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)、Microsoft Excel ファイルを表します。 Workbook クラスには、Excel ファイル内の各ワークシートへのアクセスを可能にする Worksheets コレクションが含まれています。ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラス。

Worksheet クラスは、ページ設定オプションを設定するために使用される PageSetup プロパティを提供します。実際、PageSetup プロパティは、印刷されるワークシートのページ レイアウト オプションを設定できるようにする PageSetup クラスのオブジェクトです。 PageSetup クラスは、ページ設定オプションを設定するために使用されるさまざまなプロパティを提供します。これらのプロパティのいくつかを以下で説明します。

### **ページの向き**

ページの向きは、[**ページ設定**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)クラス'[**setOrientation(PageOrientationType)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Orientation)方法。の[**setOrientation(PageOrientationType)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Orientation)メソッドは[**PageOrientationType**](https://reference.aspose.com/cells/java/com.aspose.cells/PageOrientationType)パラメータとしての列挙。のメンバー[**PageOrientationType**](https://reference.aspose.com/cells/java/com.aspose.cells/PageOrientationType)以下に列挙します。

|**ページの向きの種類**|**説明**|
|:- |:- |
|[**風景**](https://reference.aspose.com/cells/java/com.aspose.cells/pageorientationtype#LANDSCAPE)|横向き|
|[**ポートレート**](https://reference.aspose.com/cells/java/com.aspose.cells/pageorientationtype#PORTRAIT)|縦向き|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-PageOrientation-PageOrientation.java" >}}

### **スケーリング係数**

倍率を調整して、ワークシートのサイズを縮小または拡大することができます。[**setZoom**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Zoom)の方法[**ページ設定**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)クラス。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ScalingFactor-ScalingFactor.java" >}}

### **FitToPages オプション**

ワークシートの内容を特定のページ数に合わせるには、[**ページ設定**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)クラス'[**setFitToPagesTall**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesTall)と[**setFitToPagesWide**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesWide)メソッド。これらのメソッドは、ワークシートのスケーリングにも使用されます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-FitToPagesOptions-FitToPagesOptions.java" >}}

### **用紙サイズ**

を使用して、ワークシートが印刷される用紙サイズを設定します。[**ページ設定**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)クラス'[**用紙サイズ**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PaperSize)財産。 PaperSize プロパティは、[**用紙サイズの種類**](https://reference.aspose.com/cells/java/com.aspose.cells/PaperSizeType)以下に列挙します。

|**用紙サイズの種類**|**説明**|
|:- |:- |
|紙10x14|10インチ×14インチ。|
|紙11x17|11インチ×17インチ。|
|論文A3|A3（297mm×420mm）|
|用紙A4|A4（210mm×297mm）|
|紙A4小|A4小（210mm×297mm）|
|論文A5|A5（148mm×210mm）|
|論文B3|B3（13.9×19.7インチ）|
|紙B4|B4（250mm×354mm）|
|紙B5|B5（182mm×257mm）|
|紙ビジネスカード|名刺（90mm×55mm）|
|紙Cシート|Cサイズシート|
|紙Dシート|Dサイズシート|
|紙封筒10|封筒 #10 (4-1/8 インチ x 9-1/2 インチ)|
|紙封筒11|封筒 #11 (4-1/2 インチ x 10-3/8 インチ)|
|紙封筒12|封筒 #12 (4-1/2 インチ x 11 インチ)|
|紙封筒14|封筒 #14 (5 インチ x 11-1/2 インチ)|
|紙封筒9|封筒 #9 (3-7/8 インチ x 8-7/8 インチ)|
|紙封筒B4|封筒 B4 (250mm x 353mm)|
|紙封筒B5|封筒 B5 (176mm x 250mm)|
|紙封筒B6|封筒B6（176mm×125mm）|
|紙封筒C3|封筒 C3 (324 mm x 458 mm)|
|紙封筒C4|封筒 C4 (229mm x 324mm)|
|紙封筒C5|封筒 C5 (162 mm x 229 mm)|
|紙封筒C6|封筒 C6 (114 mm x 162 mm)|
|紙封筒C65|封筒 C65 (114mm x 229mm)|
|紙封筒DL|封筒 DL (110mm x 220mm)|
|紙封筒イタリア|封筒 イタリア (110 mm x 230 mm)|
|紙封筒モナーク|封筒モナーク (3-7/8 インチ x 7-1/2 インチ)|
|紙封筒個人|封筒 (3-5/8 インチ x 6-1/2 インチ)|
|紙Eシート|Eサイズシート|
|ペーパーエグゼクティブ|エグゼクティブ (7-1/2 インチ x 10-1/2 インチ)|
|PaperFanfoldLegalドイツ語|ドイツ リーガル ファンフォールド (8-1/2 インチ x 13 インチ)|
|PaperFanfoldStdGerman|ドイツ標準折り紙 (8-1/2 インチ x 12 インチ)|
|PaperFanfoldUS|米国標準の連続紙 (14-7/8 インチ x 11 インチ)|
|ペーパーフォリオ|フォリオ (8-1/2 インチ x 13 インチ)|
|ペーパーレジャー|元帳 (17 インチ x 11 インチ)|
|紙法務|リーガル (8-1/2 インチ x 14 インチ)|
|紙の手紙|レター (8-1/2 インチ x 11 インチ)|
|紙手紙小|レター小 (8-1/2 インチ x 11 インチ)|
|ペーパーノート|メモ (8-1/2 インチ x 11 インチ)|
|ペーパークォート|四つ折り（215mm×275mm）|
|論文声明|ステートメント (5-1/2 インチ x 8-1/2 インチ)|
|紙タブロイド|タブロイド (11 インチ x 17 インチ)|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ManagePaperSize-ManagePaperSize.java" >}}

### **印刷品質**

で印刷するワークシートの印刷品質を設定します。[**ページ設定**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)クラス'[**setPrintQuality**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintQuality)方法。印刷品質の測定単位は、1 インチあたりのドット数 (DPI) です。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintQuality-SetPrintQuality.java" >}}

### **最初のページ番号**

を使用して、ワークシート ページの番号付けを開始します。[**ページ設定**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)クラス'[**setFirstPageNumber**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FirstPageNumber)方法。 setFirstPageNumber メソッドは、最初のワークシート ページのページ番号を設定し、以降のページは昇順で番号付けされます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetFirstPageNumber-SetFirstPageNumber.java" >}}

## **マージンの設定**

Aspose.Cells は Microsoft Excel のページ設定オプションを完全にサポートします。開発者は、印刷プロセスを制御するためにワークシートのページ設定を構成する必要がある場合があります。このトピックでは、Aspose.Cells を使用してページの余白を構成する方法について説明します。

**Microsoft Excel のページ余白**

![todo:画像_代替_文章](page-setup-features_2.png)

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)Microsoft Excel ファイルを表します。 Workbook クラスには、Excel ファイル内の各ワークシートへのアクセスを可能にする Worksheets コレクションが含まれています。ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラス。

 Worksheet クラスは、ページ設定オプションを設定するために使用される PageSetup プロパティを提供します。 PageSetup 属性は、[**ページ設定**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)印刷されたワークシートにさまざまなページ レイアウト オプションを設定できるようにするクラス。 PageSetup クラスは、ページ設定オプションの設定に使用されるさまざまなプロパティとメソッドを提供します。

### **ページ余白**

ページの余白 (上下左右) を設定する[**ページ設定**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)クラスのメンバー。ページ余白を指定するために使用されるいくつかの方法を以下に示します。

- [**setLeftMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#LeftMargin)
- [**setRightMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#RightMargin)
- [**setTopMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#TopMargin)
- [**setBottomMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#BottomMargin)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetMargins-SetMargins.java" >}}

### **ページの中央に配置**

ページの水平方向と垂直方向の中央に何かを配置することができます。の[**ページ設定**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)クラスには、この目的のためのメンバーがあります。[**setCenterHorizontally**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#CenterHorizontally)と[**setCenterVertically**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#CenterVertically).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CenterOnPage-CenterOnPage.java" >}}

### **ヘッダーとフッターの余白**

でヘッダーとフッターの余白を設定する[**ページ設定**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)などのメンバー[**setHeaderMargin**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#HeaderMargin)と[**setFooterMargin**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FooterMargin).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HeaderAndFooterMargins-HeaderAndFooterMargins.java" >}}

## **ヘッダーとフッターの設定**

ヘッダーとフッターは、ページの上マージンの上または下マージンの下にあるテキストと画像のセクションです。ワークシートにヘッダーとフッターを追加することもできます。ヘッダーとフッターを使用して、ページ番号、著者名、ドキュメントのタイトル、日付と時刻など、あらゆる種類の有用な情報を表示できます。ヘッダーとフッターも [ページ設定] ダイアログを使用して管理されます。

**ページ設定ダイアログ** 

![todo:画像_代替_文章](page-setup-features_3.png)

Aspose.Cells では、実行時にヘッダーとフッターをワークシートに追加できますが、ヘッダーとフッターは印刷用に事前に設計されたファイルに手動で設定することをお勧めします。 Microsoft Excel を GUI ツールとして使用すると、ヘッダーとフッターを簡単に設定して開発時間を短縮できます。 Aspose.Cells は、ファイルをインポートして、これらの設定を予約できます。

実行時にヘッダーとフッターを追加するために、Aspose.Cells はフォーマットを制御する特別なクラスといくつかのスクリプト コマンドを提供します。

### **スクリプト コマンド**

スクリプト コマンドは、Aspose.Cells が提供する特別なコマンドで、開発者がヘッダーとフッターをフォーマットできるようにします。

|**スクリプト コマンド**|**説明**|
|:- |:- |
|&P|現在のページ番号。|
|&G|絵。|
|&N|総ページ数。|
|&D|現在の日付。|
|&T|現在の時刻。|
|&A|ワークシートの名前。|
|&F|パスなしのファイル名。|
|&"\<FontName>"|フォント名。例: &"Arial"|
|&"\<FontName>, \<FontStyle>"|スタイルのあるフォント名。例: &"Arial,Bold"|
|&\<FontSize>|フォントサイズを表します。例: 「&14abc」。ただし、このコマンドの後にヘッダーに印刷されるプレーンな数字が続く場合、これはフォント サイズからスペース文字で区切られる必要があります。例: 「&14 123」。|

### **ヘッダーとフッターを設定する**

の[**ページ設定**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)クラスはメソッドを提供します[**setHeader**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setHeader(int,%20java.lang.String) ヘッダーを追加し、[**setFooter**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFooter(int,%20java.lang.String)) ワークシートにフッターを追加します。スクリプトは、上記のすべてのメソッドの引数として使用されます。ヘッダーまたはフッターに使用されるスクリプトを表します。このスクリプトには、ヘッダーまたはフッターをフォーマットするためのスクリプト コマンドが含まれています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetHeadersAndFooters-SetHeadersAndFooters.java" >}}

### **グラフィックをヘッダーまたはフッターに挿入する**

の[**ページ設定**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)クラスにはメソッドがあります[**setHeadPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setHeaderPicture(int,%20byte[]) ） と[**setFooterPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFooterPicture(int,%20byte[])) ワークシートのヘッダーとフッターに画像を追加します。これらのメソッドは、次の 2 つのパラメーターを取ります。

- **セクション**、画像が配置されるヘッダーまたはフッターのセクション。左、中央、右の 3 つのセクションがあり、それぞれ数値 0、1、2 で表されます。
- **ファイル入力ストリーム**、グラフィックデータ。バイナリ データは、バイト配列のバッファーに書き込む必要があります。

コードを実行してファイルを開いた後、Microsoft Excel でワークシートのヘッダーを確認します。

1. 上で**ファイル**メニュー、選択**ページ設定**.
1.  [ページ設定] ダイアログで、**ヘッダー/フッター**タブ。

**ヘッダー/フッターへのグラフィックの挿入** 

![todo:画像_代替_文章](page-setup-features_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-InsertImageInHeaderFooter-InsertImageInHeaderFooter.java" >}}

### **最初のページ ヘッダーのみにグラフィックを挿入する**

の[**ページ設定**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)クラスには他にも便利なメソッドがあります。たとえば、[**セットピクチャー**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setPicture(boolean,%20boolean,%20boolean,%20int,%20byte[])), [**setFirstPageHeader**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFirstPageHeader(int,%20java.lang.String)), [**setFirstPageFooter**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFirstPageFooter(int,%20java.lang.String))、ワークシートの最初のページのヘッダー/フッターに画像を追加します。最初のページは特別なページです。会社のロゴなど、特別な情報を表示したいのが一般的です。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-InsertGraphicinFirstPageHeaderOnly-InsertGraphicinFirstPageHeaderOnly.java" >}}

## **印刷オプションの設定**

Microsoft Excel のページ設定には、ユーザーがワークシート ページの印刷方法を制御できるいくつかの印刷オプション (シート オプションとも呼ばれます) が用意されています。これらの印刷オプションにより、ユーザーは次のことができます。

- ワークシート上の特定の印刷領域を選択します。
- タイトルを印刷します。
- グリッド線を印刷します。
- 行と列の見出しを印刷する
- ドラフト品質を実現します。
- コメントを印刷します。
- セル エラーを出力します。
- ページの順序を定義します。

これらの印刷オプションのすべてを以下に示します。

**印刷 (シート) オプション** 

![todo:画像_代替_文章](page-setup-features_5.png)

### **印刷オプションとシート オプションの設定**

spose.Cells は、Microsoft Excel によって提供されるすべての印刷オプションをサポートし、開発者は、によって提供されるプロパティを使用して、ワークシートのこれらのオプションを簡単に構成できます。[**ページ設定**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)クラス。これらのプロパティがどのように使用されるかについては、以下で詳しく説明します。

### **印刷範囲の設定**

デフォルトでは、データを含むワークシートのすべての領域が印刷領域に組み込まれます。開発者は、ワークシートの特定の印刷領域を設定できます。

特定の印刷領域を選択するには、[**ページ設定**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)クラス'[**setPrintArea**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintArea)財産。印刷領域を定義するセル範囲をこのプロパティに割り当てます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintArea-SetPrintArea.java" >}}

### **印刷タイトルの設定**

Aspose.Cells を使用すると、印刷されたワークシートのすべてのページで行ヘッダーと列ヘッダーを繰り返すように指定できます。これを行うには、[**ページ設定**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)クラス'[**setPrintTitleColumns**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintTitleColumns)と[**setPrintTitleRows**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintTitleRows)プロパティ。

繰り返される行または列は、行番号または列番号を渡すことによって定義されます。たとえば、行は $1:$2 として定義され、列は $A:$B として定義されます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintTitle-SetPrintTitle.java" >}}

### **その他の印刷オプションの設定**

の[**ページ設定**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)クラスには、次のような一般的な印刷オプションを設定するためのその他のプロパティもいくつか用意されています。

- [**setPrintGridlines**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintGridlines)は、グリッド線を印刷するかどうかを定義するブール型のプロパティです。
- [*setPrintHeadings*](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintHeadings)行と列の見出しを印刷するかどうかを定義するブール型のプロパティです。
- [**setBlackAndWhite**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#BlackAndWhite)は、ワークシートを白黒モードで印刷するかどうかを定義するブール型のプロパティです。
- [**setPrintComments**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments)、ワークシートまたはワークシートの最後に印刷コメントを表示するかどうかを定義します。
- [**setPrintDraft**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintDraft)は、ワークシートを下書き品質で印刷するかどうかを定義するブール型のプロパティです。
- [**setPrintErrors**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors)は、セル エラーを表示、空白、ダッシュ、または N/A として出力するかどうかを定義します。

を設定するには[**印刷コメント**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments)と[**印刷エラー**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors)プロパティ、Aspose.Cells は 2 つの列挙も提供します。[**PrintCommentsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintCommentsType)と[**PrintErrorsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintErrorsType)に割り当てられる定義済みの値が含まれています。[**setPrintComments**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments)と[**setPrintErrors**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors)プロパティ。

の定義済みの値[**PrintCommentsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintCommentsType)列挙については後述します。

|**印刷コメントの種類**|**説明**|
|:- |:- |
|[**PRINT_IN_PLACE**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT_IN_PLACE)|ワークシートに表示されているコメントを印刷するように指定します。|
|[**PRINT_NO_COMMENTS**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT_NO_COMMENTS)|コメントを印刷しないように指定します。|
|[**PRINT_SHEET_END**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT_SHEET_END)|ワークシートの最後にコメントを印刷するように指定します。|

の定義済みの値[**PrintErrorsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintErrorsType)列挙については後述します。

|**印刷エラーの種類**|**説明**|
|:- |:- |
|[*PRINT_ERRORS_BLANK*](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_BLANK)|エラーを出力しないように指定します。|
|[**PRINT_ERRORS_DASH**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_DASH)|エラーを「--」として出力するように指定します。|
|[**PRINT_ERRORS_DISPLAYED**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_DISPLAYED)|エラーを表示どおりに印刷するように指定します。|
|[**PRINT_ERRORS_NA**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_NA)|エラーを「#N/A」として出力するように指定します。|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-OtherPrintOptions-OtherPrintOptions.java" >}}

### **ページの順序を設定する**

の[**ページ設定**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)クラスが提供する[**setOrder**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Order)ワークシートの複数ページの印刷を注文するために使用されるプロパティ。ページを次のように並べ替えるには、次の 2 つの方法があります。

- **ダウン・アンド・オーバー**右側のページを印刷する前に、すべてのページを下に印刷します。
- **オーバー・アンド・ダウン**下のページを印刷する前に、ページを左から右に印刷します。

 Aspose.Cells は列挙を提供し、[**PrintOrderType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintOrderType)に割り当てられるすべての事前定義された注文タイプを含む[**setOrder**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Order)方法。

の定義済みの値[**PrintOrderType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintOrderType)列挙については後述します。

|**印刷注文の種類**|**説明**|
|:- |:- |
|[**DOWN_THEN_OVER**](https://reference.aspose.com/cells/java/com.aspose.cells/printordertype#DOWN_THEN_OVER)|印刷してから重ねます。|
|[**OVER_THEN_DOWN**](https://reference.aspose.com/cells/java/com.aspose.cells/printordertype#OVER_THEN_DOWN)|重ねてから下に印刷します。|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPageOrder-SetPageOrder.java" >}}

## **Excel ファイルのワークシートの既存の PrinterSettings を削除する**

このトピックに関連するこの記事を参照してください。

## **先行トピック**
- [ページ設定倍率の計算](/cells/ja/java/calculate-page-setup-scaling-factor/)
- [ページ設定の設定をソース ワークシートからコピー先ワークシートにコピーする](/cells/ja/java/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/)
- [ワークシートの用紙サイズが自動かどうかを判断する](/cells/ja/java/determine-if-paper-size-of-worksheet-is-automatic/)
- [ワークシートの PageSetup から用紙の幅と高さを取得する](/cells/ja/java/get-paper-width-and-height-from-pagesetup-of-worksheet/)
- [レンダリング用ワークシートのカスタム用紙サイズの実装](/cells/ja/java/implement-custom-paper-size-of-worksheet-for-rendering/)
- [ページ設定と印刷オプション](/cells/ja/java/page-setup-and-printing-options/)
- [Excel ファイルのワークシートの既存の PrinterSettings を削除する](/cells/ja/java/remove-existing-printersettings-of-worksheets-in-excel-file/)
