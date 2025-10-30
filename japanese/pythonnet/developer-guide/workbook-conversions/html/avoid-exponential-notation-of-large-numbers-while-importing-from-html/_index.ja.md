---
title: HTMLからの大きな数値の指数表記を避ける
type: docs
weight: 10
url: /ja/python-net/avoid-exponential-notation-of-large-numbers-while-importing-from/
description: Aspose.Cells for Python via NETを使用して、HTMLからのインポート時に大きな数値の指数表記を回避する方法を示しています。
keywords: HTMLからのインポート時に大きな数値の指数表記を回避し、精度を保持する。
---

{{% alert color="primary" %}}

HTMLには1.234567890123456といった15桁を超える数字が含まれており、HTMLをエクセルファイルにインポートすると、これらの数字が1.23457E+15のような指数表記に変換されてしまうことがあります。これらの数字を指数表記でなくそのままインポートしたい場合は、HTMLを読み込む際に[**HTMLLoadOptions.keep_precision**](https://reference.aspose.com/cells/python-net/aspose.cells/abstracttextloadoptions/keep_precision/)プロパティを**true** に設定してください。

{{% /alert %}}

次のサンプルコードは、[**HTMLLoadOptions.keep_precision**](https://reference.aspose.com/cells/python-net/aspose.cells/abstracttextloadoptions/keep_precision/)プロパティの使用方法を説明しています。APIは指数表記に変換することなく、この番号をそのままインポートします。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-AvoidExponentialNotationWhileImportingFromHtml-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
