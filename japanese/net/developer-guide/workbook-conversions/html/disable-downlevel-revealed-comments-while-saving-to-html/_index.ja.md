---
title: HTML に保存する際にダウンレベルの公開コメントを無効にする
type: docs
weight: 20
url: /ja/net/disable-downlevel-revealed-comments-while-saving-to/
---
## **考えられる使用シナリオ**

Excel ファイルを HTML に保存すると、Aspose.Cells でダウンレベルの条件付きコメントが表示されます。これらの条件付きコメントは、主に古いバージョンの Internet Explorer に関連しており、最新の Web ブラウザーには関連していません。それらについては、次のリンクで詳しく読むことができます。

- [条件付きコメント - ダウンレベルで明らかにされた条件付きコメント](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells を設定すると、これらのダウンレベルの公開コメントを削除できます。[**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/disabledownlevelrevealedcomments)プロパティへ**真実**.

## **HTML に保存する際にダウンレベルの公開コメントを無効にする**

次のサンプル コードは、[**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/disabledownlevelrevealedcomments)財産。スクリーンショットは、このプロパティが true に設定されていない場合の効果を示しています。をダウンロードしてください[サンプル Excel ファイル](50528257.xlsx)このコードと[出力 HTML](50528258.zip)参照用にそれによって生成されます。

![todo:画像_代替_文章](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DisableDownlevelRevealedCommentsWhileSavingToHTML.cs" >}}
