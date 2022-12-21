---
title: Cell 値または範囲の一重引用符プレフィックスを保持
type: docs
weight: 1900
url: /ja/java/preserve-single-quote-prefix-of-cell-value-or-range/
---
## **考えられる使用シナリオ**

先頭にアポストロフィまたは一重引用符があるセル内に値を入力すると、Microsoft Excel はそれを非表示にしますが、セルを選択すると、次のスクリーンショットに示すように数式バーに先頭のアポストロフィまたは一重引用符が表示されます。

![todo:画像_代替_文章](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells も、Microsoft Excel のように先頭のアポストロフィまたは一重引用符を非表示にしますが、[**Style.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix)なので**真実**そのセルのために。セルの空のスタイルを設定すると、[**Style.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix)になる**間違い**また。この問題に対処するために、Aspose.Cells が提供します。[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix)プロパティ、設定時**間違い**、 それから[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix)はまったく更新されず、古い値が保持されます。の古い値が[**Style.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix)プロパティは**真実**、それは true のままで、古い値が false だった場合は false のままです。

## **Cell 値または範囲の一重引用符プレフィックスを保持**

次のサンプル コードは、[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix)プロパティは前述のとおりです。詳細については、コード内のコメントを読み、以下に示すコードのコンソール出力を参照してください。

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-PreserveSingleQuotePrefixOfCellValueOrRange.java" >}}

## **コンソール出力**

{{< highlight "java" >}}

Quote Prefix of Cell A1: false

Quote Prefix of Cell A1: true

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: true

Quote Prefix of Cell A1: false

{{< /highlight >}}
