---
title: Raggruppa i campi pivot nella tabella pivot
type: docs
weight: 90
url: /it/java/group-pivot-fields-in-the-pivot-table/
---

## **Possibili Scenari di Utilizzo**

Microsoft Excel consente di raggruppare i campi pivot della tabella pivot. Quando ci sono molte informazioni relative a un campo pivot, è spesso utile raggrupparle in sezioni. Anche Aspose.Cells fornisce questa funzionalità utilizzando il metodo [**PivotTable.setManualGroupField()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#setManualGroupField-com.aspose.cells.PivotField-com.aspose.cells.DateTime-com.aspose.cells.DateTime-java.util.ArrayList-int-).

## **Raggruppa i campi pivot nella tabella pivot**

Il seguente codice di esempio carica il [file di Excel di esempio](64716838.xlsx) e esegue il raggruppamento sul primo campo pivot utilizzando il metodo [**PivotTable.setManualGroupField()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#setManualGroupField-com.aspose.cells.PivotField-com.aspose.cells.DateTime-com.aspose.cells.DateTime-java.util.ArrayList-int-). Aggiorna quindi e calcola i dati della tabella pivot e salva il documento di lavoro come il [file di Excel di output](64716837.xlsx). Lo screenshot mostra l'effetto del codice di esempio sul file di Excel di esempio. Come si può vedere nello screenshot, il primo campo pivot è ora raggruppato per mesi e trimestri.

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-GroupPivotFieldsInPivotTable.java" >}}
{{< app/cells/assistant language="java" >}}
