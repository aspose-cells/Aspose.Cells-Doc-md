---
title: ワークシート内のセルの範囲をイメージにエクスポート
type: docs
weight: 60
url: /ja/net/export-range-of-cells-in-a-worksheet-to-image/
---

## **可能な使用シナリオ**

Aspose.Cellsを使用してワークシートのイメージを作成できます。ただし、ワークシート内のセルの範囲をイメージにエクスポートする必要がある場合があります。この記事では、これをどのように行うかについて説明します。

## **ワークシートのセルの範囲をイメージにエクスポート**

範囲のイメージを取得するには、印刷範囲を所定の範囲に設定し、すべての余白を0に設定し、さらに[**ImageOrPrintOptions.OnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/onepagepersheet) を **true**に設定します。次のコードは、範囲D8:G16のイメージを取得します。下のスクリーンショットは、コードで使用される[サンプルExcelファイル](47153160.xlsx)のイメージです。任意のExcelファイルでコードを試すことができます。

## **サンプルExcelファイルのスクリーンショットとそのエクスポートされたイメージ**

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**

コードを実行すると、範囲D8:G16のイメージが作成されます。

**![todo:image_alt_text](Output-Image.png)**

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-ExportRangeOfCellsInWorksheetToImage-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
