---
title: Найдите, начинается ли значение ячейки с одинарной кавычки
type: docs
weight: 270
url: /ru/net/find-if-the-cell-value-starts-with-single-quote-mark/
---
{{% alert color="primary" %}}

 Aspose.Cells теперь предоставляет[**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) свойство, чтобы определить, начинается ли значение ячейки с одинарной кавычки. До этого свойства не было способа различить такие строки, как образец, 'образец и т. д.

{{% /alert %}}

 В следующем примере кода поясняется, что такие строки, как sample и 'sample, нельзя различить с помощью[**Cell.StringValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/stringvalue) имущество. Поэтому мы должны использовать[**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix)свойство различать их.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindIfCellValueStartsWithSingleQuote-FindIfCellValueStartsWithSingleQuote.cs" >}}
