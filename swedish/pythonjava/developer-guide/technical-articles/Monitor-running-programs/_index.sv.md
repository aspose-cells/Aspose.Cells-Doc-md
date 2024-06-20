---
title: Bevaka körande program
type: docs
weight: 20
url: /sv/python-java/monitor-running-programs/
---

## **Hur du övervakar ett körande program**

Följande exempelkod visar hur man övervakar ett körande program. Den här koden kan användas för att övervaka körning av [Arbetsbok](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook)-relaterad kod. Använd helt enkelt klassen [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/python-java/asposecells.api/SystemTimeInterruptMonitor) för att skapa ett övervakningsobjekt, använd funktionen [setInterruptMonitor](https://reference.aspose.com/cells/python-java/asposecells.api/loadoptions#InterruptMonitor) för att lägga till det till de körande parametrarna för [LoadOptions](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions), och använd sedan funktionen [startMonitor](https://reference.aspose.com/cells/python-java/asposecells.api/systemtimeinterruptmonitor#startMonitor(int)) för att ställa in förväntad avbrottstid (i millisekunder). Om körningstiden för den övervakade koden överskrider förväntad tid, kommer programmet att avbrytas och ett undantag kastas.

## **Exempelkod**

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Examples-python-java-TechnicalArticles-MonitorRunningPrograms.py" >}}
