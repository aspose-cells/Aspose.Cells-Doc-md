---
title: セル値または範囲の接頭辞を保存します
type: docs
weight: 310
url: /ja/python-net/preserve-single-quote-prefix-of-cell-value-or-range/
description: Aspose.Cells for Python via .NET APIを介してセル値または範囲の接頭辞を保存する方法を学ぶ。
keywords: Python Excelライブラリ、Pythonセル値または範囲の接頭辞を保存、Python先頭のアポストロフィやシングルクォートマークを非表示に、Python先頭のアポストロフィやシングルクォートマークを表示
---

## **可能な使用シナリオ**

先頭にアポストロフィやシングルクォートマークがあるセルに値を入れると、Microsoft Excelはそれを非表示にしますが、セルを選択すると、次のスクリーンショットに示すように、既定の値が表示されます。

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells for Python via .NETもMicrosoft Excelと同様に、先頭にアポストロフィやシングルクォートを非表示にしますが、そのセルのために **true** を設定します。セルの空のスタイルを設定すると、それは再び **false** となります。この問題に対処するために、Aspose.Cells for Python via .NETは **false** に設定された場合、それに **true** はまったく更新されず、その古い値が保持されます。

## **セル値または範囲の先頭にシングルクォートのプレフィックスを保存**

次のサンプルコードは、以前に説明した **[**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix)** プロパティの使用方法を説明しています。コード内のコメントを読んで、以下のコードのコンソール出力を確認してください。

## **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-PreserveSingleQuotePrefixOfCellValueOrRange.py" >}}

## **コンソール出力**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.quote_prefix is False, it means, do not update the value of Cell.Style.quote_prefix.

Similarly, when StyleFlag.quote_prefix is True, it means, update the value of Cell.Style.quote_prefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
