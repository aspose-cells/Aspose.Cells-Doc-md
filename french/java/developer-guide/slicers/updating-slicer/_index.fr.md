---
title: Mise à jour de la trancheuse
type: docs
weight: 50
url: /fr/java/updating-slicer/
---

## **Scénarios d'utilisation possibles**
Si vous souhaitez mettre à jour le filtre dans Microsoft Excel, sélectionnez ou désélectionnez ses éléments, cela mettra alors à jour la table du filtre ou le tableau croisé dynamique en conséquence. Utilisez [Slicer.SlicerCache.SlicerCacheItems](https://reference.aspose.com/cells/java/com.aspose.cells/slicercache#SlicerCacheItems) pour sélectionner ou désélectionner les éléments du filtre avec Aspose.Cells, puis appelez la méthode [Slicer.refresh()](https://reference.aspose.com/cells/java/com.aspose.cells/slicer#refresh--) pour mettre à jour la table du filtre ou le tableau croisé dynamique. 
## **Mise à jour du tronçonneur**
Le code d'échantillon suivant charge le [fichier Excel d'exemple](67338506.xlsx) contenant un slicer existant. Il désélectionne les 2ème et 3ème éléments du slicer et actualise ensuite le slicer. Ensuite, il enregistre le classeur sous le nom de [fichier Excel de sortie](67338505.xlsx). La capture d'écran suivante montre l'effet du code d'échantillon sur le fichier Excel d'exemple. Comme vous pouvez le voir sur la capture d'écran, l'actualisation du slicer avec des éléments sélectionnés a également actualisé le tableau croisé dynamique en conséquence.

![todo:image_alt_text](updating-slicer_1.png)
## **Code d'exemple**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-UpdatingSlicer.java" >}}
{{< app/cells/assistant language="java" >}}
