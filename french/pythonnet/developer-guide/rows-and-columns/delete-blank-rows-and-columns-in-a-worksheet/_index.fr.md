---
title: Supprimer les lignes et colonnes vides dans une feuille de calcul
type: docs
weight: 300
url: /fr/python-net/delete-blank-rows-and-columns-in-a-worksheet/
description: Cet article décrit comment supprimer les lignes et colonnes vides dans une feuille de calcul avec la bibliothèque Aspose.Cells pour Python via .NET.
keywords: Bibliothèque Python Excel, supprimer les lignes vides en Python, supprimer les colonnes vides en Python, supprimer les colonnes vides en Python, supprimer les colonnes vides en Python, supprimer ou supprimer les lignes et colonnes vides en Python.
---

{{% alert color="primary" %}}

Il est possible de supprimer toutes les lignes et colonnes vides d'une feuille de calcul. Cela est utile, par exemple, lors de la génération d'un fichier PDF à partir d'un fichier Microsoft Excel et que vous souhaitez convertir uniquement les lignes et colonnes contenant des données ou des objets associés.

Utilisez les méthodes Aspose.Cells suivantes pour supprimer les lignes et colonnes vides :

1. Pour supprimer les lignes vides, utilisez la méthode [**Cells.delete_blank_rows()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_blank_rows). Veuillez noter que, pour les lignes vides qui seront supprimées, il est non seulement nécessaire que [**Row.is_blank**](https://reference.aspose.com/cells/python-net/aspose.cells/row/is_blank/) soit vrai, mais il ne doit également y avoir aucun commentaire visible défini pour une quelconque cellule de ces lignes, et aucun tableau croisé dynamique dont la plage intersecte avec elles.
1. Pour supprimer les colonnes vides, utilisez la méthode [**Cells.delete_blank_columns()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_blank_columns).

{{% /alert %}}

## Code C# pour supprimer les lignes vides

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-DeletingBlankRows-1.py" >}}

## Code C# pour supprimer les colonnes vides

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-DeletingBlankColumns-1.py" >}}
