---
title: Interrompre ou annuler le calcul de la formule du classeur
type: docs
weight: 30
url: /fr/java/interrupt-or-cancel-the-formula-calculation-of-workbook/
---
## **Scénarios d'utilisation possibles**

Aspose.Cells fournit un mécanisme pour interrompre ou annuler le calcul de la formule du classeur à l'aide de la méthode interrupt() du[**RésuméCalculMoniteur**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor) classer. Ceci est utile lorsque le calcul de la formule du classeur prend trop de temps et que vous souhaitez annuler son traitement.

## **Interrompre ou annuler le calcul de la formule du classeur**

L'exemple de code suivant implémente le[**avantCalcul()**](https://reference.aspose.com/cells/java/com.aspose.cells/abstractcalculationmonitor#beforeCalculate(int,%20int,%20int)) méthode de la[**RésuméCalculMoniteur**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor)classer. Dans cette méthode, il trouve le nom de la cellule à l'aide des paramètres d'index de ligne et de colonne. Si le nom de la cellule est B8, il interrompt le processus de calcul en appelant la méthode AbstractCalculationMonitor.interrupt(). Autrefois, la classe concrète de[**RésuméCalculMoniteur**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor)classe est implémentée, son instance est affectée à[**CalculationOptions.CalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#CalculationMonitor)propriété. Pour terminer,[**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(com.aspose.cells.CalculationOptions)) s'appelle en passant[**Options de calcul**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationOptions)comme paramètre. Veuillez consulter le[exemple de fichier Excel](51740744.xlsx)utilisé à l'intérieur du code ainsi que la sortie console du code donné ci-dessous pour référence.

## **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.java" >}}

## **Sortie console**

{{< highlight "java" >}}

0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
