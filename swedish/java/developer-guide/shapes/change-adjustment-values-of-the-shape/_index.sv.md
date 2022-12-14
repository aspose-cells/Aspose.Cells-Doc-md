---
title: Ändra justeringsvärden för formen
type: docs
weight: 3200
url: /sv/java/change-adjustment-values-of-the-shape/
---
{{% alert color="primary" %}} 

 Aspose.Cells tillhandahåller[Shape.getGeometry().getShapeAdjustValues()](https://reference.aspose.com/cells/java/com.aspose.cells/geometry#ShapeAdjustValues) egenskap för att göra ändringar i justeringspunkterna med former. I Microsoft Excel-gränssnittet visas justeringar som gula diamantnoder. Till exempel:

- Rundad rektangel har en justering för att ändra bågen
- Triangeln har en justering för att ändra platsen för punkten
- En trapets har en justering för att ändra bredden på toppen
- Pilarna har två justeringar för att ändra formen på huvudet och svansen

 Den här artikeln kommer att förklara användningen av[Shape.getGeometry().getShapeAdjustValues()](https://reference.aspose.com/cells/java/com.aspose.cells/geometry#ShapeAdjustValues) egenskap för att ändra justeringsvärdet för de olika formerna.

{{% /alert %}} 
## **Ändra justeringsvärden för formen**
Följande exempelkod får åtkomst till de tre första formerna av det första kalkylbladet i källexcelfilen och ändrar sedan formernas justeringsvärden. Skärmbilderna nedan visar hur formerna ser ut innan du ändrar justeringsvärden och sedan efter att justeringsvärden ändrats.
### **Rita former innan du ändrar justeringsvärden**
![todo:image_alt_text](change-adjustment-values-of-the-shape_1.png)
### **Rita former efter att ha ändrat justeringsvärden**
![todo:image_alt_text](change-adjustment-values-of-the-shape_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeAdjustmentValuesOfShape-ChangeAdjustmentValuesOfShape.java" >}}
