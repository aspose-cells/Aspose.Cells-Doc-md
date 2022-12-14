---
title: Filtrer les noms définis lors du chargement du classeur
type: docs
weight: 50
url: /fr/net/filter-defined-names-while-loading-workbook/
---
## **Scénarios d'utilisation possibles**

Aspose.Cells vous permet de filtrer ou de supprimer des noms définis présents dans le classeur. Veuillez utiliser[**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)pour charger les noms définis et utiliser ~[**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)pour les supprimer lors du chargement du classeur. Veuillez noter que si vous supprimez les noms définis, les formules à l'intérieur du classeur peuvent se briser.

## **Filtrer les noms définis lors du chargement du classeur**

 L'exemple de code suivant charge le[exemple de fichier Excel](61767860.xlsx) qui a une formule dans la cellule**C1** contenant les noms définis, c'est-à-dire*=SOMME(MonNom1, MonNom2)*. Puisque nous utilisons ~[**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) pour supprimer les noms définis lors du chargement du classeur, la formule de la cellule C1 dans[fichier Excel de sortie](61767861.xlsx) rompt et tu vois*#NAME?*Au lieu. Veuillez consulter la capture d'écran suivante qui montre l'effet du code sur l'exemple de fichier Excel.

![tâche : image_autre_texte](filter-defined-names-while-loading-workbook_1.png)

## **Exemple de code**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Workbook-FilterDefinedNamesWhileLoadingWorkbook.cs" >}}
