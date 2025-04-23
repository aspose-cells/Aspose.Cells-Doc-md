---
title: Interrompre ou annuler le calcul de formule du classeur
type: docs
weight: 30
url: /fr/java/interrupt-or-cancel-the-formula-calculation-of-workbook/
---

## **Scénarios d'utilisation possibles**

Aspose.Cells fournit un mécanisme pour interrompre ou annuler le calcul de formule du classeur en utilisant la méthode interrupt() de la classe [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor). Cela est utile lorsque le calcul de formule du classeur prend trop de temps et que vous souhaitez annuler son traitement.

## **Interrompre ou annuler le calcul de formule du classeur**

Le code d'exemple suivant implémente la méthode [**beforeCalculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/abstractcalculationmonitor#beforeCalculate-int-int-int-) de la classe [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor). À l'intérieur de cette méthode, il trouve le nom de la cellule en utilisant les paramètres d'index de ligne et de colonne. Si le nom de la cellule est B8, il interrompt le processus de calcul en appelant la méthode AbstractCalculationMonitor.interrupt(). Une fois que la classe concrète de la classe [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor) est implémentée, son instance est attribuée à la propriété [**CalculationOptions.CalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#CalculationMonitor). Enfin, [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula-com.aspose.cells.CalculationOptions-) est appelé en passant [**CalculationOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationOptions) en tant que paramètre. Veuillez consulter le [fichier Excel d'exemple](51740744.xlsx) utilisé dans le code ainsi que la sortie de la console du code ci-dessous pour référence.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.java" >}}

## **Sortie console**

{{< highlight java >}}

0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
