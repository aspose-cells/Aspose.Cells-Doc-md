---
title: Data i icke-primitiv form
type: docs
weight: 500
url: /sv/java/data-in-non-primitive-shape/
---
## **Åtkomst till data av icke-primitiv form**

Ibland behöver du komma åt data från en form som inte är inbyggd. Inbyggda former kallas primitiva former; de som inte är det kallas icke-primitiva. Du kan till exempel definiera dina egna former med hjälp av olika kurvanslutna linjer.

## **En icke-primitiv form**

 I Aspose.Cells tilldelas icke-primitiva former typen[**AutoShapeType.NOT_PRIMITIVE**](https://reference.aspose.com/cells/java/com.aspose.cells/autoshapetype#NOT_PRIMITIVE) . Du kan kontrollera deras typ med hjälp av[**Shape.getAutoShapeType()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#AutoShapeType)metod.

 Få åtkomst till formdata med hjälp av[**Shape.getPaths()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Paths)metod. Den returnerar alla anslutna banor som utgör den icke-primitiva formen. Dessa banor är av typen ShapePath som innehåller en lista över alla segment som i sin tur innehåller punkterna i varje segment.

Följande kodavsnitt visar användningen av[**Shape.getPaths()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Paths)metod för att komma åt väginformation av icke-primitiv form.

**Visar ett exempel på en icke-primitiv form** 

![todo:image_alt_text](data-in-non-primitive-shape_1.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-DrawingObjects-NonPrimitiveShape-1.java" >}}
