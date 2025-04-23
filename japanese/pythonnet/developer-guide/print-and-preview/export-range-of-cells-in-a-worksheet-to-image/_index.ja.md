---
title: ワークシート内のセルの範囲をイメージにエクスポート
type: docs
weight: 60
url: /ja/python-net/export-range-of-cells-in-a-worksheet-to-image/
---

## **可能な使用シナリオ**

Aspose.Cells for Python via .NETを使用してワークシートの画像を作成できます。ただし、時にはワークシート内のセルの範囲だけを画像としてエクスポートする必要があります。この記事では、その方法について説明します。

## **ワークシートのセルの範囲をイメージにエクスポート**

範囲のイメージを取得するには、印刷範囲を所定の範囲に設定し、すべての余白を0に設定し、さらに[**ImageOrPrintOptions.one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/one_page_per_sheet) を **true**に設定します。次のコードは、範囲D8:G16のイメージを取得します。下のスクリーンショットは、コードで使用される[サンプルExcelファイル](47153160.xlsx)のイメージです。任意のExcelファイルでコードを試すことができます。

## **サンプルExcelファイルのスクリーンショットとそのエクスポートされたイメージ**

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**

コードを実行すると、範囲D8:G16のイメージが作成されます。

**![todo:image_alt_text](Output-Image.png)**

## **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-ExportRangeOfCellsInWorksheetToImage-1.py" >}}

