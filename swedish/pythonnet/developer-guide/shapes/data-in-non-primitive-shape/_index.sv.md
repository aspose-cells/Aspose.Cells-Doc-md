---
title: data i icke primitiv form
type: docs
weight: 300
url: /sv/python-net/data-in-non-primitive-shape/
description: Denna artikel visar data i icke primära former genom Aspose.Cells för Python via .NET API.
keywords: Python Excel bibliotek, Python data i icke primär form, Python hur man får tillgång till data i icke primär form.
---

## **Åtkomst till data av icke-primitiv form**

Ibland behöver du få åtkomst till data från en form som inte är inbyggd. Inbyggda former kallas primitiva former; de som inte är det kallas icke-primitiva. Till exempel kan du definiera dina egna former med olika kurvanslutna linjer.

## **En icke-primitiv form**

I Aspose.Cells för Python via .NET tilldelas icke-primära former typen [**AutoShapeType.NOT_PRIMITIVE**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/autoshapetype). Du kan kontrollera deras typ med hjälp av [**Shape.auto_shape_type**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/auto_shape_type)-egenskapen.

Åtkomst till formdata med användning av egenskapen [**Shape.paths**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/paths). Den returnerar alla de anslutna vägarna som utgör den icke-primitiva formen. Dessa vägar är av typen [**ShapePath**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapepath) som håller en lista över alla segment som i sin tur innehåller punkterna i varje segment.

|**Visar ett exempel på en icke-primitiv form**|
| :- |
|![todo:image_alt_text](data-in-non-primitive-shape_1.jpg)|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-AccessNonPrimitiveShape-1.py" >}}
