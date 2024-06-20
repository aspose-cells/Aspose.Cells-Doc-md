---
title: Çok uzun sürüyorsa, Durdur dönüşümü veya yüklemeyi kullanarak InterruptMonitor
type: docs
weight: 100
url: /tr/net/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
---

## **Olası Kullanım Senaryoları**

Aspose.Cells, kaynakların sınırlı olduğu durumlarda dönüşüm sürecini durdurmaya yarayan [**InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor) nesnesini kullanmanıza izin verir. Dönüşüm süreci genellikle hem CPU hem de Bellek yoğun olup, kaynaklar sınırlı olduğunda durdurmak yararlı olabilir. Dönüşümü durdurmak için [**InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor) hem dönüşümü durdurmak hem de büyük çalışma kitabını yüklemeyi durdurmak için kullanabilirsiniz. Dönüşümü durdurmak için [**Workbook.InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/interruptmonitor) özelliğini ve büyük çalışma kitabını yüklemek için [**LoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/interruptmonitor) özelliğini kullanabilirsiniz.

## **Çok uzun sürüyorsa, Duraklatma İzleyiciyi kullanarak dönüşümü veya yüklemeyi durdurun**

Aşağıdaki örnek kod, [**InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor) nesnesinin kullanımını açıklar. Kod, oldukça büyük bir Excel dosyasını PDF'e dönüştürür. Bu kod satırları nedeniyle dönüştürülmesi birkaç saniye (yani, *30 saniyeden fazla*) sürecektir.

{{< highlight csharp >}}

//Access cell J1000000 and add some text inside it.

Cell cell = ws.Cells["J1000000"];

cell.PutValue("This is text.");

{{< /highlight >}}

Gördüğünüz gibi **J1000000** XLSX dosyasındaki oldukça uzağa bir hücredir. Ancak **WaitForWhileAndThenInterrupt()** metodu 10 saniye sonra dönüşümü keser ve program sona erer/sonlandırır. Örnek kodu çalıştırmak için lütfen aşağıdaki kodu kullanın.

{{< highlight csharp >}}

 new StopConversionOrLoadingUsingInterruptMonitor().TestRun();

{{< /highlight >}}

## **Örnek Kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Example-StopConversionOrLoadingUsingInterruptMonitor.cs" >}}
