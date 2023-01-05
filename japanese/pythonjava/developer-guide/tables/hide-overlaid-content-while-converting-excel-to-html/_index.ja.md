---
title: Excel を HTML に変換する際にオーバーレイ コンテンツを非表示にする
type: docs
weight: 40
url: /ja/python-java/hide-overlaid-content-while-converting-excel-to/
---
## **Excel を HTML に変換する際にオーバーレイ コンテンツを非表示にする**
Excel ファイルを HTML に保存すると、セル文字列に異なるクロス タイプを指定できます。デフォルトでは、Aspose.Cells は Microsoft Excel に従って HTML を生成しますが、[HtmlSaveOptions.HtmlCrossStringType](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#HtmlCrossStringType)に[クロス_隠れる_正しい](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT)次に、セル文字列とオーバーレイまたはオーバーラップしているセルの右側にあるすべての文字列を非表示にします。

次のサンプル コードは、[サンプル Excel ファイル](sampleHidingOverlaidContentWithCrossHideRight.xlsx)そしてそれをに保存します[出力 HTML](HTML-outputHidingOverlaidContentWithCrossHideRight.zip)を設定した後[HtmlSaveOptions.HtmlCrossStringType](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#HtmlCrossStringType)なので[クロス_隠れる_正しい](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT).スクリーンショットはその方法を説明しています[クロス_隠れる_正しい](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT)デフォルト出力からの出力 HTML に影響します。

![todo:画像_代替_文章](Hiding-Overlaid-Content-With-CrossHideRight.png)
## **サンプルコード**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.py" >}}
