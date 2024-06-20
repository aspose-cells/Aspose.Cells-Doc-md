---
title: Ta reda på om cellvärdet börjar med citattecken
type: docs
weight: 270
url: /sv/net/find-if-the-cell-value-starts-with-single-quote-mark/
description: Lär dig hur man hittar om cellvärdet börjar med ett enkelt citattecken genom API Aspose.Cells for .NET.
keywords: Hitta cellvärde som börjar med ett enkelt citattecken, Sök cellvärde som börjar med ett enkelt citattecken
---

{{% alert color="primary" %}}

Aspose.Cells tillhandahåller nu egenskapen [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) för att hitta om cellvärdet börjar med ett enkelt citattecken. Innan denna egenskap fanns det inget sätt att skilja mellan strängar som exempelvis sample och 'sample osv.

{{% /alert %}}

Följande exempelkod förklarar att strängar som exempelvis sample och 'sample inte kan skiljas åt med egenskapen [**Cell.StringValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/stringvalue). Därför måste vi använda egenskapen [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) för att skilja dem åt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindIfCellValueStartsWithSingleQuote-FindIfCellValueStartsWithSingleQuote.cs" >}}
