---
title: Calcolo della formula di matrice delle tabelle di dati
type: docs
weight: 550
url: /it/java/calculation-of-array-formula-of-data-tables/
---
{{% alert color="primary" %}} 

 È possibile creare la tabella dati in Microsoft Excel utilizzando Dati > Analisi what-if > Tabella dati.... Aspose.Cells consente ora di calcolare la formula di matrice della tabella dati. Si prega di utilizzare[Workbook.calculateFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula\(\)) come normale per il calcolo di qualsiasi tipo di formule.

{{% /alert %}} 
## **Calcolo della formula di matrice delle tabelle di dati**
 Nel seguente codice di esempio, abbiamo utilizzato this[file excel di origine](5472579.xlsx) che è mostrato anche nell'immagine seguente.

![cose da fare:immagine_alt_testo](calculation-of-array-formula-of-data-tables_1.png)

 Se si modifica il valore della cella B1 in 100, i valori della tabella dati che sono riempiti con il colore giallo diventeranno 120. Il codice di esempio genera il[uscita PDF](5472577.pdf) che mostra 120 come valori nella tabella dati come mostrato in questa immagine.

![cose da fare:immagine_alt_testo](calculation-of-array-formula-of-data-tables_2.png)

Ecco il codice di esempio utilizzato per generare il file[uscita PDF](5472577.pdf) dal[file excel di origine](5472579.xlsx). Si prega di leggere i commenti per ulteriori informazioni.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CalculationOfArrayFormula-CalculationOfArrayFormula.java" >}}
