---
title: 名前でテキストボックスにアクセスする方法をGo言語とC++を経由して学ぶ
linktitle: 名前でテキストボックスにアクセス
type: docs
weight: 230
url: /ja/go-cpp/access-the-text-box-by-the-name/
description: Aspose.Cells for C++を使って名前でテキストボックスにアクセスする方法を学びます。
---

## 名前でテキストボックスにアクセスする

以前は、テキストボックスは[**Worksheet.GetTextBoxes()**](https://reference.aspose.com/cells/go-cpp/worksheet/gettextboxes/)コレクションのインデックスでアクセスされていましたが、現在はこのコレクションから名前でアクセスすることもできます。これは、名前をすでに知っている場合に便利で迅速な方法です。

以下のサンプルコードは、最初にテキストボックスを作成し、いくつかのテキストと名前を割り当て、その後、同じ名前のテキストボックスにアクセスしてテキストを印刷します。

### C++で名前によるテキストボックスへのアクセス方法

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AccessTheTextBoxByTheName.go" >}}
### サンプルコードによって生成されたコンソール出力

上記のサンプルコードのコンソール出力は次の通りです。

{{< highlight java >}}

This is MyTextBox

{{< /highlight >}}
