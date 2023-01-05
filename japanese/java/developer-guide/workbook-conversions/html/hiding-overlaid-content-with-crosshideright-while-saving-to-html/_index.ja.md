---
title: HTML に保存するときに CrossHideRight でオーバーレイされたコンテンツを非表示にする
type: docs
weight: 100
url: /ja/java/hiding-overlaid-content-with-crosshideright-while-saving-to-html/
---
## **考えられる使用シナリオ**

Excel ファイルを HTML に保存すると、セル文字列に異なるクロス タイプを指定できます。デフォルトでは、Aspose.Cells は Microsoft Excel に従って HTML を生成しますが、[**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#HtmlCrossStringType)に[**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT)次に、セル文字列とオーバーレイまたはオーバーラップしているセルの右側にあるすべての文字列を非表示にします。

## **HTML に保存するときに CrossHideRight でオーバーレイされたコンテンツを非表示にする**

次のサンプル コードは、[サンプル Excel ファイル](64716916.xlsx)そしてそれをに保存します[出力 HTML](64716915.zip)を設定した後[**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#HtmlCrossStringType)なので[**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT).スクリーンショットはその方法を説明しています[**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT)デフォルト出力からの出力 HTML に影響します。

![todo:画像_代替_文章](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.java" >}}
