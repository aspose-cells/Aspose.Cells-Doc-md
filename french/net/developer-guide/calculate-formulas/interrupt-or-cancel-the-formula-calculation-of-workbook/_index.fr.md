---
title: Interrompre ou annuler le calcul de formule du classeur
description: Cet article présente comment utiliser la bibliothèque Aspose.Cells pour interrompre ou annuler les calculs de formules des classeurs dans Microsoft Excel. En chargeant un fichier Excel existant ou en en créant un nouveau, nous pouvons utiliser les méthodes fournies par Aspose.Cells pour interrompre ou annuler le calcul de formule et obtenir le résultat. Enfin, nous enregistrons le fichier Excel modifié sur le disque.
keywords: Aspose.Cells, Excel, classeurs, calculs de formules, interruptions, annulations
type: docs
weight: 50
url: /fr/net/interrupt-or-cancel-the-formula-calculation-of-workbook/
---

## **Scénarios d'utilisation possibles**

Aspose.Cells fournit un mécanisme pour interrompre ou annuler le calcul de formules du classeur en utilisant la méthode [**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt). Cela est utile lorsque le calcul de formules du classeur prend trop de temps et que vous souhaitez annuler son traitement.

## **Interrompre ou annuler le calcul de formule du classeur**

Le code d'échantillon suivant implémente la méthode [**BeforeCalculate()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/beforecalculate) de la classe [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor). À l'intérieur de cette méthode, il recherche le nom de la cellule en utilisant les paramètres d'index de ligne et de colonne. Si le nom de la cellule est B8, il interrompt le processus de calcul en appelant la méthode [**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt). Une fois que la classe concrète de la classe [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor) est implémentée, son instance est attribuée à la propriété [**CalculationOptions.CalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/calculationmonitor). Enfin, [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index) est appelé en passant [**CalculationOptions**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions) en tant que paramètre. Veuillez consulter le [fichier Excel d'exemple](51740731.xlsx) utilisé dans le code ainsi que la sortie de la console du code ci-dessous pour plus de détails.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.cs" >}}

## **Sortie console**

{{< highlight java >}}

 0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
