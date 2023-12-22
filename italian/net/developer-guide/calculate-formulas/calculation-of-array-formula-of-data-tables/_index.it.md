---
title: Calcolo della formula di matrice delle tabelle di dati
description: Come utilizzare la libreria Aspose.Cells per calcolare le formule di matrice per una tabella dati in Microsoft Excel. Caricando un file Excel esistente o creando un nuovo file Excel, possiamo utilizzare il metodo fornito da Aspose.Cells per calcolare la formula matriciale della tabella dati e ottenere il risultato. Infine, salviamo il file Excel modificato su disco.
keywords: Aspose.Cells, Excel, data tables, array formulas, calculations
type: docs
weight: 70
url: /it/net/calculation-of-array-formula-of-data-tables/
---
{{% alert color="primary" %}}

È possibile creare una tabella dati in Microsoft Excel utilizzando Dati > Analisi what-if > Tabella dati.... Aspose.Cells ora consente di calcolare la formula di matrice di una tabella dati. Si prega di utilizzare[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) come normale per il calcolo di qualsiasi tipo di formula.

{{% /alert %}}

Nel seguente codice di esempio è stato utilizzato il file[file Excel di origine](5115535.xlsx) . Se modifichi il valore della cella B1 in 100, i valori della tabella dati riempiti con il colore giallo diventeranno 120 come mostrato nelle immagini seguenti. Il codice di esempio genera il file[uscita PDF](5115538.pdf).

![cose da fare:immagine_alt_testo](calculation-of-array-formula-of-data-tables_1.png)

![cose da fare:immagine_alt_testo](calculation-of-array-formula-of-data-tables_2.png)

 Ecco il codice di esempio utilizzato per generare il file[uscita PDF](5115538.pdf) dal[file Excel di origine](5115535.xlsx). Si prega di leggere i commenti per ulteriori informazioni.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-CalculationOfArrayFormula-CalculateArrayFormula.cs" >}}
