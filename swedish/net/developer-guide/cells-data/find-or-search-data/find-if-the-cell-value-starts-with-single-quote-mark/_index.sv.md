---
title: Ta reda på om cellvärdet börjar med ett citattecken
type: docs
weight: 270
url: /sv/net/find-if-the-cell-value-starts-with-single-quote-mark/
---
{{% alert color="primary" %}}

 Aspose.Cells tillhandahåller nu[**Style.CitatPrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) egenskap för att hitta om cellvärdet börjar med ett enda citattecken. Innan den här egenskapen fanns det inget sätt att skilja mellan strängar som sample och 'sample etc.

{{% /alert %}}

Följande exempelkod förklarar att strängar som sample och 'sample inte kan särskiljas med[**Cell.StringValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/stringvalue) fast egendom. Därför måste vi använda[**Style.CitatPrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix)egendom för att särskilja dem.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindIfCellValueStartsWithSingleQuote-FindIfCellValueStartsWithSingleQuote.cs" >}}
