---
title: スプレッドシートを画像にレンダリングする際にデフォルトフォントを設定する
type: docs
weight: 360
url: /ja/python-net/set-default-font-while-rendering-spreadsheet-to-images/
---

{{% alert color="primary" %}}

スプレッドシートを画像にレンダリングする際に、デフォルトのフォントを設定するには、[**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) プロパティを使用してください。このプロパティは、ワークブックのデフォルトのフォントが文字をレンダリングできない場合にのみ有効です。[**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) プロパティで指定されたデフォルトのフォントは、無効または存在しないフォントを持つすべてのセルに使用されます。

{{% /alert %}}

## スプレッドシートを画像にレンダリングする際のデフォルトフォントの設定

次のサンプルコードでは、ワークブックを作成し、最初のワークシートのセルA4にテキストを追加し、そのフォントを無効または存在しないフォントに設定します。その後、ワークシートの2つの画像を取得します。最初の画像は[**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) プロパティを*Courier New*に設定して取得し、2番目の画像は[**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font)プロパティを*Times New Roman*に設定して取得します。

これは、[**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) プロパティを *Courier New* に設定した後の出力画像です。

![todo:image_alt_text](1.png)

これは、[**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) プロパティを *Times New Roman* に設定した後の出力画像です。

![todo:image_alt_text](2.png)

## サンプルコード

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SetDefaultFontWhileRenderingSpreadsheet-1.cs" >}}

