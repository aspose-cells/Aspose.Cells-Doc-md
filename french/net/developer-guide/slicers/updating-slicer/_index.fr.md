---
title: Mise à jour du segment
type: docs
weight: 50
url: /fr/net/updating-slicer/
---
## **Scénarios d'utilisation possibles**

Si vous souhaitez mettre à jour le segment dans Microsoft Excel, sélectionnez ou désélectionnez ses éléments, il mettra alors à jour le tableau du segment ou le tableau croisé dynamique en conséquence. Veuillez utiliser[**Slicer.SlicerCache.SlicerCacheItems**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicercache/properties/slicercacheitems)pour sélectionner ou désélectionner les éléments du slicer avec le Aspose.Cells puis appeler[**Slicer.Refresh()**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicer/methods/refresh)méthode pour mettre à jour la table du segment ou le tableau croisé dynamique.

## **Mise à jour du segment**

 L'exemple de code suivant charge le[exemple de fichier Excel](67338475.xlsx) qui contient un segment existant. Il désélectionne les 2ème et 3ème éléments du slicer et actualise le slicer. Il enregistre ensuite le classeur sous[fichier Excel de sortie](67338476.xlsx). La capture d'écran suivante montre l'effet de l'exemple de code sur l'exemple de fichier Excel. Comme vous pouvez le voir sur la capture d'écran, l'actualisation du segment avec les éléments sélectionnés a également actualisé le tableau croisé dynamique en conséquence.

![tâche : image_autre_texte](updating-slicer_1.png)

## **Exemple de code**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Slicers-UpdatingSlicer.cs" >}}
