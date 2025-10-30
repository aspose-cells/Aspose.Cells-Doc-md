---
title: Daten in Nicht Primitive Form mit Golang über C++
linktitle: Daten in nicht primitiver Form
type: docs
weight: 300
url: /de/go-cpp/data-in-non-primitive-shape/
description: Zugriff auf Daten in nicht primitiven Formen mit Aspose.Cells in Golang über C++
---

## **Zugriff auf Daten nicht-primitiver Form**

Manchmal müssen Sie auf Daten aus einer Form zugreifen, die nicht eingebaut ist. Eingebaute Formen werden primitive Formen genannt; solche, die es nicht sind, werden nicht-primitive genannt. Sie können beispielsweise eigene Formen mit verschiedenen verbundenen Kurvenlinien definieren.

## **Eine nicht-primitive Form**

In Aspose.Cells werden nicht-primitive Formen mit dem Typ [**AutoShapeType.NotPrimitive**](https://reference.aspose.com/cells/go-cpp/autoshapetype/) versehen. Sie können ihren Typ mithilfe der Eigenschaft [**Shape.AutoShapeType**](https://reference.aspose.com/cells/go-cpp/autoshapetype/) überprüfen.

Greifen Sie auf die Formdaten mithilfe der Eigenschaft [**Shape.GetPaths()**](https://reference.aspose.com/cells/go-cpp/shape/getpaths/) zu. Es gibt alle verbundenen Pfade zurück, die die nicht-primitive Form bilden. Diese Pfade sind vom Typ [**ShapePath**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapepath/), der eine Liste aller Segmente enthält, die wiederum die Punkte in jedem Segment enthalten.

|**Zeigt ein Beispiel für eine nicht-primitive Form**|
| :- |
|![todo:image_alt_text](data-in-non-primitive-shape_1.jpg)|

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataInNonPrimitiveShape.go" >}}
