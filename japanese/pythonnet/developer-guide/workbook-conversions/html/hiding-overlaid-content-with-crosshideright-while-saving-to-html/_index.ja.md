---
title: HTMLで保存する際のCrossHideRightでオーバーレイされたコンテンツを非表示にする
type: docs
weight: 100
url: /ja/python-net/hiding-overlaid-content-with-crosshideright-while-saving-to/
---

## **可能な使用シナリオ**

ExcelファイルをHTMLに保存する際に、セル文字列のクロスタイプを指定できます。デフォルトでは、Aspose.Cells for Python via .NETはMicrosoft Excelに準拠したHTMLを生成しますが、クロスタイプを[**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype/)に変更すると、セルの文字列の右側に重ねて表示されている文字列や重なっている文字列を非表示にします。

## **CrossHideRightを使用してオーバーレイコンテンツを非表示にする**

次のサンプルコードは、[**HtmlSaveOptions.html_cross_string_type**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/html_cross_string_type)を[**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype/)に設定してから、[サンプルExcelファイル](64716894.xlsx)を読み込み、[output HTML](64716893.zip)に保存します。スクリーンショットは**default output**から**[**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype/)**が出力されたHTMLへの影響を示しています。

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.py" >}}
{{< app/cells/assistant language="python-net" >}}
