---
title: ワークシートでコメントを管理
type: docs
weight: 110
url: /ja/net/manage-comments-in-worksheet/
---
{{% alert color="primary" %}} 

このトピックでは、ワークシートへのコメントの追加、アクセス、および削除について説明します。コメントは、シートを操作するユーザーにメモや役立つ情報を追加するのに役立ちます。開発者は、ワークシートの任意のセルにコメントを追加できる柔軟性を備えています。

{{% /alert %}} 
## **コメントの操作**
### **コメントの追加**
ワークシートにコメントを追加するには、次の手順に従ってください。

1. Aspose.Cells.GridWeb コントロールを Web フォームに追加します。
1. コメントを追加するワークシートにアクセスします。
1. セルにコメントを追加します。
1. 新しいコメントのメモを設定します。

**ワークシートにコメントが追加されました** 

![todo:画像_代替_文章](manage-comments-in-worksheet_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-AddComments.cs" >}}
### **コメントへのアクセス**
コメントにアクセスするには:

1. コメントを含むセルにアクセスします。
1. セルの参照を取得します。
1. Comment コレクションへの参照を渡して、コメントにアクセスします。
1. コメントのプロパティを変更できるようになりました。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-AccessComments.cs" >}}
### **コメントの削除**
コメントを削除するには:

1. 上で説明したように、セルにアクセスします。
1. コメントを削除するには、Comment コレクションの RemoveAt メソッドを使用します。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-RemoveComments.cs" >}}
