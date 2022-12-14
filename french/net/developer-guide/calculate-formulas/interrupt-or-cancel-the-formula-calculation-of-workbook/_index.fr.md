---
title: Interrompre ou annuler le calcul de la formule du classeur
type: docs
weight: 50
url: /fr/net/interrupt-or-cancel-the-formula-calculation-of-workbook/
---
## **Scénarios d'utilisation possibles**

Aspose.Cells fournit un mécanisme pour interrompre ou annuler le calcul de la formule du classeur à l'aide de la[**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt)méthode. Ceci est utile lorsque le calcul de la formule du classeur prend trop de temps et que vous souhaitez annuler son traitement.

## **Interrompre ou annuler le calcul de la formule du classeur**

L'exemple de code suivant implémente le[**AvantCalcul()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/beforecalculate)méthode de[**RésuméCalculMoniteur**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor) classer. Dans cette méthode, il trouve le nom de la cellule à l'aide des paramètres d'index de ligne et de colonne. Si le nom de la cellule est B8, il interrompt le processus de calcul en appelant le[**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt)méthode. Autrefois, la classe concrète de[**RésuméCalculMoniteur**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor)classe est implémentée, son instance est affectée à[**CalculationOptions.CalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/calculationmonitor)propriété. Pour terminer,[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index)s'appelle en passant[**Options de calcul**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions) comme paramètre. Veuillez consulter le[exemple de fichier Excel](51740731.xlsx) utilisé à l'intérieur du code ainsi que la sortie console du code donné ci-dessous pour référence.

## **Exemple de code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.cs" >}}

## **Sortie console**

{{< highlight "java" >}}

 0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
