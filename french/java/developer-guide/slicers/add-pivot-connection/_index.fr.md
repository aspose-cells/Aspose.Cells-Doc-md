---
title: Ajouter une connexion de tableau croisé dynamique
type: docs
weight: 30
url: /fr/java/add-pivot-connection/
description: Apprenez à ajouter une connexion pivot avec la bibliothèque Aspose.Cells Java.
keywords: Ajouter une connexion pivot sans office 2013, office 2016, office 2019 et office 365.
---

## **Scénarios d'utilisation possibles**

Si vous souhaitez associer une trancheuse et un tableau croisé dynamique dans Excel, vous devez faire un clic droit sur la trancheuse et sélectionner l'élément "Connections des rapports...". Dans la liste des options, vous pouvez cocher ou décocher la case. De même, si vous souhaitez associer une trancheuse et un tableau croisé dynamique en utilisant l'API Aspose.Cells Java de manière programmée, veuillez utiliser la méthode [**Slicer.addPivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/java/com.aspose.cells/slicer#addPivotConnection-com.aspose.cells.PivotTable-). Elle permet d'associer la trancheuse et le tableau croisé dynamique.

## **Associer une trancheuse et un tableau croisé dynamique**

Le code d'exemple suivant charge le [fichier Excel d'exemple](add-pivot-connection.xlsx) qui contient une trancheuse existante. Il accède à la trancheuse et associe ensuite la trancheuse et le tableau croisé dynamique. Enfin, il enregistre le classeur sous forme de [fichier Excel de sortie](add-pivot-connection-out.xlsx). 


## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-Adding-Pivot-Connection.java" >}}
{{< app/cells/assistant language="java" >}}
