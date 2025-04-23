---
title: Filtrer les noms définis lors du chargement du classeur
type: docs
weight: 50
url: /fr/net/filter-defined-names-while-loading-workbook/
---

## **Scénarios d'utilisation possibles**

Aspose.Cells vous permet de filtrer ou de supprimer les noms définis présents dans le classeur. Veuillez utiliser [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) pour charger les noms définis et utilisez ~[**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) pour les supprimer lors du chargement du classeur. Veuillez noter que si vous supprimez les noms définis, alors les formules à l'intérieur du classeur peuvent être altérées.

## **Filtrer les noms définis lors du chargement du classeur**

La code d'exemple suivant charge le [fichier Excel exemple](61767860.xlsx) qui contient une formule dans la cellule **C1** contenant les noms définis, c'est-à-dire *=SUM(MyName1, MyName2)*. Comme nous utilisons ~[**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) pour supprimer les noms définis lors du chargement du classeur, la formule dans la cellule C1 dans le [fichier Excel de sortie](61767861.xlsx) est altérée et vous voyez *#NAME?* à la place. Veuillez consulter la capture d'écran suivante qui montre l'effet du code sur le fichier Excel exemple.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Workbook-FilterDefinedNamesWhileLoadingWorkbook.cs" >}}
{{< app/cells/assistant language="csharp" >}}
