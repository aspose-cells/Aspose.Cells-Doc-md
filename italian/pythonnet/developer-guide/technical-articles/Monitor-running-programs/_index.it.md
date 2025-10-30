---
title: Monitorare i programmi in esecuzione
type: docs
weight: 20
url: /it/python-net/monitor-running-programs/
---

## **Come monitorare un programma in esecuzione**

Il seguente codice di esempio mostra come monitorare un programma in esecuzione. Questo codice può essere utilizzato per monitorare l'esecuzione del codice correlato a [Workbook](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/). Basta utilizzare la classe [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/python-net/aspose.cells/systemtimeinterruptmonitor/) per creare un oggetto di monitoraggio, utilizzare la funzione [setInterruptMonitor](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/interrupt_monitor/) per aggiungerlo ai parametri di esecuzione di [LoadOptions](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/) e poi utilizzare la funzione [startMonitor](https://reference.aspose.com/cells/python-net/aspose.cells/systemtimeinterruptmonitor/start_monitor/#int) per impostare il tempo di interruzione previsto (in millisecondi). Se il tempo di esecuzione del codice monitorato supera il tempo previsto, il programma verrà interrotto e verrà generata un'eccezione.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Examples-python-net-TechnicalArticles-MonitorRunningPrograms.py" >}}
{{< app/cells/assistant language="python-net" >}}
