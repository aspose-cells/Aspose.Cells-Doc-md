---
title: Undvik exponentiell notation av stora siffror när du importerar från HTML
type: docs
weight: 600
url: /sv/java/avoid-exponential-notation-of-large-numbers-while-importing-from/
---
{{% alert color="primary" %}} 

Ibland innehåller din HTML siffror som 1234567890123456 som är längre än 15 siffror och när du importerar din HTML till Excel-fil konverteras dessa siffror till exponentiell notation som 1.23457E+15. Om du vill ska ditt nummer importeras som det är och inte konverteras till exponentiell notation, använd då[HtmlLoadOptions.KeepPrecision](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#KeepPrecision) egendom och ställ in den**Sann** medan du laddar din HTML.

{{% /alert %}} 
## **Undvik exponentiell notation av stora siffror när du importerar från HTML**
 Följande exempelkod förklarar användningen av[HtmlLoadOptions.KeepPrecision](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#KeepPrecision)fast egendom. Det kommer att importera numret som det är utan att konvertera det till exponentiell notation.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-KeepPrecisionOfLargeNumbers-1.java" >}}
