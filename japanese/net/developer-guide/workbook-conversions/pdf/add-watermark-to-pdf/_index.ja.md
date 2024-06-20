---
title: PDFに透かしを追加する
type: docs
weight: 9
url: /ja/net/add-watermark-to-pdf/
---

ExcelファイルをPDFに変換する際、PDFファイルに透かしを追加する要件がある場合があります。次の例では、PDFに変換する際にテキストや画像の透かしを追加する方法が示されています。

## **PDFにテキスト透かしを追加する**

特定のテキストと対応するフォントを指定して、PDF にテキストウォーターマークを簡単に追加できます。また、[RenderingWatermark](https://reference.aspose.com/cells/net/aspose.cells.rendering/renderingwatermark/)を使用して、配置、オフセット、回転、不透明度、前景色/背景色、およびページへのスケールを設定できます。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-AddTextWatermarkToPdf.cs" >}}

## **PDFに画像透かしを追加する**

画像のバイトを指定するだけで、PDF に画像ウォーターマークを追加できます。また、[RenderingWatermark](https://reference.aspose.com/cells/net/aspose.cells.rendering/renderingwatermark/)を使用して、配置、オフセット、回転、不透明度、前景色/背景色、およびページへのスケールを設定できます。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-AddImageWatermarkToPdf.cs" >}}

