---
title: Çok uzun sürdüğünde InterruptMonitor kullanarak dönüştürmeyi veya yüklemeyi durdurun
type: docs
weight: 100
url: /tr/java/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
---
## **Olası Kullanım Senaryoları**

Aspose.Cells, Çalışma Kitabının PDF, HTML gibi çeşitli biçimlere dönüştürülmesini durdurmanıza olanak tanır.[**Kesinti İzleme**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor)çok uzun sürdüğünde itiraz edin. Dönüştürme işlemi genellikle hem CPU hem de Bellek açısından yoğundur ve kaynaklar sınırlı olduğunda genellikle işlemi durdurmak yararlıdır. Kullanabilirsiniz[**Kesinti İzleme**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor)hem dönüştürmeyi durdurmak hem de büyük çalışma kitabının yüklenmesini durdurmak için. Lütfen kullan[**Workbook.InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#InterruptMonitor)dönüştürmeyi durdurma özelliği ve[**LoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#InterruptMonitor)büyük çalışma kitabı yükleme özelliği.

## **Çok uzun sürdüğünde InterruptMonitor kullanarak dönüştürmeyi veya yüklemeyi durdurun**

Aşağıdaki örnek kod, kullanımını açıklar[**Kesinti İzleme**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor)nesne. Kod, oldukça büyük bir Excel dosyasını PDF'e dönüştürür. Birkaç saniye sürer (örn.*30 saniyeden fazla*) bu kod satırları nedeniyle dönüştürülmesini sağlamak için.

{{< highlight "java" >}}

//Access cell AB1000000 and add some text inside it.

Cell cell = ws.getCells().get("AB1000000");

cell.putValue("This is text.");

{{< /highlight >}}

Gördüğünüz gibi**AB1000000**XLSX dosyasında oldukça uzak bir hücredir. Ancak*WaitForWhileAndThenInterrupt()*yöntemi, dönüştürmeyi 10 saniye sonra keser ve program biter/sonlanır. Lütfen örnek kodu çalıştırmak için aşağıdaki kodu kullanın.

{{< highlight "java" >}}

new StopConversionOrLoadingUsingInterruptMonitor().testRun();

{{< /highlight >}}

## **Basit kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-StopConversionOrLoadingUsingInterruptMonitor-1.java" >}}
