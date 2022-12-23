---
title: ワークシートを画像に変換 - データの周りの空白を削除
type: docs
weight: 40
url: /ja/net/convert-worksheet-to-image-remove-whitespace-around-data/
---
{{% alert color="primary" %}}

場合によっては、アプリケーションまたは Web ページでワークシート イメージを表示する必要があります。たとえば、Word ドキュメント、PDF ファイル、PowerPoint プレゼンテーション、またはその他のドキュメントに画像を挿入する必要がある場合があります。基本的に、ワークシートを画像としてレンダリングして、他のアプリケーションに貼り付けることができます。 Aspose.Cells では、Microsoft Excel ワークシートを画像に変換できます。

{{% /alert %}}

## **データの周囲の空白を削除**

の[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)API は、ワークシートを指定された属性 (イメージ形式、ページ付けされたシートなど) を持つイメージ ファイルに変換します。

シートから画像への機能を使用すると、出力画像にはデフォルトで余白、つまり境界線が表示されます。これを削除するには、元のワークシートの上下左右のページ設定マージンを 0 に設定し、指定します。[**Aspose.Cells.Rendering.ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)それに応じて属性。

次のコード スニペットは、出力画像のデータの周囲の空白を削除します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RemoveWhitespaceAroundData-1.cs" >}}

