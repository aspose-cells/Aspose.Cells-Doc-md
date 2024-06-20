---
title: ワークシート内のコメントの管理
type: docs
weight: 110
url: /ja/net/aspose-cells-gridweb/manage-comment-in-worksheet/
keywords: GridWeb,comment
description: この記事では、GridWeb内のコメントの処理方法について紹介しています。
---

{{% alert color="primary" %}} 

このトピックでは、ワークシートからコメントを追加、アクセス、削除する方法について説明しています。コメントは、シートを使用するユーザーにとって注釈や有用な情報を追加するために役立ちます。 開発者はワークシートの任意のセルにコメントを追加する柔軟性があります。

{{% /alert %}} 
## **コメントの操作**
### **コメントの追加**
ワークシートにコメントを追加するには、以下の手順に従ってください：

1. Aspose.Cells.GridWebコントロールをWebフォームに追加します。
1. コメントを追加するワークシートにアクセスします。
1. セルにコメントを追加します。
1. 新しいコメントにノートを設定します。

**ワークシートにコメントが追加されました** 

![todo:image_alt_text](manage-comments-in-worksheet_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-AddComments.cs" >}}
### **コメントへのアクセス**
コメントにアクセスするには：

1. コメントを含むセルにアクセスします。
1. セルの参照を取得します。
1. 参照をCommentコレクションに渡し、コメントにアクセスします。
1. 現在、コメントのプロパティを変更することができます。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-AccessComments.cs" >}}
### **コメントの削除**
コメントを削除するには：

1. 上記の方法でセルにアクセスします。
1. CommentコレクションのRemoveAtメソッドを使用してコメントを削除します。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-RemoveComments.cs" >}}
