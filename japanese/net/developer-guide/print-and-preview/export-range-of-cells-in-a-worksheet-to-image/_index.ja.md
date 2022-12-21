---
title: ワークシートの Cells の範囲を画像にエクスポート
type: docs
weight: 60
url: /ja/net/export-range-of-cells-in-a-worksheet-to-image/
---
## **考えられる使用シナリオ**

Aspose.Cells を使用してワークシートの画像を作成できます。ただし、ワークシート内のセルの範囲のみを画像にエクスポートする必要がある場合があります。この記事では、これを実現する方法について説明します。

## **ワークシートの Cells の範囲を画像にエクスポート**

範囲の画像を取得するには、印刷領域を目的の範囲に設定し、すべての余白を 0 に設定します。[**ImageOrPrintOptions.OnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/onepagepersheet)に**真実** .次のコードは、範囲 D8:G16 の画像を取得します。以下は、[サンプル Excel ファイル](47153160.xlsx)コードで使用されます。任意の Excel ファイルでコードを試すことができます。

## **サンプル Excel ファイルとエクスポートされた画像のスクリーンショット**

**![todo:image_alt_text](export-range-of-cells in a worksheet-to-image_1.png)**

コードを実行すると、範囲 D8:G16 のみのイメージが作成されます。

**![todo:image_alt_text](Output-Image.png)**

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-ExportRangeOfCellsInWorksheetToImage-1.cs" >}}
