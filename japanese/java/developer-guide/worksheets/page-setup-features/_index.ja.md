---
title: ページ設定機能
type: docs
weight: 40
url: /ja/java/page-setup-features/
---

時々、印刷を制御するためにワークシートのページ設定設定を構成する必要があります。これらのページ設定設定にはさまざまなオプションが用意されています。

ページオプション 

![todo:image_alt_text](page-setup-features_1.png)

Aspose.Cellsではページ設定オプションを完全にサポートしています。本記事では、Aspose.Cellsを使用してページオプションを設定する方法について説明します。

## **ページオプションの設定**

Aspose.Cellsでは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスが提供されています。WorkbookクラスにはWorksheetsコレクションが含まれており、Excelファイル内の各ワークシートにアクセスできます。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスによって表されます。

WorksheetクラスにはPageSetupプロパティがあり、印刷されるワークシートのページ設定オプションを設定するために使用されます。実際、PageSetupプロパティはPageSetupクラスのオブジェクトであり、印刷されるワークシートのページレイアウトオプションを設定することが可能です。PageSetupクラスにはページ設定オプションを設定するために使用されるさまざまなプロパティがあります。これらのプロパティのうちいくつかについて以下で説明します。

### **ページの向き**

ページの向きは[**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)クラスの[**setOrientation(PageOrientationType)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Orientation)メソッドを使用して縦または横に設定できます。[**setOrientation(PageOrientationType)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Orientation)メソッドは[**PageOrientationType**](https://reference.aspose.com/cells/java/com.aspose.cells/PageOrientationType)列挙型をパラメータとして受け取ります。[**PageOrientationType**](https://reference.aspose.com/cells/java/com.aspose.cells/PageOrientationType)列挙型のメンバーは以下にリストされています。

|**ページの向きの種類**|**説明**|
| :- | :- |
|[**LANDSCAPE**](https://reference.aspose.com/cells/java/com.aspose.cells/pageorientationtype#LANDSCAPE)|横向きのページレイアウト|
|[**PORTRAIT**](https://reference.aspose.com/cells/java/com.aspose.cells/pageorientationtype#PORTRAIT)|縦向きのページレイアウト|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-PageOrientation-PageOrientation.java" >}}

### **拡大/縮小率**

ワークシートのサイズを縮小または拡大することが可能です。その際には、[**setZoom**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Zoom)クラスの[**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)メソッドを使用します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ScalingFactor-ScalingFactor.java" >}}

### **ページに合わせるオプション**

ワークシートの内容を特定のページ数に合わせるには、[**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)クラスの[**setFitToPagesTall**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesTall)および[**setFitToPagesWide**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesWide)メソッドを使用します。これらのメソッドはワークシートをスケーリングするためにも使用されます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-FitToPagesOptions-FitToPagesOptions.java" >}}

### **用紙サイズ**

ワークシートの用紙サイズを設定するには、[**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)クラスの[**PaperSize**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PaperSize)プロパティを使用します。PaperSizeプロパティは、以下にリストされている[**PaperSizeType**](https://reference.aspose.com/cells/java/com.aspose.cells/PaperSizeType)列挙型の定義済みの値の一つを受け入れます。

|**用紙サイズの種類**|**説明**|
| :- | :- |
|Paper10x14|10 in. x 14 in.|
|Paper11x17|11 in. x 17 in.|
|PaperA3|A3 (297 mm x 420 mm)|
|PaperA4|A4 (210 mm x 297 mm)|
|PaperA4Small|A4 Small (210 mm x 297 mm)|
|PaperA5|A5 (148 mm x 210 mm)|
|PaperB3|B3 (13.9 x 19.7 inches)|
|PaperB4|B4 (250 mm x 354 mm)|
|PaperB5|B5 (182 mm x 257 mm)|
|PaperBusinessCard|Business Card (90 mm x 55 mm)|
|PaperCSheet|C size sheet|
|PaperDSheet|D size sheet|
|PaperEnvelope10|Envelope #10 (4-1/8 in. x 9-1/2 in.)|
|PaperEnvelope11|Envelope #11 (4-1/2 in. x 10-3/8 in.)|
|PaperEnvelope12|Envelope #12 (4-1/2 in. x 11 in.)|
|PaperEnvelope14|Envelope #14 (5 in. x 11-1/2 in.)|
|PaperEnvelope9|Envelope #9 (3-7/8 in. x 8-7/8 in.)|
|PaperEnvelopeB4|Envelope B4 (250 mm x 353 mm)|
|PaperEnvelopeB5|Envelope B5 (176 mm x 250 mm)|
|PaperEnvelopeB6|Envelope B6 (176 mm x 125 mm)|
|PaperEnvelopeC3|Envelope C3 (324 mm x 458 mm)|
|PaperEnvelopeC4|Envelope C4 (229 mm x 324 mm)|
|PaperEnvelopeC5|Envelope C5 (162 mm x 229 mm)|
|PaperEnvelopeC6|Envelope C6 (114 mm x 162 mm)|
|PaperEnvelopeC65|Envelope C65 (114 mm x 229 mm)|
|PaperEnvelopeDL|Envelope DL (110 mm x 220 mm)|
|PaperEnvelopeItaly|Envelope Italy (110 mm x 230 mm)|
|PaperEnvelopeMonarch|Envelope Monarch (3-7/8 in. x 7-1/2 in.)|
|PaperEnvelopePersonal|Envelope (3-5/8 in. x 6-1/2 in.)|
|PaperESheet|E size sheet|
|PaperExecutive|Executive (7-1/2 in. x 10-1/2 in.)|
|PaperFanfoldLegalGerman|German Legal Fanfold (8-1/2 in. x 13 in.)|
|PaperFanfoldStdGerman|German Standard Fanfold (8-1/2 in. x 12 in.)|
|PaperFanfoldUS|U.S. Standard Fanfold (14-7/8 in. x 11 in.)|
|PaperFolio|Folio (8-1/2 in. x 13 in.)|
|PaperLedger|Ledger (17 in. x 11 in.)|
|PaperLegal|Legal (8-1/2 in. x 14 in.)|
|PaperLetter|Letter (8-1/2 in. x 11 in.)|
|PaperLetterSmall|Letter Small (8-1/2 in. x 11 in.)|
|PaperNote|Note (8-1/2 in. x 11 in.)|
|PaperQuarto|Quarto (215 mm x 275 mm)|
|PaperStatement|Statement (5-1/2 in. x 8-1/2 in.)|
|PaperTabloid|Tabloid (11 in. x 17 in.)|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ManagePaperSize-ManagePaperSize.java" >}}

### **印刷品質**

印刷されるワークシートの印刷品質を[**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)クラスの[**setPrintQuality**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintQuality)メソッドで設定します。印刷品質の計測単位は、インチあたりのドット(DPI)です。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintQuality-SetPrintQuality.java" >}}

### **最初のページ番号**

ワークシートページの番号付けを始めるには、[**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)クラスの[**setFirstPageNumber**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FirstPageNumber)メソッドを使用します。setFirstPageNumberメソッドは最初のワークシートページのページ番号を設定し、次のページは昇順に番号が付けられます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetFirstPageNumber-SetFirstPageNumber.java" >}}

## **マージンの設定**

Aspose.CellsはMicrosoft Excelのページ設定オプションを完全にサポートしています。開発者は印刷プロセスを制御するためにワークシートのページ設定設定を構成する必要があります。このトピックでは、Aspose.Cellsを使用してページ余白を設定する方法について説明します。

Microsoft Excelのページ余白

![todo:image_alt_text](page-setup-features_2.png)

Aspose.CellsではMicrosoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスが提供されています。WorkbookクラスにはExcelファイル内の各ワークシートにアクセスするためのWorksheetsコレクションが含まれています。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスによって表されます。

WorksheetクラスにはPageSetupプロパティがあり、印刷されるワークシートのページ設定オプションを設定するために使用されます。 PageSetup属性は、印刷されるワークシートの異なるページレイアウトオプションを設定することが可能にする[**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)クラスのオブジェクトです。PageSetupクラスには、ページ設定オプションを設定するために使用されるさまざまなプロパティとメソッドがあります。

### **ページ余白**

ページの余白を指定するために、[**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)クラスのメンバーを使用します。ページ余白を指定するために使用されるいくつかのメソッドが以下に示されています。

- [**setLeftMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#LeftMargin)
- [**setRightMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#RightMargin)
- [**setTopMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#TopMargin)
- [**setBottomMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#BottomMargin)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetMargins-SetMargins.java" >}}

### **ページの中央に配置**

何かをページの水平方向と垂直方向に中央配置することが可能です。[**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)クラスにはそれを目的としたメンバーがあります：[**setCenterHorizontally**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#CenterHorizontally) と [**setCenterVertically**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#CenterVertically)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CenterOnPage-CenterOnPage.java" >}}

### **ヘッダーとフッタのマージン**

[**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) のメンバー（例：[**setHeaderMargin**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#HeaderMargin) と [**setFooterMargin**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FooterMargin)）を使用して、ヘッダーとフッタのマージンを設定します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HeaderAndFooterMargins-HeaderAndFooterMargins.java" >}}

## **ヘッダーとフッタの設定**

ヘッダーとフッタはページの上部マージンの上または下部マージンの下にあるテキストや画像のセクションです。ワークシートにもヘッダーやフッタを追加することが可能です。ヘッダー＆フッタは、ページ番号、作成者名、ドキュメントタイトル、または日付と時刻などの有用な情報を表示するために使用できます。ヘッダー＆フッタは、ページ設定ダイアログを使って管理されます。

**ページ設定ダイアログ** 

![todo:image_alt_text](page-setup-features_3.png)

Aspose.Cells により、ワークシートにランタイムでヘッダーやフッタを追加することが可能ですが、印刷用にヘッダーとフッタを事前に設定されたファイルに手動で設定することが推奨されています。開発時間の短縮のために、Microsoft Excel を GUI ツールとして使用して簡単にヘッダーやフッタを設定することができます。Aspose.Cells はこの設定をインポートし、予約します。

ヘッダーやフッタをランタイムで追加するために、Aspose.Cells では特別なクラスと一部のスクリプトコマンドが提供されます。

### **スクリプトコマンド**

スクリプトコマンドは、Aspose.Cells が提供する特別なコマンドであり、開発者がヘッダーやフッタのフォーマットを制御することを可能にします。

|**スクリプトコマンド**|**説明**|
| :- | :- |
|&P|現在のページ番号。
|&G|画像。
|&N|合計ページ数。
|&D|現在の日付。
|&T|現在時刻。
|&A|ワークシートの名前。
|&F|パスを除いたファイル名。
|&&Text|は &Text を表示します。例： &&WO は &WO と表示されます|
|&"\<FontName>"|フォント名。たとえば: &"Arial"
|&"\<FontName>, \<FontStyle>"|スタイル付きのフォント名。たとえば: &"Arial,Bold"
|&\<FontSize>|フォントサイズを表します。例：「&14abc」。ただし、このコマンドの後にヘッダーに印刷されるプレーンな数字が続く場合、その数字はフォントサイズとスペースで区切る必要があります。例：「&14 123」。|

### **ヘッダーやフッタの設定**

[**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) クラスにはワークシートにヘッダーを追加するためのメソッド [**setHeader**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setHeader-int-java.lang.String-) とフッタを追加するための [**setFooter**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFooter-int-java.lang.String-) が提供されます。上記の全てのメソッドに対する引数としてスクリプトが使用されます。これは、ヘッダーやフッタを書式設定するためのスクリプトです。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetHeadersAndFooters-SetHeadersAndFooters.java" >}}

### **ヘッダーやフッタにグラフィックを挿入**

[**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) クラスには、ワークシートのヘッダーやフッタに画像を追加するための [**setHeadPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setHeaderPicture-int-byte[]-) と [**setFooterPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFooterPicture-int-byte[]-) のメソッドがあります。これらのメソッドには2つのパラメータが必要です：

- **セクション**：画像を配置するヘッダーまたはフッタのセクション。0、1、2 の数値で表される左、中央、右の3つのセクションがあります。
- **ファイル入力ストリーム**：グラフィカルデータ。バイナリデータはバイト配列のバッファに書き込まれるべきです。

コードを実行し、ファイルを開いたら、Microsoft Excel のワークシートのヘッダをチェックしてください：

1. **ファイル** メニューから **ページ設定** を選択します。
1. ページ設定ダイアログで、**ヘッダー/フッター**タブを選択します。

**ヘッダー/フッターにグラフィックを挿入する** 

![todo:image_alt_text](page-setup-features_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-InsertImageInHeaderFooter-InsertImageInHeaderFooter.java" >}}

### **最初のページヘッダーにグラフィックを挿入する**

[**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)クラスにはほかにも便利なメソッドがあり、たとえば[**setPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setPicture-boolean-boolean-boolean-int-byte[]-)、[**setFirstPageHeader**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFirstPageHeader-int-java.lang.String-)、[**setFirstPageFooter**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFirstPageFooter-int-java.lang.String-)です。ワークシートの最初のページヘッダー/フッターに図を追加するためのものです。最初のページは特別なページです：特別な情報を表示させたいということが一般的です。たとえば、会社のロゴなどです。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-InsertGraphicinFirstPageHeaderOnly-InsertGraphicinFirstPageHeaderOnly.java" >}}

## **印刷オプションの設定**

Microsoft Excelのページ設定は、ワークシートのページの印刷方法を制御するいくつかの印刷オプション（シートオプションとも呼ばれます）を提供しています。これらの印刷オプションにより、次のことが可能です。

- ワークシート上の特定の印刷範囲を選択する。
- タイトルを印刷する。
- グリッド線を印刷する。
- 行と列の見出しを印刷する
- 下書き品質を実現する。
- コメントを印刷する。
- セルエラーを印刷する。
- ページ順序を定義する。

これらの印刷オプションは以下に示されています。

**印刷（シート）オプション** 

![todo:image_alt_text](page-setup-features_5.png)

### **印刷オプションおよびシートオプションの設定**

spose.CellsはMicrosoft Excelが提供するすべての印刷オプションをサポートし、開発者は[**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)クラスが提供するプロパティを使用してワークシートの印刷オプションを簡単に設定できます。これらのプロパティの使用方法については以下でさらに詳しく説明します。

### **印刷範囲の設定**

デフォルトでは、印刷エリアにはデータを含むワークシートのすべてのエリアが含まれます。開発者はワークシートの特定の印刷エリアを設定できます。

特定の印刷エリアを選択するには、[**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)クラスの[**setPrintArea**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintArea)プロパティを使用します。このプロパティに印刷エリアを定義するセル範囲を割り当てます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintArea-SetPrintArea.java" >}}

### **印刷タイトルを設定する**

Aspose.Cellsでは、印刷されるワークシートのすべてのページで行見出しと列見出しを繰り返すことができます。これを行うには、[**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)クラスの[**setPrintTitleColumns**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintTitleColumns)および[**setPrintTitleRows**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintTitleRows)プロパティを使用します。

繰り返す行または列は、その行番号または列番号を渡すことで定義されます。たとえば、行は$1:$2と定義され、列は$A:$Bと定義されます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintTitle-SetPrintTitle.java" >}}

### **その他の印刷オプションの設定**

[**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)クラスは、次の一般的な印刷オプションを設定するためのいくつかの他のプロパティも提供します。

- [**setPrintGridlines**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintGridlines)、グリッド線を印刷するかどうかを定義するブールプロパティ。
- [*setPrintHeadings*](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintHeadings)、行見出しと列見出しを印刷するかどうかを定義するブールプロパティ。
- [**setBlackAndWhite**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#BlackAndWhite)、ワークシートを白黒モードで印刷するかどうかを定義するブールプロパティ。
- [**setPrintComments**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments)、ワークシートの印刷コメントを表示するか、ワークシートの末尾に表示するかを定義する。
- [**setPrintDraft**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintDraft)、ワークシートを下書き品質で印刷するかどうかを定義するブールプロパティ。
- [**setPrintErrors**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors)、セルのエラーを表示、空白、ダッシュ、N/A いずれで印刷するかを定義します。

Aspose.Cells は、[**PrintComments**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments) および [**PrintErrors**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors) プロパティを設定するために、[**PrintCommentsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintCommentsType) および [**PrintErrorsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintErrorsType) という 2 つの列挙体も提供しており、それぞれ [**setPrintComments**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments) および [**setPrintErrors**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors) プロパティに割り当てるための事前定義値が含まれています。

[**PrintCommentsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintCommentsType) 列挙体の事前定義値については、以下に説明します。

|**コメント印刷タイプ**|**説明**|
| :- | :- |
|[**PRINT_IN_PLACE**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT-IN-PLACE)| ワークシートに表示されているコメントを印刷する設定。 |
|[**PRINT_NO_COMMENTS**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT-NO-COMMENTS)| コメントを印刷しない設定。 |
|[**PRINT_SHEET_END**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT-SHEET-END)|ワークシートの最後にコメントを印刷することを指定します。|

[**PrintErrorsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintErrorsType) 列挙体の事前定義値については以下に説明します。

|**エラー印刷タイプ**|**説明**|
| :- | :- |
|[**PRINT_ERRORS_BLANK**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT-ERRORS-BLANK)|エラーを印刷しないことを指定します。|
|[**PRINT_ERRORS_DASH**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT-ERRORS-DASH)|エラーを「--」として印刷することを指定します。|
|[**PRINT_ERRORS_DISPLAYED**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT-ERRORS-DISPLAYED)|表示されたとおりにエラーを印刷することを指定します。|
|[**PRINT_ERRORS_NA**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT-ERRORS-NA)|エラーを「#N/A」として印刷することを指定します。|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-OtherPrintOptions-OtherPrintOptions.java" >}}

### **ページ順の設定**

[**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) クラスは、ワークシートの複数のページを印刷する際に使用される [**setOrder**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Order) プロパティを提供します。以下のような 2 つの順序の可能性があります：

- **下に続いて右** は、右側よりも下側のページを印刷します。
- **右に続いて下** は、下側よりも右側のページを印刷します。

Aspose.Cells は、[**PrintOrderType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintOrderType) という列挙体を提供しており、それを [**setOrder**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Order) メソッドに割り当てるためのすべての事前定義の順序タイプが含まれています。

[**PrintOrderType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintOrderType) 列挙体の事前定義値については以下に説明します。

|**印刷順序タイプ**|**説明**|
| :- | :- |
|[**DOWN_THEN_OVER**](https://reference.aspose.com/cells/java/com.aspose.cells/printordertype#DOWN-THEN-OVER)|下にプリントし、その後横にプリントします。|
|[**OVER_THEN_DOWN**](https://reference.aspose.com/cells/java/com.aspose.cells/printordertype#OVER-THEN-DOWN)|横にプリントし、その後下にプリントします。|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPageOrder-SetPageOrder.java" >}}

## **Excelファイルのワークシートの既存のPrinterSettingsを削除する**

このトピックに関連する記事をご覧ください。

## **高度なトピック**
- [ページ設定スケーリングファクターを計算します](/cells/ja/java/calculate-page-setup-scaling-factor/)
- [ソースワークシートからページ設定を宛先ワークシートにコピー](/cells/ja/java/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/)
- [ワークシートの用紙サイズが自動かどうかを判断する](/cells/ja/java/determine-if-paper-size-of-worksheet-is-automatic/)
- [ワークシートのページ設定から用紙の幅と高さを取得する](/cells/ja/java/get-paper-width-and-height-from-pagesetup-of-worksheet/)
- [レンダリングのためのワークシートのカスタム用紙サイズを実装する](/cells/ja/java/implement-custom-paper-size-of-worksheet-for-rendering/)
- [ページ設定および印刷オプション](/cells/ja/java/page-setup-and-printing-options/)
- [Excelファイルのワークシートの既存のPrinterSettingsを削除する](/cells/ja/java/remove-existing-printersettings-of-worksheets-in-excel-file/)
{{< app/cells/assistant language="java" >}}
