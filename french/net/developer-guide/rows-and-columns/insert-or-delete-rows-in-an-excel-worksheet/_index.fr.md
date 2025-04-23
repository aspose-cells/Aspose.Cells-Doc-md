---
title: Insérer ou supprimer des lignes dans une feuille de calcul Excel
type: docs
weight: 20
url: /fr/net/insert-or-delete-rows-in-an-excel-worksheet/
description: Cet article fournit le code C# pour insérer et supprimer des lignes dans une feuille de calcul Excel
keywords: c# insérer ou supprimer des lignes dans une feuille de calcul Excel, c# insérer ou supprimer des lignes dans Excel, c# insérer des lignes dans Excel, c# supprimer des lignes dans Excel, insérer ou supprimer des lignes dans une feuille de calcul Excel avec c#, insérer ou supprimer des lignes dans Excel avec c#, insérer des lignes dans Excel avec c#, supprimer des lignes dans Excel avec c#
---

{{% alert color="primary" %}}

Lors de la création d'une nouvelle feuille de calcul ou du travail avec une feuille de calcul existante, vous pourriez avoir besoin d'ajouter des lignes ou des colonnes supplémentaires pour accueillir des données. À d'autres moments, vous pourriez avoir besoin de supprimer des lignes ou des colonnes à des positions spécifiées dans la feuille de calcul.

{{% /alert %}}

Aspose.Cells offre deux méthodes pour insérer et supprimer des lignes : [**Cells.InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows/index) et [**Cells.DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows/index). Ces méthodes sont optimisées pour les performances et font le travail très rapidement.

Pour insérer ou supprimer un certain nombre de lignes, nous vous recommandons d'utiliser toujours les méthodes [**Cells.InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows/index) et [**Cells.DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows/index) au lieu d'utiliser les méthodes [**Cells.InsertRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow) ou [**DeleteRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterow) dans une boucle.

Aspose.Cells fonctionne de la même manière que Microsoft Excel. Lorsque des lignes ou des colonnes sont ajoutées, le contenu de la feuille de calcul est déplacé vers le bas et vers la droite. Lorsque des lignes ou des colonnes sont supprimées, le contenu de la feuille de calcul est déplacé vers le haut ou vers la gauche. Toutes les références dans les autres feuilles de calcul et cellules sont mises à jour lorsque des lignes sont ajoutées ou supprimées.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertDeleteRows-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
