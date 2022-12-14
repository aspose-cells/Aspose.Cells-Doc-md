---
title: Obtenir des avertissements lors du chargement du fichier Excel
type: docs
weight: 60
url: /fr/java/get-warnings-while-loading-excel-file/
---
## **Scénarios d'utilisation possibles**

Parfois, l'utilisateur essaie de charger le classeur qui est quelque peu corrompu mais chargeable. Dans ce cas, Aspose.Cells lance des avertissements lors du chargement du classeur. Vous pouvez intercepter ces avertissements en implémentant le**[IWarningCallback](https://reference.aspose.com/cells/java/com.aspose.cells/IWarningCallback)** interface et réglage**[LoadOptions.WarningCallback](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#WarningCallback)**propriété.

## **Obtenir des avertissements lors du chargement du fichier Excel**

 L'exemple de code suivant explique comment obtenir des avertissements lors du chargement d'un fichier Excel. Le code charge le[exemple de fichier excel](sampleDuplicateDefinedName.xlsx) qui jette**[DuplicateDefinedName](https://reference.aspose.com/cells/java/com.aspose.cells/warningtype#DUPLICATE_DEFINED_NAME)** avertissement au chargement. Cet avertissement est alors intercepté par**[IWarningCallback.Warning()](https://reference.aspose.com/cells/java/com.aspose.cells/iwarningcallback#warning(com.aspose.cells.WarningInfo))** méthode qui imprime les messages d'avertissement sur la console. Le code enregistre ensuite le classeur sous[fichier excel de sortie](outputDuplicateDefinedName.xlsx)Si vous ouvrez l'exemple de fichier Excel dans Microsoft Excel, il vous affichera également cet avertissement, comme indiqué dans cette capture d'écran. Veuillez également vérifier la sortie de la console du code ci-dessous pour plus de compréhension.

![tâche : image_autre_texte](get-warnings-while-loading-excel-file_1.png)

## **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-WarningCallback-WarningCallback.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-GetWarningLoadingAnExcel-GetWarningLoadingAnExcel.java" >}}

## **Sortie console**

 Voici la sortie de la console du code ci-dessus lorsqu'il est exécuté avec le fourni[exemple de fichier excel](sampleDuplicateDefinedName.xlsx).

{{< highlight "java" >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
