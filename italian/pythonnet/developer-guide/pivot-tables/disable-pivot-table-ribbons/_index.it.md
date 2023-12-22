---
title: Disabilita i nastri della tabella pivot
type: docs
weight: 90
url: /it/python-net/disable-pivot-table-ribbons/
description: Come disabilitare i nastri della tabella pivot con Aspose.Cells for Python via .NET.
keywords: Disable Pivot Table Ribbons.
---
{{% alert color="primary" %}}

report basati su tabelle pivot sono utili ma soggetti a errori se gli utenti target non hanno una conoscenza dettagliata di Excel per configurare questi report. In queste circostanze, le organizzazioni vorranno impedire agli utenti di modificare un report basato su tabella pivot. Le funzionalità comuni delle tabelle pivot, come l'aggiunta di ulteriori filtri, filtri dei dati, campi o la modifica dell'ordine di determinati elementi nel report, nella maggior parte dei casi non sono consigliate a tutti gli utenti. D'altro canto, questi utenti dovranno anche essere in grado di aggiornare il report e utilizzare i filtri o i filtri dei dati esistenti. Aspose.Cells for Python via .NET ha fornito questa possibilità agli sviluppatori per impedire agli utenti di modificare questi report durante la creazione di questi report. A questo scopo, Excel fornisce una funzionalità per disabilitare la barra multifunzione della tabella pivot e la stessa è fornita da Aspose.Cells for Python via .NET, ovvero lo sviluppatore può disabilitare la barra multifunzione che contiene i controlli per modificare questi report.

{{% /alert %}}

##  **Disabilitare la barra multifunzione della tabella pivot utilizzando PivotTable.EnableWizard**

 Il codice seguente dimostra questa funzionalità accedendo a una tabella pivot da un foglio e quindi impostando[**abilita_procedura guidata**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/enable_wizard/) a *falso**. Da qui è possibile scaricare un file di tabella pivot di esempio[collegamento](pivot_table_test.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-DisablePivotTableRibbon.py" >}}
