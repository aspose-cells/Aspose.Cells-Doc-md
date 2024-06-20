---
title: Insérer ou supprimer des lignes dans une feuille de calcul Excel
type: docs
weight: 20
url: /fr/python-net/insert-or-delete-rows-in-an-excel-worksheet/
description: Cet article fournit le code python pour insérer et supprimer des lignes dans une feuille de calcul Excel avec la bibliothèque Aspose.Cells pour Python via .NET.
keywords: Python Excel Library, insertion ou suppression de lignes en python dans une feuille de calcul Excel, insertion ou suppression de lignes en python dans Excel, insertion de lignes en python dans Excel, suppression de lignes en python dans Excel, insertion ou suppression de lignes dans une feuille de calcul Excel avec Python, insertion ou suppression de lignes dans Excel avec Python, insertion de lignes dans Excel avec Python, suppression de lignes dans Excel avec Python
---

{{% alert color="primary" %}}

Lors de la création d'une nouvelle feuille de calcul ou du travail avec une feuille de calcul existante, vous pourriez avoir besoin d'ajouter des lignes ou des colonnes supplémentaires pour accueillir des données. À d'autres moments, vous pourriez avoir besoin de supprimer des lignes ou des colonnes à des positions spécifiées dans la feuille de calcul.

{{% /alert %}}

Aspose.Cells for Python via .NET offre deux méthodes pour l'insertion et la suppression de lignes : [**Cells.insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/) et [**Cells.delete_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_rows/). Ces méthodes sont optimisées pour les performances et font le travail très rapidement.

Pour insérer ou supprimer un certain nombre de lignes, nous vous recommandons d'utiliser toujours les méthodes [**Cells.insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/) et [**Cells.delete_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_rows/) au lieu d'utiliser les méthodes [**Cells.insert_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_row) ou [**delete_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_row) dans une boucle.

Aspose.Cells for Python via .NET fonctionne de la même manière que Microsoft Excel. Lorsque des lignes ou des colonnes sont ajoutées, le contenu de la feuille de calcul est déplacé vers le bas et vers la droite. Lorsque des lignes ou des colonnes sont supprimées, le contenu de la feuille de calcul est déplacé vers le haut ou vers la gauche. Toutes les références dans les autres feuilles de calcul et cellules sont mises à jour lorsque des lignes sont ajoutées ou supprimées.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertDeleteRows-1.py" >}}
