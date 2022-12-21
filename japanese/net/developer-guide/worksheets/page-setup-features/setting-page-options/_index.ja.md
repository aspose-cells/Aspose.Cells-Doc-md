---
title: ページ オプションの設定
type: docs
weight: 10
url: /ja/net/setting-page-options/
---
{{% alert color="primary" %}}

場合によっては、印刷を制御するためにワークシートのページ設定を構成する必要があります。これらのページ設定の設定には、さまざまなオプションがあります。

{{% /alert %}}

## **ページ オプションの設定**

ページ設定オプションは、Aspose.Cells で完全にサポートされています。この記事では、Aspose.Cells でページ オプションを設定する方法を説明し、設定のコード サンプルを示します。

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)、Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Excel ファイル内の各ワークシートにアクセスできるコレクション。ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。

の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスが提供する[**ページ設定**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)ワークシートのページ設定オプションを設定するために使用されるプロパティ。実際、これは[**ページ設定**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)プロパティはのオブジェクトです[**ページ設定**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)印刷されたワークシートのさまざまなページ レイアウト オプションを設定するために使用されるクラス。の[**ページ設定**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)クラスは、ページ設定オプションを設定するために使用されるさまざまなプロパティを提供します。これらのプロパティのいくつかを以下で説明します。

### **ページの向き**

ページの向きは、[**ページ設定**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)クラス'[**オリエンテーション**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/orientation)財産。の[**オリエンテーション**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/orientation)プロパティは、[**PageOrientationType**](https://reference.aspose.com/cells/net/aspose.cells/pageorientationtype)以下に列挙します。

|**ページの向きの種類**|**説明**|
|:- |:- |
|風景|横向き|
|肖像画|縦向き|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-PageOrientation-1.cs" >}}

### **スケーリング係数**

倍率を調整して、ワークシートのサイズを縮小または拡大することができます。[**PageSetup.Zoom**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/zoom)財産。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-ScalingFactor-1.cs" >}}

### **FitToPages オプション**

ワークシートの内容を特定のページ数に合わせるには、[**ページ設定**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)クラス'[**FitToPagesTall**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopagestall)と[**FitToPagesWide**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopageswide)プロパティ。これらのプロパティは、ワークシートのスケーリングにも使用されます。

{{% alert color="primary" %}}

次のいずれかを選択できます。[**FitToPagesTall**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopagestall)/[**FitToPagesWide**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopageswide)または[**ズーム**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/zoom)プロパティですが、同時に両方ではありません。

{{% /alert %}}

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-FitToPagesOptions-1.cs" >}}

### **用紙サイズ**

を使用して、ワークシートが印刷される用紙サイズを設定します。[**ページ設定**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)クラス'[**用紙サイズ**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/papersize)財産。の[**用紙サイズ**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/papersize)プロパティは、[**用紙サイズの種類**](https://reference.aspose.com/cells/net/aspose.cells/papersizetype)以下に列挙します。

|**用紙サイズの種類**|**説明**|
|:- |:- |
|紙の手紙|レター (8-1/2 インチ x 11 インチ)|
|紙手紙小|レター小 (8-1/2 インチ x 11 インチ)|
|紙タブロイド|タブロイド (11 インチ x 17 インチ)|
|ペーパーレジャー|元帳 (17 インチ x 11 インチ)|
|紙法務|リーガル (8-1/2 インチ x 14 インチ)|
|論文声明|ステートメント (5-1/2 インチ x 8-1/2 インチ)|
|ペーパーエグゼクティブ|エグゼクティブ (7-1/4 インチ x 10-1/2 インチ)|
|論文A3|A3（297mm×420mm）|
|用紙A4|A4（210mm×297mm）|
|紙A4小|A4小（210mm×297mm）|
|論文A5|A5（148mm×210mm）|
|紙B4|JIS B4（257mm×364mm）|
|紙B5|JIS B5（182mm×257mm）|
|ペーパーフォリオ|フォリオ (8-1/2 インチ x 13 インチ)|
|ペーパークォート|四つ折り（215mm×275mm）|
|紙10x14|10インチ×14インチ。|
|紙11x17|11インチ×17インチ。|
|ペーパーノート|メモ (8-1/2 インチ x 11 インチ)|
|紙封筒9|封筒 #9 (3-7/8 インチ x 8-7/8 インチ)|
|紙封筒10|封筒 #10 (4-1/8 インチ x 9-1/2 インチ)|
|紙封筒11|封筒 #11 (4-1/2 インチ x 10-3/8 インチ)|
|紙封筒12|封筒 #12 (4-1/2 インチ x 11 インチ)|
|紙封筒14|封筒 #14 (5 インチ x 11-1/2 インチ)|
|紙Cシート|Cサイズシート|
|紙Dシート|Dサイズシート|
|紙Eシート|Eサイズシート|
|紙封筒DL|封筒 DL (110mm x 220mm)|
|紙封筒C5|封筒 C5 (162 mm x 229 mm)|
|紙封筒C3|封筒 C3 (324 mm x 458 mm)|
|紙封筒C4|封筒 C4 (229mm x 324mm)|
|紙封筒C6|封筒 C6 (114 mm x 162 mm)|
|紙封筒C65|封筒 C65 (114mm x 229mm)|
|紙封筒B4|封筒 B4（250mm×353mm）|
|紙封筒B5|封筒 B5 (176mm x 250mm)|
|紙封筒B6|封筒B6（176mm×125mm）|
|紙封筒イタリア|封筒 イタリア (110 mm x 230 mm)|
|紙封筒モナーク|封筒モナーク (3-7/8 インチ x 7-1/2 インチ)|
|紙封筒個人|封筒 (3-5/8 インチ x 6-1/2 インチ)|
|PaperFanfoldUS|米国標準の連続紙 (14-7/8 インチ x 11 インチ)|
|PaperFanfoldStdGerman|ドイツ標準折り紙 (8-1/2 インチ x 12 インチ)|
|PaperFanfoldLegalドイツ語|ドイツ リーガル ファンフォールド (8-1/2 インチ x 13 インチ)|
|紙ISOB4|B4（ISO）250×353mm|
|紙日本語はがき|はがき（100mm×148mm）|
|紙9x11|9インチ×11インチ。|
|紙10x11|10インチ×11インチ|
|紙15x11|15インチ×11インチ。|
|紙封筒招待|招待状封筒(220mm×220mm)|
|ペーパーレターエクストラ|US レター エクストラ 9 \275 x 12 インチ|
|ペーパーリーガルエキストラ|US Legal Extra 9 \275 x 15 インチ|
|ペーパータブロイドエキストラ|US Tabloid Extra 11.69 x 18 インチ|
|用紙A4Extra|A4 エクストラ 9.27 x 12.69 インチ|
|ペーパーレター横方向|レター横 8 \275 x 11 インチ|
|紙A4横|A4横210×297mm|
|PaperLetterExtraTransverse|レター エクストラ トランスバース 9\275 x 12 インチ|
|ペーパースーパーA|SuperA/SuperA/A4 227×356mm|
|ペーパースーパーB|SuperB/SuperB/A3 305×487mm|
|ペーパーレタープラス|US レタープラス 8.5 x 12.69 インチ|
|PaperA4Plus|A4プラス 210×330mm|
|用紙A5横|A5横148×210mm|
|紙JISB5横|B5（JIS） 横182×257mm|
|ペーパーA3エクストラ|A3エクストラ 322×445mm|
|PaperA5Extra|A5 エクストラ 174×235mm|
|用紙ISOB5Extra|B5 (ISO) エクストラ 201 x 276 mm|
|論文A2|A2 420×594mm|
|紙A3横|A3横297×420mm|
|PaperA3ExtraTransverse|A3 エクストラ横 322 x 445 mm|
|紙日本語ダブルはがき|往復はがき 200×148mm|
|論文A6|A6 105×148mm|
|紙和封筒角2|封筒 角 2 号|
|紙和封筒角3|封筒 角 3 号|
|PaperJapaneseEnvelopeChou3|封筒 長形 3 号|
|紙日本語封筒Chou4|封筒 長形 4 号|
|紙手紙回転|11インチ×8.5インチ|
|紙A3回転|420mm×297mm|
|用紙A4回転|297mm×210mm|
|用紙A5回転|210mm×148mm|
|用紙JISB4回転|B4（JIS） 回転 364×257mm|
|用紙JISB5回転|B5（JIS） 回転 257×182mm|
|紙日本語はがき回転|はがき 回転 148×100mm|
|PaperJapaneseDoublePostcardRotated|往復はがき 回転 148 x 200 mm|
|用紙A6回転|A6 回転 148 x 105 mm|
|紙日本語封筒Kaku2Rotated|封筒 角 2 号 回転|
|紙日本語封筒Kaku3Rotated|封筒 角3号 回転|
|紙日本語封筒Chou3Rotated|封筒 Chou #3 回転|
|紙日本語封筒Chou4Rotated|封筒 長形 4 回転|
|紙JISB6|B6（JIS） 128×182mm|
|用紙JISB6回転|B6（JIS） 回転 182×128mm|
|紙12x11|12×11インチ|
|紙日本語封筒You4|封筒 ゆう #4|
|紙日本語封筒You4Rotated|封筒 ゆう #4 回転|
|紙PRC16K|PRC 16K 146×215mm|
|紙PRC32K|PRC 32K 97×151mm|
|論文PRCBig32K|PRC 32K(大) 97×151mm|
|用紙PRC封筒1|中国封筒 #1 102 x 165 mm|
|用紙PRC封筒2|中国封筒 #2 102 x 176 mm|
|用紙PRC封筒3|中国封筒 #3 125 x 176 mm|
|用紙PRC封筒4|中国封筒 #4 110 x 208 mm|
|用紙PRC封筒5|中国封筒 #5 110 x 220 mm|
|用紙PRC封筒6|中国封筒 #6 120 x 230 mm|
|用紙PRC封筒7|中国封筒 #7 160 x 230 mm|
|用紙PRC封筒8|中国封筒 #8 120 x 309 mm|
|用紙PRC封筒9|中国封筒 #9 229 x 324 mm|
|用紙PRC封筒10|中国封筒 #10 324 x 458 mm|
|紙PRC16K回転|PRC 16K 回転|
|紙PRC32K回転|PRC 32K 回転|
|紙PRCBig32K回転|PRC 32K(大) 回転|
|PaperPRCEnvelope1Rotated|中国封筒 #1 回転 165 x 102 mm|
|PaperPRCEnvelope2Rotated|中国封筒 #2 回転 176 x 102 mm|
|PaperPRCEnvelope3Rotated|中国封筒 #3 回転 176 x 125 mm|
|PaperPRCEnvelope4Rotated|中国封筒 #4 回転 208 x 110 mm|
|PaperPRCEnvelope5Rotated|中国封筒 #5 回転 220 x 110 mm|
|PaperPRCEnvelope6Rotated|中国封筒 #6 回転 230 x 120 mm|
|PaperPRCEnvelope7Rotated|中国封筒 #7 回転 230 x 160 mm|
|PaperPRCEnvelope8Rotated|中国封筒 #8 回転 309 x 120 mm|
|PaperPRCEnvelope9Rotated|中国封筒 #9 回転 324 x 229 mm|
|PaperPRCEnvelope10Rotated|中国封筒 #10 回転 458 x 324 mm|
|論文B3|通常のB3(13.9×19.7インチ)|
|紙ビジネスカード|名刺(90mm×55mm)|
|紙熱|サーマル (3 x 11 インチ)|
|カスタム|カスタム用紙サイズを表します。|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-ManagePaperSize-1.cs" >}}

### **印刷品質**

で印刷するワークシートの印刷品質を設定します。[**ページ設定**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)クラス'[**印刷品質**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printquality)財産。印刷品質の測定単位はインチあたりのドット数 (DPI) です。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintQuality-1.cs" >}}

### **最初のページ番号**

を使用して、ワークシート ページの番号付けを開始します。[**ページ設定**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)クラス'[**最初のページ番号**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/firstpagenumber)財産。の[**最初のページ番号**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/firstpagenumber)プロパティは、ワークシートの最初のページのページ番号を設定し、次のページは昇順で番号が付けられます。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetFirstPageNumber-1.cs" >}}
