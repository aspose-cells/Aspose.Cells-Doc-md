---
title: GolangをC++経由で保存時にOverlaidコンテンツをCrossHideRightで非表示にする
linktitle: HTMLで保存する際のCrossHideRightでオーバーレイされたコンテンツを非表示にする
type: docs
weight: 100
url: /ja/go-cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/
description: Aspose.CellsをC++で使用して、HTML保存時に重なったコンテンツを非表示にするためにCrossHideRightを使用します。
---

## **可能な使用シナリオ**

ExcelファイルをHTMLに保存する際に、セル文字列のクロスタイプを指定できます。デフォルトでは、Aspose.CellsはMicrosoft Excelに準拠したHTMLを生成しますが、クロスタイプを[**CrossHideRight**](https://reference.aspose.com/cells/go-cpp/htmlcrosstype)に変更すると、セル文字列の右側に重なったり重なり合ったりしているすべての文字列が非表示となります。

## **CrossHideRightを使用してオーバーレイコンテンツを非表示にする**

以下のサンプルコードは、[サンプルExcelファイル](64716894.xlsx)を読み込み、[**HtmlSaveOptions.GetHtmlCrossStringType()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/gethtmlcrossstringtype/)を[**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype)に設定し、[出力HTML](64716893.zip)に保存します。スクリーンショットは、[**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype)がデフォルトの出力にどのように影響を与えるかを示しています。

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-HidingOverlaidContentWithCrosshiderightWhileSavingToHtml.go" >}}
