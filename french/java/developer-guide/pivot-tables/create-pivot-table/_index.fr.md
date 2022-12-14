---
title: Créer un tableau croisé dynamique
type: docs
weight: 10
url: /fr/java/create-pivot-table/
---
## **Créer un tableau croisé dynamique**

### **Créer un tableau croisé dynamique à l'aide de Aspose.Cells**

{{% alert color="primary" %}}

 Avec Aspose.Cells, il est possible d'ajouter des tableaux croisés dynamiques aux feuilles de calcul. Aspose.Cells a un certain nombre de classes spéciales utilisées spécifiquement pour créer et contrôler des tableaux croisés dynamiques. Ces classes sont utilisées pour créer et définir les propriétés d'un[**Tableau croisé dynamique**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable)objet, utilisé comme blocs de construction du tableau croisé dynamique.

Les objets du tableau croisé dynamique sont :

- [**Champ Pivot**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField): il représente un champ dans un tableau croisé dynamique.
- [**PivotFieldCollectionPivotFieldCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection) : il représente une collection de tous les[**Champ Pivot**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField)objets dans le tableau croisé dynamique.
- [**Tableau croisé dynamique**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable): il représente un tableau croisé dynamique.
- [**Collection de tableaux croisés dynamiques**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection): il représente la collection de tous les objets de tableau croisé dynamique de la feuille de calcul.

{{% /alert %}}

### **Création d'un tableau croisé dynamique simple**

Pour créer un tableau croisé dynamique à l'aide du Aspose.Cells, veuillez suivre les étapes ci-dessous :

1.  Ajoutez des données aux cellules de la feuille de calcul à l'aide de la[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) objets[**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)méthode. Ces données seront utilisées comme source de données pour le tableau croisé dynamique.
1. Ajoutez un tableau croisé dynamique à la feuille de calcul en appelant le[**ajouter**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#add(com.aspose.cells.PivotTable,%20int,%20int,%20java.lang.String) ) méthode de la[**Collection de tableaux croisés dynamiques**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection) classe, encapsulée dans la[**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)objet.
1.  Accéder au[**Tableau croisé dynamique**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) objet de la[**Collection de tableaux croisés dynamiques**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection) en passant le[**Tableau croisé dynamique**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable)indice.
1.  Utilisez n'importe lequel des objets de tableau croisé dynamique (expliqués ci-dessus) encapsulés dans le[**Tableau croisé dynamique**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable)objet pour gérer le tableau croisé dynamique.

{{% alert color="primary" %}}

Lors de l'affectation d'une plage de cellules comme source de données, la plage doit être définie du haut à gauche au bas à droite. Par exemple, "A1:C3" est valide ; "C3:A1" n'est pas valide.

{{% /alert %}}

L'exemple de code ci-dessous montre comment créer un tableau croisé dynamique simple en suivant les étapes de base répertoriées ci-dessus. Lors de l'exécution du code, un tableau croisé dynamique est ajouté à la feuille de calcul :

**Créer un tableau croisé dynamique basé sur un champ correspondant**

![tâche : image_autre_texte](create-pivot-table_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-CreatePivotTable-CreatePivotTable.java" >}}
