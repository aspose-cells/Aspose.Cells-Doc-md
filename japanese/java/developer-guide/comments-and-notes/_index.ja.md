---
title: コメントとノートの管理
linktitle: コメントとノート
type: docs
weight: 128
url: /ja/java/comments-and-notes/
description: Aspose.Cells for javaでコメントやノートを挿入・管理します。
keywords: コメントを挿入、ノートを挿入
---

## **紹介**

コメントはセルに追加情報を追加するために使用されます。Aspose.Cellsでは、セルにコメントを追加するための2つの方法が提供されます。最初の方法は、デザイナーファイルで手動でコメントを作成することです。これらのコメントはその後、Aspose.Cellsを使用してインポートされます。2番目は、Aspose.Cells APIを使用してランタイムでコメントを追加することです。このトピックでは、Aspose.Cells APIを使用してセルにコメントを追加する方法について説明します。コメントの書式設定についても説明します。

## **コメントの追加**

 [**Comments**](https://reference.aspose.com/cells/java/com.aspose.cells/CommentCollection) セレクションの**追加** メソッド ( [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) オブジェクトにカプセル化されています) を呼び出して、セルにコメントを追加します。新しい [**Comment**](https://reference.aspose.com/cells/java/com.aspose.cells/Comment) オブジェクトは、コメントインデックスを渡して [**Comments**](https://reference.aspose.com/cells/java/com.aspose.cells/CommentCollection) コレクションからアクセスできます。 [**Comment**](https://reference.aspose.com/cells/java/com.aspose.cells/Comment) オブジェクトにアクセスした後に、 [**Comment**](https://reference.aspose.com/cells/java/com.aspose.cells/Comment) オブジェクトの [**Note**](https://reference.aspose.com/cells/java/com.aspose.cells/comment#Note) プロパティを使ってコメントノートをカスタマイズします。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "AddingComment-1.java" >}}

## **コメントの書式設定**

コメントの高さ、幅、フォント設定を構成することで、コメントの外観を書式設定することも可能です。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "CommentFormatting-1.java" >}}

## **コメントに画像を追加する**

Microsoft Excel 2007では、セルコメントの背景として画像を使用することもできます。Excel 2007では、次の手順を実行することでこれが実現されます。（すでにセルにコメントを追加していることを前提とします。）

1. コメントを含むセルを右クリックします。
1. **表示/非表示**を選択し、コメント内のテキストをクリアします。
1. コメントの境界線をクリックして選択します。
1. **書式**、次に**コメント**を選択します。
1. **色と線**タブで、**色**リストを展開します。
1. **塗りつぶしの効果**をクリックします。
1. **図**タブで、**ピクチャを選択**をクリックします。
1. 画像を探し、選択します。
1. すべてのダイアログが閉じるまで**OK**をクリックします。

Aspose.Cellsもこの機能を提供します。以下は、セル"A1"に画像を背景として設定したコメントを追加し、からXLSXファイルをスクラッチから作成するコードサンプルです。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "AddImageToComment-1.java" >}}

## **高度なトピック**
- [コメントのテキスト方向を変更する](/cells/ja/java/change-text-direction-of-the-comment/)
- [コメントのフォント色を変更する方法](/cells/ja/java/how-to-change-the-comment-font-color/)
- [コメントの背景を設定する方法](/cells/ja/java/how-to-set-comment-background/)
- [スレッド化されたコメント](/cells/ja/java/threaded-comments/)

