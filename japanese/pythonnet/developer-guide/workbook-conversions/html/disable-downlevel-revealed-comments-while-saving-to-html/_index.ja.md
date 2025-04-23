---
title: HTMLへの保存時にDownlevel表示されたコメントを無効にする
type: docs
weight: 20
url: /ja/python-net/disable-downlevel-revealed-comments-while-saving-to/
---

## **可能な使用シナリオ**

ExcelファイルをHTMLに保存するとき、Aspose.Cells for Python via .NETはDownlevel Conditional Commentsを表示します。これらの条件付きコメントは、古いバージョンのInternet Explorer向けであり、現代のWebブラウザには関係ありません。詳しくは以下のリンクを参照してください。

- [条件付きコメント - Downlevel-revealed条件付きコメント](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells for Python via .NETは、[**HtmlSaveOptions.disable_downlevel_revealed_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/disable_downlevel_revealed_comments) プロパティを**true**に設定することで、これらのDownlevel Revealed Commentsを除去できます。

## **HTML への保存時にダウンレベルの表示されたコメントを無効にする**

[**HtmlSaveOptions.disable_downlevel_revealed_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/disable_downlevel_revealed_comments) プロパティの使用例を示す次のサンプルコードです。このプロパティが true に設定されていない場合のこのプロパティの効果をスクリーンショットで表示しています。このコードとそれによって生成される[サンプルExcelファイル](50528257.xlsx)および[出力HTML](50528258.zip)を参照してください。

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-DisableDownlevelRevealedCommentsWhileSavingToHTML.py" >}}
