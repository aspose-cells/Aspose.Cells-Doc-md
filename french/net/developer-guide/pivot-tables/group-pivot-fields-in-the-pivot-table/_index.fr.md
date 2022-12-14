---
title: Champs de groupe de pivot dans le tableau croisé dynamique
type: docs
weight: 80
url: /fr/net/group-pivot-fields-in-the-pivot-table/
---
## **Scénarios d'utilisation possibles**

Microsoft Excel vous permet de regrouper les champs croisés dynamiques du tableau croisé dynamique. Lorsqu'il y a une grande quantité de données liées à un champ pivot, il est souvent utile de les regrouper en sections. Aspose.Cells fournit également cette fonctionnalité en utilisant le[**Tableau croisé dynamique.SetManualGroupField()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/setmanualgroupfield/index)méthode.

## **Champs de groupe de pivot dans le tableau croisé dynamique**

 L'exemple de code suivant charge le[exemple de fichier Excel](64716818.xlsx) et effectue le regroupement sur le premier champ pivot à l'aide de la[**Tableau croisé dynamique.SetManualGroupField()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/setmanualgroupfield/index)méthode. Il actualise et calcule ensuite les données du tableau croisé dynamique et enregistre le classeur sous[fichier Excel de sortie](64716817.xlsx). La capture d'écran montre l'effet de l'exemple de code sur l'exemple de fichier Excel. Comme vous pouvez le voir sur la capture d'écran, le premier champ pivot est maintenant regroupé par mois et trimestres.

![tâche : image_autre_texte](group-pivot-fields-in-the-pivot-table_1.png)

## **Exemple de code**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-GroupPivotFieldsInPivotTable.cs" >}}
