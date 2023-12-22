---
title: Akıllı İşaretleyicileri İşleyerek Grafik Oluşturun
description: Aspose.Cells for .NET numaralı telefonu kullanarak akıllı işaretçilerle nasıl grafik oluşturacağınızı öğrenin. Rehberimiz, grafiklerinizin görünümünü ve kullanılabilirliğini geliştirmek için akıllı işaretçileri ve bunların özelliklerini nasıl işleyeceğinizi gösterecektir.
keywords: Aspose.Cells for .NET, chart generation, smart markers, appearance, usability, processing.
type: docs
weight: 2100
url: /tr/net/generate-chart-by-processing-smart-markers/
---
{{% alert color="primary" %}}

 Aspose.Cells API'ler şunları sağlar:[**Çalışma Kitabı Tasarımcısı**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) biçimlendirmenin ve formüllerin tasarımcı elektronik tablolarına yerleştirildiği ve ardından işlendiği Akıllı İşaretleyiciler ile çalışma sınıfı[**Çalışma Kitabı Tasarımcısı**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)verileri belirtilen Akıllı İşaretleyicilere göre doldurmak için sınıf. Aşağıdaki adımları gerektirecek Akıllı İşaretleyicileri işleyerek Excel grafikleri oluşturmak da mümkündür.

- Tasarımcı elektronik tablosunun oluşturulması
- Tasarımcı elektronik tablosu belirtilen veri kaynağına göre işleniyor
- Doldurulmuş verilere dayalı grafiğin oluşturulması

{{% /alert %}}

##  Tasarımcı Elektronik Tablosunun Oluşturulması

Tasarımcı elektronik tablosu, içeriğin çalışma zamanında doldurulabileceği görsel biçimlendirmeyi, formülleri ve akıllı işaretçileri içeren Microsoft Excel uygulaması veya Aspose.Cells API'leri ile oluşturulan basit bir Excel dosyasıdır.

Basitlik adına, Aspose.Cells for .NET API'i kullanarak tasarımcı elektronik tablosunu oluşturacağız ve daha sonra bunu gösterim amacıyla dinamik olarak oluşturulmuş bir veri kaynağına karşı işleyeceğiz.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfDesignerSpreadsheet.cs" >}}

##  İşleme Tasarımcısı Elektronik Tablosu

Tasarımcı elektronik tablosunu işlemek için, tasarımcı elektronik tablosunda kullanılan Akıllı İşaretleyicilere karşılık gelen bir veri kaynağına sahip olunması gerekir. Örneğin, DataTable Sales'teki Yıl sütununu temsil eden &=Satış.Yıl şeklinde bir Akıllı İşaretleyici girişi oluşturduk. Veri kaynağında karşılık gelen bir sütunun bulunmaması durumunda, Aspose.Cells API'leri söz konusu Akıllı İşaretleyiciye ilişkin işlemi atlayacak ve sonuç olarak söz konusu Akıllı İşaretleyiciye ilişkin veriler doldurulmayacaktır.

Bu kullanım durumunu göstermek için veri kaynağını sıfırdan oluşturacağız ve onu önceki adımda oluşturulan tasarımcı elektronik tablosuna göre işleyeceğiz. Ancak gerçek zamanlı bir senaryoda, veriler daha sonraki işlemler için zaten mevcut olabilir; dolayısıyla, veriler zaten mevcutsa veri kaynağı oluşturma işlemini atlayabilirsiniz.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingDesignerSpreadsheet.cs" >}}

Akıllı İşaretleyicilerin işlenmesi aşağıdaki kod parçacığında da gösterildiği gibi oldukça basittir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingOfSmartMarkers.cs" >}}

{{% alert color="primary" %}}

 Yukarıdaki kod parçacığı, mevcut örneğini kullanır.[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) İlk adımda oluşturulan sınıf. Diskte veya bellekte tasarımcı elektronik tablosu dosyanız zaten varsa, bunun bir örneğini oluşturabilirsiniz.[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook)mevcut tasarımcı e-tablosunu yükleyerek sınıf.

{{% /alert %}}

##  Grafiğin Oluşturulması

 Veriler yerleştirildikten sonra tek yapmamız gereken, veri kaynağına dayalı bir grafik oluşturmaktır. Örneği basit tutmak için şunu kullanacağız:[**Chart.SetChartDataRange**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/setchartdatarange)Grafiği daha fazla yapılandırmamıza gerek kalmayacak şekilde.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfChart.cs" >}}
