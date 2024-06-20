---
title: Mise à jour de la trancheuse
type: docs
weight: 60
url: /fr/python-java/updating-slicer/
---

## **Mise à jour du tronçonneur**
Aspose.Cells pour Python via Java prend en charge la mise à jour des filtres. Pour cela, l'API fournit la propriété Slicer.SlicerCache.SlicerCacheItems qui est utilisée pour sélectionner ou désélectionner des éléments de filtre. Le code suivant charge le [fichier Excel exemple](106365050.xlsx) qui contient un filtre.  Il désélectionne les 2ème et 3ème éléments du filtre et actualise le filtre en utilisant la méthode Slicer.refresh(). Il enregistre ensuite le classeur sous le nom de [fichier Excel de sortie](106365051.xlsx). La capture d'écran suivante montre l'effet du code exemple sur le fichier Excel exemple. Comme vous pouvez le voir sur la capture d'écran, l'actualisation du filtre avec des éléments sélectionnés a également actualisé le tableau croisé dynamique en conséquence.

![todo:image_alt_text](Updating-Slicer-using-Aspose.Cells.png)
## **Code d'exemple**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Slicers-UpdatingSlicer.py" >}}
