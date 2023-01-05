---
title: 改行とテキストの折り返し
type: docs
weight: 60
url: /ja/net/line-breaks-and-text-wrapping/
---
{{% alert color="primary" %}}

セル内のテキストを確実に読み取れるようにするために、明示的な改行とテキストの折り返しを適用できます。テキストの折り返しにより、セル内の 1 行が複数の行に変わり、明示的な改行によって、必要な場所に正確に改行が挿入されます。

{{% /alert %}}

## **テキストを Cell で折り返すには**

セル内でテキストを折り返すには、[**Aspose.Cells.Style.IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped)財産。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-WrapText-1.cs" >}}

## **明示的な改行を使用するには**

C# では '\n' を、VB.NET では ' vbLf' を使用して、セルに明示的な改行を挿入できます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-UseExplicitLineBreaks-1.cs" >}}
