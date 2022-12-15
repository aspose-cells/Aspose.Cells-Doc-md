---
title: Créer un segment dans un tableau croisé dynamique
type: docs
weight: 10
url: /fr/python-java/create-slicer-to-a-pivot-table/
---
## **Scénarios d'utilisation possibles**
Les segments sont utilisés pour filtrer rapidement les données. Ils peuvent être utilisés pour filtrer les données à la fois dans un tableau ou un tableau croisé dynamique. Microsoft Excel vous permet de créer un segment en sélectionnant un tableau ou un tableau croisé dynamique, puis en cliquant sur le*Insertion > Trancheur*. Aspose.Cells for Python via Java fournit la méthode Worksheet.getSlicers().add() pour créer un slicer.
## **Créer un segment dans un tableau croisé dynamique**
L'extrait de code suivant charge le[exemple de fichier Excel](106364966.xlsx)qui contient le tableau croisé dynamique. Il crée ensuite le segment en fonction du premier champ pivot de base. Enfin, il enregistre le classeur dans[sortie XLSX](106364967.xlsx)format. La capture d'écran suivante montre le segment créé par Aspose.Cells dans le fichier Excel de sortie.

![tâche : image_autre_texte](create-slicer-to-a-pivot-table_1.png)
## **Exemple de code**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Slicers-CreateSlicerToPivotTable.py" >}}
