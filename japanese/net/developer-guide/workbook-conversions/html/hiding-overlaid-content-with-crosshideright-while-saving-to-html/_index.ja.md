---
title: HTML に保存するときに CrossHideRight でオーバーレイされたコンテンツを非表示にする
type: docs
weight: 100
url: /ja/net/hiding-overlaid-content-with-crosshideright-while-saving-to/
---
## **考えられる使用シナリオ**

Excel ファイルを HTML に保存すると、セル文字列に異なるクロス タイプを指定できます。デフォルトでは、Aspose.Cells は Microsoft Excel に従って HTML を生成しますが、クロス タイプを[**CrossHideRight**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype)、次に、セル文字列と重なっている、または重なっているセルの右側にあるすべての文字列を非表示にします。

## **Html への保存中に CrossHideRight でオーバーレイされたコンテンツを非表示にする**

次のサンプル コードは、[サンプル Excel ファイル](64716894.xlsx)そしてそれをに保存します[出力 HTML](64716893.zip)を設定した後[**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/htmlcrossstringtype)なので[**CrossHideRight**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype).スクリーンショットはその方法を説明しています[**CrossHideRight**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype)デフォルト出力からの出力 HTML に影響します。

![todo:画像_代替_文章](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.cs" >}}
