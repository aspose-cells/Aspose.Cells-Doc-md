---
title: Çalışma kitabını şablon dosyasından yüklerken veri türünü filtreleme
type: docs
weight: 400
url: /tr/net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---
{{% alert color="primary" %}}

 Bazen, çalışma kitabını şablon dosyasından oluştururken ne tür verilerin yüklenmesi gerektiğini belirtmek istersiniz. Yüklenen verileri filtrelemek, özellikle kullanırken özel amacınız için performansı artırabilir.[LightCells API'leri](/cells/tr/net/using-lightcells-api/) . lütfen[**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter) Bu amaçla mülk.

{{% /alert %}}

Aşağıdaki örnek kod, çalışma kitabını bilgisayardan yüklerken yalnızca şekil nesnelerini yükler.[şablon dosyası](5115552.xlsx) verilen linkten indirebilirsiniz. Aşağıdaki ekran görüntüsü[şablon dosyası](5115552.xlsx) içeriği ve ayrıca Kırmızı renkli ve Sarı arka plandaki verilerin yüklenmeyeceğini açıklar çünkü[**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter)özellik ayarlandı[**LoadDataFilterOptions.Shape**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)

![yapılacaklar:resim_alternatif_Metin](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

Aşağıdaki ekran görüntüsü[çıktı PDF](5115555.pdf) verilen linkten indirebilirsiniz. Burada kırmızı renkteki ve Sarı arka plandaki verilerin mevcut olmadığını ancak tüm şekillerin orada olduğunu görebilirsiniz.

![yapılacaklar:resim_alternatif_Metin](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilterDataWhileLoadingWorkbook-1.cs" >}}
