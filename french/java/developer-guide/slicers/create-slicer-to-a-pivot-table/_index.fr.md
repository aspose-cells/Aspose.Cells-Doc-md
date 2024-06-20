---
title: Créer un segment de tarte à un tableau croisé dynamique
type: docs
weight: 10
url: /fr/java/create-slicer-to-a-pivot-table/
---

## **Scénarios d'utilisation possibles**
La trancheuse est utilisée pour filtrer rapidement les données. Elle peut être utilisée pour filtrer les données dans un tableau ou un tableau croisé dynamique. Microsoft Excel vous permet de créer une trancheuse en sélectionnant un tableau ou un tableau croisé dynamique, puis en cliquant sur *Insertion > Tranche*. Aspose.Cells vous permet également de créer une trancheuse en utilisant la méthode [Worksheet.getSlicers().add()](https://reference.aspose.com/cells/java/com.aspose.cells/slicercollection#add\(com.aspose.cells.PivotTable,%20int,%20int,%20com.aspose.cells.PivotField\)).
## **Créer un segmentateur pour un tableau croisé dynamique**
Veuillez consulter le code d'exemple suivant. Il charge le [fichier Excel d'exemple](67338498.xlsx) qui contient le tableau croisé dynamique. Ensuite, il crée la trancheuse en fonction du premier champ pivot. Enfin, il enregistre le classeur au format [XLSX de sortie](67338497.xlsx) et [XLSB de sortie](67338496.xlsb). La capture d'écran suivante montre la trancheuse créée par Aspose.Cells dans le fichier Excel de sortie.

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)
## **Code d'exemple**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-CreateSlicerToPivotTable.java" >}}
