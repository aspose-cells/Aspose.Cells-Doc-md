---
title: HTMLへの保存時にDownlevel表示されたコメントを無効にする
type: docs
weight: 20
url: /ja/net/disable-downlevel-revealed-comments-while-saving-to/
---

## **可能な使用シナリオ**

ExcelファイルをHTMLに保存すると、Aspose.Cellsが下位レベルの条件付きコメントを公開します。これらの条件付きコメントは主に古いバージョンのInternet Explorerに関連しており、現代のWebブラウザには無関係です。以下のリンクで詳細をご覧いただけます。

- [条件付きコメント - Downlevel-revealed条件付きコメント](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cellsを使用して、[**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/disabledownlevelrevealedcomments) プロパティを**true**に設定することで、これらの下位レベルの公開されたコメントを削除できます。

## **HTML への保存時にダウンレベルの表示されたコメントを無効にする**

[**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/disabledownlevelrevealedcomments) プロパティの使用例を示す次のサンプルコードです。このプロパティが true に設定されていない場合のこのプロパティの効果をスクリーンショットで表示しています。このコードとそれによって生成される[サンプルExcelファイル](50528257.xlsx)および[出力HTML](50528258.zip)を参照してください。

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DisableDownlevelRevealedCommentsWhileSavingToHTML.cs" >}}
