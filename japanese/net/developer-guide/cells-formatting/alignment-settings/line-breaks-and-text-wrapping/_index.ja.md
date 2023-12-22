---
title: 改行とテキストの折り返し
description: C# の Aspose.Cells ライブラリを使用してテキストの折り返しとワードラップを実装する方法。Aspose.Cells ライブラリを使用すると、セルにテキストを簡単に挿入し、手動ワードラップやワードラップなどのテキスト折り返し方法を設定できます。このドキュメントでは、その方法について詳しく説明します。これらの機能を実装するためのサンプル コードを参照用に提供します。
keywords: Aspose.Cells, line breaks, text wraps, text layout
type: docs
weight: 60
url: /ja/net/line-breaks-and-text-wrapping/
---
{{% alert color="primary" %}}

セル内のテキストを確実に読めるようにするために、明示的な改行とテキストの折り返しを適用できます。テキストの折り返しにより、セル内の 1 行が複数の行に変わります。明示的な改行により、必要な位置に正確に改行が挿入されます。

{{% /alert %}}

##  **Cell でテキストを折り返すには**

セル内のテキストを折り返すには、[**Aspose.Cells.Style.IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped)財産。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-WrapText-1.cs" >}}

##  **明示的な改行を使用するには**

C# の「\n」および VB.NET の「vbLf」を使用して、セルに明示的な改行を挿入できます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-UseExplicitLineBreaks-1.cs" >}}
