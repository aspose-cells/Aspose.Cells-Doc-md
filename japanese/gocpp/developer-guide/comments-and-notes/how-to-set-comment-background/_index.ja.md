---
title: Go言語とC++を使ったExcelのコメント背景の変更方法
linktitle: コメント背景
type: docs
weight: 190
url: /ja/go-cpp/how-to-set-comment-background/
description: Excelのコメントの色を変更する方法。C++を使用してExcelのコメントに画像や写真を挿入する方法。
keywords: 挿入画像、色付きコメント背景、Excel
---

{{% alert color="primary" %}}

コメントはセルに追加され、コメントの詳細、数式の仕組みや値の出所、レビュアーの質問などを記録します。複数人が同じドキュメントを異なる時間に議論やレビューを行う際に非常に重要な役割を果たします。異なる人のコメントを区別するにはどうすればよいですか？はい、それぞれのコメントに異なる背景色を設定できます。しかし、多くのドキュメントや多くのコメントを処理する必要がある場合、手動で行うのは大変です。幸い、[**Aspose.Cells**](https://products.aspose.com/cells/go-cpp/)はこれをコードで実行できるAPIを提供します。

{{% /alert %}}

## **Excel でコメントの色を変更する方法**

コメントのデフォルト背景色が不要な場合は、お好きな色に置き換えることもできます。Excelのコメントボックスの背景色を変更するにはどうすればよいですか？

以下のコードは、[**Aspose.Cells**](https://products.aspose.com/cells/go-cpp/)を使用して、自分の好きな背景色をコメントに追加する方法を案内します。

こちらに[サンプルファイル](exmaple.xlsx)を用意しました。このファイルは、以下のコードでWorkbookオブジェクトを初期化するために使われます。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-HowToSetCommentBackground.go" >}}
上記のコードを実行すると、[出力ファイル](result.xlsx)が得られます。

## **Excel でコメントに画像を挿入する方法**

Microsoft Excelは、スプレッドシートの外観と感触を大きくカスタマイズ可能です。コメントに背景画像を追加することも可能です。背景画像の追加は、見た目の工夫やブランディング強化に役立ちます。

以下のサンプルコードは、[**Aspose.Cells**](https://products.aspose.com/cells/go-cpp/) APIを使用して、好きな背景色を持つコメントを作成し、セルA1に追加する方法を示しています。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-HowToSetCommentBackground-1.go" >}}
