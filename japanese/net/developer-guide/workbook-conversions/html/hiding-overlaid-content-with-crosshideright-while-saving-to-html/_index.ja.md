---
title: HTMLで保存する際のCrossHideRightでオーバーレイされたコンテンツを非表示にする
type: docs
weight: 100
url: /ja/net/hiding-overlaid-content-with-crosshideright-while-saving-to/
---

## **可能な使用シナリオ**

ExcelファイルをHTMLに保存する際に、セル文字列の異なるクロスタイプを指定できます。デフォルトでは、Aspose.CellsはMicrosoft Excelに従ったHTMLを生成しますが、クロスタイプを[**CrossHideRight**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype)に変更すると、セル文字列と重なり合う右側のすべての文字列が非表示になります。

## **CrossHideRightを使用してオーバーレイコンテンツを非表示にする**

次のサンプルコードは、[**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/htmlcrossstringtype)を[**CrossHideRight**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype)に設定してから、[サンプルExcelファイル](64716894.xlsx)を読み込み、[output HTML](64716893.zip)に保存します。スクリーンショットは**default output**から**[**CrossHideRight**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype)**が出力されたHTMLへの影響を示しています。

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.cs" >}}
{{< app/cells/assistant language="csharp" >}}
