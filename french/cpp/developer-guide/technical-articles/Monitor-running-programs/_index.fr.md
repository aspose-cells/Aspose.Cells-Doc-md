---
title: Surveiller l exécution des programmes
type: docs
weight: 20
url: /fr/cpp/Monitor-running-programs/
---

## **Comment surveiller l'exécution d'un programme**

Le code d'exemple suivant montre comment surveiller l'exécution d'un programme. Ce code peut être utilisé pour surveiller l'exécution du code lié à [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/). Il suffit d'utiliser la classe [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/cpp/aspose.cells/systemtimeinterruptmonitor/) pour créer un objet de surveillance, d'utiliser la fonction [SetInterruptMonitor](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/setinterruptmonitor/) pour l'ajouter aux paramètres de fonctionnement de [LoadOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/), puis d'utiliser la fonction [StartMonitor](https://reference.aspose.com/cells/cpp/aspose.cells/systemtimeinterruptmonitor/startmonitor/) pour définir le temps d'interruption prévu (en millisecondes). Si le temps d'exécution du code surveillé dépasse le temps prévu, le programme sera interrompu et une exception sera levée.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-TechnicalArticles-MonitorRunningPrograms.cpp" >}}
