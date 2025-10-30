---
title: Calcolo della formula di array di tabelle dati con Golang tramite C++
linktitle: Calcolo della Formula Array delle Tabelle Dati
description: Come usare la libreria Aspose.Cells per calcolare le formule di array per una tabella dati in Microsoft Excel con Golang tramite C++. Caricando un file Excel esistente o creando uno nuovo, possiamo usare il metodo fornito da Aspose.Cells per calcolare la formula di array della tabella dati e ottenere il risultato. Infine, salviamo il file Excel modificato su disco.
keywords: Aspose.Cells, Excel, tabelle dati, formule di array, calcoli, C++
type: docs
weight: 70
url: /it/go-cpp/calculation-of-array-formula-of-data-tables/
---

{{% alert color="primary" %}}

È possibile creare una tabella dati in Microsoft Excel utilizzando Dati > Analisi if > Tabella dati... Aspose.Cells ora consente di calcolare la formula matrice di una tabella dati. Si prega di utilizzare [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) come normale per calcolare qualsiasi tipo di formula.

{{% /alert %}}

Nel seguente codice di esempio, abbiamo utilizzato il [file Excel di origine](5115535.xlsx). Se si cambia il valore della cella B1 a 100, i valori della tabella dati riempiti con il colore giallo diventeranno 120 come mostrato nelle immagini seguenti. Il codice di esempio genera il [PDF di output](5115538.pdf).

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

Ecco il codice di esempio utilizzato per generare il [PDF di output](5115538.pdf) dal [file Excel di origine](5115535.xlsx). Si prega di leggere i commenti per ulteriori informazioni.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CalculationOfArrayFormulaOfDataTables.go" >}}
