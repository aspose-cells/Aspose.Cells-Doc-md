---
title: Surveiller l exécution des programmes
type: docs
weight: 20
url: /fr/python-net/monitor-running-programs/
---

## **Comment surveiller l'exécution d'un programme**

Le code d'exemple suivant montre comment surveiller l'exécution d'un programme. Ce code peut être utilisé pour surveiller l'exécution de code lié à [Workbook](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) . Utilisez simplement la classe [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/python-net/aspose.cells/systemtimeinterruptmonitor/) pour créer un objet de surveillance, utilisez la fonction [setInterruptMonitor](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/interrupt_monitor/) pour l'ajouter aux paramètres d'exécution de l'[LoadOptions](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/) , puis utilisez la fonction [startMonitor](https://reference.aspose.com/cells/python-net/aspose.cells/systemtimeinterruptmonitor/start_monitor/#int) pour définir le temps d'interruption attendu (en millisecondes). Si le temps d'exécution du code surveillé dépasse le temps attendu, le programme sera interrompu et une exception sera levée.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Examples-python-net-TechnicalArticles-MonitorRunningPrograms.py" >}}
{{< app/cells/assistant language="python-net" >}}
