---
title: Créer un segment de tarte à un tableau croisé dynamique
type: docs
weight: 10
url: /fr/python-java/create-slicer-to-a-pivot-table/
---

## **Scénarios d'utilisation possibles**
Les segments de tarte sont utilisés pour filtrer rapidement les données. Ils peuvent être utilisés pour filtrer les données aussi bien dans un tableau que dans un tableau croisé dynamique. Microsoft Excel vous permet de créer un segment de tarte en sélectionnant un tableau ou un tableau croisé dynamique, puis en cliquant sur *Insertion > Segment de tarte*. Aspose.Cells pour Python via Java fournit la méthode Worksheet.getSlicers().add() pour créer un segment de tarte.
## **Créer un segmentateur pour un tableau croisé dynamique**
Le code suivant charge le *fichier Excel d'exemple*(106364966.xlsx) qui contient le tableau croisé dynamique. Il crée ensuite le segment de tarte en fonction du premier champ de base du tableau croisé dynamique. Enfin, il enregistre le classeur au format *XLSX de sortie*(106364967.xlsx). La capture d'écran suivante montre le segment de tarte créé par Aspose.Cells dans le fichier Excel de sortie.

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)
## **Code d'exemple**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Slicers-CreateSlicerToPivotTable.py" >}}
