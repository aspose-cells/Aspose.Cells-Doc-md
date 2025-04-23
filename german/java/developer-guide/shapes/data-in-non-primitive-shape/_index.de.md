---
title: Daten in nicht primitiver Form
type: docs
weight: 500
url: /de/java/data-in-non-primitive-shape/
---

## **Zugriff auf Daten nicht-primitiver Form**

Manchmal müssen Sie auf Daten aus einer Form zugreifen, die nicht eingebaut ist. Eingebaute Formen werden primitive Formen genannt; solche, die es nicht sind, werden nicht-primitive genannt. Sie können beispielsweise eigene Formen mit verschiedenen verbundenen Kurvenlinien definieren.

## **Eine nicht-primitive Form**

In Aspose.Cells werden nicht-primitive Formen dem Typ [**AutoShapeType.NOT_PRIMITIVE**](https://reference.aspose.com/cells/java/com.aspose.cells/autoshapetype#NOT-PRIMITIVE) zugewiesen. Sie können ihren Typ mit der Methode [**Shape.getAutoShapeType()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#AutoShapeType) überprüfen.

Greifen Sie mit der Methode [**Shape.getPaths()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Paths) auf die Formdaten zu. Sie gibt alle verbundenen Pfade zurück, die die nicht-primitive Form bilden. Diese Pfade sind vom Typ ShapePath, der eine Liste aller Segmente enthält, die wiederum die Punkte in jedem Segment enthalten.

Der folgende Codeausschnitt zeigt die Verwendung der Methode [**Shape.getPaths()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Paths) zur Zugriff auf Pfadinformationen einer nicht-primitiven Form.

**Zeigt ein Beispiel für eine nicht-primitive Form** 

![todo:image_alt_text](data-in-non-primitive-shape_1.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-DrawingObjects-NonPrimitiveShape-1.java" >}}
{{< app/cells/assistant language="java" >}}
