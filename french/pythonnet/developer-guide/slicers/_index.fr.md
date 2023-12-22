---
title: Insérer une trancheuse
linktitle: Trancheuses
type: docs
weight: 170
url: /fr/python-net/create-slicer/
description: Gérez les slicers de fichiers Excel avec le Aspose.Cells.
---
##  **Scénarios d'utilisation possibles**

Un slicer est utilisé pour filtrer les données rapidement. Il peut être utilisé pour filtrer les données dans un tableau ou un tableau croisé dynamique. Microsoft Excel vous permet de créer un slicer en sélectionnant un tableau ou un tableau croisé dynamique, puis en cliquant sur *Insérer > Slicer*. Aspose.Cells for Python via .NET vous permet également de créer un slicer à l'aide du[**Feuille de calcul.slicers.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.slicers/slicercollection/add/#aspose.cells.pivot.PivotTable-int-int-aspose.cells.pivot.PivotField)méthode.

##  **Créer un slicer dans un tableau croisé dynamique**

 Veuillez consulter l'exemple de code suivant. Il charge le[exemple de fichier Excel](67338470.xlsx) qui contient le tableau croisé dynamique. Il crée ensuite le slicer basé sur le premier champ pivot de base. Enfin, il enregistre le classeur dans[sortie XLSX](67338471.xlsx) et[sortie XLSB](67338472.xlsb) format. La capture d'écran suivante montre le slicer créé par Aspose.Cells dans le fichier Excel de sortie.

![tâche : image_alt_text](create-slicer-to-a-pivot-table_1.png)

###  **Exemple de code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Slicers-CreateSlicerToPivotTable.py" >}}

##  **Créer un slicer dans un tableau Excel**

 Veuillez consulter l'exemple de code suivant. Il charge le[exemple de fichier Excel](sampleCreateSlicerToExcelTable.xlsx) qui contient un tableau. Il crée ensuite le slicer basé sur la première colonne. Enfin, il enregistre le classeur dans[sortie XLSX](outputCreateSlicerToExcelTable.xlsx) format.

###  **Exemple de code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Examples-CSharp-Slicers-CreateSlicerToExcelTable-1.py" >}}

##  **Sujets avancés**
- [Modifier les propriétés du segment](/cells/fr/python-net/change-slicer-properties/)
- [Dessinez Slicer lors du rendu d'Excel au PDF](/cells/fr/python-net/draw-slicer-while-rendering-excel-to-pdf/)
- [Trancheur de formatage](/cells/fr/python-net/formatting-slicer/)
- [Suppression du trancheur](/cells/fr/python-net/removing-slicer/)
- [Trancheur de rendu](/cells/fr/python-net/rendering-slicer/)
- [Mise à jour du trancheur](/cells/fr/python-net/updating-slicer/)
