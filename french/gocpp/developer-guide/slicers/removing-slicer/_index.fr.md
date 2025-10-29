---
title: Suppression du Slicer avec Golang via C++
linktitle: Suppression de la trancheuse
type: docs
weight: 30
url: /fr/go-cpp/removing-slicer/
description: Apprenez comment supprimer les coupeurs dans les fichiers Excel de manière programmatique en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

Si vous souhaitez supprimer un coupeur dans Microsoft Excel, il suffit de le sélectionner et d'appuyer sur le bouton *Supprimer*. De même, si vous souhaitez le supprimer en utilisant l'API Aspose.Cells de manière programmatique, veuillez utiliser la méthode [**Worksheet.Slicers.Remove()**](https://reference.aspose.com/cells/go-cpp/slicercollection/remove/). Cela supprimera le coupeur de la feuille de calcul.

## **Suppression du tronçonneur**

Le code d'exemple suivant charge le [fichier Excel d'exemple](67338478.xlsx) qui contient une trancheuse existante. Il accède aux tranches et les supprime. Enfin, il enregistre le classeur sous le nom de [fichier Excel de sortie](67338477.xlsx). La capture d'écran suivante montre la trancheuse qui sera supprimée après l'exécution du code d'exemple.

![todo:image_alt_text](removing-slicer_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RemovingSlicer.go" >}}
