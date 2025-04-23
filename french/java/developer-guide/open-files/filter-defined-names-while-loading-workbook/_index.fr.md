---
title: Filtrer les noms définis lors du chargement du classeur
type: docs
weight: 50
url: /fr/java/filter-defined-names-while-loading-workbook/
---

## **Scénarios d'utilisation possibles**

Aspose.Cells vous permet de filtrer ou de supprimer les noms définis présents dans le classeur. Veuillez utiliser [**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED-NAMES) pour charger les noms définis et utilisez ~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED-NAMES) pour les supprimer lors du chargement du classeur. Veuillez noter que si vous supprimez les noms définis, alors les formules à l'intérieur du classeur peuvent être altérées.

## **Filtrer les noms définis lors du chargement du classeur**

Le code d'exemple suivant charge le [fichier Excel d'exemple](61767873.xlsx) qui contient une formule dans la cellule C1 contenant les noms définis, c'est-à-dire *=SUM(MyName1, MyName2)*. Puisque nous utilisons ~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED-NAMES) pour supprimer les noms définis lors du chargement du classeur, la formule dans la cellule C1 du [fichier Excel de sortie](61767872.xlsx) se rompt et vous voyez *#NAME?* à la place. Veuillez consulter la capture d'écran suivante qui montre l'effet du code sur le fichier Excel d'exemple.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Workbook-FilterDefinedNamesWhileLoadingWorkbook.java" >}}
{{< app/cells/assistant language="java" >}}
