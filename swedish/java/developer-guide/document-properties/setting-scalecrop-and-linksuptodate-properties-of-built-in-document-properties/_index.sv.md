---
title: Ställa in egenskaperna ScaleCrop och LinksUpToDate för inbyggda dokumentegenskaper
type: docs
weight: 1050
url: /sv/java/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
---
## **Möjliga användningsscenarier**
[ScaleCrop](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#ScaleCrop) och[LinksUpToDate](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#LinksUpToDate)är två utökade inbyggda dokumentegenskaper definierade i OpenXml-formatet. Syftet med dessa egenskaper är följande
## **1) ScaleCrop**
 Detta element indikerar visningsläget för dokumentminiatyren. Ställ in detta element på**Sann**för att möjliggöra skalning av dokumentets miniatyrbild till displayen. Ställ in detta element på**falsk** för att möjliggöra beskärning av dokumentminiatyren för att endast visa avsnitt som passar skärmen.

De möjliga värdena för detta element definieras av den booleska datatypen W3C XML Schema.
## **2) LinksUpToDate**
 Detta element indikerar om hyperlänkar i ett dokument är uppdaterade. Ställ in detta element på**Sann** för att indikera att hyperlänkar är uppdaterade. Ställ in detta element på**falsk**för att indikera att hyperlänkar är föråldrade.

De möjliga värdena för detta element definieras av den booleska datatypen W3C XML Schema.
## **Skärmdump som visar dessa egenskaper i app.xml-filen**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)
## **Ställa in egenskaperna ScaleCrop och LinksUpToDate för inbyggda dokumentegenskaper**
 Följande exempelkod ställer in[ScaleCrop](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#ScaleCrop)och[LinksUpToDate](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#LinksUpToDate) utökade inbyggda dokumentegenskaper i arbetsboken. Vänligen kontrollera[output excel-fil](5472494.xlsx) som genereras med den här koden, ändra dess tillägg till .zip och extrahera dess innehåll och visa aap.xml som visas i skärmdumpen ovan.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingScaleCropLinksUpToDate-SettingScaleCropLinksUpToDate.java" >}}
