---
title: Çalışan Programları İzleme
type: docs
weight: 20
url: /tr/cpp/Monitor-running-programs/
---

## ** Bir çalışan programı nasıl izlenir**

Aşağıdaki örnek kod, bir çalışan programı nasıl izleneceğini göstermektedir. Bu kod, [Çalışma Kitabı](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) ile ilgili kodun çalışmasını izlemek için kullanılabilir. Basitçe, izleme nesnesi oluşturmak için [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/cpp/aspose.cells/systemtimeinterruptmonitor/) sınıfını kullanın, çalışma parametrelerine eklemek için [SetInterruptMonitor](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/setinterruptmonitor/) işlevini kullanın ve ardından beklenen kesinti süresini (milisaniye cinsinden) ayarlamak için [StartMonitor](https://reference.aspose.com/cells/cpp/aspose.cells/systemtimeinterruptmonitor/startmonitor/) işlevini kullanın. İzlenen kodun çalışma süresi beklenen süreyi aşarsa, program kesilecek ve bir istisna atılacaktır.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-TechnicalArticles-MonitorRunningPrograms.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
