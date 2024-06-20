---
title: Bevaka körande program
type: docs
weight: 20
url: /sv/cpp/Monitor-running-programs/
---

## **Hur du övervakar ett körande program**

Följande exempelkod visar hur du övervakar ett körande program. Denna kod kan användas för att övervaka körningen av [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)-relaterad kod. Använd helt enkelt klassen [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/cpp/aspose.cells/systemtimeinterruptmonitor/) för att skapa en övervakningsobjekt, använd funktionen [SetInterruptMonitor](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/setinterruptmonitor/) för att lägga till den i [LoadOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) körparametrar, och använd sedan funktionen [StartMonitor](https://reference.aspose.com/cells/cpp/aspose.cells/systemtimeinterruptmonitor/startmonitor/) för att ställa in förväntad avbrotts tid (i millisekunder). Om körningstiden för övervakad kod överstiger förväntad tid, avbryts programmet och ett undantag kastas.

## **Exempelkod**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-TechnicalArticles-MonitorRunningPrograms.cpp" >}}
