---
title: Supprimer la connexion de tableau croisé dynamique
type: docs
weight: 30
url: /fr/java/remove-pivot-connection/
description: Apprenez comment supprimer une connexion pivot avec la bibliothèque Aspose.Cells Java.
keywords: Supprimer la connexion pivot sans office 2013, office 2016, office 2019 et office 365.
---

## **Scénarios d'utilisation possibles**

Si vous souhaitez dissocier une trancheuse et un tableau croisé dynamique dans Excel, vous devez faire un clic droit sur la trancheuse et sélectionner l'élément "Connections des rapports...". Dans la liste des options, vous pouvez cocher ou décocher la case. De même, si vous souhaitez dissocier une trancheuse et un tableau croisé dynamique en utilisant l'API Aspose.Cells de manière programmée, veuillez utiliser la méthode [**Slicer.removePivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/java/com.aspose.cells/slicer#removePivotConnection(com.aspose.cells.PivotTable)). Elle permet de dissocier la trancheuse et le tableau croisé dynamique.

## **Suppression du tronçonneur**

Le code d'exemple suivant charge le [fichier Excel d'exemple](remove-pivot-connection.xlsx) qui contient une trancheuse existante. Il accède aux tranches et dissocie ensuite la trancheuse et le tableau croisé dynamique. Enfin, il enregistre le classeur sous le nom de [fichier Excel de sortie](remove-pivot-connection-out.xlsx). 


## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-Removing-Pivot-Connection.java" >}}
