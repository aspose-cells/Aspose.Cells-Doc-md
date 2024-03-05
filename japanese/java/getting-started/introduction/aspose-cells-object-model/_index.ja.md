---
title: Aspose.Cells オブジェクト モデル
type: docs
weight: 20
url: /ja/java/aspose-cells-object-model/
---
{{% alert color="primary" %}}

Aspose.Cells オブジェクト モデルは、Aspose.Cells クラス ライブラリのオブジェクト間の構造的関係に関する情報を提供します。

{{% /alert %}}

Aspose.Cells オブジェクト モデルのトップ レベルの構造を以下に階層的に示します。

|**Aspose.Cells オブジェクト モデルの最上位構造**|
|:- |
|![todo:画像_代替_文章](aspose-cells-object-model_1.png)|
上の図からわかるように、オブジェクト モデルのルートは Workbook オブジェクトです。紹介目的で、いくつかのオブジェクトの簡単な説明を以下に示します。

## **WorksheetCollection/ワークシート**

Workbook オブジェクトには、以下に示すように、スプレッドシート内のすべての Worksheet オブジェクトのコレクションを表す WorksheetCollection が含まれています。

|**ワークシートとワークシート オブジェクト**|
|:- |
|![todo:画像_代替_文章](aspose-cells-object-model_2.png)|

## **Cells/Cell**

各 Worksheet オブジェクトには、以下に示すように、ワークシート内のすべての Cell オブジェクトのコレクションを表す Cells オブジェクトが含まれています。

|**Cells & Cell オブジェクト**|
|:- |
|![todo:画像_代替_文章](aspose-cells-object-model_3.png)|
Cell オブジェクトを使用して、1 つのセルの値、スタイル、数式、およびその他のプロパティを取得および設定できます。

## **ChartCollection/チャート**

Charts オブジェクトは、Worksheet 内のすべての Chart オブジェクトのコレクションを表します。各 Chart オブジェクトは、連携してチャートを作成および管理するいくつかの他のオブジェクトで構成されています。 Aspose.Cells のチャート構造を以下の図に示します。

|**チャートのオブジェクト モデル**|
|:- |
|![todo:画像_代替_文章](aspose-cells-object-model_4.png)|

## **Commentコレクション/コメント**

各 Worksheet オブジェクトには、以下に示すように、ワークシート内のすべての Comment オブジェクトのコレクションを表す Comments オブジェクトも含まれています。

|**コメント & コメント オブジェクト**|
|:- |
|![todo:画像_代替_文章](aspose-cells-object-model_5.png)|
Comment オブジェクトは、ワークシート内の指定されたセルにコメントを追加するために使用されます。

## **HorizontalPageBreakCollection/HorizontalPageBreak**

以下に示すように、各 Worksheet オブジェクトには、ワークシート内のすべての HorizontalPageBreak オブジェクトのコレクションを表す HorizontalPageBreakCollection が含まれています。

|**HPageBreaks & HPageBreak オブジェクト**|
|:- |
|![todo:画像_代替_文章](aspose-cells-object-model_6.png)|
HorizontalPageBreak オブジェクトは、ワークシートに水平改ページを作成するために使用されます。

## **HyperlinkCollection/ハイパーリンク**

Worksheet オブジェクトには、次に示すように、ワークシート内のすべての Hyperlink オブジェクトのコレクションを表す HyperlinkCollection も含まれています。

|**ハイパーリンクとハイパーリンク オブジェクト**|
|:- |
|![todo:画像_代替_文章](aspose-cells-object-model_7.png)|
Hyperlink オブジェクトは、ワークシート内のハイパーリンクを表します。開発者は、Hyperlink オブジェクトを使用して、ハイパーリンク アドレスおよびその他の関連プロパティを設定できます。

## **PictureCollection/画像**

各 Worksheet オブジェクトには、以下に示すように、ワークシート内のすべての Picture オブジェクトのコレクションを表す PictureCollection オブジェクトが含まれています。

|**写真と写真オブジェクト**|
|:- |
|![todo:画像_代替_文章](aspose-cells-object-model_8.png)|
Picture オブジェクトは、ワークシート内の画像を表します。 Picture オブジェクトを使用すると、開発者はワークシートに画像を追加できるだけでなく、これらの画像を任意の場所に配置することもできます。画像の境界線やその他のプロパティを設定することもできます。

## **VerticalPageBreakCollection/VerticalPageBreak**

各 Worksheet オブジェクトには、以下に示すように、ワークシート内のすべての VerticalPageBreak オブジェクトのコレクションを表す VerticalPageBreakCollection オブジェクトが含まれています。

|**VPageBreaks & VPageBreak オブジェクト**|
|:- |
|![todo:画像_代替_文章](aspose-cells-object-model_9.png)|
VerticalPageBreak オブジェクトは、ワークシートに垂直改ページを作成するために使用されます。
