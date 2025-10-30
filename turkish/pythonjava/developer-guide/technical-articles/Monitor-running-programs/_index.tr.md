---
title: Çalışan Programları İzleme
type: docs
weight: 10
url: /tr/python-java/monitor-running-programs/
---

## ** Bir çalışan programı nasıl izlenir**

Aşağıdaki örnek kod bir çalışan programı izlemenin nasıl yapıldığını gösterir. Bu kod, [Workbook](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook) ile ilgili kodu izlemek için kullanılabilir. Basitçe, izleme nesnesi oluşturmak için [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/python-java/asposecells.api/SystemTimeInterruptMonitor) sınıfını kullanın, [setInterruptMonitor](https://reference.aspose.com/cells/python-java/asposecells.api/loadoptions#InterruptMonitor) fonksiyonunu [LoadOptions](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions) çalışma parametrelerine eklemek için ve ardından beklenen kesme zamanını (milisaniye cinsinden) ayarlamak için [startMonitor](https://reference.aspose.com/cells/python-java/asposecells.api/systemtimeinterruptmonitor#startMonitor(int)) fonksiyonunu kullanın. İzlenen kodun çalışma süresi beklenen süreyi aştığında, program kesilecek ve bir istisna fırlatılacaktır.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Examples-python-java-TechnicalArticles-MonitorRunningPrograms.py" >}}
