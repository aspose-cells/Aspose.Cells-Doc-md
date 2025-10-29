---
title: Réduire le temps de calcul de la méthode Cell.Calculate avec Golang via C++
linktitle: Diminuer le temps de calcul de Cell.Calculate
description: Cet article présente comment utiliser la bibliothèque Aspose.Cells pour réduire le temps de calcul de la méthode de calcul des cellules dans Microsoft Excel. En chargeant un fichier Excel existant ou en en créant un nouveau, nous pouvons utiliser les méthodes fournies par Aspose.Cells pour optimiser la méthode de calcul des cellules et améliorer ses performances. Finalement, nous enregistrons le fichier Excel modifié sur le disque.
keywords: Aspose.Cells, Excel, méthodes de calcul des cellules, optimisation, performances, réduction du temps de calcul
type: docs
weight: 100
url: /fr/go-cpp/decrease-the-calculation-time-of-cell-calculate-method/
---

## **Scénarios d'utilisation possibles**

Normalement, nous recommandons aux utilisateurs d'appeler la méthode [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) une fois, puis d'obtenir les valeurs calculées des cellules individuelles. Mais parfois, les utilisateurs ne veulent pas calculer tout le classeur. Ils souhaitent simplement calculer une seule cellule. Aspose.Cells fournit la propriété [**CalculationOptions.GetRecursive()**](https://reference.aspose.com/cells/cpp/aspose.cells/calculationoptions/getrecursive/) que vous pouvez définir sur **false** et cela réduira considérablement le temps de calcul des cellules individuelles. Parce que lorsque la propriété récursive est réglée sur **true**, tous les dépendants des cellules sont recalculés à chaque appel. Mais lorsque la propriété récursive est **false**, seules les cellules dépendantes sont calculées une fois et ne sont pas recalculées lors des appels suivants.

## **Diminuer le temps de calcul de la méthode Cell.Calculate()**

Le code d'exemple suivant illustre l'utilisation de la propriété [**CalculationOptions.GetRecursive()**](https://reference.aspose.com/cells/go-cpp/calculationoptions/getrecursive/). Exécutez ce code avec le [fichier Excel d'exemple](5113710.xlsx) fourni et vérifiez sa sortie console. Vous verrez que le fait de définir la propriété récursive sur **false** a considérablement réduit le temps de calcul. Veuillez également lire les commentaires pour une meilleure compréhension de cette propriété.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DecreaseTheCalculationTimeOfCellCalculateMethod.go" >}}
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DecreaseTheCalculationTimeOfCellCalculateMethod-1.go" >}}
## **Sortie console**

Ceci est la sortie console du code d'exemple ci-dessus lorsqu'il est exécuté avec le [fichier excel d'exemple](5113710.xlsx) sur notre machine. Veuillez noter que votre sortie peut différer, mais le temps écoulé après avoir défini la propriété récursive sur **false** sera toujours inférieur à celui lorsque cette propriété est sur **true**.

{{< highlight java >}}

Recursive True: 96 seconds

Recursive False: 42 seconds

{{< /highlight >}}
