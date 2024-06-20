---
title: 改行とテキストの折り返し
description: Aspose.Cellsライブラリを使用して、C#でテキストの折り返しとワードラップを実装する方法について説明します。Aspose.Cellsライブラリを使用すると、セルにテキストを簡単に挿入し、手動でのワードラップ、ワードラップなどのテキストの折り返し方法を設定できます。このドキュメントでは、これらの機能の実装方法について詳しく説明し、参照用のサンプルコードを提供します。
keywords: Aspose.Cells, 改行, テキストの折り返し, テキストレイアウト
type: docs
weight: 60
url: /ja/net/line-breaks-and-text-wrapping/
---

{{% alert color="primary" %}}

セル内のテキストが読み取れるようにするために、明示的な改行とテキストの折り返しを適用することができます。テキストの折り返しは、セル内の一行を複数行に変換し、明示的な改行は望む場所に改行を挿入します。

{{% /alert %}}

## **セル内でテキストを折り返す**

セル内でテキストを折り返すには、[**Aspose.Cells.Style.IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped)プロパティを使用します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-WrapText-1.cs" >}}

## **明示的な改行を使用する**

C#では、セル内に明示的な改行を挿入するために、「\n」、VB.NETでは「vbLf」を使用できます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-UseExplicitLineBreaks-1.cs" >}}
