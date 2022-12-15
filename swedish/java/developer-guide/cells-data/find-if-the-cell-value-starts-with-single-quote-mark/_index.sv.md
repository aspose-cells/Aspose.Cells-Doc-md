---
title: Ta reda på om cellvärdet börjar med ett citattecken
type: docs
weight: 610
url: /sv/java/find-if-the-cell-value-starts-with-single-quote-mark/
---
{{% alert color="primary" %}} 

 Aspose.Cells tillhandahåller nu[Style.CitatPrefix](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) egenskap för att hitta om cellvärdet börjar med ett enda citattecken. Innan den här egenskapen fanns det inget sätt att skilja mellan strängar som sample och 'sample etc.

{{% /alert %}} 
## **Ta reda på om cellvärdet börjar med ett citattecken**
Följande exempelkod förklarar att strängar som sample och 'sample inte kan särskiljas med[Cell.StringValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#StringValue) fast egendom. Därför måste vi använda[Style.CitatPrefix](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix)egendom för att särskilja dem.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Technical-Articles-DetectCellValueStartsWithSingleQuote.java" >}}
