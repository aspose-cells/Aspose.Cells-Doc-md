---
title: ワークシートでの画像の管理
type: docs
weight: 100
url: /ja/net/aspose-cells-griddesktop/manage-pictures-in-a-worksheet/
keywords: GridDesktop、picture、pictures
description: この記事では、GridDesktopのワークシートで画像を使用する方法について紹介します。
---

{{% alert color="primary" %}} 

多くの人々が、画像が言葉よりもよりよく説明できると考えています。そのため、Aspose.Cells.GridDesktopは、人々のこの考えを実行するためにワークシートに画像を追加する機能をサポートしています。このトピックでは、ワークシートへの画像の追加と操作について説明します。

{{% /alert %}} 
## **画像の追加**
Aspose.Cells.GridDesktopを使用してセルにハイパーリンクを追加するには、以下の手順に従ってください。

- Aspose.Cells.GridDesktop コントロールを **Form** に追加します
- 任意の **Worksheet** にアクセスします
- 画像のファイルパスと画像が挿入されるセル名を指定して、ワークシートに**Picture**を追加します

**Worksheet**オブジェクトの**Pictures**コレクションには、オーバーロードされた**Add**メソッドが用意されています。開発者は、特定のニーズに応じて、いずれかのオーバーロードされた**Add**メソッドを使用できます。これらのオーバーロードされた**Add**メソッドを使用すると、ファイル、ストリーム、または**Image**オブジェクトから画像を追加することが可能です。

ワークシートに画像を追加するためのサンプルコードが以下に示されています。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-AddingPictures.cs" >}}
## **画像のアクセス**
ワークシート内の既存の画像にアクセスして変更するには、開発者はワークシートの**Pictures**コレクションから画像にアクセスできます。画像が挿入されたセル（セル名または行と列番号での指定）を指定します。画像にアクセスしたら、開発者は実行時に画像を変更できます。

ワークシート内の画像にアクセスして変更するサンプルコードが以下に示されています。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-AccessAndModifyPicture.cs" >}}
## **画像の削除**
既存の画像を削除するには、開発者は単に希望するワークシートにアクセスし、そのワークシートの**Pictures**コレクションから画像を**Remove**します。画像を含むセル（その名前または行＆列番号）を指定してください。

以下のコードでは、ワークシートから画像を削除する方法が示されています。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-RemovePicture.cs" >}}
