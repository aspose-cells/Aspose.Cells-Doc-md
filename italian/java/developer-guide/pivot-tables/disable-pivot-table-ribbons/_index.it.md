---
title: Disabilita le barre delle tabelle pivot
type: docs
weight: 40
url: /it/java/disable-pivot-table-ribbons/
---

{{% alert color="primary" %}}

I report basati su tabelle pivot sono utili ma soggetti a errori se gli utenti destinatari non hanno conoscenze dettagliate di Excel per configurare questi report. In queste circostanze, le organizzazioni vorranno impedire agli utenti di poter modificare un report basato su una tabella pivot. Le funzionalità comuni delle tabelle pivot come l'aggiunta di filtri aggiuntivi, slicer, campi o la modifica dell'ordine di alcune cose nel report non sono generalmente consigliate per tutti gli utenti. D'altra parte, questi utenti devono essere in grado di aggiornare il report e utilizzare filtri o slicer esistenti. Aspose.Cells ha fornito questa capacità agli sviluppatori per impedire agli utenti di modificare questi report durante la creazione di questi report. A questo scopo, Excel fornisce una funzione per disabilitare la barra delle tabelle pivot e lo stesso è fornito da Aspose.Cells, ovvero lo sviluppatore può disabilitare la barra che contiene i controlli per modificare questi report.

{{% /alert %}}

## **Disabilitare la barra degli strumenti della tabella pivot utilizzando PivotTable.setEnableWizard**

Il seguente codice dimostra questa funzionalità accedendo a una tabella pivot da un foglio e quindi chiamando il [**setEnableWizard**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#EnableWizard) per impostare questo flag **false**. Il file di esempio della tabella pivot può essere scaricato da questo [link](71630876.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-DisablePivotTableRibbon-1.java" >}}
