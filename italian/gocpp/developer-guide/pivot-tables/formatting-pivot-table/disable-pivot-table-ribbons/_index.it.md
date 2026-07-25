---
title: Disabilita le barre degli strumenti della tabella pivot con Golang tramite C++
linktitle: Disabilita le barre delle tabelle pivot
type: docs
weight: 90
url: /it/go-cpp/disable-pivot-table-ribbons/
description: Impara come disabilitare le ribbon delle pivot table nei file Excel usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

I report basati su pivot table sono utili, ma soggetti a errori se gli utenti target non hanno conoscenze approfondite di Excel per configurare questi report. In queste circostanze, le organizzazioni vorranno limitare la possibilità degli utenti di modificare un report basato su pivot table. Caratteristiche comuni come l'aggiunta di filtri, slicer, campi o la modifica dell'ordine di alcune cose nel report di solito non sono raccomandate per ogni utente. D'altro canto, questi utenti dovrebbero poter aggiornare il report e usare filtri o slicer esistenti. Aspose.Cells ha fornito questa possibilità agli sviluppatori per limitare le modifiche di report mentre vengono creati. A tal fine, Excel offre una funzione per disabilitare il nastro della pivot table, funzione che viene offerta anche da Aspose.Cells. Gli sviluppatori possono disabilitare il nastro che contiene i controlli per modificare questi report.

{{% /alert %}}

## **Disabilita la barra delle tabelle pivot utilizzando PivotTable.EnableWizard**

Il codice seguente dimostra questa funzione accedendo a una pivot table da un foglio e poi impostando [**GetEnableWizard()**](https://reference.aspose.com/cells/go-cpp/pivottable/getenablewizard/) a **false**. È possibile scaricare un file esempio di pivot table da questa [link](pivot_table_test.xlsx).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DisablePivotTableRibbons.go" >}}
