---
title: HTMLへの保存時にDownlevel表示されたコメントを無効にする
type: docs
weight: 20
url: /ja/python-java/disable-downlevel-revealed-comments-while-saving-to/
---

## **HTML への保存時にダウンレベルの表示されたコメントを無効にする**
Excel ファイルを HTML に変換する際、Aspose.Cells は出力の HTML ファイルに Downlevel-revealed 条件付きコメントを追加します。これらの条件付きコメントは、主に古いバージョンの Internet Explorer に関連しており、モダンブラウザでは無関係です。Downlevel-revealed 条件付きコメントの詳細については、以下のリンクを参照してください

[条件付きコメント - Downlevel-revealed conditional comment](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Downlevel-revealedの条件付きコメントを削除するには、Aspose.Cellsは[HtmlSaveOptions.DisableDownlevelRevealedComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#DisableDownlevelRevealedComments)プロパティを提供しています。[HtmlSaveOptions.DisableDownlevelRevealedComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#DisableDownlevelRevealedComments)プロパティを**True**に設定すると、出力HTMLファイルからDownlevel-revealedの条件付きコメントが削除されます。

次のイメージは、出力HTMLファイルから削除されるDownlevel-revealedの条件付きコメントを示しています

![todo:image_alt_text](Disable-Downlevel-Revealed-Comments.png)
## **サンプルコード**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-DisableDownlevelRevealedCommentsWhileSavingToHTML.py" >}}
