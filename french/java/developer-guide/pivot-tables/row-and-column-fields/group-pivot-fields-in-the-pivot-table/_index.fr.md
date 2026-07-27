---
title: Regrouper les champs de tableau croisé dynamique dans le tableau croisé dynamique
type: docs
weight: 90
url: /fr/java/group-pivot-fields-in-the-pivot-table/
---

## **Scénarios d'utilisation possibles**

Microsoft Excel vous permet de regrouper les champs de tableau croisé dynamique. Lorsqu'une grande quantité de données est liée à un champ de tableau croisé dynamique, il est souvent utile de les regrouper en sections. Aspose.Cells offre également cette fonctionnalité en utilisant la méthode [**PivotTable.setManualGroupField()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#setManualGroupField-com.aspose.cells.PivotField-com.aspose.cells.DateTime-com.aspose.cells.DateTime-java.util.ArrayList-int-).

## **Grouper les champs du tableau croisé dynamique dans le tableau croisé dynamique**

Le code d'exemple suivant charge le [fichier Excel d'exemple](64716838.xlsx) et effectue un regroupement sur le premier champ de tableau croisé dynamique en utilisant la méthode [**PivotTable.setManualGroupField()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#setManualGroupField-com.aspose.cells.PivotField-com.aspose.cells.DateTime-com.aspose.cells.DateTime-java.util.ArrayList-int-). Ensuite, il actualise et calcule les données du tableau croisé dynamique et enregistre le classeur sous le nom de [fichier Excel de sortie](64716837.xlsx). La capture d'écran montre l'effet du code d'exemple sur le fichier Excel d'exemple. Comme vous pouvez le voir sur la capture d'écran, le premier champ de tableau croisé dynamique est maintenant regroupé par mois et trimestres.

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-GroupPivotFieldsInPivotTable.java" >}}
{{< app/cells/assistant language="java" >}}
