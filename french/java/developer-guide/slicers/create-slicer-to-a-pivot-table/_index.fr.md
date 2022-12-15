---
title: Créer un segment dans un tableau croisé dynamique
type: docs
weight: 10
url: /fr/java/create-slicer-to-a-pivot-table/
---
## **Scénarios d'utilisation possibles**
Le slicer est utilisé pour filtrer rapidement les données. Il peut être utilisé pour filtrer les données à la fois dans un tableau ou un tableau croisé dynamique. Microsoft Excel vous permet de créer un segment en sélectionnant un tableau ou un tableau croisé dynamique, puis en cliquant sur le*Insertion > Trancheur*. Aspose.Cells vous permet également de créer une trancheuse à l'aide du[Feuille de calcul.getSlicers().add()](https://reference.aspose.com/cells/java/com.aspose.cells/slicercollection#add\(com.aspose.cells.PivotTable,%20int,%20int,%20com.aspose.cells.PivotField\)) méthode.
## **Créer un segment dans un tableau croisé dynamique**
Veuillez consulter l'exemple de code suivant. Il charge le[exemple de fichier Excel](67338498.xlsx)qui contient le tableau croisé dynamique. Il crée ensuite le segment en fonction du premier champ pivot de base. Enfin, il enregistre le classeur dans[sortie XLSX](67338497.xlsx)et[sortie XLSB](67338496.xlsb)format. La capture d'écran suivante montre le segment créé par Aspose.Cells dans le fichier Excel de sortie.

![tâche : image_autre_texte](create-slicer-to-a-pivot-table_1.png)
## **Exemple de code**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-CreateSlicerToPivotTable.java" >}}
