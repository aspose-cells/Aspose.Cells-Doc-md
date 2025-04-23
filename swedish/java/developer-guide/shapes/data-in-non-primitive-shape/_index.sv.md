---
title: data i icke primitiv form
type: docs
weight: 500
url: /sv/java/data-in-non-primitive-shape/
---

## **Åtkomst till data av icke-primitiv form**

Ibland behöver du få åtkomst till data från en form som inte är inbyggd. Inbyggda former kallas primitiva former; de som inte är det kallas icke-primitiva. Till exempel kan du definiera dina egna former med olika kurvanslutna linjer.

## **En icke-primitiv form**

I Aspose.Cells är icke-primitiva former tilldelade typ [**AutoShapeType.NOT_PRIMITIVE**](https://reference.aspose.com/cells/java/com.aspose.cells/autoshapetype#NOT-PRIMITIVE). Du kan kontrollera deras typ med hjälp av metoden [**Shape.getAutoShapeType()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#AutoShapeType).

Få tillgång till formdata med hjälp av metoden [**Shape.getPaths()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Paths). Den returnerar alla anslutna banor som utgör den icke-primitiva formen. Dessa banor är av typen ShapePath som innehåller en lista över alla segment som i sin tur innehåller punkterna i varje segment.

Följande kodsnutt visar användningen av metoden [**Shape.getPaths()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Paths) för att få tillgång till baninformation för icke-primitiv form.

**Visar ett exempel på en icke-primitiv form** 

![todo:image_alt_text](data-in-non-primitive-shape_1.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-DrawingObjects-NonPrimitiveShape-1.java" >}}
{{< app/cells/assistant language="java" >}}
