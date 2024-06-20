---
title: Suppression de la trancheuse
type: docs
weight: 30
url: /fr/java/removing-slicer/
---

## **Scénarios d'utilisation possibles**
Si vous souhaitez supprimer une trancheuse dans Microsoft Excel, il vous suffit de la sélectionner et d'appuyer sur le bouton *Supprimer*. De même, si vous souhaitez la supprimer en utilisant l'API Aspose.Cells de manière programmée, veuillez utiliser la méthode [Worksheet.getSlicers().remove()](https://reference.aspose.com/cells/java/com.aspose.cells/slicercollection#remove\(com.aspose.cells.Slicer\)). Elle supprimera la trancheuse de la feuille de calcul. 
## **Suppression du tronçonneur**
Le code d'exemple suivant charge le [fichier Excel d'exemple](67338504.xlsx) qui contient une trancheuse existante. Il accède aux tranches et les supprime, puis enregistre le classeur au format [fichier Excel de sortie](67338502.xlsx). La capture d'écran suivante montre la trancheuse qui sera supprimée après l'exécution du code d'exemple.

![todo:image_alt_text](removing-slicer_1.png)
## **Code d'exemple**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-RemovingSlicer.java" >}}
