---
title: Şablon dosyasından çalışma kitabını yüklerken veri türünü filtreleme
type: docs
weight: 680
url: /tr/java/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---

{{% alert color="primary" %}} 

Şablon dosyasından çalışma kitabını yüklerken veri türünü filtreleme

{{% /alert %}} 
## **Aşağıdaki örnek kod, [şu bağlantıdan](5472556.xlsx) indirebileceğiniz şablon dosyasından yalnızca şekil nesnelerini yükler.**
Aşağıdaki ekran görüntüsü, [şu bağlantıdan](5472556.xlsx) indirebileceğiniz şablon dosyasının içeriğini gösterir ve ayrıca Kırmızı renkli ve Sarı arka planlı verilerin, [LoadOptions.getLoadFilter().setLoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#LoadDataFilterOptions) özelliğinin [LoadDataFilterOptions.SHAPE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHAPE) olarak ayarlandığı için yüklenmeyeceğini açıklar.

Aşağıdaki ekran görüntüsü [şablon dosyasını](5472556.xlsx) içeriğini göstermekte ve ayrıca verinin Kırmızı renkli ve Sarı arka planlı olacağını ve [LoadOptions.getLoadFilter().setLoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#LoadDataFilterOptions) özelliğinin [LoadDataFilterOptions.SHAPE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHAPE) olarak ayarlandığını göstermektedir. Yani yalnızca Yüklem veri filtresi seçeneği 'SHAPE' olarak ayarlandığında yüklenmeyecektir.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

Aşağıdaki ekran görüntüsü, [şu bağlantıdan](5472554.pdf) indirebileceğiniz çıktı PDF'sini gösterir. Burada, Kırmızı renkli ve Sarı arka planlı verilerin bulunmadığını, ancak tüm şekillerin olduğunu görebilirsiniz.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-FilterDataWhileLoadingWorkbook-1.java" >}}
{{< app/cells/assistant language="java" >}}
