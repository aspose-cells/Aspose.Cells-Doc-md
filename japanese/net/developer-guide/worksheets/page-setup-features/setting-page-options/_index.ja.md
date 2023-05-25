---
title: ページオプションの設定
type: docs
weight: 10
url: /ja/net/setting-page-options/
description: この記事では、C# API および .NET ライブラリを使用して Excel ワークシートのページ オプションをプログラムで設定するサンプル コードを提供します。ページの向き、倍率、FitToPages オプション、用紙サイズ、印刷品質、最初のページ番号を設定できます。
keywords: set excel page orientation c#, set excel scaling factor c#, set excel worksheets paper size c#
---
{{% alert color="primary" %}}

場合によっては、印刷を制御するためにワークシートのページ設定を構成する必要があります。これらのページ設定設定にはさまざまなオプションが用意されています。

{{% /alert %}}

##  **ページオプションの設定**

ページ設定オプションは Aspose.Cells で完全にサポートされています。この記事では、Aspose.Cells でページ オプションを設定する方法を説明し、設定用のコード サンプルを示します。

 Aspose.Cells はクラスを提供します。[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)、これは Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Excel ファイル内の各ワークシートへのアクセスを許可するコレクション。ワークシートは次のように表されます。[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。

の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスが提供するのは、[**ページ設定**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)ワークシートのページ設定オプションを設定するために使用されるプロパティ。実はこれ、[**ページ設定**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)プロパティはのオブジェクトです[**ページ設定**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)印刷されるワークシートのさまざまなページ レイアウト オプションを設定するために使用されるクラス。の[**ページ設定**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)クラスは、ページ設定オプションを設定するために使用されるさまざまなプロパティを提供します。これらのプロパティのいくつかについては以下で説明します。

###  **ページの向き**

ページの向きは、[**ページ設定**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)クラス'[**オリエンテーション**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/orientation)財産。の[**オリエンテーション**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/orientation)プロパティは、事前に定義された値の 1 つを受け入れます。[**PageOrientationType**](https://reference.aspose.com/cells/net/aspose.cells/pageorientationtype)以下に列挙します。

|**ページの向きの種類**|**説明**|
| :- | :- |
|風景|横向き|
|肖像画|縦向き|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-PageOrientation-1.cs" >}}

###  **スケーリング係数**

で倍率を調整することで、ワークシートのサイズを縮小または拡大することができます。[**PageSetup.Zoom**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/zoom)財産。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-ScalingFactor-1.cs" >}}

###  **ページに合わせるオプション**

ワークシートの内容を特定のページ数に合わせるには、[**ページ設定**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)クラス'[**ページに合わせる背の高い**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopagestall)と[**ページ幅に合わせる**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopageswide)プロパティ。これらのプロパティは、ワークシートを拡大縮小するためにも使用されます。

{{% alert color="primary" %}}

どちらかを選択できます[**ページに合わせる背の高い**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopagestall)/[**ページ幅に合わせる**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopageswide)または[**ズーム**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/zoom)プロパティですが、同時に両方ではありません。

{{% /alert %}}

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-FitToPagesOptions-1.cs" >}}

###  **用紙サイズ**

ワークシートを印刷する用紙サイズを設定します。[**ページ設定**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)クラス'[**用紙サイズ**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/papersize)財産。の[**用紙サイズ**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/papersize)プロパティは、事前に定義された値の 1 つを受け入れます。[**用紙サイズの種類**](https://reference.aspose.com/cells/net/aspose.cells/papersizetype)以下に列挙します。

|**用紙サイズの種類**|**説明**|
| :- | :- |
|紙の手紙|レター (8-1/2 インチ x 11 インチ)|
|紙手紙小|レター小 (8-1/2 インチ x 11 インチ)|
|紙タブロイド紙|タブロイド紙 (11 インチ x 17 インチ)|
|紙台帳|元帳 (17 インチ x 11 インチ)|
|ペーパーリーガル|リーガル (8-1/2 インチ x 14 インチ)|
|紙の声明|ステートメント (5-1/2 インチ x 8-1/2 インチ)|
|ペーパーエグゼクティブ|エグゼクティブ (7-1/4 インチ x 10-1/2 インチ)|
|紙A3|A3（297mm×420mm）|
|紙A4|A4(210mm×297mm)|
|紙A4小|A4小（210mm×297mm）|
|紙A5|A5（148mm×210mm）|
|紙B4|JIS B4（257mm×364mm）|
|紙B5|JIS B5（182mm×257mm）|
|ペーパーフォリオ|フォリオ (8-1/2 インチ x 13 インチ)|
|ペーパークアルト|四つ折り（215mm×275mm）|
|紙10x14|10インチ×14インチ|
|紙11x17|11インチ×17インチ|
|紙メモ|注 (8-1/2 インチ x 11 インチ)|
|紙封筒9|封筒 #9 (3-7/8 インチ x 8-7/8 インチ)|
|紙封筒10|封筒 #10 (4-1/8 インチ x 9-1/2 インチ)|
|紙封筒11|封筒 #11 (4-1/2 インチ x 10-3/8 インチ)|
|紙封筒12|封筒 #12 (4-1/2 インチ x 11 インチ)|
|紙封筒14|封筒 #14 (5 インチ x 11-1/2 インチ)|
|紙Cシート|Cサイズシート|
|紙Dシート|Dサイズシート|
|紙Eシート|Eサイズシート|
|紙封筒DL|封筒DL（110mm×220mm）|
|紙封筒C5|封筒 C5 (162 mm x 229 mm)|
|紙封筒C3|封筒 C3 (324 mm x 458 mm)|
|紙封筒C4|封筒 C4 (229 mm x 324 mm)|
|紙封筒C6|封筒 C6 (114 mm x 162 mm)|
|紙封筒C65|封筒 C65 (114 mm x 229 mm)|
|紙封筒B4|封筒B4（250mm×353mm）|
|紙封筒B5|封筒B5（176mm×250mm）|
|紙封筒B6|封筒B6（176mm×125mm）|
|紙封筒イタリア|封筒 イタリア (110 mm x 230 mm)|
|紙封筒モナーク|エンベロープ モナーク (3-7/8 インチ x 7-1/2 インチ)|
|紙封筒個人用|封筒 (3-5/8 インチ x 6-1/2 インチ)|
|ペーパーファンフォールドUS|米国標準ファンフォールド (14-7/8 インチ x 11 インチ)|
|PaperFanfoldStdドイツ語|ドイツ標準ファンフォールド (8-1/2 インチ x 12 インチ)|
|紙扇子法的ドイツ語|ドイツの法的ファンフォールド (8-1/2 インチ x 13 インチ)|
|紙ISOB4|B4（ISO）250×353mm|
|紙日本語はがき|はがき（100mm×148mm）|
|ペーパー9x11|9インチ×11インチ|
|紙10x11|10インチ×11インチ|
|紙15x11|15インチ×11インチ|
|紙封筒招待状|招待状封筒(220mm×220mm)|
|ペーパーレターエキストラ|US レター エクストラ 9 \275 x 12 インチ|
|PaperLegalExtra|US Legal Extra 9 \275 x 15 インチ|
|紙タブロイドエキストラ|US タブロイド エクストラ 11.69 x 18 インチ|
|用紙A4エキストラ|A4 エクストラ 9.27 x 12.69 インチ|
|紙手紙横|レター トランスバース 8 \275 x 11 インチ|
|紙A4横|A4横210×297mm|
|紙レターエクストラトランスバース|レター エクストラ トランスバース 9\275 x 12 インチ|
|ペーパースーパーA|スーパーA/スーパーA/A4 227×356mm|
|ペーパースーパーB|スーパーB/スーパーB/A3 305×487mm|
|ペーパーレタープラス|US レター プラス 8.5 x 12.69 インチ|
|紙A4Plus|A4プラス 210×330mm|
|紙A5横|A5横148×210mm|
|紙JISB5横|B5(JIS) 横182×257mm|
|用紙A3エキストラ|A3 特大 322×445mm|
|用紙A5エキストラ|A5 特大 174×235mm|
|紙ISOB5Extra|B5 (ISO) 特大 201 x 276 mm|
|紙A2|A2 420×594mm|
|紙A3横|A3横 297×420mm|
|紙A3エクストラトランスバース|A3 特横 322 x 445 mm|
|紙日本語ダブルはがき|往復はがき 200×148mm|
|紙A6|A6 105×148mm|
|紙日本語封筒角2|和封筒 角2号|
|紙日本語封筒角3|和封筒 角3号|
|紙日本語封筒Chou3|和封筒 長3号|
|紙日本語封筒Chou4|和封筒 長4号|
|紙手紙回転|11インチ×8.5インチ|
|紙A3回転|420mm×297mm|
|紙A4回転|297mm×210mm|
|紙A5回転|210mm×148mm|
|紙JISB4回転|B4（JIS）回転時 364×257mm|
|紙JISB5回転|B5(JIS) 回転時 257×182mm|
|紙日本語はがき回転|日本郵便はがき 回転 148 x 100 mm|
|紙日本語ダブルはがき回転|往復はがき 回転 148 x 200 mm|
|紙A6回転|A6 回転時 148 x 105 mm|
|紙日本語封筒角2回転|日本封筒 角2号 回転|
|紙日本語封筒角3回転|日本封筒 角3号 回転|
|紙日本語封筒Chou3回転|和封筒 長3号 回転|
|紙日本語封筒Chou4回転|和封筒 長4号 回転|
|紙JISB6|B6(JIS) 128×182mm|
|紙JISB6回転|B6（JIS）回転時 182×128mm|
|紙12x11|12×11インチ|
|紙日本語封筒You4|和封筒 あなた #4|
|紙日本語封筒You4Rotated|あなたが回転した和封筒 #4|
|紙PRC16K|PRC 16K 146 x 215 mm|
|紙PRC32K|PRC 32K 97 x 151 mm|
|紙PRCBig32K|PRC 32K(大) 97 x 151 mm|
|紙PRCE封筒1|PRC 封筒 #1 102 x 165 mm|
|PaperPRCEEnvelope2|PRC 封筒 #2 102 x 176 mm|
|PaperPRCEEnvelope3|PRC 封筒 #3 125 x 176 mm|
|紙PRCE封筒4|PRC 封筒 #4 110 x 208 mm|
|PaperPRCEEnvelope5|PRC 封筒 #5 110 x 220 mm|
|PaperPRCEEnvelope6|PRC 封筒 #6 120 x 230 mm|
|紙PRCE封筒7|PRC 封筒 #7 160 x 230 mm|
|PaperPRCEEnvelope8|PRC 封筒 #8 120 x 309 mm|
|紙PRCE封筒9|PRC 封筒 #9 229 x 324 mm|
|PaperPRCEEnvelope10|PRC 封筒 #10 324 x 458 mm|
|紙PRC16K回転あり|PRC 16K 回転|
|ペーパーPRC32K回転あり|PRC 32K 回転|
|PaperPRCBig32K回転|PRC 32K(大) 回転|
|PaperPRCEEnvelope1Rotated|PRC 封筒 #1 回転時 165 x 102 mm|
|PaperPRCEEnvelope2Rotated|PRC 封筒 #2 回転時 176 x 102 mm|
|PaperPRCEEnvelope3Rotated|PRC 封筒 #3 回転時 176 x 125 mm|
|PaperPRCEEnvelope4Rotated|PRC 封筒 #4 回転時 208 x 110 mm|
|PaperPRCEEnvelope5Rotated|PRC 封筒 #5 回転 220 x 110 mm|
|PaperPRCEEnvelope6Rotated|PRC 封筒 #6 回転 230 x 120 mm|
|紙PRCE封筒7回転|PRC 封筒 #7 回転時 230 x 160 mm|
|PaperPRCEEnvelope8Rotated|PRC 封筒 #8 回転時 309 x 120 mm|
|紙PRCE封筒9回転|PRC 封筒 #9 回転時 324 x 229 mm|
|PaperPRCEEnvelope10Rotated|PRC 封筒 #10 回転時 458 x 324 mm|
|紙B3|通常のB3(13.9×19.7インチ)|
|紙名刺|名刺(90mm×55mm)|
|紙サーマル|サーマル(3 x 11 インチ)|
|カスタム|カスタム用紙サイズを表します。|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-ManagePaperSize-1.cs" >}}

###  **印刷品質**

で印刷するワークシートの印刷品質を設定します。[**ページ設定**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)クラス'[**印刷品質**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printquality)財産。印刷品質の測定単位はドット/インチ (DPI) です。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintQuality-1.cs" >}}

###  **最初のページ番号**

ワークシートのページの番号付けを開始するには、[**ページ設定**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)クラス'[**最初のページ番号**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/firstpagenumber)財産。の[**最初のページ番号**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/firstpagenumber)プロパティはワークシートの最初のページのページ番号を設定し、次のページには昇順で番号が付けられます。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetFirstPageNumber-1.cs" >}}
