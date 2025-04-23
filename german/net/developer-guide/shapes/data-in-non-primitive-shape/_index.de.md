---
title: Daten in nicht primitiver Form
type: docs
weight: 300
url: /de/net/data-in-non-primitive-shape/
---

## **Zugriff auf Daten nicht-primitiver Form**

Manchmal müssen Sie auf Daten aus einer Form zugreifen, die nicht eingebaut ist. Eingebaute Formen werden primitive Formen genannt; solche, die es nicht sind, werden nicht-primitive genannt. Sie können beispielsweise eigene Formen mit verschiedenen verbundenen Kurvenlinien definieren.

## **Eine nicht-primitive Form**

In Aspose.Cells werden nicht-primitive Formen mit dem Typ [**AutoShapeType.NotPrimitive**](https://reference.aspose.com/cells/net/aspose.cells.drawing/autoshapetype) versehen. Sie können ihren Typ mithilfe der Eigenschaft [**Shape.AutoShapeType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/autoshapetype) überprüfen.

Greifen Sie auf die Formdaten mithilfe der Eigenschaft [**Shape.Paths**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/paths) zu. Es gibt alle verbundenen Pfade zurück, die die nicht-primitive Form bilden. Diese Pfade sind vom Typ [**ShapePath**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapepath), der eine Liste aller Segmente enthält, die wiederum die Punkte in jedem Segment enthalten.

|**Zeigt ein Beispiel für eine nicht-primitive Form**|
| :- |
|![todo:image_alt_text](data-in-non-primitive-shape_1.jpg)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-AccessNonPrimitiveShape-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
