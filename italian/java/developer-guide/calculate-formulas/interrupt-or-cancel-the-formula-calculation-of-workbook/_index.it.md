---
title: Interrompere o annullare il calcolo della formula della cartella di lavoro
type: docs
weight: 30
url: /it/java/interrupt-or-cancel-the-formula-calculation-of-workbook/
---
## **Possibili scenari di utilizzo**

Aspose.Cells fornisce un meccanismo per interrompere o annullare il calcolo della formula della cartella di lavoro utilizzando il metodo interrupt() del[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor) classe. Ciò è utile quando il calcolo della formula della cartella di lavoro richiede troppo tempo e si desidera annullarne l'elaborazione.

## **Interrompere o annullare il calcolo della formula della cartella di lavoro**

Il codice di esempio seguente implementa il[**primaCalcola()**](https://reference.aspose.com/cells/java/com.aspose.cells/abstractcalculationmonitor#beforeCalculate(int,%20int,%20int)) metodo del[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor)classe. All'interno di questo metodo, trova il nome della cella utilizzando i parametri dell'indice di riga e colonna. Se il nome della cella è B8, interrompe il processo di calcolo chiamando il metodo AbstractCalculationMonitor.interrupt(). Una volta, la classe concreta di[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor)class è implementata, la sua istanza è assegnata a[**CalculationOptions.CalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#CalculationMonitor)proprietà. Infine,[**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(com.aspose.cells.CalculationOptions)) è chiamato passando[**Opzioni di calcolo**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationOptions)come parametro. Si prega di consultare il[esempio di file Excel](51740744.xlsx)utilizzato all'interno del codice così come l'output della console del codice indicato di seguito per riferimento.

## **Codice d'esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.java" >}}

## **Uscita console**

{{< highlight "java" >}}

0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
