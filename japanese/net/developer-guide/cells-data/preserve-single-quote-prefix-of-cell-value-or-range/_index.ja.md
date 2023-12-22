---
title: Cell 値または範囲の一重引用符プレフィックスを保持する
type: docs
weight: 310
url: /ja/net/preserve-single-quote-prefix-of-cell-value-or-range/
description: Cell 値または範囲の一重引用符プレフィックスを Aspose.Cells for .NET API まで保持する方法を学びます。
keywords: Preserve Single Quote Prefix of Cell Value or Range, Hide leading apostrophe or single quote mark, Show leading apostrophe or single quote mark
---
##  **考えられる使用シナリオ**

先頭にアポストロフィまたは一重引用符があるセル内に値を入力すると、Microsoft Excel はその値を非表示にしますが、セルを選択すると、次のスクリーンショットに示すように、数式バーに先頭にアポストロフィまたは一重引用符が表示されます。

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells も、Microsoft Excel と同様に先頭のアポストロフィまたは一重引用符を非表示にしますが、[**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix)として**真実**その細胞のために。セルの空のスタイルを設定すると、[**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix)になる**間違い**また。この問題に対処するために、Aspose.Cells は以下を提供します。[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix)プロパティ、設定時**false** の場合、[**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) はまったく更新されず、古い値が保持されます。 。これは、[**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) プロパティの古い値が **true** であった場合を意味します。 **true のままになります**古い値が *false** だった場合、それは *false** のままになります。

##  **Cell 値または範囲の一重引用符プレフィックスを保持する**

次のサンプルコードは、[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix)前述のプロパティ。詳細については、コード内のコメントを読み、以下に示すコードのコンソール出力を参照してください。

##  **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-PreserveSingleQuotePrefixOfCellValueOrRange.cs" >}}

##  **コンソール出力**

{{< highlight "java" >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
