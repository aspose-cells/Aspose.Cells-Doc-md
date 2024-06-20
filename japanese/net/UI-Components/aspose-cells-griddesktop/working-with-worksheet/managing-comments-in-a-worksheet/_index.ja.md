---
title: ワークシートでのコメントの管理
type: docs
weight: 110
url: /ja/net/aspose-cells-griddesktop/manage-comments-in-a-worksheet/
keywords: GridDesktop,コメント,コメント
description: この記事では、GridDesktopでコメントを扱う方法について紹介します。
---

{{% alert color="primary" %}} 

MS Excelでは、セルにコメントを追加する機能があります。この機能は、ユーザーがセルに値を入力しようとしている時に、ユーザーに情報を提供する必要がある場合に役立ちます。ユーザーがコメント付きのセルにマウスカーソルを置くと、ユーザーに情報を提供するための小さなポップアップメッセージが表示されます。Aspose.Cells.GridDesktopを使用すると、開発者はセルにコメントを作成することができます。このトピックでは、この機能の使用方法について詳しく説明します。

{{% /alert %}} 
## **コメントの追加**
Aspose.Cells.GridDesktopを使用してセルにコメントを追加するには、以下の手順に従ってください。

- Aspose.Cells.GridDesktop コントロールを **Form** に追加します
- 任意の **Worksheet** にアクセスします
- **コメント**をワークシートに追加するには、コメントが追加されるセル（その名前または行＆列番号を使用して）を指定してください。

以下のコードは、ワークシートの**b2**および**b4**セルにコメントを追加します。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-AddingComments.cs" >}}


**Worksheet**オブジェクトの**Comments**コレクションには、オーバーロードされた**Add**メソッドが用意されています。開発者は、特定のニーズに応じて、いずれかのオーバーロードされた**Add**メソッドを使用できます。
## **コメントへのアクセス**
既存のコメントにアクセスして変更するには、ワークシートの**Comments**コレクションからコメントにアクセスし、コメントが挿入されたセル（セルの名前または行列番号に基づく位置）を指定します。コメントにアクセスした後、開発者は実行時にそのテキストを変更できます。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-AccessingComments.cs" >}}
## **コメントの削除**
既存のコメントを削除するには、簡単に目的のワークシートにアクセスし、**Comments**コレクションから**Remove**コメントを指定して、コメントを挿入するセル（その名前または行＆列番号を使用して）を指定してください。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-RemovingComments.cs" >}}
