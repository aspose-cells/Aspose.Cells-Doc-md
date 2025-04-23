---
title: Supprimer la connexion de tableau croisé dynamique
type: docs
weight: 30
url: /fr/net/remove-pivot-connection/
description: Apprenez comment supprimer une connexion de tableau croisé dynamique avec la bibliothèque Aspose.Cells.
keywords: Supprimer la connexion pivot sans office 2013, office 2016, office 2019 et office 365.
---

## **Scénarios d'utilisation possibles**

Si vous souhaitez dissocier une trancheuse et un tableau croisé dynamique dans Excel, vous devez faire un clic droit sur la trancheuse et sélectionner l'élément "Connections des rapports...". Dans la liste des options, vous pouvez cocher ou décocher la case. De même, si vous souhaitez dissocier une trancheuse et un tableau croisé dynamique en utilisant l'API Aspose.Cells de manière programmée, veuillez utiliser la méthode [**Slicer.RemovePivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicer/removepivotconnection/). Elle permet de dissocier la trancheuse et le tableau croisé dynamique.

## **Dissocier le filtre et le tableau croisé dynamique**

Le code d'exemple suivant charge le [fichier Excel d'exemple](remove-pivot-connection.xlsx) qui contient une trancheuse existante. Il accède aux tranches et dissocie ensuite la trancheuse et le tableau croisé dynamique. Enfin, il enregistre le classeur sous le nom de [fichier Excel de sortie](remove-pivot-connection-out.xlsx). 


## **Code d'exemple**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Slicers-Removing-Pivot-Connection.cs" >}}
{{< app/cells/assistant language="csharp" >}}
