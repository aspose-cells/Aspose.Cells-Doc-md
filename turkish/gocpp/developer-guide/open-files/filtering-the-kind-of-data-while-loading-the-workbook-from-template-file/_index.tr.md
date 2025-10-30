---
title: Golang ve C++ kullanarak şablon dosyasından çalışma kitabı yüklerken veri türlerini filtreleme
linktitle: Çalışma Kitabı Yüklerken Veri Filtreleme
type: docs
weight: 400
url: /tr/go-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
description: Aspose.Cells kullanarak Golang ve C++ ile şablon dosyasından çalışma kitabı yüklerken belirli veri türlerini filtrelemeyi öğrenin.
---

{{% alert color="primary" %}}

 Bazen, çalışma kitabını şablon dosyasından oluştururken hangi tür verinin yükleneceğini belirtmek istersiniz. Yüklenen veriyi filtrelemek, özellikle [LightCells API'leri](/cells/tr/cpp/using-lightcells-api/) kullanırken, performansı artırabilir. Bu amaçla [**LoadOptions.GetLoadFilter()**](https://reference.aspose.com/cells/go-cpp/loadoptions/getloadfilter/) özelliğini kullanın.

{{% /alert %}}

Aşağıdaki örnek kod, şablon dosyasından çalışma kitabı yüklenirken yalnızca şekil nesnelerini yükler. Bu amaçla ayarladığınız [**LoadOptions.GetLoadFilter()**](https://reference.aspose.com/cells/go-cpp/loadoptions/getloadfilter/) özelliği [**LoadDataFilterOptions.Shape**](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions/) olacağı için, kırmızı renkli ve sarı arka planlı verilerin yüklenmeyeceği şablon dosyasının içeriğini ve açıklamasını gösterir.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

Aşağıdaki ekran görüntüsü, verilerin kırmızı renkli ve sarı arka planlı olmadığını, ancak tüm şekillerin olduğunu gösterir.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilteringTheKindOfDataWhileLoadingTheWorkbookFromTemplateFile.go" >}}
