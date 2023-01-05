---
title: ワークシートでのハイパーリンクの管理
type: docs
weight: 90
url: /ja/net/managing-hyperlinks-in-a-worksheet/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop を使用すると、ワークシートのセルに格納されている単純な値にハイパーリンクを追加することもできます。一部のセルに、Web ページのより詳細な情報にリンクしたい値があるとします。その場合、そのセルにハイパーリンクを追加して、ユーザーがセルをクリックするとその Web ページに移動するようにすることが望ましいでしょう。このトピックでは、開発者がワークシートにハイパーリンクを追加および操作する方法について説明します。

{{% /alert %}} 
## **ハイパーリンクの追加**
Aspose.Cells.GridDesktop を使用してセルにハイパーリンクを追加するには、次の手順に従ってください。

-  Aspose.Cells.GridDesktop コントロールを**形**
- 任意のアクセス**ワークシート**
- 希望のアクセス**Cell**ハイパーリンクされるワークシートで
- ハイパーリンクするセルに値を追加します
- 追加**ハイパーリンク**ハイパーリンクが適用されるセル名を指定して、ワークシートに

**ハイパーリンク**のコレクション**ワークシート**オブジェクトはオーバーロードを提供します**追加**方法。開発者は、オーバーロードされた任意のバージョンを使用できます**追加**特定のニーズに応じた方法。

以下のコードはハイパーリンクを追加します**B2**と**C3**ワークシートのセル。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-AddHyperlink.cs" >}}
## **ハイパーリンクへのアクセス**
ハイパーリンクがセルに追加されると、実行時にハイパーリンクにアクセスして変更する必要がある場合もあります。これを行うには、開発者はハイパーリンクに簡単にアクセスできます。**ハイパーリンク**のコレクション**ワークシート**ハイパーリンクを追加するセルを (セル名またはセルの行番号と列番号を使用して) 指定します。ハイパーリンクにアクセスすると、開発者は実行時にその URL を変更できます。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-AccessHyperlink.cs" >}}
## **ハイパーリンクの削除**
既存のハイパーリンクを削除するには、開発者は単に目的のワークシートにアクセスしてから**削除する**からのハイパーリンク**ハイパーリンク**のコレクション**ワークシート**ハイパーリンクされたセルを指定する (その名前または行と列の番号を使用)。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-RemoveHyperlink.cs" >}}

{{% alert color="primary" %}} 

セルにハイパーリンクを追加し、値の代わりにハイパーリンクの URL をセルに表示したい場合は、セルに値を追加せず、ハイパーリンクをそのセルに追加するだけです。そうすることで、セルはハイパーリンクされ、ハイパーリンクの URL もその値としてセルに表示されます。

{{% /alert %}}
