---
title: Çalışma kitabını şablon dosyasından yüklerken veri türünü filtreleme
type: docs
weight: 680
url: /tr/java/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---
{{% alert color="primary" %}} 

 Bazen, çalışma kitabını bir şablon dosyasından oluştururken ne tür verilerin yüklenmesi gerektiğini belirtmek istersiniz. Yüklenen verileri filtrelemek, özellikle kullanırken özel amacınız için performansı artırabilir.[LightCells API'leri](/cells/tr/java/using-lightcells-api/) . lütfen[LoadOptions.getLoadFilter().setLoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#LoadDataFilterOptions) Bu amaçla mülk.

{{% /alert %}} 
## **Çalışma kitabını bir şablon dosyasından yüklerken veri türünü filtreleme**
Aşağıdaki örnek kod, çalışma kitabını bilgisayardan yüklerken yalnızca şekil nesnelerini yükler.[şablon dosyası](5472556.xlsx)verilen linkten indirebilirsiniz.

Aşağıdaki ekran görüntüsü[şablon dosyası](5472556.xlsx) içeriği ve ayrıca Kırmızı renkli ve Sarı arka plandaki verilerin yüklenmeyeceğini açıklar çünkü[LoadOptions.getLoadFilter().setLoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#LoadDataFilterOptions)özellik ayarlandı[LoadDataFilterOptions.SHAPE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHAPE).

![yapılacaklar:resim_alternatif_Metin](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

Aşağıdaki ekran görüntüsü[çıktı PDF](5472554.pdf) verilen linkten indirebilirsiniz. Burada kırmızı renkteki ve Sarı arka plandaki verilerin mevcut olmadığını ancak tüm şekillerin orada olduğunu görebilirsiniz.

![yapılacaklar:resim_alternatif_Metin](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-FilterDataWhileLoadingWorkbook-1.java" >}}
