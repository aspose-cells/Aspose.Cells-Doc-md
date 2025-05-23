---
title: Regrouper les champs de tableau croisé dynamique dans le tableau croisé dynamique
type: docs
weight: 80
url: /fr/net/group-pivot-fields-in-the-pivot-table/
---

## **Scénarios d'utilisation possibles**

Microsoft Excel vous permet de regrouper les champs de tableau croisé dynamique. Lorsqu'il y a une grande quantité de données liées à un champ de tableau croisé dynamique, il est souvent utile de les regrouper en sections. Aspose.Cells fournit également cette fonctionnalité en utilisant la méthode [**PivotTable.GroupBy()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield/groupby/).

## **Grouper les champs du tableau croisé dynamique dans le tableau croisé dynamique**

Le code d'exemple suivant charge le [fichier Excel d'exemple](64716818.xlsx) et effectue un groupement sur le premier champ de tableau croisé dynamique en utilisant la méthode [**PivotTable.GroupBy()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield/groupby/). Ensuite, il actualise et calcule les données du tableau croisé dynamique et enregistre le classeur sous le nom de [fichier Excel de sortie](64716817.xlsx). La capture d'écran montre l'effet du code d'exemple sur le fichier Excel d'exemple. Comme vous pouvez le voir sur la capture d'écran, le premier champ de tableau croisé dynamique est maintenant regroupé par mois et par trimestres.

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-GroupPivotFieldsInPivotTable.cs" >}}
{{< app/cells/assistant language="csharp" >}}
