---
title: Mise à jour du segment
type: docs
weight: 60
url: /fr/python-java/updating-slicer/
---
## **Mise à jour du segment**
Aspose.Cells for Python via Java prend en charge la mise à jour des slicers. Pour cela, le API fournit la propriété Slicer.SlicerCache.SlicerCacheItems qui est utilisée pour sélectionner ou désélectionner les éléments du slicer. L'extrait de code suivant charge le[exemple de fichier Excel](106365050.xlsx)qui contient un trancheur. Il désélectionne les 2ème et 3ème éléments du slicer et actualise le slicer à l'aide de la méthode Slicer.refresh(). Il enregistre ensuite le classeur en tant que[fichier Excel de sortie](106365051.xlsx). La capture d'écran suivante montre l'effet de l'exemple de code sur l'exemple de fichier Excel. Comme vous pouvez le voir sur la capture d'écran, l'actualisation du segment avec les éléments sélectionnés a également actualisé le tableau croisé dynamique en conséquence.

![tâche : image_autre_texte](Updating-Slicer-using-Aspose.Cells.png)
## **Exemple de code**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Slicers-UpdatingSlicer.py" >}}
