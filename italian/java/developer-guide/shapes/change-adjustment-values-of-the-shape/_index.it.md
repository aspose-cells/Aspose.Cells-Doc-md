---
title: Modifica i valori di regolazione della forma
type: docs
weight: 3200
url: /it/java/change-adjustment-values-of-the-shape/
---

{{% alert color="primary" %}} 

Aspose.Cells fornisce la proprietà [Shape.getGeometry().getShapeAdjustValues()](https://reference.aspose.com/cells/java/com.aspose.cells/geometry#ShapeAdjustValues) per apportare modifiche ai punti di regolazione con le forme. Nell'interfaccia utente di Microsoft Excel, le modifiche vengono visualizzate come nodi diamanti gialli. Ad esempio:

- Il rettangolo arrotondato ha una regolazione per cambiare l'arco
- Il triangolo ha una regolazione per cambiare la posizione del punto
- Un trapezio ha un'ajustamento per cambiare la larghezza della parte superiore
- Le frecce hanno due ajustamenti per cambiare la forma della testa e della coda

Questo articolo spiegherà l'uso della proprietà [Shape.getGeometry().getShapeAdjustValues()](https://reference.aspose.com/cells/java/com.aspose.cells/geometry#ShapeAdjustValues) per cambiare il valore dell'ajustamento delle diverse forme.

{{% /alert %}} 
## **Modifica dei valori di regolazione della forma**
Il codice di esempio seguente accede alle prime tre forme del primo foglio di lavoro nel file di Excel di origine e quindi cambia i valori di ajustamento delle forme. Le schermate seguenti mostrano come appaiono le forme prima e dopo aver cambiato i valori di ajustamento.
### **Disegno delle Forme Prima del Cambiamento dei Valori di Ajustamento**
![todo:image_alt_text](change-adjustment-values-of-the-shape_1.png)
### **Disegno delle Forme Dopo il Cambiamento dei Valori di Ajustamento**
![todo:image_alt_text](change-adjustment-values-of-the-shape_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeAdjustmentValuesOfShape-ChangeAdjustmentValuesOfShape.java" >}}
{{< app/cells/assistant language="java" >}}
