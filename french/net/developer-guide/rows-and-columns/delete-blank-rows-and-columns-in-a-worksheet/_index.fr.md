---
title: Supprimer les lignes et colonnes vides dans une feuille de calcul
type: docs
weight: 300
url: /fr/net/delete-blank-rows-and-columns-in-a-worksheet/
---

{{% alert color="primary" %}}

Il est possible de supprimer toutes les lignes et colonnes vides d'une feuille de calcul. Cela est utile, par exemple, lors de la génération d'un fichier PDF à partir d'un fichier Microsoft Excel et que vous souhaitez convertir uniquement les lignes et colonnes contenant des données ou des objets associés.

Utilisez les méthodes Aspose.Cells suivantes pour supprimer les lignes et colonnes vides :

1. Pour supprimer les lignes vides, utilisez la méthode [**Cells.DeleteBlankRows()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleteblankrows). Veuillez noter que, pour les lignes vides qui seront supprimées, il est non seulement nécessaire que [**Row.IsBlank**](https://reference.aspose.com/cells/net/aspose.cells/row/isblank/) soit vrai, mais il ne doit également y avoir aucun commentaire visible défini pour une quelconque cellule de ces lignes, et aucun tableau croisé dynamique dont la plage intersecte avec elles.
1. Pour supprimer les colonnes vides, utilisez la méthode [**Cells.DeleteBlankColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleteblankcolumns).

{{% /alert %}}

## Code C# pour supprimer les lignes vides

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteBlankRowsColumns-DeletingBlankRows-1.cs" >}}

## Code C# pour supprimer les colonnes vides

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteBlankRowsColumns-DeletingBlankColumns-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
