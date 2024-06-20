---
title: Obtenir des avertissements lors du chargement du fichier Excel
type: docs
weight: 60
url: /fr/java/get-warnings-while-loading-excel-file/
---

## **Scénarios d'utilisation possibles**

Parfois, l'utilisateur essaie de charger le classeur qui est quelque peu corrompu mais chargeable. Dans ce cas, Aspose.Cells lance des avertissements lors du chargement du classeur. Vous pouvez attraper ces avertissements en implémentant l'interface [**IWarningCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IWarningCallback) et en réglant la propriété [**LoadOptions.WarningCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#WarningCallback).

## **Obtenir des avertissements lors du chargement d'un fichier Excel**

Le code d'exemple suivant explique comment obtenir des avertissements lors du chargement d'un fichier Excel. Le code charge le [fichier Excel d'exemple](sampleDuplicateDefinedName.xlsx) qui lance l'avertissement [**DuplicateDefinedName**](https://reference.aspose.com/cells/java/com.aspose.cells/warningtype#DUPLICATE_DEFINED_NAME) lors du chargement. Cet avertissement est ensuite capturé par la méthode [**IWarningCallback.Warning()**](https://reference.aspose.com/cells/java/com.aspose.cells/iwarningcallback#warning(com.aspose.cells.WarningInfo)) qui imprime les messages d'avertissement dans la console. Le code enregistre ensuite le classeur en tant que [fichier Excel de sortie](outputDuplicateDefinedName.xlsx). Si vous ouvrez le fichier Excel d'exemple dans Microsoft Excel, il affichera également cet avertissement comme le montre cette capture d'écran. Veuillez également vérifier la sortie de la console du code ci-dessous pour mieux comprendre.

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-WarningCallback-WarningCallback.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-GetWarningLoadingAnExcel-GetWarningLoadingAnExcel.java" >}}

## **Sortie console**

Voici la sortie de la console du code ci-dessus lors de son exécution avec le [fichier Excel d'exemple fourni](sampleDuplicateDefinedName.xlsx).

{{< highlight java >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
