---
title: Surveiller l exécution des programmes
type: docs
weight: 20
url: /fr/net/Monitor-running-programs/
---

## **Comment surveiller l'exécution d'un programme**

Le code d'exemple suivant montre comment surveiller un programme en cours d'exécution. Ce code peut être utilisé pour surveiller l'exécution du code lié à [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook/). Utilisez simplement la classe [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/net/aspose.cells/systemtimeinterruptmonitor/) pour créer un objet de surveillance, utilisez la fonction [SetInterruptMonitor](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/interruptmonitor/) pour l'ajouter aux paramètres en cours d'exécution de [LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/), puis utilisez la fonction [StartMonitor](https://reference.aspose.com/cells/net/aspose.cells/systemtimeinterruptmonitor/startmonitor/) pour définir le temps d'interruption prévu (en millisecondes). Si le temps d'exécution du code surveillé dépasse le temps prévu, le programme sera interrompu et une exception sera déclenchée.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-TechnicalArticles-MonitorRunningPrograms.cs" >}}
