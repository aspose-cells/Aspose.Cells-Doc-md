---
title: Trier les données dans une colonne avec une liste de tri personnalisée
type: docs
weight: 210
url: /fr/java/sort-data-in-column-with-custom-sort-list/
---

## **Scénarios d'utilisation possibles**

Vous pouvez trier les données dans la colonne en utilisant une liste personnalisée. Cela peut être fait en utilisant la méthode [DataSorter.AddKey(int key, SortOrder order, String customList)](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey-int-int-java.lang.String-). Cependant, cette méthode ne fonctionne que si les éléments de la liste personnalisée ne contiennent pas de virgules. Si elles contiennent des virgules comme "USA, US", "Chine, CN" etc., vous devez utiliser la méthode [DataSorter.AddKey(int key, SortOrder order, String customList)](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey-int-int-java.lang.String-). Ici, le dernier paramètre n'est pas une chaîne mais un tableau de chaînes.

## **Trier les données dans une colonne avec une liste de tri personnalisée**

Le code d'exemple suivant explique comment utiliser la méthode `DataSorter.AddKey(int key, SortOrder order, String[] customList)` pour trier les données avec une liste de tri personnalisée. Veuillez consulter le [fichier Excel d'exemple](50528359.xlsx) utilisé dans ce code et le [fichier Excel de sortie](50528358.xlsx) généré par celui-ci. La capture d'écran suivante montre l'effet du code sur le fichier Excel d'exemple à l'exécution.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-SortDataInColumnWithCustomSortList.java" >}}
{{< app/cells/assistant language="java" >}}
