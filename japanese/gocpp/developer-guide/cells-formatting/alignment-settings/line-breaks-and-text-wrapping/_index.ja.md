---
title: Golangを使用してC++経由の改行とテキストの折り返し
description: Aspose.Cellsライブラリを使用して、C++でテキスト折り返しと語句折り返しを実装する方法。Aspose.Cellsライブラリを使用すると、セルにテキストを簡単に挿入でき、手動の語句折り返しや自動折り返しなどのテキスト折り返し方法を設定できます。これらの機能を実装する方法とサンプルコードを示します。
keywords: Aspose.Cells, 改行, テキストの折り返し, テキストレイアウト
type: docs
weight: 60
url: /ja/go-cpp/line-breaks-and-text-wrapping/
---

{{% alert color="primary" %}}

セル内のテキストが読み取れるようにするために、明示的な改行とテキストの折り返しを適用することができます。テキストの折り返しは、セル内の一行を複数行に変換し、明示的な改行は望む場所に改行を挿入します。

{{% /alert %}}

## **セル内でテキストを折り返す**

 セルのテキストを折り返すには、[**Aspose.Cells.Style.IsTextWrapped**](https://reference.aspose.com/cells/go-cpp/style/istextwrapped/) プロパティを使用します。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LineBreaksAndTextWrapping.go" >}}
## **明示的な改行を使用する**

 C++では、‘\n’を使用してセル内に明示的な改行を挿入できます。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LineBreaksAndTextWrapping-1.go" >}}
