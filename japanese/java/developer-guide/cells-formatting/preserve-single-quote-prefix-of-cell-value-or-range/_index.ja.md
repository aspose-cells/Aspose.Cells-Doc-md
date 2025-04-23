---
title: セル値または範囲の接頭辞を保存します
type: docs
weight: 1900
url: /ja/java/preserve-single-quote-prefix-of-cell-value-or-range/
---

## **可能な使用シナリオ**

先頭にアポストロフィやシングルクォートマークがあるセルに値を入れると、Microsoft Excelはそれを非表示にしますが、セルを選択すると、次のスクリーンショットに示すように、既定の値が表示されます。

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells は、Microsoft Excel のように先頭のアポストロフィやシングルクォートを非表示にしますが、そのセルに対して[**Style.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix)を**true**に設定します。セルの空のスタイルを設定すると、[**Style.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix)は再び **false**になります。この問題に対処するために、Aspose.Cells は[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix)プロパティを提供し、それが**false**に設定されている場合、[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix) は全く更新されず、古い値が保持されます。つまり、[**Style.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) プロパティの古い値が**true**であれば、それは変わらず、古い値がfalseであれば、そのままfalseのままです。

## **セル値または範囲の先頭にシングルクォートのプレフィックスを保存**

次のサンプルコードは、前述の[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix)プロパティの使用法を説明しています。コード内のコメントを読んで、以下のコードのコンソール出力を参照してください。

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-PreserveSingleQuotePrefixOfCellValueOrRange.java" >}}

## **コンソール出力**

{{< highlight java >}}

Quote Prefix of Cell A1: false

Quote Prefix of Cell A1: true

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: true

Quote Prefix of Cell A1: false

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
