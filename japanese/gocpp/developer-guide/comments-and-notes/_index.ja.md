---
title: Golangを使用したC++経由でのコメントとノートの管理
linktitle: コメントとノート
type: docs
weight: 128
url: /ja/go-cpp/comments-and-notes/
description: Aspose.Cells for C++を使ったコメントやノートの挿入と管理。
keywords: コメントを挿入、ノートを挿入
---

## **紹介**

コメントはセルに追加情報を追加するために使用されます。Aspose.Cellsでは、セルにコメントを追加するための2つの方法が提供されます。最初の方法は、デザイナーファイルで手動でコメントを作成することです。これらのコメントはその後、Aspose.Cellsを使用してインポートされます。2番目は、Aspose.Cells APIを使用してランタイムでコメントを追加することです。このトピックでは、Aspose.Cells APIを使用してセルにコメントを追加する方法について説明します。コメントの書式設定についても説明します。

## **コメントの追加**

[**Comments**](https://reference.aspose.com/cells/go-cpp/commentcollection/)コレクションの[**Add**](https://reference.aspose.com/cells/go-cpp/commentcollection/add/)メソッド（[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)オブジェクト内にカプセル化）を呼び出すことによって、セルにコメントを追加します。新しい[**Comment**](https://reference.aspose.com/cells/cpp/aspose.cells/comment/)オブジェクトは、コメントインデックスを渡して[**Comments**](https://reference.aspose.com/cells/go-cpp/commentcollection/)コレクションからアクセスできます。[**Comment**](https://reference.aspose.com/cells/cpp/aspose.cells/comment/)オブジェクトにアクセスした後、[**Comment**](https://reference.aspose.com/cells/cpp/aspose.cells/comment/)オブジェクトの[**GetNote()**](https://reference.aspose.com/cells/cpp/aspose.cells/comment/getnote/)プロパティを使用してコメントノートをカスタマイズします。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CommentsAndNotes.go" >}}
## **コメントの書式設定**

コメントの高さ、幅、フォント設定を構成することで、コメントの外観を書式設定することも可能です。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CommentsAndNotes-1.go" >}}
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

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CommentsAndNotes-2.go" >}}
## **高度なトピック**
- [コメントのテキスト方向を変更する](/cells/ja/cpp/change-text-direction-of-the-comment/)
- [コメントのフォント色を変更する方法](/cells/ja/cpp/how-to-change-the-comment-font-color/)
- [コメントの背景を設定する方法](/cells/ja/cpp/how-to-set-comment-background/)
- [スレッド化されたコメント](/cells/ja/cpp/threaded-comments/)
