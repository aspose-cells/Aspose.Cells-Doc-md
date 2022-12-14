---
title: Diminuez le temps de calcul de la méthode Cell.Calculate
type: docs
weight: 860
url: /fr/java/decrease-the-calculation-time-of-cell-calculate-method/
---
Scénarios d'utilisation possibles

 Normalement, nous recommandons aux utilisateurs d'appeler[Workbook.CalculateFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula\(\) ) méthode une fois, puis obtenez les valeurs calculées des cellules individuelles. Mais parfois, les utilisateurs ne veulent pas calculer le classeur entier. Ils veulent juste calculer une seule cellule. Aspose.Cells fournit[CalculationOptions.Recursive](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#Recursive) propriété que vous pouvez définir**faux**et cela réduira considérablement le temps de calcul de chaque cellule. Parce que lorsque la propriété récursive est définie sur**vrai**, alors toutes les dépendances des cellules sont recalculées à chaque appel. Mais lorsque la propriété récursive est définie sur**faux**, les cellules dépendantes ne sont calculées qu'une seule fois et ne sont plus recalculées lors des appels suivants.
## **Diminuer le temps de calcul de la méthode Cell.Calculate()**
 L'exemple de code suivant illustre l'utilisation de[CalculationOptions.Recursive](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#Recursive) propriété. Veuillez exécuter ce code avec le[exemple de fichier excel](5472288.xlsx) et vérifiez sa sortie console. Vous constaterez que définir la propriété récursive sur**faux**a considérablement réduit le temps de calcul. Veuillez également lire les commentaires pour une meilleure compréhension de cette propriété.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DecreaseCalculationTime-DecreaseCalculationTime.java" >}}
## **Sortie console**
 Ceci est la sortie de la console de l'exemple de code ci-dessus lorsqu'il est exécuté avec le[exemple de fichier excel](5472288.xlsx) sur notre appareil. Veuillez noter que votre sortie peut différer, mais le temps écoulé après avoir défini la propriété récursive sur**faux** sera toujours inférieur au réglage**vrai**.



{{< highlight "java" >}}

 Recursive true: 51 seconds

Recursive false: 16 seconds

{{< /highlight >}}
