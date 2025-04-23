---
title: Çok uzun sürüyorsa, Durdur dönüşümü veya yüklemeyi kullanarak InterruptMonitor
type: docs
weight: 100
url: /tr/java/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
---

## **Olası Kullanım Senaryoları**

Aspose.Cells, kaynakların sınırlı olduğu durumlarda dönüşümün uzun sürdüğünde PDF, HTML vb. farklı formattaki dönüşümü **[**InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor)** nesnesini kullanarak durdurmanıza izin verir. Dönüşüm süreci genellikle hem CPU hem de Bellek yoğundur ve kaynaklar sınırlı olduğunda durdurmak faydalı olabilir. Dönüşümü durdurmak için [**Workbook.InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#InterruptMonitor) özelliğini, büyük bir çalışma kitabını yüklerken durdurmak için [**InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor) kullanabilirsiniz lütfen. Dönüşüm durdurmak ve büyük bir çalışma kitabını yüklemek için lütfen [**LoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#InterruptMonitor) özelliğini kullanın.

## **Çok uzun sürüyorsa, Duraklatma İzleyiciyi kullanarak dönüşümü veya yüklemeyi durdurun**

Aşağıdaki örnek kod, [**InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor) nesnesinin kullanımını açıklar. Bu kod oldukça büyük bir Excel dosyasını PDF'ye dönüştürür. Kodlar nedeniyle dönüşümün alması birkaç saniye sürebilir (örneğin *30 saniyeden fazla*)

{{< highlight java >}}

//Access cell AB1000000 and add some text inside it.

Cell cell = ws.getCells().get("AB1000000");

cell.putValue("This is text.");

{{< /highlight >}}

Görüldüğü gibi **AB1000000** XLSX dosyasında oldukça uzak bir hücredir. Ancak, *WaitForWhileAndThenInterrupt()* metodu dönüşümü 10 saniye sonra keser ve program sona erer/bitirilir. Örnek kodu çalıştırmak için aşağıdaki kodu kullanın.

{{< highlight java >}}

new StopConversionOrLoadingUsingInterruptMonitor().testRun();

{{< /highlight >}}

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-StopConversionOrLoadingUsingInterruptMonitor-1.java" >}}
{{< app/cells/assistant language="java" >}}
