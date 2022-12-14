---
title: Trier les données en colonne avec une liste de tri personnalisée
type: docs
weight: 210
url: /fr/java/sort-data-in-column-with-custom-sort-list/
---
## **Scénarios d'utilisation possibles**

Vous pouvez trier les données dans la colonne à l'aide d'une liste personnalisée. Cela peut être fait en utilisant[DataSorter.AddKey (clé int, ordre SortOrder, chaîne customList)](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int,%20java.lang.String)) méthode. Cependant, cette méthode ne fonctionne que si les éléments de la liste personnalisée ne contiennent pas de virgules. S'ils ont des virgules comme "USA, US", "China, CN" etc., alors vous devez utiliser[DataSorter.AddKey (clé int, ordre SortOrder, chaîne customList)](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int,%20java.lang.String)) méthode. Ici, le dernier paramètre n'est pas une chaîne mais un tableau de chaînes.

## **Trier les données en colonne avec une liste de tri personnalisée**

L'exemple de code suivant explique comment utiliser la méthode DataSorter.AddKey(int key, SortOrder order, String[]customList) pour trier les données avec une liste de tri personnalisée. Veuillez consulter le[exemple de fichier Excel](50528359.xlsx)utilisé dans ce code et[fichier Excel de sortie](50528358.xlsx)généré par celui-ci. La capture d'écran suivante montre l'effet du code sur l'exemple de fichier Excel lors de l'exécution.

![tâche : image_autre_texte](sort-data-in-column-with-custom-sort-list_1.png)

## **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-SortDataInColumnWithCustomSortList.java" >}}
