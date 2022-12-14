---
title: Insérer ou supprimer des lignes dans une feuille de calcul Excel
type: docs
weight: 20
url: /fr/net/insert-or-delete-rows-in-an-excel-worksheet/
description: Cet article fournit le code C# pour insérer et supprimer des lignes dans la feuille de calcul Excel
keywords: c# insert or delete rows in excel worksheet, c# insert or delete rows in excel, c# insert rows in excel, c# delete rows in excel, insert or delete rows in excel worksheet with c#, insert or delete rows in excel with c#, insert rows in excel with c#, delete rows in excel with c#
---
{{% alert color="primary" %}}

Lors de la création d'une nouvelle feuille de calcul ou de l'utilisation d'une feuille de calcul existante, vous devrez peut-être ajouter des lignes ou des colonnes supplémentaires pour contenir les données. À d'autres moments, vous devrez peut-être supprimer des lignes ou des colonnes à partir de positions spécifiées dans la feuille de calcul.

{{% /alert %}}

 Aspose.Cells propose deux méthodes pour insérer et supprimer des lignes :[**Cells.InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows/index) et[**Cells.DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows/index). Ces méthodes sont optimisées pour les performances et font le travail très rapidement.

 Pour insérer ou supprimer plusieurs lignes, nous vous recommandons de toujours utiliser la[**Cells.InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows/index) et[**Cells.DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows/index) méthodes au lieu d'utiliser les[**Cells.InsertRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow) ou[**Supprimer la ligne**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterow)méthodes en boucle.

Aspose.Cells fonctionne de la même manière que Microsoft Excel. Lorsque des lignes ou des colonnes sont ajoutées, le contenu de la feuille de calcul est décalé vers le bas et vers la droite. Lorsque des lignes ou des colonnes sont supprimées, le contenu de la feuille de calcul est décalé vers le haut ou vers la gauche. Toutes les références dans d'autres feuilles de calcul et cellules sont mises à jour lorsque des lignes sont ajoutées ou supprimées.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertDeleteRows-1.cs" >}}
