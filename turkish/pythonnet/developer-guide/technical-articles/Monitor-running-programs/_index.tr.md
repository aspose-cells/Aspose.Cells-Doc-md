---
title: Çalışan Programları İzleme
type: docs
weight: 20
url: /tr/python-net/monitor-running-programs/
---

## ** Bir çalışan programı nasıl izlenir**

Aşağıdaki örnek kod, bir programın çalışmasını nasıl izleyeceğinizi gösterir. Bu kod, [Workbook](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) ile ilgili kodu izlemek için kullanılabilir. Basitçe bir izleme nesnesi oluşturmak için [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/python-net/aspose.cells/systemtimeinterruptmonitor/) sınıfını kullanın, onu [LoadOptions](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/) çalışma parametrelerine eklemek için [setInterruptMonitor](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/interrupt_monitor/) işlevini kullanın ve ardından beklenen kesme süresini (milisaniye cinsinden) belirlemek için [startMonitor](https://reference.aspose.com/cells/python-net/aspose.cells/systemtimeinterruptmonitor/start_monitor/#int) işlevini kullanın. İzlenen kodun çalışma süresi beklenen süreyi aşarsa, program kesilecek ve bir istisna atılacaktır.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Examples-python-net-TechnicalArticles-MonitorRunningPrograms.py" >}}
