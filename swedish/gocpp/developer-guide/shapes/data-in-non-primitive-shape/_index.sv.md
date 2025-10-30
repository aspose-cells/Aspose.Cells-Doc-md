---
title: Data i icke primär form med Golang via C++
linktitle: data i icke primitiv form
type: docs
weight: 300
url: /sv/go-cpp/data-in-non-primitive-shape/
description: Åtkomst och hantering av data i icke primära former med Aspose.Cells för Golang via C++.
---

## **Åtkomst till data av icke-primitiv form**

Ibland behöver du få åtkomst till data från en form som inte är inbyggd. Inbyggda former kallas primitiva former; de som inte är det kallas icke-primitiva. Till exempel kan du definiera dina egna former med olika kurvanslutna linjer.

## **En icke-primitiv form**

I Aspose.Cells tilldelas icke-primitiva former typen [**AutoShapeType.NotPrimitive**](https://reference.aspose.com/cells/go-cpp/autoshapetype/). Du kan kontrollera deras typ med hjälp av egenskapen [**Shape.AutoShapeType**](https://reference.aspose.com/cells/go-cpp/autoshapetype/).

Åtkomst till formdata med användning av egenskapen [**Shape.GetPaths()**](https://reference.aspose.com/cells/go-cpp/shape/getpaths/). Den returnerar alla de anslutna vägarna som utgör den icke-primitiva formen. Dessa vägar är av typen [**ShapePath**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapepath/) som håller en lista över alla segment som i sin tur innehåller punkterna i varje segment.

|**Visar ett exempel på en icke-primitiv form**|
| :- |
|![todo:image_alt_text](data-in-non-primitive-shape_1.jpg)|

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataInNonPrimitiveShape.go" >}}
