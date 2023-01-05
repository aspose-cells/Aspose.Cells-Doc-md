---
title: 組み込みスタイルの使用
type: docs
weight: 480
url: /ja/java/using-built-in-styles/
---
{{% alert color="primary" %}} 

Aspose.Cells は、スプレッドシート ドキュメントのセルを書式設定するための再利用可能なスタイルの膨大なコレクションを提供します。ワークブックで組み込みのスタイルを使用したり、カスタム スタイルを作成したりできます。

{{% /alert %}} 
## **組み込みスタイルの使用方法**
方法[Workbook.createBuiltinStyle](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#createBuiltinStyle\(int\) ) とクラス[BuiltinStyleType](https://reference.aspose.com/cells/java/com.aspose.cells/BuiltinStyleType)再利用可能なスタイルを作成するのに便利です。可能なすべての組み込みスタイルのリストを次に示します。

- [20_パーセント_ACCENT_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_1)
- [20_パーセント_ACCENT_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_2)
- [20_パーセント_ACCENT_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_3)
- [20_パーセント_ACCENT_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_4)
- [20_パーセント_ACCENT_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_5)
- [20_パーセント_ACCENT_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_6)
- [フォーティー_パーセント_ACCENT_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_1)
- [フォーティー_パーセント_ACCENT_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_2)
- [フォーティー_パーセント_ACCENT_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_3)
- [フォーティー_パーセント_ACCENT_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_4)
- [フォーティー_パーセント_ACCENT_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_5)
- [フォーティー_パーセント_ACCENT_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_6)
- [シックスティ_パーセント_ACCENT_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_1)
- [シックスティ_パーセント_ACCENT_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_2)
- [シックスティ_パーセント_ACCENT_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_3)
- [シックスティ_パーセント_ACCENT_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_4)
- [シックスティ_パーセント_ACCENT_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_5)
- [シックスティ_パーセント_ACCENT_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_6)
- [ACCENT_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_1)
- [ACCENT_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_2)
- [ACCENT_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_3)
- [ACCENT_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_4)
- [ACCENT_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_5)
- [ACCENT_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_6)
- [悪い](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#BAD)
- [計算](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CALCULATION)
- [CHECK_CELL](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CHECK_CELL)
- [コンマ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#COMMA)
- [COMMA_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#COMMA_1)
- [通貨](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CURRENCY)
- [CURRENCY_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CURRENCY_1)
- [EXPLANATORY_TEXT](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#EXPLANATORY_TEXT)
- [良い](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#GOOD)
- [HEADER_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER_1)
- [HEADER_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER_2)
- [HEADER_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER_3)
- [HEADER_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER_4)
- [ハイパーリンク](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HYPERLINK)
- [FOLLOWED_HYPERLINK](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FOLLOWED_HYPERLINK)
- [入力](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#INPUT)
- [LINKED_CELL](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#LINKED_CELL)
- [中性](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#NEUTRAL)
- [正常](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#NORMAL)
- [ノート](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#NOTE)
- [出力](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#OUTPUT)
- [パーセント](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#PERCENT)
- [題名](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TITLE)
- [合計](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TOTAL)
- [WARNING_TEXT](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#WARNING_TEXT)
- [ROW_LEVEL](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ROW_LEVEL)
- [COLUMN_LEVEL](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#COLUMN_LEVEL)

次のコードは、組み込みスタイルの使用方法を示しています。

![todo:画像_代替_文章](using-built-in-styles_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingBuiltinStyles-UsingBuiltinStyles.java" >}}
