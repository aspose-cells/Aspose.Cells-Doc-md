---
title: Interrompere o annullare il calcolo della formula della cartella di lavoro
description: Questo articolo illustra come utilizzare la libreria Aspose.Cells per interrompere o annullare i calcoli delle formule delle cartelle di lavoro in Microsoft Excel. Caricando un file Excel esistente o creandone uno nuovo, possiamo utilizzare i metodi forniti dallo Aspose.Cells per interrompere o annullare il calcolo della formula e ottenere il risultato. Infine, salviamo il file Excel modificato su disco.
keywords: Aspose.Cells, Excel, workbooks, formula calculations, breaks, cancellations
type: docs
weight: 50
url: /it/net/interrupt-or-cancel-the-formula-calculation-of-workbook/
---
##  **Possibili scenari di utilizzo**

Aspose.Cells fornisce un meccanismo per interrompere o annullare il calcolo della formula della cartella di lavoro utilizzando il file[**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt)metodo. Ciò è utile quando il calcolo della formula della cartella di lavoro richiede troppo tempo e si desidera annullarne l'elaborazione.

##  **Interrompere o annullare il calcolo della formula della cartella di lavoro**

Il seguente codice di esempio implementa il[**BeforeCalculate()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/beforecalculate)metodo di[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor) classe. All'interno di questo metodo, trova il nome della cella utilizzando i parametri di indice di riga e colonna. Se il nome della cella è B8, interrompe il processo di calcolo chiamando il file[**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt)metodo. Una volta, la classe concreta di[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor)viene implementata la classe, a cui viene assegnata la sua istanza[**CalculationOptions.CalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/calculationmonitor)proprietà. Finalmente,[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index)si chiama passando[**Opzioni di calcolo**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions) come parametro. Si prega di consultare il[file Excel di esempio](51740731.xlsx) utilizzato all'interno del codice così come l'output della console del codice fornito di seguito come riferimento.

##  **Codice d'esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.cs" >}}

##  **Uscita della console**

{{< highlight "java" >}}

 0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
