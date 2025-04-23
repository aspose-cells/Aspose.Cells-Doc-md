---
title: HTMLへの保存時にDownlevel表示されたコメントを無効にする
type: docs
weight: 20
url: /ja/java/disable-downlevel-revealed-comments-while-saving-to-html/
---

## **可能な使用シナリオ**

ExcelファイルをHTMLに保存すると、Aspose.CellsはDownlevel条件付きコメントを表示します。これらの条件付きコメントは、古いバージョンのInternet Explorerに関連することが多く、現代のWebブラウザには関係ありません。詳細については、次のリンクで詳しく説明しています。

- [条件付きコメント - Downlevel-revealed条件付きコメント](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cellsを使用して、[**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DisableDownlevelRevealedComments)プロパティを**true**に設定することで、これらのDownlevel Revealed Commentsを排除できます。

## **HTML への保存時にダウンレベルの表示されたコメントを無効にする**

以下のサンプルコードは、[**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DisableDownlevelRevealedComments)プロパティの使用例を示しています。このプロパティを**true**に設定しない場合の効果を示すスクリーンショットをダウンロードしてください。

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DisableDownlevelRevealedCommentsWhileSavingToHTML.java" >}}
{{< app/cells/assistant language="java" >}}
