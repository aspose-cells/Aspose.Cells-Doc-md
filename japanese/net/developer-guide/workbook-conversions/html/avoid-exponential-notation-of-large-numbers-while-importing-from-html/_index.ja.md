---
title: HTMLからの大きな数値の指数表記を避ける
type: docs
weight: 10
url: /ja/net/avoid-exponential-notation-of-large-numbers-while-importing-from/
---

{{% alert color="primary" %}}

HTMLには1.234567890123456といった15桁を超える数字が含まれており、HTMLをエクセルファイルにインポートすると、これらの数字が1.23457E+15のような指数表記に変換されてしまうことがあります。これらの数字を指数表記でなくそのままインポートしたい場合は、HTMLを読み込む際に[**HTMLLoadOptions.KeepPrecision**](https://reference.aspose.com/cells/net/aspose.cells/abstracttextloadoptions/properties/keepprecision)プロパティを**true** に設定してください。

{{% /alert %}}

次のサンプルコードは、[**HTMLLoadOptions.KeepPrecision**](https://reference.aspose.com/cells/net/aspose.cells/abstracttextloadoptions/properties/keepprecision)プロパティの使用方法を説明しています。APIは指数表記に変換することなく、この番号をそのままインポートします。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AvoidExponentialNotationWhileImportingFromHtml-1.cs" >}}
