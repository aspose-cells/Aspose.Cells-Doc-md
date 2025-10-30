---
title: Usare la funzione FormulaText in Aspose.Cells con Golang tramite C++
linktitle: Uso della funzione FormulaText
description: Questo articolo presenta come utilizzare la funzione FormulaText nella libreria Aspose.Cells per elaborare formule in Microsoft Excel. Caricando un file Excel esistente o creandone uno nuovo, possiamo utilizzare il metodo fornito da Aspose.Cells per ottenere e impostare il testo della formula della cella e ottenere il risultato. Infine, salviamo il file Excel modificato su disco.
keywords: Aspose.Cells, Excel, funzioni FormulaText
type: docs
weight: 60
url: /it/go-cpp/using-formulatext-function-in-aspose-cells/
---

{{% alert color="primary" %}} 

FormulaText è una funzione di Excel 2013 e versioni successive. Non è supportata dalle versioni precedenti come Excel 2010 o 2007, ecc. Come suggerisce il suo nome, stampa il testo della formula presente in una determinata cella. Questo articolo mostrerà come utilizzare questa funzione utilizzando Aspose.Cells.

{{% /alert %}} 

Il seguente codice di esempio mostra l'uso di FormulaText con Aspose.Cells. Il codice scrive prima una formula nella cella A1 e poi stampa il testo della formula utilizzando FormulaText nella cella A2.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UsingFormulatextFunctionInAsposeCells.go" >}}
## **Output della console**
Ecco l'output della console del codice di esempio sopra.

{{< highlight java >}}

 =SUM(B1:B10)

{{< /highlight >}}
