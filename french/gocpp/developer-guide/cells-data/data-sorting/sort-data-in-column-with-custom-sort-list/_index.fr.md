---
title: Trier des données dans une colonne avec une liste de tri personnalisé avec Golang via C++
linktitle: Trier les données dans une colonne avec une liste de tri personnalisée
type: docs
weight: 290
url: /fr/go-cpp/sort-data-in-column-with-custom-sort-list/
description: Apprenez comment trier des données dans une colonne en utilisant une liste personnalisée avec l API Aspose.Cells for C++.
keywords: Trier les données dans une colonne avec une liste de tri personnalisée, trier les données par liste personnalisée.
---

## **Scénarios d'utilisation possibles**

Vous pouvez trier des données dans une colonne à l'aide d'une liste personnalisée. Cela peut être fait en utilisant la méthode [**DataSorter::AddKey(int key, SortOrder order, String customList)**](https://reference.aspose.com/cells/go-cpp/datasorter/addkey_int_sortorder/). Cependant, cette méthode ne fonctionne que si les éléments de la liste personnalisée ne contiennent pas de virgules. Si elles contiennent des virgules comme "USA,US", "China,CN", vous devez utiliser la méthode [**DataSorter::AddKey Method (Int32, SortOrder, String[])**](https://reference.aspose.com/cells/go-cpp/datasorter/addkey_int_sortorder/). Ici, le dernier paramètre n'est pas une chaîne, mais un tableau de chaînes.

## **Trier les données dans une colonne avec une liste de tri personnalisée**

Le code d'exemple suivant explique comment utiliser la méthode [**DataSorter::AddKey Method (Int32, SortOrder, String[])**](https://reference.aspose.com/cells/go-cpp/datasorter/addkey_int_sortorder/) pour trier les données avec une liste de tri personnalisée. Veuillez voir le [fichier Excel d'exemple](50528327.xlsx) utilisé dans ce code et le [fichier Excel de sortie](50528328.xlsx) généré par celui-ci. La capture d'écran suivante montre l'effet du code sur le fichier Excel d'exemple lors de son exécution.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SortDataInColumnWithCustomSortList.go" >}}
