---
title: Modifica i valori di regolazione della forma
type: docs
weight: 3200
url: /it/java/change-adjustment-values-of-the-shape/
---
{{% alert color="primary" %}} 

 Aspose.Cells fornisce[Shape.getGeometry().getShapeAdjustValues()](https://reference.aspose.com/cells/java/com.aspose.cells/geometry#ShapeAdjustValues) proprietà per apportare modifiche ai punti di regolazione con le forme. Nell'interfaccia utente di Excel Microsoft, le regolazioni vengono visualizzate come nodi romboidali gialli. Per esempio:

- Rettangolo arrotondato ha una regolazione per cambiare l'arco
- Triangolo ha una regolazione per cambiare la posizione del punto
- Un trapezio ha una regolazione per modificare la larghezza della parte superiore
- Le frecce hanno due regolazioni per cambiare la forma della testa e della coda

 Questo articolo spiegherà l'uso di[Shape.getGeometry().getShapeAdjustValues()](https://reference.aspose.com/cells/java/com.aspose.cells/geometry#ShapeAdjustValues) proprietà per modificare il valore di regolazione delle diverse forme.

{{% /alert %}} 
## **Modifica i valori di regolazione della forma**
Il codice di esempio seguente accede alle prime tre forme del primo foglio di lavoro nel file Excel di origine e quindi modifica i valori di regolazione delle forme. Gli screenshot di seguito mostrano l'aspetto delle forme prima di modificare i valori di regolazione e quindi dopo aver modificato i valori di regolazione.
### **Disegno di forme prima di modificare i valori di regolazione**
![cose da fare:immagine_alt_testo](change-adjustment-values-of-the-shape_1.png)
### **Disegno di forme dopo aver modificato i valori di regolazione**
![cose da fare:immagine_alt_testo](change-adjustment-values-of-the-shape_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeAdjustmentValuesOfShape-ChangeAdjustmentValuesOfShape.java" >}}
