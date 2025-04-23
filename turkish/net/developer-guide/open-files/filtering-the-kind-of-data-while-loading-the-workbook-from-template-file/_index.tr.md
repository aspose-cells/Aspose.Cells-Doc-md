---
title: Şablon dosyasından çalışma kitabını yüklerken veri türünü filtreleme
type: docs
weight: 400
url: /tr/net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---

{{% alert color="primary" %}}

Bazen, şablon dosyasından çalışma kitabını oluştururken yüklenmesi gereken veri türünü belirtmek isteyebilirsiniz. Yüklenen verileri filtrelemek, özellikle [LightCells API'leri](/cells/tr/net/using-lightcells-api/) kullanılırken özel amaçlarınız için performansı artırabilir. Bu amaçla lütfen [**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter) özelliğini kullanın.

{{% /alert %}}

Aşağıdaki örnek kod, şablon dosyasından çalışma kitabı yüklenirken yalnızca şekil nesnelerini yükler. Bu amaçla ayarladığınız [**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter) özelliği [**LoadDataFilterOptions.Shape**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) olacağı için, kırmızı renkli ve sarı arka planlı verilerin yüklenmeyeceği şablon dosyasının içeriğini ve açıklamasını gösterir.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

Aşağıdaki ekran görüntüsü, verilerin kırmızı renkli ve sarı arka planlı olmadığını, ancak tüm şekillerin olduğunu gösterir.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilterDataWhileLoadingWorkbook-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
