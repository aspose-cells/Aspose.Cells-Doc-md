---
title: Daten in nicht primitiver Form
type: docs
weight: 300
url: /de/python-net/data-in-non-primitive-shape/
description: Dieser Artikel zeigt Daten in Nicht Primitiven Formen durch die Aspose.Cells für Python via .NET API.
keywords: Python Excel Bibliothek, Python Daten in Nicht Primitiven Formen, Python wie man auf Daten in Nicht Primitiven Formen zugreift.
---

## **Zugriff auf Daten nicht-primitiver Form**

Manchmal müssen Sie auf Daten aus einer Form zugreifen, die nicht eingebaut ist. Eingebaute Formen werden primitive Formen genannt; solche, die es nicht sind, werden nicht-primitive genannt. Sie können beispielsweise eigene Formen mit verschiedenen verbundenen Kurvenlinien definieren.

## **Eine nicht-primitive Form**

In Aspose.Cells für Python via .NET werden nicht-primitiven Formen der [**AutoShapeType.NOT_PRIMITIVE**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/autoshapetype) Typ zugewiesen. Sie können ihren Typ mit der [**Shape.auto_shape_type**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/auto_shape_type) Eigenschaft überprüfen.

Greifen Sie auf die Formdaten mithilfe der Eigenschaft [**Shape.paths**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/paths) zu. Es gibt alle verbundenen Pfade zurück, die die nicht-primitive Form bilden. Diese Pfade sind vom Typ [**ShapePath**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapepath), der eine Liste aller Segmente enthält, die wiederum die Punkte in jedem Segment enthalten.

|**Zeigt ein Beispiel für eine nicht-primitive Form**|
| :- |
|![todo:image_alt_text](data-in-non-primitive-shape_1.jpg)|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-AccessNonPrimitiveShape-1.py" >}}
