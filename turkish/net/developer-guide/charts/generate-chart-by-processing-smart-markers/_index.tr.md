---
title: Akıllı İşaretleyicileri İşleyerek Grafik Oluşturun
type: docs
weight: 2100
url: /tr/net/generate-chart-by-processing-smart-markers/
---
{{% alert color="primary" %}}

 Aspose.Cells API'ler şunları sağlar:[**Çalışma KitabıTasarımcısı**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)biçimlendirmenin ve formüllerin tasarımcı elektronik tablolarına yerleştirildiği ve ardından işlendiği Akıllı İşaretleyicilerle çalışmak için sınıf[**Çalışma KitabıTasarımcısı**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)belirtilen Akıllı İşaretleyicilere göre verileri doldurmak için sınıf. Aşağıdaki adımları gerektirecek Akıllı İşaretleyicileri işleyerek Excel grafikleri oluşturmak da mümkündür.

- Tasarımcı e-tablosunun oluşturulması
- Belirtilen veri kaynağına göre tasarımcı elektronik tablosu işleniyor
- Doldurulmuş verilere dayalı grafiğin oluşturulması

{{% /alert %}}

## Tasarımcı Elektronik Tablosunun Oluşturulması

Bir tasarımcı elektronik tablosu, Microsoft Excel uygulaması veya Aspose.Cells API'leri ile oluşturulmuş, içeriğin çalışma zamanında doldurulabileceği görsel biçimlendirme, formüller ve akıllı işaretleyiciler içeren basit bir Excel dosyasıdır.

Basitlik adına, Aspose.Cells for .NET API'i kullanarak tasarımcı elektronik tablosunu oluşturacağız ve daha sonra gösteri amacıyla dinamik olarak oluşturulmuş bir veri kaynağına karşı işleyeceğiz.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfDesignerSpreadsheet.cs" >}}

## İşleme Tasarımcısı Elektronik Tablosu

Tasarımcı elektronik tablosunu işlemek için, tasarımcı elektronik tablosunda kullanılan Akıllı İşaretleyicilere karşılık gelen bir veri kaynağına sahip olunmalıdır. Örneğin, &=Sales.Year olarak DataTable Sales'de Year sütununu temsil eden bir Smart Marker girdisi oluşturduk. Veri kaynağında karşılık gelen bir sütun yoksa, Aspose.Cells API'leri söz konusu Akıllı İşaretleyici için işlemeyi atlayacak ve sonuç olarak belirli Akıllı İşaretleyici için veriler doldurulmayacaktır.

Bu kullanım örneğini göstermek için veri kaynağını sıfırdan oluşturacağız ve onu önceki adımda oluşturulan tasarımcı elektronik tablosuna göre işleyeceğiz. Bununla birlikte, gerçek zamanlı bir senaryoda, veriler daha sonraki işlemler için zaten mevcut olabilir; bu nedenle, veriler zaten mevcutsa veri kaynağının oluşturulmasını atlayabilirsiniz.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingDesignerSpreadsheet.cs" >}}

Akıllı İşaretleyicilerin işlenmesi, aşağıdaki kod parçacığında gösterildiği gibi oldukça basittir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingOfSmartMarkers.cs" >}}

{{% alert color="primary" %}}

 Yukarıdaki kod parçacığı, mevcut örneğini kullanır.[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook)ilk adımda oluşturulan sınıf. Diskte veya bellekte zaten tasarımcı elektronik tablosu dosyanız varsa, bir örneğini oluşturabilirsiniz.[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook)mevcut tasarımcı elektronik tablosunu yükleyerek sınıf.

{{% /alert %}}

## Grafiğin Oluşturulması

 Veriler yerleştirildikten sonra, tek yapmamız gereken veri kaynağına dayalı bir grafik oluşturmaktır. Örneği basit tutmak için, kullanacağız[**Chart.SetChartDataRange**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/setchartdatarange)yöntemi, böylece grafiği daha fazla yapılandırmamız gerekmez.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfChart.cs" >}}
