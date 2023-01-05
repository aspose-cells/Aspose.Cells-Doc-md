---
title: Champs de groupe de pivot dans le tableau croisé dynamique
type: docs
weight: 90
url: /fr/java/group-pivot-fields-in-the-pivot-table/
---
## **Scénarios d'utilisation possibles**

Microsoft Excel vous permet de regrouper les champs croisés dynamiques du tableau croisé dynamique. Lorsqu'il y a une grande quantité de données relatives à un champ pivot, il est souvent utile de les regrouper en sections. Aspose.Cells fournit également cette fonctionnalité en utilisant le[**Tableau croisé dynamique.setManualGroupField()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#setManualGroupField(com.aspose.cells.PivotField,%20com.aspose.cells.DateTime,%20com.aspose.cells.DateTime,%20java.util.ArrayList,%20int)) méthode.

## **Champs de groupe de pivot dans le tableau croisé dynamique**

L'exemple de code suivant charge le[exemple de fichier Excel](64716838.xlsx)et effectue le regroupement sur le premier champ pivot à l'aide de la[**Tableau croisé dynamique.setManualGroupField()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#setManualGroupField(com.aspose.cells.PivotField,%20com.aspose.cells.DateTime,%20com.aspose.cells.DateTime,%20java.util.ArrayList,%20int)) méthode. Il actualise et calcule ensuite les données du tableau croisé dynamique et enregistre le classeur en tant que[fichier Excel de sortie](64716837.xlsx). La capture d'écran montre l'effet de l'exemple de code sur l'exemple de fichier Excel. Comme vous pouvez le voir sur la capture d'écran, le premier champ pivot est maintenant regroupé par mois et trimestres.

![tâche : image_autre_texte](group-pivot-fields-in-the-pivot-table_1.png)

## **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-GroupPivotFieldsInPivotTable.java" >}}
