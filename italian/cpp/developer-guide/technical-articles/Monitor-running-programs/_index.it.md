---
title: Monitorare i programmi in esecuzione
type: docs
weight: 20
url: /it/cpp/Monitor-running-programs/
---

## **Come monitorare un programma in esecuzione**

Il codice di esempio seguente mostra come monitorare un programma in esecuzione. Questo codice può essere utilizzato per monitorare l'esecuzione del codice correlato a [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/). Basta utilizzare la classe [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/cpp/aspose.cells/systemtimeinterruptmonitor/) per creare un oggetto di monitoraggio, utilizzare la funzione [SetInterruptMonitor](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/setinterruptmonitor/) per aggiungerlo ai parametri di esecuzione di [LoadOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) e quindi utilizzare la funzione [StartMonitor](https://reference.aspose.com/cells/cpp/aspose.cells/systemtimeinterruptmonitor/startmonitor/) per impostare il tempo di interruzione previsto (in millisecondi). Se il tempo di esecuzione del codice monitorato supera il tempo previsto, il programma verrà interrotto e verrà generata un'eccezione.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-TechnicalArticles-MonitorRunningPrograms.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
