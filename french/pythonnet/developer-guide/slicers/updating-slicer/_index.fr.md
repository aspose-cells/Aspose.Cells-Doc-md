---
title: Mise à jour de la trancheuse
type: docs
weight: 50
url: /fr/python-net/updating-slicer/
description: Apprenez comment mettre à jour un segment avec Aspose.Cells pour Python via .NET.
keywords: Aspose.Cells pour Python Excel, bibliothèque Excel Python, mise à jour de segment sans Excel Python, Mise à jour de segment à l aide de Aspose.Cells pour Python.
---

## **Scénarios d'utilisation possibles**

Si vous souhaitez mettre à jour un segment dans Microsoft Excel, sélectionnez ou désélectionnez ses éléments, celui-ci mettra ensuite à jour le tableau de segments ou le tableau croisé dynamique en conséquence. Veuillez utiliser [**Slicer.slicer_cache.slicer_cache_items**](https://reference.aspose.com/cells/python-net/aspose.cells.slicers/slicercache/slicer_cache_items/) pour sélectionner ou désélectionner les éléments du segment avec Aspose.Cells pour Python via .NET, puis appelez la méthode [**Slicer.refresh()**](https://reference.aspose.com/cells/python-net/aspose.cells.slicers/slicer/refresh/#) pour mettre à jour le tableau de segments ou le tableau croisé dynamique.

## **Comment mettre à jour un segment en utilisant la bibliothèque Excel Aspose.Cells pour Python**

Le code d'exemple suivant charge le [fichier Excel d'exemple](67338475.xlsx) qui contient un segment existant. Il désélectionne les 2ème et 3ème éléments du segment et actualise le segment. Il enregistre ensuite le classeur sous la forme de [fichier Excel de sortie](67338476.xlsx). La capture d'écran suivante montre l'effet du code d'exemple sur le fichier Excel d'exemple. Comme vous pouvez le voir sur la capture d'écran, l'actualisation du segment avec les éléments sélectionnés a également actualisé le tableau croisé dynamique en conséquence.

![todo:image_alt_text](updating-slicer_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Slicers-UpdatingSlicer.py" >}}
