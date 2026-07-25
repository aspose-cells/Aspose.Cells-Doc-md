---
title: Disabilita le barre delle tabelle pivot
type: docs
weight: 90
url: /it/net/disable-pivot-table-ribbons/
---

{{% alert color="primary" %}}

I report basati su tabelle pivot sono utili ma soggetti a errori se gli utenti destinatari non hanno conoscenze dettagliate di Excel per configurare questi report. In queste circostanze, le organizzazioni vorranno impedire agli utenti di poter modificare un report basato su una tabella pivot. Le funzionalità comuni delle tabelle pivot come l'aggiunta di filtri aggiuntivi, slicer, campi o la modifica dell'ordine di alcune cose nel report non sono generalmente consigliate per tutti gli utenti. D'altra parte, questi utenti devono essere in grado di aggiornare il report e utilizzare filtri o slicer esistenti. Aspose.Cells ha fornito questa capacità agli sviluppatori per impedire agli utenti di modificare questi report durante la creazione di questi report. A questo scopo, Excel fornisce una funzione per disabilitare la barra delle tabelle pivot e lo stesso è fornito da Aspose.Cells, ovvero lo sviluppatore può disabilitare la barra che contiene i controlli per modificare questi report.

{{% /alert %}}

## **Disabilita la barra delle tabelle pivot utilizzando PivotTable.EnableWizard**

Il seguente codice dimostra questa funzionalità accedendo a una tabella pivot da un foglio e impostando [**EnableWizard**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/enablewizard) su **false**. Il file di esempio della tabella pivot può essere scaricato da questo [link](pivot_table_test.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-DisablePivotTableRibbon.cs" >}}
{{< app/cells/assistant language="csharp" >}}
