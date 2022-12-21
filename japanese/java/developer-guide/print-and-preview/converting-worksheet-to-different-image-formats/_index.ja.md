---
title: ワークシートを別の画像形式に変換する
type: docs
weight: 30
url: /ja/java/converting-worksheet-to-different-image-formats/
---
{{% alert color="primary" %}}

Aspose.Cells を使用すると、ブックからワークシートをエクスポートして、別の形式に変換できます。この記事では、ワークシートを別の形式に変換する方法について説明します。

{{% /alert %}}

## **ワークシートを画像に変換する**

ワークシートの画像を保存すると便利な場合があります。画像はオンラインで共有したり、他のドキュメント (Microsoft Word で書かれたレポートや PowerPoint プレゼンテーションなど) に挿入したりできます。

Aspose.Cells は、**[SheetRender](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)**クラス。このクラスは、画像にレンダリングされるワークシートを表します。の**[SheetRender](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)**クラスが提供する**[toImage()](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toImage(int,%20java.io.OutputStream))**ワークシートを画像ファイルに変換するメソッド。 BMP、PNG、JPEG、TIFF、および EMF 形式がサポートされています。

{{% alert color="primary" %}}

Aspose.Cells for Java は TIFF 形式への変換にも対応しています。ワークシートを TIFF 画像に変換するには、JAI ライブラリをクラスパスに追加します。

{{% /alert %}} {{% alert color="primary" %}}

現在、ワークシートを画像 API に変換する場合、3D バブル チャートはサポートされていません。

{{% /alert %}}

以下のコードは、Microsoft Excel ファイルのワークシートを PNG ファイルに変換する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-WorksheetToImage-1.java" >}}

## **ワークシートを SVG に変換する**

 SVG は**スケーラブルなベクター グラフィックス**SVG は、2 次元ベクター グラフィックスの XML 標準に基づく仕様です。これは、1999 年から World Wide Web Consortium (W3C) によって開発されているオープン標準です。

v7.1.0 のリリース以降、**Aspose.Cells for Java**ワークシートを SVG 画像に変換できます。

この機能を使用するには、com.aspose.cells 名前空間をプログラムまたはプロジェクトにインポートする必要があります。レンダリングと印刷に役立ついくつかのクラスがあります。たとえば、**[SheetRender](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)**, **[ImageOrPrintOptions](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)**, **[WorkbookRender](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender)**、 その他。

の**[com.aspose.cells.ImageOrPrintOptions](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)**クラスは、ワークシートが SVG 形式で保存されることを指定します。

の**[SheetRender](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)**クラスはのオブジェクトを取ります**[ImageOrPrintOptions](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)**保存形式を SVG 形式に設定するパラメーターとして。

次のコード スニペットは、Excel ファイルのワークシートを SVG イメージ ファイルに変換する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingWorksheetToSVG-ConvertingWorksheetToSVG.java" >}}

### **ワークブックにアクティブなワークシートを表示する**

ワークブック内のアクティブなワークシートを変換する簡単な方法は、アクティブなシート インデックスを設定し、ワークブックを SVG として保存することです。アクティブなシートを SVG にレンダリングします。次のサンプル コードは、この機能を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertActiveWorksheetToSVG-1.java" >}}

## 関連記事

- [viewBox 属性を使用してチャートを SVG にエクスポート](/cells/ja/java/export-chart-to-svg-with-viewbox-attribute/)
- [ワークシートまたはチャートを目的の幅と高さの画像にエクスポート](/cells/ja/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [ワークシートから画像へ、ワークシートから画像へのページ単位での変換](/cells/ja/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
