---
title: Trier les données dans une colonne avec une liste de tri personnalisée
type: docs
weight: 290
url: /fr/nodejs-cpp/sort-data-in-column-with-custom-sort-list/
description: Apprenez comment trier les données dans la colonne à l aide d une liste personnalisée en utilisant l API Aspose.Cells for Node.js via C++.
keywords: Trier les données dans une colonne avec une liste de tri personnalisée, trier les données par liste personnalisée.
---

## **Scénarios d'utilisation possibles**

Vous pouvez trier les données dans la colonne en utilisant une liste personnalisée. Cela peut être réalisé avec la méthode [**DataSorter.addKey**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#addKey-number-sortorder-string-). Cependant, cette méthode ne fonctionne que si les éléments de la liste personnalisée ne contiennent pas de virgules. Si elles contiennent des virgules comme "USA,US", "Chine,CN", vous devez utiliser la méthode [**DataSorter.addKey(number, SortOrder, string[])**)](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#addKey-number-sortorder-stringarray-) . Ici, le dernier paramètre n'est pas une chaîne mais un tableau de chaînes.

## **Trier les données dans une colonne avec une liste de tri personnalisée**

Le code d'exemple suivant explique comment utiliser la méthode [**DataSorter.addKey(number, SortOrder, string[])**)](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#addKey-number-sortorder-stringarray-) pour trier les données avec une liste de tri personnalisée. Veuillez voir le fichier Excel [exemple](50528327.xlsx) utilisé dans ce code et le [fichier de sortie](50528328.xlsx) généré. La capture d'écran suivante montre l'effet du code sur le fichier Excel à l'exécution.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SortDataInColumnWithCustomSortList.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
