---
title: Surveiller l exécution des programmes
type: docs
weight: 10
url: /fr/python-java/monitor-running-programs/
---

## **Comment surveiller l'exécution d'un programme**

Le code d'exemple suivant montre comment surveiller un programme en cours d'exécution. Ce code peut être utilisé pour surveiller l'exécution du code lié au [classeur](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook). Il suffit d'utiliser la classe [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/python-java/asposecells.api/SystemTimeInterruptMonitor) pour créer un objet de surveillance, utiliser la fonction [setInterruptMonitor](https://reference.aspose.com/cells/python-java/asposecells.api/loadoptions#InterruptMonitor) pour l'ajouter aux paramètres d'exécution de [LoadOptions](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions), puis utiliser la fonction [startMonitor](https://reference.aspose.com/cells/python-java/asposecells.api/systemtimeinterruptmonitor#startMonitor(int)) pour définir le temps d'interruption prévu (en millisecondes). Si le temps d'exécution du code surveillé dépasse le temps prévu, le programme sera interrompu et une exception sera levée.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Examples-python-java-TechnicalArticles-MonitorRunningPrograms.py" >}}
