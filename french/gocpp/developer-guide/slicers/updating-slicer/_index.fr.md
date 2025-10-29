---
title: Mise à jour du Slicer avec Golang via C++
linktitle: Mise à jour de la trancheuse
type: docs
weight: 50
url: /fr/go-cpp/updating-slicer/
description: Cet article montre comment mettre à jour les tableaux croisés dynamiques liés en mettant à jour le coupeur en utilisant l API Aspose.Cells for C++.
keywords: Aspose.Cells C++ Mettre à jour le coupeur, C++ comment modifier le coupeur, comment ajuster le coupeur en C++, comment sélectionner ou désélectionner les éléments du coupeur.
---

## **Scénarios d'utilisation possibles**

Si vous souhaitez mettre à jour un coupeur dans Microsoft Excel, sélectionnez ou désélectionnez ses éléments, cela mettra à jour en conséquence la table ou le tableau croisé dynamique du coupeur. Veuillez utiliser [**Slicer.GetSlicerCacheItems()**](https://reference.aspose.com/cells/go-cpp/slicercache/getslicercacheitems/) pour sélectionner ou désélectionner les éléments du coupeur avec Aspose.Cells, puis appeler la méthode [**Slicer.Refresh()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/refresh/) pour mettre à jour la table ou le tableau croisé dynamique.

## **Comment mettre à jour le filtre**

Le code d'exemple suivant charge le [fichier Excel d'exemple](67338475.xlsx) qui contient un segment existant. Il désélectionne les 2ème et 3ème éléments du segment et actualise le segment. Il enregistre ensuite le classeur sous la forme de [fichier Excel de sortie](67338476.xlsx). La capture d'écran suivante montre l'effet du code d'exemple sur le fichier Excel d'exemple. Comme vous pouvez le voir sur la capture d'écran, l'actualisation du segment avec les éléments sélectionnés a également actualisé le tableau croisé dynamique en conséquence.

![todo:image_alt_text](updating-slicer_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UpdatingSlicer.go" >}}
