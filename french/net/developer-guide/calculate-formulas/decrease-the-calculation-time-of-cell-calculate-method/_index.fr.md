---
title: Réduire le temps de calcul de la méthode Cell.Calculate
description: Cet article présente comment utiliser la bibliothèque Aspose.Cells pour réduire le temps de calcul de la méthode de calcul des cellules dans Microsoft Excel. En chargeant un fichier Excel existant ou en en créant un nouveau, nous pouvons utiliser les méthodes fournies par Aspose.Cells pour optimiser la méthode de calcul des cellules et améliorer ses performances. Finalement, nous enregistrons le fichier Excel modifié sur le disque.
keywords: Aspose.Cells, Excel, méthodes de calcul des cellules, optimisation, performances, réduction du temps de calcul
type: docs
weight: 100
url: /fr/net/decrease-the-calculation-time-of-cell-calculate-method/
---

## **Scénarios d'utilisation possibles**

Normalement, nous recommandons aux utilisateurs d'appeler la méthode [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index) une fois, puis d'obtenir les valeurs calculées des cellules individuelles. Mais parfois, les utilisateurs ne veulent pas calculer l'ensemble du classeur. Ils veulent juste calculer une seule cellule. Aspose.Cells fournit la propriété [**CalculationOptions.Recursive**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive) que vous pouvez définir sur **false** et elle diminuera considérablement le temps de calcul de la cellule individuelle. En effet, lorsque la propriété récursive est définie sur **true**, alors toutes les dépendances des cellules sont recalculées à chaque appel. Mais lorsque la propriété récursive est **false**, alors les cellules dépendantes ne sont calculées qu'une seule fois et ne sont pas recalculées lors des appels ultérieurs.

## **Diminuer le temps de calcul de la méthode Cell.Calculate()**

Le code d'exemple suivant illustre l'utilisation de la propriété [**CalculationOptions.Recursive**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive). Veuillez exécuter ce code avec le fichier Excel d'exemple donné et vérifiez sa sortie console. Vous constaterez que le fait de définir la propriété récursive sur **false** a considérablement diminué le temps de calcul. Veuillez également lire les commentaires pour mieux comprendre cette propriété.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-1.cs" >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-TestCalcTimeRecursive.cs" >}}

## **Sortie console**

Il s'agit de la sortie console du code d'exemple ci-dessus lors de son exécution avec le fichier Excel d'exemple donné sur notre machine. Veuillez noter que votre sortie peut différer, mais le temps écoulé après avoir défini la propriété récursive sur **false** sera toujours inférieur à sa définition sur **true**.

{{< highlight java >}}

Recursive True: 96 seconds

Recursive False: 42 seconds

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
