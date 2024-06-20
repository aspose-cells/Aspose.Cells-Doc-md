---
title: HTMLで保存する際のCrossHideRightでオーバーレイされたコンテンツを非表示にする
type: docs
weight: 100
url: /ja/java/hiding-overlaid-content-with-crosshideright-while-saving-to-html/
---

## **可能な使用シナリオ**

ExcelファイルをHTMLに保存する際、セル文字列のさまざまな交差タイプを指定できます。デフォルトでは、Aspose.CellsはMicrosoft Excelに従ってHTMLを生成しますが、[**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#HtmlCrossStringType)を[**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT)に変更すると、セル文字列と重なっているセルの右側にあるすべての文字列を非表示にします。

## **HTMLに保存する際のボーダースタイルがWebブラウザでサポートされていない場合に似たボーダースタイルをエクスポートする**

以下のサンプルコードでは、[サンプルExcelファイル](64716916.xlsx)をロードし、[**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#HtmlCrossStringType)を[**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT)に設定した後に[output HTML](64716915.zip)に保存します。スクリーンショットは、[**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT)がデフォルトの出力から出力されたHTMLに影響を与える方法を説明しています。

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.java" >}}
