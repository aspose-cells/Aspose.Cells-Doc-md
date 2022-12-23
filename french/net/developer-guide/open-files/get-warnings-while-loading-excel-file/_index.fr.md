---
title: Obtenir des avertissements lors du chargement du fichier Excel
type: docs
weight: 110
url: /fr/net/get-warnings-while-loading-excel-file/
---
## **Scénarios d'utilisation possibles**

Parfois, l'utilisateur essaie de charger le classeur qui est quelque peu corrompu mais chargeable. Dans ce cas, Aspose.Cells lance des avertissements lors du chargement du classeur. Vous pouvez intercepter ces avertissements en implémentant le**[IWarningCallback](https://reference.aspose.com/cells/net/aspose.cells/iwarningcallback)** interface et réglage**[LoadOptions.WarningCallback](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/warningcallback)**la propriété.

## **Obtenir des avertissements lors du chargement du fichier Excel**

 L'exemple de code suivant explique comment obtenir des avertissements lors du chargement d'un fichier Excel. Le code charge le[exemple de fichier excel](sampleDuplicateDefinedName.xlsx) qui jette**[DuplicateDefinedName](https://reference.aspose.com/cells/net/aspose.cells/warningtype)** avertissement au chargement. Cet avertissement est alors intercepté par**[IWarningCallback.Warning()](https://reference.aspose.com/cells/net/aspose.cells/iwarningcallback/methods/warning)** méthode qui imprime les messages d'avertissement sur la console. Le code enregistre ensuite le classeur sous[fichier excel de sortie](outputDuplicateDefinedName.xlsx)Si vous ouvrez l'exemple de fichier Excel dans Microsoft Excel, il vous affichera également cet avertissement, comme indiqué dans cette capture d'écran. Veuillez également vérifier la sortie de la console du code ci-dessous pour plus de compréhension.

![tâche : image_autre_texte](get-warnings-while-loading-excel-file_1.png)

## **Exemple de code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-GetWarningsWhileLoadingExcelFile.cs" >}}

## **Sortie console**

 Voici la sortie de la console du code ci-dessus lorsqu'il est exécuté avec le fourni[exemple de fichier excel](sampleDuplicateDefinedName.xlsx).

{{< highlight "java" >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
