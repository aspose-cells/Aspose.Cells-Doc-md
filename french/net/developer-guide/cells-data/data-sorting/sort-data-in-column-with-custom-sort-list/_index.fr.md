---
title: Trier les données dans une colonne avec une liste de tri personnalisée
type: docs
weight: 290
url: /fr/net/sort-data-in-column-with-custom-sort-list/
description: Apprenez à trier les données dans la colonne en utilisant une liste personnalisée en utilisant l API Aspose.Cells for .NET.
keywords: Trier les données dans une colonne avec une liste de tri personnalisée, trier les données par liste personnalisée.
---

## **Scénarios d'utilisation possibles**

Vous pouvez trier les données dans la colonne en utilisant une liste personnalisée. Cela peut être fait en utilisant la méthode [**DataSorter.AddKey(int key, SortOrder order, String customList)**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/2). Cependant, cette méthode fonctionne uniquement si les éléments de la liste personnalisée n'ont pas de virgules à l'intérieur. S'ils ont des virgules comme "USA,US", "Chine,CN" etc., alors vous devez utiliser [** DataSorter.AddKey Méthode (Int32, SortOrder, String[])**)](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/3) méthode. Ici, le dernier paramètre n'est pas une chaîne mais un tableau de chaînes.

## **Trier les données dans une colonne avec une liste de tri personnalisée**

Le code d'exemple suivant explique comment utiliser la méthode [**DataSorter.AddKey (Int32, SortOrder, String[])**)](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/3) pour trier les données avec une liste de tri personnalisée. Veuillez consulter le [fichier Excel d'exemple](50528327.xlsx) utilisé dans ce code et le [fichier Excel de sortie](50528328.xlsx) généré par celui-ci. La capture d'écran suivante montre l'effet du code sur le fichier Excel d'exemple lors de l'exécution.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithCustomSortList.cs" >}}
