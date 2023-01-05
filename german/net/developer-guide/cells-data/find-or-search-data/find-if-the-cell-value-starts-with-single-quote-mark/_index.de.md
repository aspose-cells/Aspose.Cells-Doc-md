---
title: Finden Sie heraus, ob der Zellenwert mit einem einfachen Anführungszeichen beginnt
type: docs
weight: 270
url: /de/net/find-if-the-cell-value-starts-with-single-quote-mark/
---
{{% alert color="primary" %}}

 Aspose.Cells bietet jetzt die[**Style.QuotePräfix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) -Eigenschaft, um festzustellen, ob der Zellenwert mit einem einfachen Anführungszeichen beginnt. Vor dieser Eigenschaft gab es keine Möglichkeit, zwischen Zeichenketten wie sample und 'sample etc.

{{% /alert %}}

Der folgende Beispielcode erklärt, dass die Zeichenfolgen wie sample und 'sample nicht mit unterschieden werden können[**Cell.StringValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/stringvalue) Eigentum. Deshalb müssen wir verwenden[**Style.QuotePräfix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix)Eigenschaft, sie zu unterscheiden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindIfCellValueStartsWithSingleQuote-FindIfCellValueStartsWithSingleQuote.cs" >}}
