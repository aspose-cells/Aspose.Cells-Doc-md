---
title: Trier les données dans une colonne avec une liste de tri personnalisée
type: docs
weight: 290
url: /fr/net/sort-data-in-column-with-custom-sort-list/
description: Découvrez comment trier les données dans la colonne à l'aide d'une liste personnalisée en utilisant le Aspose.Cells for .NET API.
keywords: Sort Data in Column with Custom Sort List, Sort data by custom list.
---
##  **Scénarios d'utilisation possibles**

 Vous pouvez trier les données dans la colonne à l'aide d'une liste personnalisée. Cela peut être fait en utilisant[**DataSorter.AddKey (clé int, ordre SortOrder, String customList)**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/2)méthode. Cependant, cette méthode ne fonctionne que si les éléments de la liste personnalisée ne contiennent pas de virgules. S'ils ont des virgules comme "USA, US", "China, CN", etc., vous devez utiliser [**DataSorter.AddKey Method (Int32, SortOrder,String[])**)](https://reference. aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/3). Ici, le dernier paramètre n'est pas String mais un Array of Strings.

##  **Trier les données dans une colonne avec une liste de tri personnalisée**

L'exemple de code suivant explique comment utiliser la [**DataSorter.AddKey Method (Int32, SortOrder,String[])**)](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey /methods/3) pour trier les données avec une liste de tri personnalisée. Veuillez consulter le[exemple de fichier Excel](50528327.xlsx) utilisé dans ce code et[sortie du fichier Excel](50528328.xlsx) généré par celui-ci. La capture d'écran suivante montre l'effet du code sur l'exemple de fichier Excel lors de l'exécution.

![tâche : image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

##  **Exemple de code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithCustomSortList.cs" >}}
