---
title: HTMLからの大きな数値の指数表記を避ける
type: docs
weight: 600
url: /ja/java/avoid-exponential-notation-of-large-numbers-while-importing-from/
---

{{% alert color="primary" %}} 

HTMLには 1234567890123456 のような15桁以上の長い数字が含まれることがあり、これらの数字をエクセルファイルにインポートすると、1.23457E+15 のように指数表記に変換されることがあります。もし、数値をそのままインポートし、指数表記に変換しないで欲しい場合は、HTMLをロードする際に[HtmlLoadOptions.KeepPrecision](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#KeepPrecision)プロパティを **true** に設定してください。

{{% /alert %}} 
## **HTMLからの大きな数値の指数表記を避ける**
次のサンプルコードは、[HtmlLoadOptions.KeepPrecision](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#KeepPrecision)プロパティの使用方法を説明しています。これにより、指数表記に変換せずに数値をインポートします。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-KeepPrecisionOfLargeNumbers-1.java" >}}
{{< app/cells/assistant language="java" >}}
