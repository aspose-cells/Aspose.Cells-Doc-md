---
title: Mise à jour de la trancheuse
type: docs
weight: 50
url: /fr/net/updating-slicer/
description: Cet article montre comment mettre à jour les tableaux croisés dynamiques liés en mettant à jour le filtre avec le code Aspose.Cells for .NET.
keywords: Mettre à jour le filtre Aspose.Cells C#, C# comment changer le filtre, comment ajuster le filtre en C#, comment sélectionner ou désélectionner les éléments du filtre.
---

## **Scénarios d'utilisation possibles**

Si vous souhaitez mettre à jour le filtre dans Microsoft Excel, sélectionnez ou désélectionnez ses éléments, puis mettez à jour le tableau filtre ou le tableau croisé dynamique en conséquence. Veuillez utiliser [**Slicer.SlicerCache.SlicerCacheItems**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicercache/properties/slicercacheitems) pour sélectionner ou désélectionner les éléments du filtre avec Aspose.Cells, puis appeler la méthode [**Slicer.Refresh()**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicer/methods/refresh) pour mettre à jour le tableau filtre ou le tableau croisé dynamique.

## **Comment mettre à jour le filtre**

Le code d'exemple suivant charge le [fichier Excel d'exemple](67338475.xlsx) qui contient un segment existant. Il désélectionne les 2ème et 3ème éléments du segment et actualise le segment. Il enregistre ensuite le classeur sous la forme de [fichier Excel de sortie](67338476.xlsx). La capture d'écran suivante montre l'effet du code d'exemple sur le fichier Excel d'exemple. Comme vous pouvez le voir sur la capture d'écran, l'actualisation du segment avec les éléments sélectionnés a également actualisé le tableau croisé dynamique en conséquence.

![todo:image_alt_text](updating-slicer_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Slicers-UpdatingSlicer.cs" >}}
