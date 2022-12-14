---
title: Raggruppa i campi pivot nella tabella pivot
type: docs
weight: 90
url: /it/java/group-pivot-fields-in-the-pivot-table/
---
## **Possibili scenari di utilizzo**

Microsoft Excel consente di raggruppare i campi pivot della tabella pivot. Quando c'è una grande quantità di dati relativi a un campo pivot, è spesso utile raggrupparli in sezioni. Aspose.Cells fornisce anche questa funzione utilizzando il[**Tabella pivot.setManualGroupField()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#setManualGroupField(com.aspose.cells.PivotField,%20com.aspose.cells.DateTime,%20com.aspose.cells.DateTime,%20java.util.ArrayList,%20int)) metodo.

## **Raggruppa i campi pivot nella tabella pivot**

Il codice di esempio seguente carica il file[esempio di file Excel](64716838.xlsx)ed esegue il raggruppamento sul primo campo pivot utilizzando il file[**Tabella pivot.setManualGroupField()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#setManualGroupField(com.aspose.cells.PivotField,%20com.aspose.cells.DateTime,%20com.aspose.cells.DateTime,%20java.util.ArrayList,%20int)) metodo. Quindi aggiorna e calcola i dati della tabella pivot e salva la cartella di lavoro come file[file Excel di output](64716837.xlsx). Lo screenshot mostra l'effetto del codice di esempio sul file Excel di esempio. Come puoi vedere nello screenshot, il primo campo pivot è ora raggruppato per mesi e trimestri.

![cose da fare:immagine_alt_testo](group-pivot-fields-in-the-pivot-table_1.png)

## **Codice di esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-GroupPivotFieldsInPivotTable.java" >}}
