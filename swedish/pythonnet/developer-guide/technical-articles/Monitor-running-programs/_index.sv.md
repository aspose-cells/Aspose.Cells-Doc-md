---
title: Bevaka körande program
type: docs
weight: 20
url: /sv/python-net/monitor-running-programs/
---

## **Hur du övervakar ett körande program**

Följande exempelkod visar hur man övervakar ett körande program. Denna kod kan användas för att övervaka körningen av [arbetsboken](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) relaterad kod. Använd helt enkelt [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/python-net/aspose.cells/systemtimeinterruptmonitor/) klassen för att skapa en övervakningsobjekt, använd [setInterruptMonitor](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/interrupt_monitor/) funktionen för att lägga till den till [LoadOptions](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/) körparametrar, och använd sedan [startMonitor](https://reference.aspose.com/cells/python-net/aspose.cells/systemtimeinterruptmonitor/start_monitor/#int) funktionen för att ställa in förväntad avbrottstid (i millisekunder). Om körtiden för den övervakade koden överskrider den förväntade tiden kommer programmet att avbrytas och ett undantag kommer att kastas.

## **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Examples-python-net-TechnicalArticles-MonitorRunningPrograms.py" >}}
