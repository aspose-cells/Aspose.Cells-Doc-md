---
title: Monitorare i programmi in esecuzione
type: docs
weight: 20
url: /it/java/Monitor-running-programs/
---

## **Come monitorare un programma in esecuzione**

Il seguente codice di esempio mostra come monitorare un programma in esecuzione. Questo codice può essere utilizzato per monitorare l'esecuzione di codice correlato a [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook/). Basta utilizzare la classe [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/java/com.aspose.cells/systemtimeinterruptmonitor/) per creare un oggetto di monitoraggio, utilizzare la funzione [SetInterruptMonitor](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions/#setInterruptMonitor-com.aspose.cells.AbstractInterruptMonitor-) per aggiungerlo ai parametri di esecuzione di [LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions/), e quindi utilizzare la funzione [StartMonitor](https://reference.aspose.com/cells/java/com.aspose.cells/systemtimeinterruptmonitor/#startMonitor-int-) per impostare il tempo di interruzione previsto (in millisecondi). Se il tempo di esecuzione del codice monitorato supera il tempo previsto, il programma verrà interrotto e verrà generata un'eccezione.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-TechnicalArticles-MonitorRunningPrograms.java" >}}
{{< app/cells/assistant language="java" >}}
