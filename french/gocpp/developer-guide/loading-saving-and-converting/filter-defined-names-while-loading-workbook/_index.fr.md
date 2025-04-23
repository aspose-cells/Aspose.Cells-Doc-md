---
title: Filtrer les noms définis lors du chargement du classeur
type: docs
weight: 50
url: /fr/go-cpp/filter-defined-names-while-loading-workbook/
---

## **Scénarios d'utilisation possibles**

Aspose.Cells vous permet de filtrer ou de supprimer les noms définis présents dans le classeur. Veuillez utiliser [**LoadDataFilterOptions_DefinedNames**](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions/) pour charger les noms définis lors du chargement du classeur. Notez que si vous supprimez les noms définis, les formules à l’intérieur du classeur peuvent ne plus fonctionner.

## **Filtrer les noms définis lors du chargement du classeur**

Le code d'exemple suivant charge le [fichier Excel d'exemple](61767860.xlsx), qui a une formule dans la cellule **C1** contenant les noms définis, c’est-à-dire, *=SUM(MyName1, MyName2)*. Comme nous utilisons ~[**LoadDataFilterOptions_DefinedNames**](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions/) pour supprimer les noms définis lors du chargement du classeur, la formule dans la cellule C1 dans le [fichier Excel de sortie](61767861.xlsx) se brise, et vous voyez à la place *#NAME?*. Voir la capture d'écran suivante montrant l'effet du code sur le fichier Excel d'exemple.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilterDefinedNamesWhileLoadingWorkbook.go" >}}
