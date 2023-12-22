---
title: Raggruppare i campi pivot nella tabella pivot
type: docs
weight: 80
url: /it/python-net/group-pivot-fields-in-the-pivot-table/
description: Come raggruppare i campi pivot nella tabella pivot con Aspose.Cells for Python via .NET.
keywords: Group Pivot Fields in the Pivot Table.
---
##  **Possibili scenari di utilizzo**

Microsoft Excel consente di raggruppare i campi pivot della tabella pivot. Quando è presente una grande quantità di dati relativi ad un campo pivot, spesso è utile raggrupparli in sezioni. Aspose.Cells for Python via .NET fornisce questa funzionalità anche utilizzando il[**Tabella pivot.set_manual_group_field()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/set_manual_group_field/#int-float-float-list-float)metodo.

##  **Raggruppare i campi pivot nella tabella pivot**

 Il codice di esempio seguente carica il file[file Excel di esempio](64716818.xlsx) ed esegue il raggruppamento sul primo campo pivot utilizzando il comando[**Tabella pivot.set_manual_group_field()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/set_manual_group_field/#int-float-float-list-float) metodo. Quindi aggiorna e calcola i dati della tabella pivot e salva la cartella di lavoro come[file Excel di output](64716817.xlsx)Lo screenshot mostra l'effetto del codice di esempio sul file Excel di esempio. Come puoi vedere nello screenshot, il primo campo pivot è ora raggruppato per mesi e trimestri.

![cose da fare:immagine_alt_testo](group-pivot-fields-in-the-pivot-table_1.png)

##  **Codice d'esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-GroupPivotFieldsInPivotTable.py" >}}
