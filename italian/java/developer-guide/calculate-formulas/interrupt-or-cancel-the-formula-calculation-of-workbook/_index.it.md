---
title: Interrompere o Annullare il Calcolo della Formula del Workbook
type: docs
weight: 30
url: /it/java/interrupt-or-cancel-the-formula-calculation-of-workbook/
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells fornisce un meccanismo per interrompere o annullare il calcolo della formula del foglio di lavoro utilizzando il metodo interrupt() della classe [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor). Questo è utile quando il calcolo della formula del foglio di lavoro sta richiedendo troppo tempo e si desidera annullarne l'elaborazione.

## **Interrompere o annullare il calcolo della formula del foglio di lavoro**

Il seguente codice di esempio implementa il metodo [**beforeCalculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/abstractcalculationmonitor#beforeCalculate(int,%20int,%20int)) della classe [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor). All'interno di questo metodo, trova il nome della cella utilizzando i parametri dell'indice di riga e colonna. Se il nome della cella è B8, interrompe il processo di calcolo chiamando il metodo AbstractCalculationMonitor.interrupt(). Una volta implementata la classe concreta della classe [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor), la sua istanza viene assegnata alla proprietà [**CalculationOptions.CalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#CalculationMonitor). Infine, si chiama [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(com.aspose.cells.CalculationOptions)) passando [**CalculationOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationOptions) come parametro. Si prega di vedere il[sample file Excel](51740744.xlsx) utilizzato all'interno del codice così come l'output della console del codice seguente per riferimento.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.java" >}}

## **Output della console**

{{< highlight java >}}

0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
