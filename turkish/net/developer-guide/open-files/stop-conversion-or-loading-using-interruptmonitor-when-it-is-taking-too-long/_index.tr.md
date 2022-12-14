---
title: Çok uzun sürdüğünde InterruptMonitor kullanarak dönüştürmeyi veya yüklemeyi durdurun
type: docs
weight: 100
url: /tr/net/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
---
## **Olası Kullanım Senaryoları**

Aspose.Cells, Çalışma Kitabının PDF, HTML vb.[**Kesinti İzleme**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor) çok uzun sürdüğünde itiraz edin. Dönüştürme işlemi genellikle hem CPU hem de Bellek açısından yoğundur ve kaynaklar sınırlı olduğunda genellikle işlemi durdurmak yararlıdır. Kullanabilirsiniz[**Kesinti İzleme**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor) hem dönüştürmeyi durdurmak hem de büyük çalışma kitabının yüklenmesini durdurmak için. Lütfen kullan[**Workbook.InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/interruptmonitor) dönüştürmeyi durdurma özelliği ve[**LoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/interruptmonitor) büyük çalışma kitabı yükleme özelliği.

## **Çok uzun sürdüğünde InterruptMonitor kullanarak dönüştürmeyi veya yüklemeyi durdurun**

Aşağıdaki örnek kod, kullanımını açıklar[**Kesinti İzleme**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor) nesne. Kod, oldukça büyük bir Excel dosyasını PDF'ye dönüştürür. Birkaç saniye sürecektir (örn.*30 saniyeden fazla*) bu kod satırları nedeniyle dönüştürülmesini sağlamak için.

{{< highlight "csharp" >}}

//Access cell J1000000 and add some text inside it.

Cell cell = ws.Cells["J1000000"];

cell.PutValue("This is text.");

{{< /highlight >}}

 Gördüğünüz gibi**J1000000** XLSX dosyasında oldukça uzak bir hücredir. Ancak**WaitForWhileAndThenInterrupt()**yöntemi, dönüştürmeyi 10 saniye sonra keser ve program biter/sonlanır. Lütfen örnek kodu çalıştırmak için aşağıdaki kodu kullanın.

{{< highlight "csharp" >}}

 new StopConversionOrLoadingUsingInterruptMonitor().TestRun();

{{< /highlight >}}

## **Basit kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Example-StopConversionOrLoadingUsingInterruptMonitor.cs" >}}
