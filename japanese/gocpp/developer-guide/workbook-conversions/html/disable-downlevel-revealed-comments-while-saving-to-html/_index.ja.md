---
title: 保存時にDownlevel Revealed Commentsを無効にする（GolaingとC++経由）
linktitle: Downlevel Revealed Commentsを無効にする
type: docs
weight: 20
url: /ja/go-cpp/disable-downlevel-revealed-comments-while-saving-to/
description: Aspose.Cellsを使用してExcelファイルをHTMLに保存する際にDownlevel Revealed Commentsを削除する（GolaingとC++経由）
---

## **可能な使用シナリオ**

ExcelファイルをHTMLに保存すると、Aspose.CellsはDownlevel Conditional Commentsを表示します。これらの条件付きコメントは主に古いバージョンのInternet Explorerに関連しており、最新のWebブラウザには無関係です。詳細については以下のリンクをご参照ください。

- [条件付きコメント - Downlevel-revealed条件付きコメント](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cellsでは、[**HtmlSaveOptions.GetDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdisabledownlevelrevealedcomments/) プロパティを **true** に設定して、これらのDownlevel Revealed Commentsを排除することができます。

## **HTML への保存時にダウンレベルの表示されたコメントを無効にする**

以下のサンプルコードは [**HtmlSaveOptions.GetDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdisabledownlevelrevealedcomments/) プロパティの使用例を示しています。スクリーンショットは、このプロパティが true に設定されていない場合の効果を示しています。このコードで使用されるサンプルExcelファイル（50528257.xlsx）と、それによって生成された出力HTML（50528258.zip）もダウンロードしてください。

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DisableDownlevelRevealedCommentsWhileSavingToHtml.go" >}}
