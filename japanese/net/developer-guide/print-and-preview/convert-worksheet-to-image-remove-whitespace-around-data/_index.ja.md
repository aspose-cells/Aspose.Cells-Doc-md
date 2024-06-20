---
title: ワークシートを画像に変換  データ周りの余白を削除する
type: docs
weight: 40
url: /ja/net/convert-worksheet-to-image-remove-whitespace-around-data/
---

{{% alert color="primary" %}}

時には、ワークシートの画像をアプリケーションやWebページで表示する必要があります。たとえば、画像をWord文書、PDFファイル、PowerPointプレゼンテーション、あるいは他のドキュメントに挿入する必要があるかもしれません。基本的に、ワークシートを画像としてレンダリングして、他のアプリケーションに貼り付けられるようにしたいと思うでしょう。Aspose.Cellsを使用すると、Microsoft Excelのワークシートを画像に変換することができます。

{{% /alert %}}

## **データ周りの余白を削除してください**

[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)APIは、ワークシートを指定された属性（たとえば、画像形式、ページ化されたシートなど）で画像ファイルに変換します。いくつかの画像形式がサポートされており、BMP、GIF、JPG、TIFF、EMFなどが含まれています。

シートを画像化する際、出力画像にはデフォルトで余白（ボーダー）があります。これを削除するには、元のワークシートの上部、下部、左側、右側のページ設定のマージンを0に設定し、それに応じて[**Aspose.Cells.Rendering.ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)属性を指定してください。

次のコードスニペットは、出力画像のデータ周りの余白を削除します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RemoveWhitespaceAroundData-1.cs" >}}

