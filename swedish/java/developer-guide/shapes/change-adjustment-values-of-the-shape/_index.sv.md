---
title: Ändra justeringsvärden för formen
type: docs
weight: 3200
url: /sv/java/change-adjustment-values-of-the-shape/
---

{{% alert color="primary" %}} 

Aspose.Cells tillhandahåller egenskapen [Shape.getGeometry().getShapeAdjustValues()](https://reference.aspose.com/cells/java/com.aspose.cells/geometry#ShapeAdjustValues) för att göra ändringar i justeringspunkterna med former. I Microsoft Excel visas justeringar som gula diamantnoder. Till exempel:

- Avrundad rektangel har en justering för att ändra buen
- Triangel har en justering för att ändra platsen för punkten
- En parallellogram har en justering för att ändra bredden på toppen
- Pilar har två justeringar för att ändra formen på huvudet och svansen

Den här artikeln kommer att förklara användningen av [Shape.getGeometry().getShapeAdjustValues()](https://reference.aspose.com/cells/java/com.aspose.cells/geometry#ShapeAdjustValues)egenskapen för att ändra justeringsvärdet för olika former.

{{% /alert %}} 
## **Ändra justeringsvärden för formen**
Följande exempelkod får åtkomst till de tre första formerna i den första kalkylbladet i källan excelfilen och ändrar sedan justeringsvärdena för formerna. Nedan visas skärmbilder på hur formerna ser ut innan ändring av justeringsvärden och sedan efter ändring av justeringsvärden.
### **Rita former innan ändring av justeringsvärden**
![todo:image_alt_text](change-adjustment-values-of-the-shape_1.png)
### **Rita former efter ändring av justeringsvärden**
![todo:image_alt_text](change-adjustment-values-of-the-shape_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeAdjustmentValuesOfShape-ChangeAdjustmentValuesOfShape.java" >}}
{{< app/cells/assistant language="java" >}}
