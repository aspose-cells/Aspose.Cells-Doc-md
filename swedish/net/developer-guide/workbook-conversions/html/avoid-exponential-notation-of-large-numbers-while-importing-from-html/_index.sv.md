---
title: Undvik exponentiell notation av stora siffror när du importerar från HTML
type: docs
weight: 10
url: /sv/net/avoid-exponential-notation-of-large-numbers-while-importing-from/
---
{{% alert color="primary" %}}

Ibland innehåller din HTML-kod siffror som 1234567890123456 som är längre än 15 siffror och när du importerar din HTML till Excel-fil, konverteras dessa till exponentiell notation som 1.23457E+15. Om du vill ska ditt nummer importeras som det är och inte konverteras till exponentiell notation, använd då[**HTMLLoadOptions.KeepPrecision**](https://reference.aspose.com/cells/net/aspose.cells/abstracttextloadoptions/properties/keepprecision) egendom och ställ in den**Sann** medan du laddar din HTML.

{{% /alert %}}

 Följande exempelkod förklarar användningen av[**HTMLLoadOptions.KeepPrecision**](https://reference.aspose.com/cells/net/aspose.cells/abstracttextloadoptions/properties/keepprecision)fast egendom. API:et importerar numret som det är utan att konvertera det till exponentiell notation.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AvoidExponentialNotationWhileImportingFromHtml-1.cs" >}}
