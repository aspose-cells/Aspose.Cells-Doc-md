---
title: Créer un tableau croisé dynamique
type: docs
weight: 10
url: /fr/java/create-pivot-table/
---

## **Créer un tableau croisé dynamique**

### **Créer une table pivot avec Aspose.Cells**

{{% alert color="primary" %}}

Avec Aspose.Cells, il est possible d'ajouter des tables pivot aux feuilles de calcul. Aspose.Cells dispose d'un certain nombre de classes spéciales utilisées spécifiquement pour créer et contrôler les tables pivot. Ces classes sont utilisées pour créer et définir les propriétés d'un objet [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable), utilisé comme les blocs de construction de la table pivot.

Les objets de table pivot sont :

- [**PivotField**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField) : il représente un champ dans une table pivot.
- [**PivotFieldCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection) : il représente une collection de tous les objets [**PivotField**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField) dans la table pivot.
- [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) : il représente une table pivot.
- [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection) : il représente la collection de tous les objets de table pivot sur la feuille de travail.

{{% /alert %}}

### **Créer une table pivot simple**

Pour créer une table pivot à l'aide d'Aspose.Cells, veuillez suivre les étapes ci-dessous :

1. Ajoutez des données aux cellules de la feuille de calcul en utilisant la méthode [**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value) de l'objet [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell). Ces données seront utilisées comme source de données pour la table pivot.
1. Ajoutez une table pivot à la feuille de calcul en appelant la méthode [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#add-com.aspose.cells.PivotTable-int-int-java.lang.String-) de la classe [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection), encapsulée dans l'objet [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet).
1. Accédez à l'objet [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) à partir de [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection) en passant l'index [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable).
1. Utilisez l'un quelconque des objets de table pivot (expliqués ci-dessus) encapsulés dans l'objet [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) pour gérer la table pivot.

{{% alert color="primary" %}}

Lors de l'attribution d'une plage de cellules comme source de données, la plage doit être définie du haut à gauche au bas à droite. Par exemple, "A1:C3" est valide ; "C3:A1" est invalide.

{{% /alert %}}

L'exemple de code ci-dessous montre comment créer une table pivot simple en suivant les étapes de base décrites ci-dessus. Lors de l'exécution du code, une table pivot est ajoutée à la feuille de calcul :

**Création d'un tableau croisé dynamique basé sur un champ correspondant**

![todo:image_alt_text](create-pivot-table_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-CreatePivotTable-CreatePivotTable.java" >}}
{{< app/cells/assistant language="java" >}}
