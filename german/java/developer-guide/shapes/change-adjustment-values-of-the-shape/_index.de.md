---
title: Anpassung von Formwerten ändern
type: docs
weight: 3200
url: /de/java/change-adjustment-values-of-the-shape/
---

{{% alert color="primary" %}} 

Aspose.Cells bietet die [Shape.getGeometry().getShapeAdjustValues()](https://reference.aspose.com/cells/java/com.aspose.cells/geometry#ShapeAdjustValues)-Eigenschaft, um Änderungen an den Anpassungspunkten mit Formen vorzunehmen. In der Microsoft Excel-Benutzeroberfläche werden Anpassungen als gelbe Diamantknoten angezeigt. Zum Beispiel:

- Das abgerundete Rechteck hat eine Anpassung, um den Bogen zu ändern
- Das Dreieck hat eine Anpassung, um die Position des Punktes zu ändern
- Ein Trapezoid hat eine Anpassung, um die Breite des oberen Teils zu ändern
- Pfeile haben zwei Anpassungen, um die Form des Kopfes und des Endes zu ändern

Dieser Artikel erläutert die Verwendung der [Shape.getGeometry().getShapeAdjustValues()](https://reference.aspose.com/cells/java/com.aspose.cells/geometry#ShapeAdjustValues)-Eigenschaft, um den Anpassungswert der verschiedenen Formen zu ändern.

{{% /alert %}} 
## **Ändern der Anpassungswerte der Form**
Der folgende Beispielcode greift auf die ersten drei Formen des ersten Arbeitsblatts in der Quelldatei Excel zu und ändert dann die Anpassungswerte der Formen. Unten sind Screenshots davon, wie die Formen vor und nach der Änderung der Anpassungswerte aussehen.
### **Zeichnen von Formen vor Änderung der Anpassungswerte**
![todo:image_alt_text](change-adjustment-values-of-the-shape_1.png)
### **Zeichnen von Formen nach Änderung der Anpassungswerte**
![todo:image_alt_text](change-adjustment-values-of-the-shape_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeAdjustmentValuesOfShape-ChangeAdjustmentValuesOfShape.java" >}}
