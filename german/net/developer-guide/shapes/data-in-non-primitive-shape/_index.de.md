---
title: Daten in nicht primitiver Form
type: docs
weight: 300
url: /de/net/data-in-non-primitive-shape/
---
## **Zugreifen auf Daten nicht-primitiver Form**

Manchmal müssen Sie auf Daten aus einem Shape zugreifen, das nicht integriert ist. Eingebaute Formen werden primitive Formen genannt; diejenigen, die es nicht sind, werden als nicht-primitiv bezeichnet. Beispielsweise können Sie Ihre eigenen Formen definieren, indem Sie verschiedene Kurven verbundene Linien verwenden.

## **Eine nicht primitive Form**

In Aspose.Cells wird nicht primitiven Formen der Typ zugewiesen[**AutoShapeType.NotPrimitive**](https://reference.aspose.com/cells/net/aspose.cells.drawing/autoshapetype) . Sie können ihren Typ mit überprüfen[**Shape.AutoShapeType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/autoshapetype)Eigentum.

 Greifen Sie mit dem auf die Formdaten zu[**Form.Pfade**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/paths)Eigentum. Es gibt alle verbundenen Pfade zurück, die die nicht primitive Form umfassen. Diese Pfade sind vom Typ[**ShapePath**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapepath)die eine Liste aller Segmente enthält, die wiederum die Punkte in jedem Segment enthalten.

|**Zeigt ein Beispiel einer nicht primitiven Form**|
|:- |
|![todo: Bild_alt_Text](data-in-non-primitive-shape_1.jpg)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-AccessNonPrimitiveShape-1.cs" >}}
