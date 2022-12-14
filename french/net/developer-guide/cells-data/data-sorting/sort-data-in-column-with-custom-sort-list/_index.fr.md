---
title: Trier les données en colonne avec une liste de tri personnalisée
type: docs
weight: 290
url: /fr/net/sort-data-in-column-with-custom-sort-list/
---
## **Scénarios d'utilisation possibles**

 Vous pouvez trier les données dans la colonne à l'aide d'une liste personnalisée. Cela peut être fait en utilisant[**DataSorter.AddKey (clé int, ordre SortOrder, chaîne customList)**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/2)méthode. Cependant, cette méthode ne fonctionne que si les éléments de la liste personnalisée ne contiennent pas de virgules. S'ils ont des virgules comme "USA,US", "China,CN", etc., vous devez utiliser [**DataSorter.AddKey Method (Int32, SortOrder,String[])**)](https://reference. aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/3) méthode. Ici, le dernier paramètre n'est pas une chaîne mais un tableau de chaînes.

## **Trier les données en colonne avec une liste de tri personnalisée**

L'exemple de code suivant explique comment utiliser [**DataSorter.AddKey Method (Int32, SortOrder,String[])**)](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey /methods/3) méthode pour trier les données avec une liste de tri personnalisée. Veuillez consulter le [fichier Excel d'exemple] (50528327.xlsx) utilisé dans ce code et le [fichier Excel de sortie] (50528328.xlsx) généré par celui-ci. La capture d'écran suivante montre l'effet du code sur l'exemple de fichier Excel lors de l'exécution.

![tâche : image_autre_texte](sort-data-in-column-with-custom-sort-list_1.png)

## **Exemple de code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithCustomSortList.cs" >}}
