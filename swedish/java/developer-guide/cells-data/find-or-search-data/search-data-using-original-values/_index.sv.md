---
title: Sök efter data med originalvärden
type: docs
weight: 540
url: /sv/java/search-data-using-original-values/
---
{{% alert color="primary" %}} 

 Ibland döljs värdet av datan eftersom det är formaterat på något sätt. Anta till exempel att cell D4 har formeln =Sum(A1:A2) och dess värde är 20 men den är formaterad som ---, då är värdet 20 dolt och kan inte hittas med Microsoft Excel-sökalternativ. Du kan dock hitta den med Aspose.Cells med[LookInType.ORIGINAL_VALUES](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#ORIGINAL_VALUES)

{{% /alert %}} 
## **Sök efter data med originalvärden**
 Följande exempelkod illustrerar punkten ovan. Den hittar cell D4 som inte kan hittas med Microsoft Excel-sökalternativ men Aspose.Cells kan hitta den med[LookInType.ORIGINAL_VALUES](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#ORIGINAL_VALUES). Läs kommentarerna i koden för mer information.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.java" >}}
## **Konsolutgång**
Här är konsolutgången för ovanstående exempelkod.

{{< highlight "java" >}}

 Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]{{< /highlight >}}
