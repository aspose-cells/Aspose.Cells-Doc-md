---
title: 画像にレンダリングする前にデータから空白を削除する
type: docs
weight: 270
url: /ja/java/remove-white-spaces-from-the-data-before-rendering-to-image/
---
{{% alert color="primary" %}}

場合によっては、アプリケーションまたは Web ページでワークシート イメージを表示する必要があります。たとえば、Word 文書、PDF ファイル、PowerPoint プレゼンテーション、またはその他の文書に画像を挿入する必要がある場合があります。基本的に、ワークシートを画像としてレンダリングして、他のアプリケーションに貼り付けることができます。 Aspose.Cells API を使用すると、Microsoft Excel ワークシートを画像に変換できます。

{{% /alert %}}

の[**シートレンダリング**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender)クラスは、指定された属性 (イメージ形式、ページ付けされたシートなど) を持つイメージ ファイルにワークシートを変換できます。BMP、GIF、JPG、TIFF、EMF など、いくつかのイメージ形式がサポートされています。

シートから画像への機能を使用する場合、出力画像には、デフォルトで周囲に白/空白スペース、つまり境界線があります。これを削除できます。ソースワークシートの上、左、下、および右のページ設定余白を 0 に設定し、指定します。[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)それに応じて属性。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-RemoveWhitespaceAroundData-1.java" >}}
