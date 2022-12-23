---
title: Diminuez le temps de calcul de la méthode Cell.Calculate
type: docs
weight: 100
url: /fr/net/decrease-the-calculation-time-of-cell-calculate-method/
---
## **Scénarios d'utilisation possibles**

Normalement, nous recommandons aux utilisateurs d'appeler[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index)méthode une fois, puis obtenir les valeurs calculées des cellules individuelles. Mais parfois, les utilisateurs ne veulent pas calculer le classeur entier. Ils veulent juste calculer une seule cellule. Aspose.Cells fournit[**CalculationOptions.Recursive**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive) propriété sur laquelle vous pouvez définir**faux** et cela réduira considérablement le temps de calcul de chaque cellule. Parce que lorsque la propriété récursive est définie sur**vrai** , alors toutes les dépendances des cellules sont recalculées à chaque appel. Mais lorsque la propriété récursive est**faux**, les cellules dépendantes ne sont calculées qu'une seule fois et ne sont plus recalculées lors des appels suivants.

## **Diminuer le temps de calcul de la méthode Cell.Calculate()**

 L'exemple de code suivant illustre l'utilisation de[**CalculationOptions.Recursive**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive) la propriété. Veuillez exécuter ce code avec le[exemple de fichier excel](5113710.xlsx) et vérifiez sa sortie console. Vous constaterez que définir la propriété récursive sur**faux**a considérablement réduit le temps de calcul. Veuillez également lire les commentaires pour une meilleure compréhension de cette propriété.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-1.cs" >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-TestCalcTimeRecursive.cs" >}}

## **Sortie console**

 Ceci est la sortie de la console de l'exemple de code ci-dessus lorsqu'il est exécuté avec le[exemple de fichier excel](5113710.xlsx) sur notre appareil. Veuillez noter que votre sortie peut différer, mais le temps écoulé après avoir défini la propriété récursive sur**faux** sera toujours inférieur au réglage**vrai**.

{{< highlight "java" >}}

Recursive True: 96 seconds

Recursive False: 42 seconds

{{< /highlight >}}
