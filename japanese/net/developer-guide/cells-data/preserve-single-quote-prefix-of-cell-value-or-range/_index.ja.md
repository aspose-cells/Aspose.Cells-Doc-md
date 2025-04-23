---
title: セル値または範囲の接頭辞を保存します
type: docs
weight: 310
url: /ja/net/preserve-single-quote-prefix-of-cell-value-or-range/
description: Aspose.Cells for .NET APIを介して、セル値または範囲の先頭アポストロフィを保持する方法について学びます。
keywords: セル値または範囲の先頭アポストロフィを保持し、先頭のアポストロフィまたはシングルクォートマークを非表示にする、先頭のアポストロフィまたはシングルクォートマークを表示する
---

## **可能な使用シナリオ**

先頭にアポストロフィやシングルクォートマークがあるセルに値を入れると、Microsoft Excelはそれを非表示にしますが、セルを選択すると、次のスクリーンショットに示すように、既定の値が表示されます。

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cellsも先頭のアポストロフィまたはシングルクォートを非表示にしますが、そのセルの [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) を **true** に設定します。セルの空のスタイルを設定すると、 [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) が再び **false** になります。この問題に対処するために、Aspose.Cellsは [**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix) プロパティを提供し、これが **false** に設定されている場合、 [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) は全く更新されず、その旧い値が保持されます。つまり、 [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) プロパティの古い値が **true** であれば、 **true** のままであり、古い値が **false** であれば、 **false** のままです。

## **セル値または範囲の先頭にシングルクォートのプレフィックスを保存**

次のサンプルコードは、以前に説明した **[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix)** プロパティの使用方法を説明しています。コード内のコメントを読んで、以下のコードのコンソール出力を確認してください。

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-PreserveSingleQuotePrefixOfCellValueOrRange.cs" >}}

## **コンソール出力**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
