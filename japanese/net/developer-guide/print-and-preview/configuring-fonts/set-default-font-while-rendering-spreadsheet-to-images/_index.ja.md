---
title: スプレッドシートを画像にレンダリングする際にデフォルトフォントを設定する
type: docs
weight: 360
url: /ja/net/set-default-font-while-rendering-spreadsheet-to-images/
---

{{% alert color="primary" %}}

スプレッドシートを画像にレンダリングする際に、デフォルトのフォントを設定するには、[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) プロパティを使用してください。このプロパティは、ワークブックのデフォルトのフォントが文字をレンダリングできない場合にのみ有効です。[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) プロパティで指定されたデフォルトのフォントは、無効または存在しないフォントを持つすべてのセルに使用されます。

{{% /alert %}}

## スプレッドシートを画像にレンダリングする際のデフォルトフォントの設定

次のサンプルコードでは、ワークブックを作成し、最初のワークシートのセルA4にテキストを追加し、そのフォントを無効または存在しないフォントに設定します。その後、ワークシートの2つの画像を取得します。最初の画像は[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) プロパティを*Courier New*に設定して取得し、2番目の画像は[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont)プロパティを*Times New Roman*に設定して取得します。

これは、[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) プロパティを *Courier New* に設定した後の出力画像です。

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_1.png)

これは、[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) プロパティを *Times New Roman* に設定した後の出力画像です。

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_2.png)

## サンプルコード

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetDefaultFontWhileRenderingSpreadsheet-1.cs" >}}
