---
title: ワークシートで画像を管理する
type: docs
weight: 100
url: /ja/net/managing-pictures-in-a-worksheet/
---
{{% alert color="primary" %}} 

ほとんどの人は、写真は言葉よりも物事をよりよく説明できると信じています。そのため、Aspose.Cells.GridDesktop はワークシートへの画像の追加をサポートし、人々のこの信念を実行します。このトピックでは、ワークシートでの画像の追加と操作について説明します。

{{% /alert %}} 
## **写真を追加する**
Aspose.Cells.GridDesktop を使用してセルにハイパーリンクを追加するには、次の手順に従ってください。

-  Aspose.Cells.GridDesktop コントロールを**形**
- 任意のアクセス**ワークシート**
- 追加**写真**画像のファイルパスと画像が挿入されるセル名を指定して、ワークシートに

**ピクチャー**のコレクション**ワークシート**オブジェクトはオーバーロードを提供します**追加**方法。開発者は、オーバーロードされた任意のバージョンを使用できます**追加**特定のニーズに応じた方法。これらのオーバーロードされたバージョンの使用**追加**メソッド、ファイル、ストリーム、またはから画像を追加することが可能です**画像**物体。

以下は、ワークシートに画像を追加するためのサンプル コードです。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-AddingPictures.cs" >}}
## **写真へのアクセス**
ワークシート内の既存の画像にアクセスして変更するために、開発者は**ピクチャー**のコレクション**ワークシート**画像が挿入されるセルを (セル名または行番号と列番号の観点からセルの位置を使用して) 指定します。画像にアクセスすると、開発者は実行時にその画像を変更できます。

以下は、ワークシート内の画像にアクセスして変更するためのサンプル コードです。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-AccessAndModifyPicture.cs" >}}
## **写真を削除する**
既存の画像を削除するには、開発者は単に目的のワークシートにアクセスしてから**削除する**からの写真**ピクチャー**のコレクション**ワークシート**画像を含むセルを (名前または行と列の番号を使用して) 指定します。

以下のコードでは、ワークシートから画像を削除する方法を示しています。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-RemovePicture.cs" >}}
