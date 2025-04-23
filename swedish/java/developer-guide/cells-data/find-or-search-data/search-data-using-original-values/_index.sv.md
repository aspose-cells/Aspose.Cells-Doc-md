---
title: Sök data med hjälp av ursprungliga värden
type: docs
weight: 540
url: /sv/java/search-data-using-original-values/
---

{{% alert color="primary" %}} 

Ibland är värdet av datan dolt eftersom det är formaterat på något sätt. Till exempel, anta att cell D4 har formeln =Sum(A1:A2) och dess värde är 20, men det är formaterat som ---, då är värdet 20 dolt och kan inte hittas med Microsoft Excel sökfunktioner. Men du kan hitta det med Aspose.Cells med [LookInType.ORIGINAL_VALUES](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#ORIGINAL-VALUES)

{{% /alert %}} 
## **Sök data med originalvärden**
Följande exempel visar hur detta fungerar. Det hittar cell D4 som inte kan hittas med Microsoft Excel sökfunktioner, men Aspose.Cells kan hitta det med [LookInType.ORIGINAL_VALUES](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#ORIGINAL-VALUES). Läs kommentarerna i koden för mer information.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.java" >}}
## **Konsoloutput**
Här är konsoloutputen från ovanstående exempelkod.

{{< highlight java >}}

 Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
