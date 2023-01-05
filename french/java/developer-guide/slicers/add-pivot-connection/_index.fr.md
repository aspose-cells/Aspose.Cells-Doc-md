---
title: Ajouter une connexion pivot
type: docs
weight: 30
url: /fr/java/add-pivot-connection/
description: Apprenez à ajouter une connexion pivot avec la bibliothèque Aspose.Cells Java.
keywords: Add pivot connection without office 2013, office 2016, office 2019 and office 365.
---
## **Scénarios d'utilisation possibles**

 Si vous souhaitez associer un segment et un tableau croisé dynamique dans Excel, vous devez cliquer avec le bouton droit sur le segment et sélectionner l'élément "Connexions de rapport...". Dans la liste d'options, vous pouvez opérer sur la case à cocher. De même, si vous souhaitez associer un segment et un tableau croisé dynamique à l'aide de Aspose.Cells Java API par programme, veuillez utiliser le[**Slicer.addPivotConnection (pivot du tableau croisé dynamique)**](https://reference.aspose.com/cells/java/com.aspose.cells/slicer#addPivotConnection(com.aspose.cells.PivotTable)/) méthode. Il associera slicer et tableau croisé dynamique.

## **Associer un segment et un tableau croisé dynamique**

L'exemple de code suivant charge le[exemple de fichier Excel](add-pivot-connection.xlsx)qui contient un segment existant. Il accède au Slicer puis associe Slicer et PivotTable. Enfin, il enregistre le classeur sous[fichier Excel de sortie](add-pivot-connection-out.xlsx). 


## **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-Adding-Pivot-Connection.java" >}}