---
title: Daten in nicht primitiver Form
type: docs
weight: 500
url: /de/java/data-in-non-primitive-shape/
---
## **Zugreifen auf Daten nicht-primitiver Form**

Manchmal müssen Sie auf Daten aus einem Shape zugreifen, das nicht integriert ist. Eingebaute Formen werden primitive Formen genannt; diejenigen, die es nicht sind, werden als nicht-primitiv bezeichnet. Beispielsweise können Sie Ihre eigenen Formen definieren, indem Sie verschiedene Kurven verbundene Linien verwenden.

## **Eine nicht primitive Form**

 In Aspose.Cells wird nicht primitiven Formen der Typ zugewiesen[**AutoShapeType.NOT_PRIMITIVE**](https://reference.aspose.com/cells/java/com.aspose.cells/autoshapetype#NOT_PRIMITIVE) . Sie können ihren Typ mit überprüfen[**Shape.getAutoShapeType()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#AutoShapeType)Methode.

 Greifen Sie mit dem auf die Formdaten zu[**Shape.getPaths()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Paths)Methode. Es gibt alle verbundenen Pfade zurück, die die nicht primitive Form umfassen. Diese Pfade sind vom Typ ShapePath, der eine Liste aller Segmente enthält, die wiederum die Punkte in jedem Segment enthalten.

Das folgende Code-Snippet demonstriert die Verwendung von[**Shape.getPaths()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Paths)Methode zum Zugreifen auf Pfadinformationen von nicht-primitiver Form.

**Zeigt ein Beispiel einer nicht primitiven Form** 

![todo: Bild_alt_Text](data-in-non-primitive-shape_1.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-DrawingObjects-NonPrimitiveShape-1.java" >}}
