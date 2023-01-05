---
title: ワークシートでのコメントの管理
type: docs
weight: 110
url: /ja/net/managing-comments-in-a-worksheet/
---
{{% alert color="primary" %}} 

MS Excel では、ユーザーがセルにコメントを追加できるコメント機能に精通している必要があります。この機能は、ユーザーがセルに値を入力しようとしているときに何らかの情報を提供する必要がある場合に役立ちます。ユーザーがマウス カーソルをコメント付きのセルに置くと、小さなポップアップ メッセージが表示され、ユーザーに情報が提供されます。 Aspose.Cells.GridDesktop を使用すると、開発者はセルにコメントを作成できます。このトピックでは、この機能の使用方法について詳しく説明します。

{{% /alert %}} 
## **コメントの追加**
Aspose.Cells.GridDesktop を使用してセルにコメントを追加するには、次の手順に従ってください。

-  Aspose.Cells.GridDesktop コントロールを**形**
- 任意のアクセス**ワークシート**
- 追加**コメント**コメントを追加するセル (名前または行と列番号を使用) を指定して、ワークシートに追加します。

以下のコードは、**b2**と**b4**ワークシートのセル。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-AddingComments.cs" >}}


**コメント**のコレクション**ワークシート**オブジェクトはオーバーロードを提供します**追加**方法。開発者は、オーバーロードされた任意のバージョンを使用できます**追加**特定のニーズに応じた方法。
## **コメントへのアクセス**
ワークシート内の既存のコメントにアクセスして変更するには、開発者は**コメント**のコレクション**ワークシート**コメントが挿入されるセルを指定する (セル名または行番号と列番号によるセルの位置を使用)。コメントにアクセスすると、開発者は実行時にそのテキストを変更できます。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-AccessingComments.cs" >}}
## **コメントの削除**
既存のコメントを削除するには、開発者は目的のワークシートにアクセスして、**削除する**からのコメント**コメント**のコレクション**ワークシート**コメントを含むセルを（名前または行と列番号を使用して）指定することにより。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-RemovingComments.cs" >}}
