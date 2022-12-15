---
title: Insérer un trancheur
linktitle: Trancheuses
type: docs
weight: 170
url: /fr/net/create-slicer/
description: Gérez les slicers de fichiers Excel avec le Aspose.Cells.
---
## **Scénarios d'utilisation possibles**

 Un segment est utilisé pour filtrer rapidement les données. Il peut être utilisé pour filtrer les données à la fois dans un tableau ou un tableau croisé dynamique. Microsoft Excel vous permet de créer un segment en sélectionnant un tableau ou un tableau croisé dynamique, puis en cliquant sur le*Insertion > Trancheur*. Aspose.Cells vous permet également de créer une trancheuse à l'aide du[**Feuille de calcul.Slicers.Add()**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicercollection/methods/add/index)méthode.

## **Créer un segment dans un tableau croisé dynamique**

 Veuillez consulter l'exemple de code suivant. Il charge le[exemple de fichier Excel](67338470.xlsx) qui contient le tableau croisé dynamique. Il crée ensuite le segment en fonction du premier champ pivot de base. Enfin, il enregistre le classeur dans[sortie XLSX](67338471.xlsx) et[sortie XLSB](67338472.xlsb) format. La capture d'écran suivante montre le segment créé par Aspose.Cells dans le fichier Excel de sortie.

![tâche : image_autre_texte](create-slicer-to-a-pivot-table_1.png)

### **Exemple de code**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Slicers-CreateSlicerToPivotTable.cs" >}}

## **Créer un segment dans un tableau Excel**

 Veuillez consulter l'exemple de code suivant. Il charge le[exemple de fichier Excel](sampleCreateSlicerToExcelTable.xlsx) qui contient un tableau. Il crée ensuite le segment en fonction de la première colonne. Enfin, il enregistre le classeur dans[sortie XLSX](outputCreateSlicerToExcelTable.xlsx) format.

### **Exemple de code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Slicers-CreateSlicerToExcelTable-1.cs" >}}

## **Sujets avancés**
- [Modifier les propriétés du segment](/cells/fr/net/change-slicer-properties/)
- [Dessiner Slicer lors du rendu d'Excel au format PDF](/cells/fr/net/draw-slicer-while-rendering-excel-to-pdf/)
- [Formatage du segment](/cells/fr/net/formatting-slicer/)
- [Retrait du trancheur](/cells/fr/net/removing-slicer/)
- [Trancheur de rendu](/cells/fr/net/rendering-slicer/)
- [Mise à jour du segment](/cells/fr/net/updating-slicer/)
