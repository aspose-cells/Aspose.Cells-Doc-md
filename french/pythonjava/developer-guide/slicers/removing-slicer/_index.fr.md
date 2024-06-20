---
title: Suppression de la trancheuse
type: docs
weight: 40
url: /fr/python-java/removing-slicer/
---

## **Suppression du tronçonneur**
Pour supprimer un filtre dans Microsoft Excel, il suffit de sélectionner le filtre et d'appuyer sur le bouton *Supprimer*. Pour réaliser cela en utilisant Aspose.Cells for Python via Java, utilisez la méthode Worksheet.getSlicers().remove(). Cela supprimera le filtre de la feuille de calcul. 

Le code suivant charge le [fichier Excel exemple](106364970.xlsx) qui contient un filtre existant. Il accède au filtre, le supprime, puis enregistre le [fichier Excel de sortie](106364971.xlsx). La capture d'écran suivante montre le filtre qui sera supprimé.

![todo:image_alt_text](Removing-Slicer-using-Aspose.Cells.png)
## **Code d'exemple**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Slicers-RemovingSlicer.py" >}}
