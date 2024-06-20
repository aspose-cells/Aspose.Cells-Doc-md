---
title: Sök data med hjälp av ursprungliga värden
type: docs
weight: 540
url: /sv/java/search-data-using-original-values/
---

{{% alert color="primary" %}} 

Ibland är datavärdet dolt eftersom det är formaterat på något sätt. Till exempel, anta att cell D4 har formeln =Sum(A1:A2) och dess värde är 20, men det är formaterat som ---, då är värdet 20 dolt och kan inte hittas med hjälp av Microsoft Excels sökalternativ. Du kan dock hitta det med Aspose.Cells genom att använda [LookInType.ORIGINAL_VALUES](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#ORIGINAL_VALUES).

{{% /alert %}} 
## **Sök data med originalvärden**
Följande exemplarkod illustrerar ovanstående punkt. Den hittar cell D4 vilken inte kan hittas med Microsoft Excels sökalternativ men Aspose.Cells kan hitta den med [LookInType.ORIGINAL_VALUES](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#ORIGINAL_VALUES). Läs gärna kommentarerna i koden för mer information.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.java" >}}
## **Konsoloutput**
Här är konsoloutputen från ovanstående exempelkod.

{{< highlight java >}}

 Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}
