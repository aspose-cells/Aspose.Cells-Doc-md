---
title: Ta reda på om cellvärdet börjar med citattecken
type: docs
weight: 610
url: /sv/java/find-if-the-cell-value-starts-with-single-quote-mark/
---

{{% alert color="primary" %}} 

Aspose.Cells tillhandahåller nu [Style.QuotePrefix](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) -egenskapen för att ta reda på om cellvärdet börjar med ett enda citattecken. Innan denna egenskap fanns det inget sätt att skilja mellan strängar som exempelvis sample och 'sample etc.

{{% /alert %}} 
## **Ta reda på om cellvärdet börjar med citattecken**
Följande exempelkod förklarar att strängarna som exempelvis sample och 'sample inte kan skiljas åt med hjälp av egenskapen [Cell.StringValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#StringValue). Därför måste vi använda egenskapen [Style.QuotePrefix](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) för att skilja dem åt.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Technical-Articles-DetectCellValueStartsWithSingleQuote.java" >}}
