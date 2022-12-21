---
title: HTML からのインポート時に大きな数の指数表記を避ける
type: docs
weight: 10
url: /ja/net/avoid-exponential-notation-of-large-numbers-while-importing-from/
---
{{% alert color="primary" %}}

 Html に 1234567890123456 のような 15 桁を超える数字が含まれている場合があり、HTML を Excel ファイルにインポートすると、これらの数字は 1.23457E+15 のような指数表記に変換されます。必要に応じて、数値をそのままインポートし、指数表記に変換しないでください。[**HTMLLoadOptions.KeepPrecision**](https://reference.aspose.com/cells/net/aspose.cells/abstracttextloadoptions/properties/keepprecision)プロパティと設定**真実**HTMLのロード中。

{{% /alert %}}

次のサンプル コードは、[**HTMLLoadOptions.KeepPrecision**](https://reference.aspose.com/cells/net/aspose.cells/abstracttextloadoptions/properties/keepprecision)財産。 API は、指数表記に変換せずに数値をそのままインポートします。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AvoidExponentialNotationWhileImportingFromHtml-1.cs" >}}
