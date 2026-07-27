---
title: Raggruppa i campi pivot nella tabella pivot
type: docs
weight: 80
url: /it/net/group-pivot-fields-in-the-pivot-table/
---

## **Possibili Scenari di Utilizzo**

Microsoft Excel consente di raggruppare i campi pivot della tabella pivot. Quando c'è una grande quantità di dati relativi a un campo pivot, è spesso utile raggrupparli in sezioni. Aspose.Cells fornisce anche questa funzionalità utilizzando il metodo [**PivotTable.GroupBy()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield/groupby/).

## **Raggruppa i campi pivot nella tabella pivot**

Il codice di esempio seguente carica il [file Excel di esempio](64716818.xlsx) e esegue il raggruppamento sul primo campo pivot utilizzando il metodo [**PivotTable.GroupBy()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield/groupby/). Aggiorna quindi e calcola i dati della tabella pivot e salva il foglio di calcolo come [file Excel di output](64716817.xlsx). Lo screenshot mostra l'effetto del codice di esempio sul file Excel di esempio. Come si può vedere dallo screenshot, il primo campo pivot è ora raggruppato per mesi e trimestri.

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-GroupPivotFieldsInPivotTable.cs" >}}
{{< app/cells/assistant language="csharp" >}}
