---
title: Çalışan Programları İzleme
type: docs
weight: 20
url: /tr/java/Monitor-running-programs/
---

## ** Bir çalışan programı nasıl izlenir**

Aşağıdaki örnek kod, bir çalışan programı nasıl izleyeceğinizi gösterir. Bu kod, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook/) ile ilgili kodların çalışmasını izlemek için kullanılabilir. Basitçe, bir izleme nesnesi oluşturmak için [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/java/com.aspose.cells/systemtimeinterruptmonitor/) sınıfını kullanın, bunu [LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions/) çalışma parametrelerine eklemek için [SetInterruptMonitor](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions/#setInterruptMonitor-com.aspose.cells.AbstractInterruptMonitor-) işlevini kullanın ve ardından [StartMonitor](https://reference.aspose.com/cells/java/com.aspose.cells/systemtimeinterruptmonitor/#startMonitor-int-) işlevini kullanarak beklenen kesinti süresini (milisaniye cinsinden) ayarlayın. İzlenen kodun çalışma süresi beklenen süreyi aştığında, program kesilecek ve bir istisna atılacaktır.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-TechnicalArticles-MonitorRunningPrograms.java" >}}
