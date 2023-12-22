---
title: Regrouper les champs croisés dynamiques dans le tableau croisé dynamique
type: docs
weight: 80
url: /fr/python-net/group-pivot-fields-in-the-pivot-table/
description: Comment regrouper les champs croisés dynamiques dans le tableau croisé dynamique avec Aspose.Cells for Python via .NET.
keywords: Group Pivot Fields in the Pivot Table.
---
##  **Scénarios d'utilisation possibles**

Microsoft Excel permet de regrouper les champs pivot du tableau croisé dynamique. Lorsqu’il existe une grande quantité de données liées à un champ pivot, il est souvent utile de les regrouper en sections. Aspose.Cells for Python via .NET fournit également cette fonctionnalité en utilisant le[**PivotTable.set_manual_group_field()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/set_manual_group_field/#int-float-float-list-float)méthode.

##  **Regrouper les champs croisés dynamiques dans le tableau croisé dynamique**

 L'exemple de code suivant charge le[exemple de fichier Excel](64716818.xlsx) et effectue un regroupement sur le premier champ pivot à l'aide du[**PivotTable.set_manual_group_field()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/set_manual_group_field/#int-float-float-list-float) méthode. Il actualise et calcule ensuite les données du tableau croisé dynamique et enregistre le classeur sous[sortie du fichier Excel](64716817.xlsx)La capture d'écran montre l'effet de l'exemple de code sur l'exemple de fichier Excel. Comme vous pouvez le voir sur la capture d'écran, le premier champ pivot est désormais regroupé par mois et trimestres.

![tâche : image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

##  **Exemple de code**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-GroupPivotFieldsInPivotTable.py" >}}
