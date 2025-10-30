---
title: Şablon dosyasından çalışma kitabını yüklerken veri türünü filtreleme
type: docs
weight: 400
url: /tr/python-net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---

{{% alert color="primary" %}}

Bazen, şablon dosyasından çalışma kitabı oluştururken hangi tür verilerin yüklenmesini istediğinizi belirtmek istersiniz. Yüklenen veriyi filtrelemek performansı artırabilir. Bu amaçla [**LoadOptions.load_filter**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/load_filter) özelliğini kullanın.

{{% /alert %}}

Aşağıdaki örnek kod, şablon dosyasından çalışma kitabı yüklenirken yalnızca şekil nesnelerini yükler. Bu amaçla ayarladığınız [**LoadOptions.load_filter**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/load_filter) özelliği [**LoadDataFilterOptions.SHAPE**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions/) olacağı için, kırmızı renkli ve sarı arka planlı verilerin yüklenmeyeceği şablon dosyasının içeriğini ve açıklamasını gösterir.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

Aşağıdaki ekran görüntüsü, verilerin kırmızı renkli ve sarı arka planlı olmadığını, ancak tüm şekillerin olduğunu gösterir.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-FilterDataWhileLoadingWorkbook-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
