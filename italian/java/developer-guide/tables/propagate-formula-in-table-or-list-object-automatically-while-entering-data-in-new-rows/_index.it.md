---
title: Propaga automaticamente la formula nella tabella o nell'oggetto elenco durante l'inserimento dei dati in nuove righe
type: docs
weight: 980
url: /it/java/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
---
## **Possibili scenari di utilizzo**
 A volte, si desidera che una formula nella tabella o nell'oggetto elenco si propaghi automaticamente a nuove righe durante l'inserimento di nuovi dati. Questo è il comportamento predefinito di Microsoft Excel. Per ottenere la stessa cosa con Aspose.Cells, si prega di utilizzare[ListColumn.Formula](https://reference.aspose.com/cells/java/com.aspose.cells/listcolumn#Formula)proprietà.
## **Propaga automaticamente la formula nella tabella o nell'oggetto elenco durante l'inserimento dei dati in nuove righe**
Il seguente codice di esempio crea una tabella o un oggetto elenco in modo tale che la formula nella colonna B si propaghi automaticamente alle nuove righe quando si immettono nuovi dati. Si prega di controllare[file excel di output](5472519.xlsx) generato con questo codice. Se inserisci un numero qualsiasi nella cella A3, vedrai che la formula nella cella B2 si propaga automaticamente alla cella B3.
## **Codice d'esempio**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PropagateFormulaInTableorListObject-PropagateFormulaInTableorListObject.java" >}}
