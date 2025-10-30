---
title: Golangを使ったC++経由でHTMLからのインポート時に大きな数値の指数表記を避ける
linktitle: HTMLからの大きな数値の指数表記を避ける
type: docs
weight: 10
url: /ja/go-cpp/avoid-exponential-notation-of-large-numbers-while-importing-from/
description: HTMLのインポート時に大きな数字の指数表記を避ける方法を、Aspose.Cells for C++を使用して学びます。
---

{{% alert color="primary" %}}

時折、HTMLに1234567890123456のような15桁以上の数字が含まれている場合、Excelにインポートするとこれらの数字は1.23457E+15のような指数表記に変換されます。数字をそのままインポートし、指数表記に変換したくない場合は、[**HTMLLoadOptions.GetKeepPrecision()**](https://reference.aspose.com/cells/go-cpp/abstracttextloadoptions/getkeepprecision/)プロパティを使用し、読み込み時に**true**に設定してください。

{{% /alert %}}

次のサンプルコードは、[**HTMLLoadOptions.GetKeepPrecision()**](https://reference.aspose.com/cells/go-cpp/abstracttextloadoptions/getkeepprecision/)プロパティの使い方を説明します。APIは数字を指数表記に変換せず、そのままインポートします。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AvoidExponentialNotationOfLargeNumbersWhileImportingFromHtml.go" >}}
