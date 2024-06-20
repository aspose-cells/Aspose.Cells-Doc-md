---
title: Interrompere o Annullare il Calcolo della Formula del Workbook
description: Questo articolo introduce come usare la libreria Aspose.Cells per interrompere o annullare il calcolo delle formule dei workbooks in Microsoft Excel. Caricando un file Excel esistente o creandone uno nuovo, possiamo usare i metodi forniti da Aspose.Cells per interrompere o annullare il calcolo della formula e ottenere il risultato. Infine, salviamo il file Excel modificato su disco.
keywords: Aspose.Cells, Excel, workbooks, calcoli delle formule, interruzioni, annullamenti
type: docs
weight: 50
url: /it/net/interrupt-or-cancel-the-formula-calculation-of-workbook/
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells fornisce un meccanismo per interrompere o annullare il calcolo delle formule su un workbook utilizzando il metodo [**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt). Questo è utile quando il calcolo delle formule del workbook sta richiedendo troppo tempo e si desidera annullarne l'elaborazione.

## **Interrompere o annullare il calcolo della formula del foglio di lavoro**

Il seguente codice di esempio implementa il metodo [**BeforeCalculate()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/beforecalculate) della classe [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor). All'interno di questo metodo, trova il nome della cella utilizzando i parametri dell'indice di riga e colonna. Se il nome della cella è B8, interrompe il processo di calcolo chiamando il metodo [**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt). Una volta implementata la classe concreta della classe [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor), la sua istanza viene assegnata alla proprietà [**CalculationOptions.CalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/calculationmonitor). Infine, viene chiamato [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index) passando [**CalculationOptions**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions) come parametro. Si prega di vedere il [file Excel di esempio](51740731.xlsx) utilizzato all'interno del codice e l'output della console del codice sottostante come riferimento.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.cs" >}}

## **Output della console**

{{< highlight java >}}

 0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
