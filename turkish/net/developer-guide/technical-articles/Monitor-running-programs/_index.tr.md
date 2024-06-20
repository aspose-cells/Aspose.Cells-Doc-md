---
title: Çalışan Programları İzleme
type: docs
weight: 20
url: /tr/net/Monitor-running-programs/
---

## ** Bir çalışan programı nasıl izlenir**

Aşağıdaki örnek kod, bir çalışan programın nasıl izleneceğini göstermektedir. Bu kod, [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook/) ile ilgili kodların çalışmasını izlemek için kullanılabilir. Basitçe [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/net/aspose.cells/systemtimeinterruptmonitor/) sınıfını kullanarak bir izleme nesnesi oluşturun, [LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/) çalışan parametrelerine eklemek için [SetInterruptMonitor](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/interruptmonitor/) fonksiyonunu kullanın ve ardından beklenen kesinti süresini (milisaniye cinsinden) ayarlamak için [StartMonitor](https://reference.aspose.com/cells/net/aspose.cells/systemtimeinterruptmonitor/startmonitor/) fonksiyonunu kullanın. İzlenen kodun çalışma süresi beklenen süreyi aşarsa, program kesilecek ve bir istisna fırlatılacaktır.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-TechnicalArticles-MonitorRunningPrograms.cs" >}}
