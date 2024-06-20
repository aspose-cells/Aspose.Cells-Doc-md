---
title: Propagare la formula in un entità tabella o elenco automaticamente durante l inserimento dei dati in nuove righe
type: docs
weight: 980
url: /it/java/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
---

## **Possibili Scenari di Utilizzo**
A volte si desidera che una formula nella tua Tabella o Oggetto Elenco si propaghi automaticamente alle nuove righe durante l'inserimento di nuovi dati. Questo è il comportamento predefinito di Microsoft Excel. Per ottenere lo stesso risultato con Aspose.Cells, utilizzare la proprietà [ListaColonna.Formula](https://reference.aspose.com/cells/java/com.aspose.cells/listcolumn#Formula).
## **Propagare la formula nella tabella o nell'oggetto elenco automaticamente durante l'inserimento dei dati nelle nuove righe**
Il codice di esempio seguente crea una Tabella o un Oggetto Elenco in modo che la formula nella colonna B si propaghi automaticamente alle nuove righe quando inserisci nuovi dati. Verifica il [file di lavoro excel di output](5472519.xlsx) generato con questo codice. Se inserisci un numero in cella A3, vedrai che la formula in cella B2 si propaga automaticamente alla cella B3.
## **Codice di Esempio**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PropagateFormulaInTableorListObject-PropagateFormulaInTableorListObject.java" >}}
