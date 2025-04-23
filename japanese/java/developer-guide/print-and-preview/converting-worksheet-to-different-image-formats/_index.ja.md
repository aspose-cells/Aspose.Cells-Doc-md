---
title: ワークシートを異なる画像形式に変換
type: docs
weight: 30
url: /ja/java/converting-worksheet-to-different-image-formats/
---

{{% alert color="primary" %}}

Aspose.Cellsでは、ワークブックからワークシートをエクスポートし、異なる形式に変換することができます。この記事ではワークシートを異なる形式に変換する方法について説明します。

{{% /alert %}}

## **ワークシートをイメージに変換**

時々、ワークシートの画像を保存することが役立ちます。画像はオンラインで共有したり、他のドキュメントに挿入したり（例えば、Microsoft Wordで書かれたレポートやPowerPointプレゼンテーションに）、利用できます。

Aspose.Cells は [**toImage()**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toImage-int-java.io.OutputStream-) メソッドを提供する [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender) クラスを介して画像のエクスポートを提供します。BMP、PNG、JPEG、TIFF、およびEMF形式がサポートされています。

{{% alert color="primary" %}}

Aspose.Cells for Java は TIFF形式への変換もサポートしています。ワークシートをTIFF画像に変換するには、JAIライブラリをクラスパスに追加してください。

{{% /alert %}} {{% alert color="primary" %}}

現在のところ、ワークシートを画像に変換するAPIは3Dバブルチャートをサポートしていません。

{{% /alert %}}

以下のコードは、Microsoft Excelファイル内のワークシートをPNGファイルに変換する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-WorksheetToImage-1.java" >}}

## **ワークシートをSVGに変換**

SVG は **Scalable Vector Graphics** の略です。SVG は2次元ベクターグラフィックスに関するXML標準に基づいた仕様です。1999年以来、世界中でW3C（World Wide Web Consortium）によって開発されているオープン標準です。

v7.1.0以降のリリースでは、**Aspose.Cells for Java** でワークシートをSVG画像に変換できます。

この機能を使用するには、プログラムまたはプロジェクトに com.aspose.cells ネームスペースをインポートする必要があります。描画および印刷には、例えば [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)、[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)、[**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender)などの貴重なクラスがいくつか含まれています。

[**com.aspose.cells.ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) クラスはSVG形式で保存されることを指定します。

[**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender) クラスは SVG 形式への保存形式を設定する [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) オブジェクトをパラメータとして受け取ります。

次のコードスニペットは、Excelファイル内のワークシートをSVGイメージファイルに変換する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingWorksheetToSVG-ConvertingWorksheetToSVG.java" >}}

### **ブック内のアクティブなワークシートをレンダリング**

ブック内のアクティブなワークシートを変換する簡単な方法は、アクティブシートのインデックスを設定し、その後ブックをSVGとして保存することです。アクティブシートはSVGにレンダリングされます。次のサンプルコードは、この機能を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertActiveWorksheetToSVG-1.java" >}}

## 関連記事

- [viewBox属性を使用してチャートをSVGにエクスポート](/cells/ja/java/export-chart-to-svg-with-viewbox-attribute/)
- [希望の幅と高さでワークシートまたはチャートを画像にエクスポート](/cells/ja/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [ワークシートを画像に変換し、ページごとに画像をワークシートに変換する](/cells/ja/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
{{< app/cells/assistant language="java" >}}
