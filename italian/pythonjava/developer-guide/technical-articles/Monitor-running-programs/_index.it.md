---
title: Monitorare i programmi in esecuzione
type: docs
weight: 10
url: /it/python-java/monitor-running-programs/
---

## **Come monitorare un programma in esecuzione**

Il seguente codice di esempio mostra come monitorare l'esecuzione di un programma. Questo codice può essere utilizzato per monitorare l'esecuzione del codice relativo a [Workbook](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook). Basta utilizzare la classe [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/python-java/asposecells.api/SystemTimeInterruptMonitor) per creare un oggetto di monitoraggio, utilizzare la funzione [setInterruptMonitor](https://reference.aspose.com/cells/python-java/asposecells.api/loadoptions#InterruptMonitor) per aggiungerlo ai parametri di esecuzione di [LoadOptions](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions), e poi utilizzare la funzione [startMonitor](https://reference.aspose.com/cells/python-java/asposecells.api/systemtimeinterruptmonitor#startMonitor(int)) per impostare il tempo di interruzione previsto (in millisecondi). Se il tempo di esecuzione del codice monitorato supera il tempo previsto, il programma verrà interrotto e verrà generata un'eccezione.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Examples-python-java-TechnicalArticles-MonitorRunningPrograms.py" >}}
