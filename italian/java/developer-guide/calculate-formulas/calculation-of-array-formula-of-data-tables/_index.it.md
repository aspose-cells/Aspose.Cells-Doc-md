---
title: Calcolo della Formula Array delle Tabelle Dati
type: docs
weight: 550
url: /it/java/calculation-of-array-formula-of-data-tables/
---

{{% alert color="primary" %}} 

È possibile creare una tabella dati in Microsoft Excel usando Dati > Analisi di Scenario > Tabella Dati.... Aspose.Cells consente ora di calcolare la formula matriciale della tabella dati. Si prega di utilizzare [Workbook.calculateFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula\(\)) come al solito per calcolare qualsiasi tipo di formule.

{{% /alert %}} 
## **Calcolo della formula matriciale delle tabelle dei dati**
Nel seguente codice di esempio, abbiamo utilizzato questo [file excel di origine](5472579.xlsx) che è anche mostrato nell'immagine seguente.

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

Se si modifica il valore della cella B1 in 100, i valori della tabella dati riempiti con il colore giallo diventeranno 120. Il codice di esempio genera il [PDF di output](5472577.pdf) che mostra 120 come valori nella tabella di dati come mostrato in quest'immagine.

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

Ecco il codice di esempio utilizzato per generare il [PDF di output](5472577.pdf) dal [file excel di origine](5472579.xlsx). Si prega di leggere i commenti per ulteriori informazioni.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CalculationOfArrayFormula-CalculationOfArrayFormula.java" >}}
