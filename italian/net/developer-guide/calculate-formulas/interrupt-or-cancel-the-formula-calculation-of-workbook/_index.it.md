---
title: Interrompere o annullare il calcolo della formula della cartella di lavoro
type: docs
weight: 50
url: /it/net/interrupt-or-cancel-the-formula-calculation-of-workbook/
---
## **Possibili scenari di utilizzo**

Aspose.Cells fornisce un meccanismo per interrompere o annullare il calcolo della formula della cartella di lavoro utilizzando il[**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt)metodo. Ciò è utile quando il calcolo della formula della cartella di lavoro richiede troppo tempo e si desidera annullarne l'elaborazione.

## **Interrompere o annullare il calcolo della formula della cartella di lavoro**

Il codice di esempio seguente implementa il[**Prima di Calcola()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/beforecalculate)metodo di[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor) classe. All'interno di questo metodo, trova il nome della cella utilizzando i parametri dell'indice di riga e colonna. Se il nome della cella è B8, interrompe il processo di calcolo chiamando il file[**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt)metodo. Una volta, la classe concreta di[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor)class è implementata, la sua istanza è assegnata a[**CalculationOptions.CalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/calculationmonitor)proprietà. Infine,[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index)è chiamato di passaggio[**Opzioni di calcolo**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions) come parametro. Si prega di consultare il[esempio di file Excel](51740731.xlsx) utilizzato all'interno del codice così come l'output della console del codice indicato di seguito per riferimento.

## **Codice di esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.cs" >}}

## **Uscita console**

{{< highlight "java" >}}

 0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
