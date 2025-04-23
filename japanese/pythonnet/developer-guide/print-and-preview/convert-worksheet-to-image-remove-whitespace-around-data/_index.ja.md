---
title: ワークシートを画像に変換  データ周りの余白を削除する
type: docs
weight: 40
url: /ja/python-net/convert-worksheet-to-image-remove-whitespace-around-data/
---

{{% alert color="primary" %}}

時には、ワークシートの画像をアプリケーションやWebページに表示する必要があります。たとえば、画像をWord文書、PDF、PowerPointプレゼンテーション、または他のドキュメントに挿入したい場合です。基本的に、ワークシートを画像としてレンダリングし、他のアプリケーションに貼り付けられるようにしたいのです。Aspose.Cells for Python via .NETは、Microsoft Excelのワークシートを画像に変換することができます。

{{% /alert %}}

## **データ周りの余白を削除してください**

[**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender)APIは、ワークシートを指定された属性（たとえば、画像形式、ページ化されたシートなど）で画像ファイルに変換します。いくつかの画像形式がサポートされており、BMP、GIF、JPG、TIFF、EMFなどが含まれています。

シートを画像化する際、出力画像にはデフォルトで余白（ボーダー）があります。これを削除するには、元のワークシートの上部、下部、左側、右側のページ設定のマージンを0に設定し、それに応じて[**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions)属性を指定してください。

次のコードスニペットは、出力画像のデータ周りの余白を削除します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-RemoveWhitespaceAroundData-1.py" >}}

