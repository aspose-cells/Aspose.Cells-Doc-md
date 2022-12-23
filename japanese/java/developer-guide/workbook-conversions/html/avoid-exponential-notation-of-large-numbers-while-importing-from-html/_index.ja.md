---
title: HTML からインポートする際に、大きな数の指数表記を避ける
type: docs
weight: 600
url: /ja/java/avoid-exponential-notation-of-large-numbers-while-importing-from/
---
{{% alert color="primary" %}} 

HTML に 1234567890123456 のような 15 桁を超える数字が含まれている場合があり、HTML を Excel ファイルにインポートすると、これらの数字は 1.23457E+15 のような指数表記に変換されます。必要に応じて、数値をそのままインポートし、指数表記に変換しないでください。[HtmlLoadOptions.KeepPrecision](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#KeepPrecision)プロパティと設定**真実**HTML の読み込み中。

{{% /alert %}} 
## **HTML からインポートする際に、大きな数の指数表記を避ける**
次のサンプル コードは、[HtmlLoadOptions.KeepPrecision](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#KeepPrecision)財産。指数表記に変換せずに数値をそのままインポートします。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-KeepPrecisionOfLargeNumbers-1.java" >}}
