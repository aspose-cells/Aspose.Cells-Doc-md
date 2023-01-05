---
title: HTML に保存する際にダウンレベルの公開コメントを無効にする
type: docs
weight: 20
url: /ja/java/disable-downlevel-revealed-comments-while-saving-to-html/
---
## **考えられる使用シナリオ**

Excel ファイルを HTML に保存すると、Aspose.Cells でダウンレベルの条件付きコメントが表示されます。これらの条件付きコメントは主に古いバージョンの Internet Explorer に関連しており、最新の Web ブラウザーには関連していません。それらについては、次のリンクで詳しく読むことができます。

- [条件付きコメント - ダウンレベルで明らかにされた条件付きコメント](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells を設定すると、これらのダウンレベルの公開コメントを削除できます。[**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DisableDownlevelRevealedComments)プロパティへ**真実**.

## **HTML に保存する際にダウンレベルの公開コメントを無効にする**

次のサンプル コードは、[**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DisableDownlevelRevealedComments)財産。スクリーンショットは、このプロパティが に設定されていない場合の効果を示しています。**真実**.をダウンロードしてください[サンプル Excel ファイル](50528267.xlsx)このコードと[出力 HTML](50528266.zip)参照用にそれによって生成されたファイル。

![todo:画像_代替_文章](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DisableDownlevelRevealedCommentsWhileSavingToHTML.java" >}}
