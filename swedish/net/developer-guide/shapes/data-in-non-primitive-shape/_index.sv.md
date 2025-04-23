---
title: data i icke primitiv form
type: docs
weight: 300
url: /sv/net/data-in-non-primitive-shape/
---

## **Åtkomst till data av icke-primitiv form**

Ibland behöver du få åtkomst till data från en form som inte är inbyggd. Inbyggda former kallas primitiva former; de som inte är det kallas icke-primitiva. Till exempel kan du definiera dina egna former med olika kurvanslutna linjer.

## **En icke-primitiv form**

I Aspose.Cells tilldelas icke-primitiva former typen [**AutoShapeType.NotPrimitive**](https://reference.aspose.com/cells/net/aspose.cells.drawing/autoshapetype). Du kan kontrollera deras typ med hjälp av egenskapen [**Shape.AutoShapeType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/autoshapetype).

Åtkomst till formdata med användning av egenskapen [**Shape.Paths**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/paths). Den returnerar alla de anslutna vägarna som utgör den icke-primitiva formen. Dessa vägar är av typen [**ShapePath**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapepath) som håller en lista över alla segment som i sin tur innehåller punkterna i varje segment.

|**Visar ett exempel på en icke-primitiv form**|
| :- |
|![todo:image_alt_text](data-in-non-primitive-shape_1.jpg)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-AccessNonPrimitiveShape-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
