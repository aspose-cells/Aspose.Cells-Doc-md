---
title: Bevaka körande program
type: docs
weight: 20
url: /sv/net/Monitor-running-programs/
---

## **Hur du övervakar ett körande program**

Det följande kodexemplet visar hur man övervakar ett körande program. Denna kod kan användas för att övervaka det körande [Arbetsbok](https://reference.aspose.com/cells/net/aspose.cells/workbook/)-relaterad kod. Använd helt enkelt klassen [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/net/aspose.cells/systemtimeinterruptmonitor/) för att skapa ett övervakningsobjekt, använd funktionen [SetInterruptMonitor](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/interruptmonitor/) för att lägga till det i [LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/)-körningsparametrarna, och använd sedan funktionen [StartMonitor](https://reference.aspose.com/cells/net/aspose.cells/systemtimeinterruptmonitor/startmonitor/) för att ange förväntad avbrotts tid (i millisekunder). Om körtiden för den övervakade koden överstiger den förväntade tiden kommer programmet att avbrytas och ett undantag kastas.

## **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-TechnicalArticles-MonitorRunningPrograms.cs" >}}
