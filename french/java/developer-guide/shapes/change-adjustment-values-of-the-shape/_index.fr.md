---
title: Modifier les valeurs d'ajustement de la forme
type: docs
weight: 3200
url: /fr/java/change-adjustment-values-of-the-shape/
---
{{% alert color="primary" %}} 

 Aspose.Cells fournit[Forme.getGeometry().getShapeAdjustValues()](https://reference.aspose.com/cells/java/com.aspose.cells/geometry#ShapeAdjustValues) propriété pour apporter des modifications aux points de réglage avec des formes. Dans l'interface utilisateur Excel Microsoft, les ajustements s'affichent sous forme de nœuds en losange jaune. Par exemple:

- Le rectangle arrondi a un ajustement pour changer l'arc
- Triangle a un ajustement pour changer l'emplacement du point
- Un trapèze a un ajustement pour changer la largeur du haut
- Les flèches ont deux ajustements pour changer la forme de la tête et de la queue

 Cet article explique l'utilisation de[Forme.getGeometry().getShapeAdjustValues()](https://reference.aspose.com/cells/java/com.aspose.cells/geometry#ShapeAdjustValues) propriété pour modifier la valeur d'ajustement des différentes formes.

{{% /alert %}} 
## **Modifier les valeurs d'ajustement de la forme**
L'exemple de code suivant accède aux trois premières formes de la première feuille de calcul dans le fichier Excel source, puis modifie les valeurs d'ajustement des formes. Les captures d'écran ci-dessous montrent à quoi ressemblent les formes avant de modifier les valeurs de réglage, puis après la modification des valeurs de réglage.
### **Dessiner des formes avant de modifier les valeurs de réglage**
![tâche : image_autre_texte](change-adjustment-values-of-the-shape_1.png)
### **Dessiner des formes après avoir modifié les valeurs de réglage**
![tâche : image_autre_texte](change-adjustment-values-of-the-shape_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeAdjustmentValuesOfShape-ChangeAdjustmentValuesOfShape.java" >}}
