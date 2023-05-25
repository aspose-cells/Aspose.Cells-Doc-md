---
title: Supprimer des lignes et des colonnes vides dans une feuille de calcul
type: docs
weight: 300
url: /fr/net/delete-blank-rows-and-columns-in-a-worksheet/
---
{{% alert color="primary" %}}

Il est possible de supprimer toutes les lignes et colonnes vides d'une feuille de calcul. Ceci est utile lorsque, par exemple, vous générez un fichier PDF à partir d'un fichier Excel Microsoft et souhaitez convertir uniquement les lignes et les colonnes contenant des données ou un objet associé.

Utilisez les méthodes Aspose.Cells suivantes pour supprimer les lignes et les colonnes vides :

1.  Pour supprimer des lignes vides, utilisez le[**Cells.DeleteBlankRows()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleteblankrows) méthode. Veuillez noter que pour les lignes vides qui seront supprimées, il n'est pas seulement nécessaire que[**Row.IsBlank**](https://reference.aspose.com/cells/net/aspose.cells/row/isblank/) doit être vrai, mais aucun commentaire visible ne doit être défini pour aucune cellule de ces lignes, ni aucun tableau croisé dynamique dont la plage les croise.
1.  Pour supprimer des colonnes vides, utilisez la[**Cells.DeleteBlankColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleteblankcolumns) méthode.

{{% /alert %}}

##  C# code pour supprimer les lignes vides

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteBlankRowsColumns-DeletingBlankRows-1.cs" >}}

##  Code C# pour supprimer les colonnes vides

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteBlankRowsColumns-DeletingBlankColumns-1.cs" >}}
