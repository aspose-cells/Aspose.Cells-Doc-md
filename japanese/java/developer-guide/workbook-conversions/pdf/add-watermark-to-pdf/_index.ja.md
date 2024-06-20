---
title: PDFに透かしを追加する
type: docs
weight: 9
url: /ja/java/add-watermark-to-pdf/
---

ExcelファイルをPDFに変換する際、PDFファイルに透かしを追加する要件がある場合があります。次の例では、PDFに変換する際にテキストや画像の透かしを追加する方法が示されています。

## **PDFにテキスト透かしを追加する**

テキストと対応するフォントを指定することで、簡単にPDFにテキスト透かしを追加できます。また、[RenderingWatermark](https://reference.aspose.com/cells/java/com.aspose.cells/renderingwatermark/)でページへの配置、オフセット、回転、不透明度、前景色/背景色、ページへのスケーリングを設定することができます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-AddTextWatermarkToPdf.java" >}}

## **PDFに画像透かしを追加する**

画像のバイトを指定するだけで、PDFに画像透かしを簡単に追加できます。また、[RenderingWatermark](https://reference.aspose.com/cells/java/com.aspose.cells/renderingwatermark/)でページへの配置、オフセット、回転、不透明度、前景色/背景色、ページへのスケーリングを設定することができます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-AddImageWatermarkToPdf.java" >}}

