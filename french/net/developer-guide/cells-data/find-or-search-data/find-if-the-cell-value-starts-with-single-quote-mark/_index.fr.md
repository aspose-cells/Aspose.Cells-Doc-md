---
title: Rechercher si la valeur de la cellule commence par un guillemet simple
type: docs
weight: 270
url: /fr/net/find-if-the-cell-value-starts-with-single-quote-mark/
---
{{% alert color="primary" %}}

 Aspose.Cells fournit désormais le[**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) propriété pour déterminer si la valeur de la cellule commence par un guillemet simple. Avant cette propriété, il n'y avait aucun moyen de faire la distinction entre des chaînes comme sample et 'sample etc.

{{% /alert %}}

 L'exemple de code suivant explique que les chaînes telles que sample et 'sample ne peuvent pas être différenciées avec[**Cell.StringValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/stringvalue) propriété. Nous devons donc utiliser[**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix)propriété de les distinguer.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindIfCellValueStartsWithSingleQuote-FindIfCellValueStartsWithSingleQuote.cs" >}}
