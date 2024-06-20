---
title: Monitorare i programmi in esecuzione
type: docs
weight: 20
url: /it/net/Monitor-running-programs/
---

## **Come monitorare un programma in esecuzione**

Il seguente codice di esempio mostra come monitorare un programma in esecuzione. Questo codice può essere utilizzato per monitorare l'esecuzione del codice correlato a [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook/). Utilizzare semplicemente la classe [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/net/aspose.cells/systemtimeinterruptmonitor/) per creare un oggetto di monitoraggio, utilizzare la funzione [SetInterruptMonitor](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/interruptmonitor/) per aggiungerla ai parametri di esecuzione di [LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/), e quindi utilizzare la funzione [StartMonitor](https://reference.aspose.com/cells/net/aspose.cells/systemtimeinterruptmonitor/startmonitor/) per impostare il tempo di interruzione previsto (in millisecondi). Se il tempo di esecuzione del codice monitorato supera il tempo previsto, il programma verrà interrotto e verrà generata un'eccezione.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-TechnicalArticles-MonitorRunningPrograms.cs" >}}
