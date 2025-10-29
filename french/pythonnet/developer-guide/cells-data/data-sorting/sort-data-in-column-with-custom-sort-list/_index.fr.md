---
title: Trier les données dans une colonne avec une liste de tri personnalisée
type: docs
weight: 290
url: /fr/python-net/sort-data-in-column-with-custom-sort-list/
description: Apprenez à trier des données dans la colonne en utilisant une liste personnalisée en utilisant l API Aspose.Cells for Python via .NET.
keywords: Bibliothèque Python pour Excel, Trier les données en colonne avec une liste de tri personnalisée en Python, Trier les données en Python par liste personnalisée.
---

## **Scénarios d'utilisation possibles**

Vous pouvez trier des données dans la colonne en utilisant une liste personnalisée. Cela peut être fait en utilisant la méthode [**DataSorter.add_key(key, order, custom_list)**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOrder-list). Cependant, cette méthode ne fonctionne que si les éléments de la liste personnalisée ne contiennent pas de virgules à l'intérieur. S'ils contiennent des virgules comme "États-Unis, US", "Chine, CN", etc., alors vous devez utiliser la méthode [**DataSorter.add_key(key, order, custom_list)**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOrder-list). Ici, le dernier paramètre n'est pas une chaîne mais un tableau de chaînes.

## **Trier les données dans une colonne avec une liste de tri personnalisée**

Le code d'exemple suivant explique comment utiliser la méthode [**DataSorter.add_key(key, order, custom_list)**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOrder-list) pour trier des données avec une liste de tri personnalisée. Veuillez consulter le [fichier Excel d'exemple](50528327.xlsx) utilisé dans ce code et le [fichier Excel de sortie](50528328.xlsx) généré par celui-ci. La capture d'écran suivante montre l'effet du code sur le fichier Excel d'exemple lors de son exécution.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-SortDataInColumnWithCustomSortList.py" >}}
{{< app/cells/assistant language="python-net" >}}
