---
title: Mise à jour du trancheur
type: docs
weight: 50
url: /fr/net/updating-slicer/
description: Cet article montre comment mettre à jour les tableaux croisés dynamiques liés en mettant à jour le slicer par le Aspose.Cells for .NET API.
keywords: Aspose.Cells C# Update slicer, C# how to change the slicer, how to adjust the slicer in C#, how to select or unselect he slicer items.
---
##  **Scénarios d'utilisation possibles**

Si vous souhaitez mettre à jour le slicer dans Excel Microsoft, sélectionnez ou désélectionnez ses éléments, il mettra alors à jour le tableau du slicer ou le tableau croisé dynamique en conséquence. Veuillez utiliser[**Slicer.SlicerCache.SlicerCacheItems**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicercache/properties/slicercacheitems)pour sélectionner ou désélectionner les éléments du slicer avec le Aspose.Cells puis appeler[**Trancheuse.Refresh()**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicer/methods/refresh)méthode pour mettre à jour le tableau de découpage ou le tableau croisé dynamique.

##  **Comment mettre à jour le trancheur**

 L'exemple de code suivant charge le[exemple de fichier Excel](67338475.xlsx) qui contient un slicer existant. Il désélectionne les 2ème et 3ème éléments du slicer et actualise le slicer. Il enregistre ensuite le classeur sous[sortie du fichier Excel](67338476.xlsx)La capture d'écran suivante montre l'effet de l'exemple de code sur l'exemple de fichier Excel. Comme vous pouvez le voir sur la capture d'écran, l'actualisation du slicer avec les éléments sélectionnés a également actualisé le tableau croisé dynamique en conséquence.

![tâche : image_alt_text](updating-slicer_1.png)

##  **Exemple de code**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Slicers-UpdatingSlicer.cs" >}}
