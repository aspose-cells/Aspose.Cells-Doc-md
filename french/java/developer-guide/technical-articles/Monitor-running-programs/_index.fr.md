---
title: Surveiller l exécution des programmes
type: docs
weight: 20
url: /fr/java/Monitor-running-programs/
---

## **Comment surveiller l'exécution d'un programme**

Le code d'exemple suivant montre comment surveiller un programme en cours d'exécution. Ce code peut être utilisé pour surveiller l'exécution du code lié à [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook/). Il suffit d'utiliser la classe [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/java/com.aspose.cells/systemtimeinterruptmonitor/) pour créer un objet de surveillance, d'utiliser la fonction [SetInterruptMonitor](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions/#setInterruptMonitor-com.aspose.cells.AbstractInterruptMonitor-) pour l'ajouter aux paramètres d'exécution de [LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions/), puis d'utiliser la fonction [StartMonitor](https://reference.aspose.com/cells/java/com.aspose.cells/systemtimeinterruptmonitor/#startMonitor-int-) pour définir le temps d'interruption attendu (en millisecondes). Si le temps d'exécution du code surveillé dépasse le temps attendu, le programme sera interrompu et une exception sera levée.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-TechnicalArticles-MonitorRunningPrograms.java" >}}
{{< app/cells/assistant language="java" >}}
