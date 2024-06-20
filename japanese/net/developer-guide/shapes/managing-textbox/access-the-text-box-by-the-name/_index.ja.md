---
title: 名前でテキストボックスにアクセス
type: docs
weight: 230
url: /ja/net/access-the-text-box-by-the-name/
---

## 名前でテキストボックスにアクセスする

以前は、[**Worksheet.TextBoxes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/textboxes)コレクションからインデックスでテキストボックスにアクセスしていましたが、名前でこのコレクションからテキストボックスにアクセスすることもできるようになりました。これは、テキストボックスの名前をすでに知っている場合に便利で素早いアクセス方法です。

次のサンプルコードはまずテキストボックスを作成し、テキストと名前を割り当てます。次に、その名前で同じテキストボックスにアクセスし、そのテキストを出力します。

### 名前でテキストボックスにアクセスするためのC#コード

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AccessTextBoxName-AccessTextBoxName.cs" >}}

### サンプルコードによって生成されたコンソール出力

上記のサンプルコードのコンソール出力は次の通りです。

{{< highlight java >}}

This is MyTextBox

{{< /highlight >}}
