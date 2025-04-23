---
title: Modifier les valeurs d ajustement de la forme.
type: docs
weight: 3200
url: /fr/java/change-adjustment-values-of-the-shape/
---

{{% alert color="primary" %}} 

Aspose.Cells fournit la propriété [Shape.getGeometry().getShapeAdjustValues()](https://reference.aspose.com/cells/java/com.aspose.cells/geometry#ShapeAdjustValues) pour apporter des modifications aux points d'ajustement avec les formes. Dans l'interface utilisateur de Microsoft Excel, les ajustements s'affichent sous forme de nœuds de diamant jaune. Par exemple :

- Le rectangle arrondi possède un ajustement pour changer l'arc.
- Le triangle a un ajustement pour changer l'emplacement du point.
- Un trapèze possède un ajustement pour changer la largeur du haut.
- Les flèches ont deux ajustements pour changer la forme de la tête et de la queue.

Cet article expliquera l'utilisation de la propriété [Shape.getGeometry().getShapeAdjustValues()](https://reference.aspose.com/cells/java/com.aspose.cells/geometry#ShapeAdjustValues) pour changer la valeur d'ajustement des différentes formes.

{{% /alert %}} 
## **Modifier les valeurs d'ajustement de la forme**
Le code d'échantillon suivant accède aux trois premières formes de la première feuille de calcul du fichier Excel source, puis modifie les valeurs d'ajustement des formes. Les captures d'écran ci-dessous montrent l'aspect des formes avant et après le changement des valeurs d'ajustement.
### **Dessin des formes avant le changement des valeurs d'ajustement**
![todo:image_alt_text](change-adjustment-values-of-the-shape_1.png)
### **Dessin des formes après le changement des valeurs d'ajustement**
![todo:image_alt_text](change-adjustment-values-of-the-shape_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeAdjustmentValuesOfShape-ChangeAdjustmentValuesOfShape.java" >}}
{{< app/cells/assistant language="java" >}}
