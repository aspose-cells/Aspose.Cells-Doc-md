---
title: Diminuez le temps de calcul de Cell. Méthode de calcul
description: Cet article explique comment utiliser la bibliothèque Aspose.Cells pour réduire le temps de calcul des méthodes de calcul de cellules dans Excel Microsoft. En chargeant un fichier Excel existant ou en en créant un nouveau, nous pouvons utiliser les méthodes fournies par Aspose.Cells pour optimiser la méthode de calcul des cellules et améliorer ses performances. Enfin, nous enregistrons le fichier Excel modifié sur le disque.
keywords: Aspose.Cells, Excel, Cell calculation methods, optimization, performance, reduction of calculation time
type: docs
weight: 100
url: /fr/net/decrease-the-calculation-time-of-cell-calculate-method/
---
##  **Scénarios d'utilisation possibles**

Normalement, nous recommandons aux utilisateurs d'appeler[**Classeur.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index)méthode une fois, puis obtenez les valeurs calculées des cellules individuelles. Mais parfois, les utilisateurs ne souhaitent pas calculer l’intégralité du classeur. Ils veulent juste calculer une seule cellule. Aspose.Cells fournit[**CalculationOptions.Récursif**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive) propriété que vous pouvez définir sur**FAUX**et cela réduira considérablement le temps de calcul de chaque cellule. Car lorsque la propriété récursive est définie sur *true**, alors toutes les dépendances des cellules sont recalculées à chaque appel. Mais lorsque la propriété récursive est *false**, alors les cellules dépendantes ne sont calculées qu'une seule fois et ne sont pas calculées à nouveau lors des appels ultérieurs.

##  **Diminuer le temps de calcul de la méthode Cell.Calculate()**

 L'exemple de code suivant illustre l'utilisation de[**CalculationOptions.Récursif**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive) propriété. Veuillez exécuter ce code avec le donné[exemple de fichier Excel](5113710.xlsx) et vérifiez sa sortie de console. Vous constaterez que définir la propriété récursive sur**FAUX**considérablement réduit le temps de calcul. Merci de lire également les commentaires pour une meilleure compréhension de ce bien.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-1.cs" >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-TestCalcTimeRecursive.cs" >}}

##  **Sortie console**

 Il s'agit de la sortie console de l'exemple de code ci-dessus lorsqu'il est exécuté avec le paramètre donné.[exemple de fichier Excel](5113710.xlsx) sur notre machine. Veuillez noter que votre sortie peut différer, mais le temps écoulé après avoir défini la propriété récursive sur**FAUX**sera toujours inférieur à la valeur *true**.

{{< highlight "java" >}}

Recursive True: 96 seconds

Recursive False: 42 seconds

{{< /highlight >}}
