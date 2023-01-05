---
title: Disattiva i nastri della tabella pivot
type: docs
weight: 40
url: /it/java/disable-pivot-table-ribbons/
---
{{% alert color="primary" %}}

report basati su tabelle pivot sono utili ma soggetti a errori se gli utenti di destinazione non hanno una conoscenza dettagliata di Excel per configurare questi report. In queste circostanze, le organizzazioni vorranno impedire agli utenti di modificare un report basato su tabella pivot. Le funzionalità comuni della tabella pivot come l'aggiunta di ulteriori filtri, filtri dei dati, campi o la modifica dell'ordine di determinate cose nel rapporto non sono per lo più consigliate per tutti gli utenti. D'altra parte, questi utenti saranno anche in grado di aggiornare il report e utilizzare filtri o affettatrici esistenti. Aspose.Cells ha fornito questa possibilità agli sviluppatori per impedire agli utenti di modificare questi rapporti durante la creazione di questi rapporti. A tale scopo, Excel fornisce una funzionalità per disabilitare il nastro della tabella pivot e lo stesso è fornito da Aspose.Cells, ovvero lo sviluppatore può disabilitare il nastro che contiene i controlli per modificare questi rapporti.

{{% /alert %}}

## **Disabilita la barra multifunzione della tabella pivot utilizzando PivotTable.setEnableWizard**

Il codice seguente dimostra questa funzionalità accedendo a una tabella pivot da un foglio e quindi chiamando il metodo[**setEnableWizard**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#EnableWizard) per impostare questo flag**falso** . Il file di tabella pivot di esempio può essere scaricato da questo[collegamento](71630876.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-DisablePivotTableRibbon-1.java" >}}
