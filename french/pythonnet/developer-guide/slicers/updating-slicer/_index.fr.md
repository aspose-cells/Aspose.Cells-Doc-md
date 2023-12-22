---
title: Mise à jour du trancheur
type: docs
weight: 50
url: /fr/python-net/updating-slicer/
---
##  **Scénarios d'utilisation possibles**

Si vous souhaitez mettre à jour le slicer dans Excel Microsoft, sélectionnez ou désélectionnez ses éléments, il mettra alors à jour le tableau du slicer ou le tableau croisé dynamique en conséquence. Veuillez utiliser[**Slicer.slicer_cache.slicer_cache_items**](https://reference.aspose.com/cells/python-net/aspose.cells.slicers/slicercache/slicer_cache_items/)pour sélectionner ou désélectionner les éléments du slicer avec le Aspose.Cells for Python via .NET puis appeler[**Trancheuse.refresh()**](https://reference.aspose.com/cells/python-net/aspose.cells.slicers/slicer/refresh/#)méthode pour mettre à jour le tableau de découpage ou le tableau croisé dynamique.

##  **Mise à jour du trancheur**

 L'exemple de code suivant charge le[exemple de fichier Excel](67338475.xlsx) qui contient un slicer existant. Il désélectionne les 2ème et 3ème éléments du slicer et actualise le slicer. Il enregistre ensuite le classeur sous[sortie du fichier Excel](67338476.xlsx)La capture d'écran suivante montre l'effet de l'exemple de code sur l'exemple de fichier Excel. Comme vous pouvez le voir sur la capture d'écran, l'actualisation du slicer avec les éléments sélectionnés a également actualisé le tableau croisé dynamique en conséquence.

![tâche : image_alt_text](updating-slicer_1.png)

##  **Exemple de code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Slicers-UpdatingSlicer.py" >}}
