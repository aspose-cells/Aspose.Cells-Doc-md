---
title: Aspose.Cells オブジェクトモデル
type: docs
weight: 20
url: /ja/python-java/aspose-cells-object-model/
---

{{% alert color="primary" %}}

Aspose.Cells オブジェクトモデルは、Aspose.Cells クラスライブラリのオブジェクト間の構造的関係についての情報を提供します。

{{% /alert %}}

Aspose.Cells オブジェクトモデルのトップレベル構造は、階層的に以下に示されています。

|**Aspose.Cells オブジェクトモデルのトップレベル構造**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_1.png)|
上記の図から分かるように、オブジェクトモデルのルートは Workbook オブジェクトです。簡単な説明として、いくつかのオブジェクトについて以下に提供されています。

## **WorksheetCollection/Worksheet**

Workbook オブジェクトにはスプレッドシートのすべての Worksheet オブジェクトを表す WorksheetCollection が含まれています。

|**Worksheet および Worksheet オブジェクト**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_2.png)|

## **Cells/Cell**

各 Worksheet オブジェクトには、ワークシート内のすべての Cell オブジェクトを表す Cells オブジェクトが含まれています。

|**Cells および Cell オブジェクト**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_3.png)|
Cell オブジェクトを使用して、単一のセルの値、スタイル、式などのプロパティを取得および設定できます。

## **ChartCollection/Chart**

Charts オブジェクトはワークシート内のすべての Chart オブジェクトのコレクションを表します。各 Chart オブジェクトは、チャートを作成・管理するために協力しているいくつかの他のオブジェクトから構成されています。Aspose.Cells の Chart 構造は以下の図に示されています。

|**Chart のオブジェクトモデル**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_4.png)|

## **CommentCollection/Comment**

各 Worksheet オブジェクトには、ワークシート内のすべての Comment オブジェクトを表す Comments オブジェクトが含まれています。

|**コメントおよびコメントオブジェクト**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_5.png)|
コメントオブジェクトは、ワークシート内の任意のセルにコメントを追加するために使用されます。

## **HorizontalPageBreakCollection/HorizontalPageBreak**

各ワークシートオブジェクトには、ワークシート内のすべての水平ページブレイクオブジェクトのコレクションを表すHorizontalPageBreakCollectionが含まれています。

|**HPageBreaksおよびHPageBreakオブジェクト**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_6.png)|
水平ページブレイクオブジェクトは、ワークシート内に水平ページブレイクを作成するために使用されます。

## **HyperlinkCollection/Hyperlink**

ワークシートオブジェクトには、ワークシート内のすべてのハイパーリンクオブジェクトのコレクションを表すHyperlinkCollectionも含まれています。

|**ハイパーリンクおよびハイパーリンクオブジェクト**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_7.png)|
ハイパーリンクオブジェクトは、ワークシート内のハイパーリンクを表します。開発者は、ハイパーリンクオブジェクトを使用してハイパーリンクアドレスやその他関連プロパティを設定することができます。

## **PictureCollection/Picture**

各ワークシートオブジェクトには、ワークシート内のすべてのピクチャオブジェクトのコレクションを表すPictureCollectionオブジェクトも含まれています。

|**ピクチャおよびピクチャオブジェクト**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_8.png)|
ピクチャオブジェクトは、ワークシート内の画像を表します。ピクチャオブジェクトを使用すると、開発者はワークシートに画像を追加するだけでなく、これらの画像を任意の位置に配置することもできます。また、画像の境界線やその他のプロパティを設定することも可能です。

## **VerticalPageBreakCollection/VerticalPageBreak**

各ワークシートオブジェクトには、ワークシート内のすべての垂直ページブレイクオブジェクトのコレクションを表すVerticalPageBreakCollectionオブジェクトも含まれています。

|**VPageBreaksおよびVPageBreakオブジェクト**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_9.png)|
垂直ページブレイクオブジェクトは、ワークシート内に垂直ページブレイクを作成するために使用されます。
