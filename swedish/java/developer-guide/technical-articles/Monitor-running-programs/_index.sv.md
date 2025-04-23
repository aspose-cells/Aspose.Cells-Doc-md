---
title: Bevaka körande program
type: docs
weight: 20
url: /sv/java/Monitor-running-programs/
---

## **Hur du övervakar ett körande program**

Följande exempelkod visar hur man övervakar ett körande program. Denna kod kan användas för att övervaka körningen av [workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook/) relaterad kod. Använd helt enkelt klassen [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/java/com.aspose.cells/systemtimeinterruptmonitor/) för att skapa ett övervakningsobjekt, använd funktionen [SetInterruptMonitor](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions/#setInterruptMonitor-com.aspose.cells.AbstractInterruptMonitor-) för att lägga till det i [LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions/) löptidsparametrar, och använd sedan funktionen [StartMonitor](https://reference.aspose.com/cells/java/com.aspose.cells/systemtimeinterruptmonitor/#startMonitor-int-) för att ange den förväntade avbrottstiden (i millisekunder). Om den övervakade kodens körtid överskrider den förväntade tiden kommer programmet att avbrytas och ett undantag kastas.

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-TechnicalArticles-MonitorRunningPrograms.java" >}}
{{< app/cells/assistant language="java" >}}
