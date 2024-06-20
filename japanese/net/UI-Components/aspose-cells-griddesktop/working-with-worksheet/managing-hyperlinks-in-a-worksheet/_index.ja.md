---
title: ワークシートでのハイパーリンクの管理
type: docs
weight: 90
url: /ja/net/aspose-cells-griddesktop/manage-hyperlinks-in-a-worksheet/
keywords: GridDesktop、ハイパー、リンク、ハイパーリンク、ハイパーリンク
description: この記事では、GridDesktopでハイパーリンクを使用する方法について紹介します。
---

{{% alert color="primary" %}} 

Aspose.Cells.GridDesktopを使用すると、ワークシートのセルに格納されている単純な値にハイパーリンクを追加することも可能です。例えば、いくつかのセルには、Webページ上の詳細情報にリンクしたい値が格納されているかもしれません。その場合、セルにハイパーリンクを追加して、ユーザーがセルをクリックするとそのWebページに移動できるようにすることが望ましいでしょう。このトピックでは、開発者がワークシートでハイパーリンクを追加および操作する方法について説明します。

{{% /alert %}} 
## **ハイパーリンクの追加**
Aspose.Cells.GridDesktopを使用してセルにハイパーリンクを追加するには、以下の手順に従ってください。

- Aspose.Cells.GridDesktop コントロールを **Form** に追加します
- 任意の **Worksheet** にアクセスします
- ハイパーリンクされるワークシート内の**セル**にアクセスします
- ハイパーリンクされるセルに値を追加します
- ワークシートに**ハイパーリンク**を追加するには、ハイパーリンクが適用されるセル名を指定します

**Worksheet**オブジェクトの**Hyperlinks**コレクションには、オーバーロードされた**Add**メソッドが用意されています。開発者は、特定のニーズに応じて、いずれかのオーバーロードされた**Add**メソッドを使用できます。

以下のコードは、ワークシートの**B2**および**C3**セルにハイパーリンクを追加します。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-AddHyperlink.cs" >}}
## **ハイパーリンクのアクセス**
セルにハイパーリンクが追加されると、実行時にハイパーリンクにアクセスして変更する場合があります。そのため、開発者は単に、ハイパーリンクが追加されたワークシートの**Hyperlinks**コレクションからハイパーリンクにアクセスし、ハイパーリンクが追加されたセル（セルの名前または行列番号に基づく位置）を指定します。ハイパーリンクにアクセスした後、開発者は実行時にそのURLを変更できます。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-AccessHyperlink.cs" >}}
## **ハイパーリンクの削除**
既存のハイパーリンクを削除するには、簡単に目的のワークシートにアクセスし、**Hyperlinks**コレクションから**Remove**ハイパーリンクを指定して、ハイパーリンク付きセル（その名前または行＆列番号を使用して）を指定します。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-RemoveHyperlink.cs" >}}

{{% alert color="primary" %}} 

セルにハイパーリンクを追加し、ハイパーリンクのURLをセルに表示したい場合は、セルに値を追加せずにそのセルにハイパーリンクを追加します。そうすることで、セルにハイパーリンクが追加され、ハイパーリンクのURLもセルにその値として表示されます。

{{% /alert %}}
