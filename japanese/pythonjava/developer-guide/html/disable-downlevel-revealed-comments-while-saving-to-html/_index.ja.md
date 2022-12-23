---
title: HTML に保存する際にダウンレベルの公開コメントを無効にする
type: docs
weight: 20
url: /ja/python-java/disable-downlevel-revealed-comments-while-saving-to/
---
## **HTML に保存する際にダウンレベルの公開コメントを無効にする**
Excel ファイルが HTML に変換されると、Aspose.Cells は、出力 HTML ファイルにダウンレベルが明らかにされた条件付きコメントを追加します。これらの条件付きコメントは主に古いバージョンの Internet Explorer に関連しており、最新のブラウザーには関係ありません。ダウンレベルが公開された条件付きコメントの詳細については、次のリンクにアクセスしてください。

[条件付きコメント - ダウンレベルで明らかにされた条件付きコメント](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

ダウンレベルが明らかにされた条件付きコメントを削除するには、Aspose.Cells が[HtmlSaveOptions.DisableDownlevelRevealedComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#DisableDownlevelRevealedComments)財産。の設定[HtmlSaveOptions.DisableDownlevelRevealedComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#DisableDownlevelRevealedComments)プロパティへ**真実**出力 HTML ファイルで、Downlevel-revealed 条件付きコメントを削除します。

次の図は、出力 HTML ファイルで削除される、ダウンレベルが明らかにされた条件付きコメントを示しています。

![todo:画像_代替_文章](Disable-Downlevel-Revealed-Comments.png)
## **サンプルコード**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-DisableDownlevelRevealedCommentsWhileSavingToHTML.py" >}}
