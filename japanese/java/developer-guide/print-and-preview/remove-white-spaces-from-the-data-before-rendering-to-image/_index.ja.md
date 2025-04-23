---
title: 画像にレンダリングする前にデータから余分なスペースを削除する
type: docs
weight: 270
url: /ja/java/remove-white-spaces-from-the-data-before-rendering-to-image/
---

{{% alert color="primary" %}}

時折、ワークシート画像をアプリケーションやWebページに表示する必要があります。たとえば、Wordドキュメント、PDFファイル、PowerPointプレゼンテーションなどに画像を挿入する必要があるかもしれません。基本的には、ワークシートを画像としてレンダリングし、他のアプリケーションに貼り付けられるようにしたいと思うでしょう。Aspose.CellsのAPIでは、Microsoft Excelワークシートを画像に変換することができます。

{{% /alert %}}

[**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender)クラスは、画像形式、ページ化されたシートなどを含む任意の属性でワークシートを画像ファイルに変換する機能を備えています。BMP、GIF、JPG、TIFF、およびEMFなどのさまざまな画像形式がサポートされています。

シートを画像に変換する機能を使用すると、出力画像にはデフォルトでホワイト/ブランクスペース、つまり周囲にボーダーがあります。このボーダーを削除できます。ソースワークシートの上部、左部、下部、右部のページ設定マージンを0に設定し、それに応じて[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)属性を指定します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-RemoveWhitespaceAroundData-1.java" >}}
{{< app/cells/assistant language="java" >}}
