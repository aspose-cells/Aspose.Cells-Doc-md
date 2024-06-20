---
title: Akıllı İşaretlerin İşlenmesiyle Grafik Oluşturma
description: Aspose.Cells for .NET kullanarak akıllı işaretleyicileri kullanan grafiklerin nasıl oluşturulacağını öğrenin. Rehberimiz, akıllı işaretleyicileri ve özelliklerini işlemek ve grafiklerinizin görünüşünü ve kullanılabilirliğini artırmak için nasıl kullanacağınızı gösterecektir.
keywords: Aspose.Cells for .NET, grafik oluşturma, akıllı işaretleyiciler, görünüş, kullanılabilirlik, işleme.
type: docs
weight: 2100
url: /tr/net/generate-chart-by-processing-smart-markers/
---

{{% alert color="primary" %}}

Aspose.Cells API'ları, biçimlendirme ve formüllerin tasarım elektronik tablolara yerleştirilmiş ve ardından belirli Akıllı İşaretleyicilere göre verilerin doldurulması için [**WorkbookDesigner**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) sınıfını sağlar. İşaretlenen akıllı işaretleyicileri işleyerek Excel grafikleri oluşturulabilir, bu da aşağıdaki adımları gerektirecektir.

- Tasarımcı elektronik tablosunun oluşturulması
- Belirli veri kaynağına karşı tasarımcı elektronik tablonun işlenmesi
- Popüle edilmiş veriye dayalı olarak grafik oluşturulması

{{% /alert %}}

## Tasarımcı Elektronik Tablonun Oluşturulması

Tasarımcı elektronik tablo, Microsoft Excel uygulaması veya Aspose.Cells API'leri ile oluşturulmuş basit bir Excel dosyasıdır; görsel biçimlendirme, formüller ve akıllı işaretleyiciler içeren, içerikler çalışma zamanında doldurulabilir.

Basitlik açısından, Aspose.Cells for .NET API kullanarak tasarımcı elektronik tablo oluşturacağız ve daha sonra gösterim amaçları için dinamik olarak oluşturulmuş bir veri kaynağına karşı işleyeceğiz.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfDesignerSpreadsheet.cs" >}}

## Tasarımcı Elektronik Tablonun İşlenmesi

Tasarımcı elektronik tablonun işlenmesi için, tasarımcı elektronik tabloda kullanılan Akıllı İşaretleyicilere uygun bir veri kaynağınız olmalıdır. Örneğin, Sales.DataTable'daki Yıl sütununu temsil eden &=Sales.Year şeklinde bir Akıllı İşaretleyici girdisi oluşturduk. Karşılık gelen bir sütun veri kaynağında bulunmuyorsa, Aspose.Cells API'leri o belirli Akıllı İşaretleyici için işlemeyi atlayacak ve sonuç olarak belirli Akıllı İşaretleyici için veriler doldurulmayacaktır.

Bu kullanım durumunu göstermek için, veri kaynağını sıfırdan oluşturacağız ve hazırladığımız tasarımcı elektronik tabloya karşı işleyeceğiz. Bununla birlikte, gerçek zamanlı bir senaryoda, veri zaten mevcutsa, veri kaynağının oluşturulmasını atlayabilirsiniz.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingDesignerSpreadsheet.cs" >}}

Akıllı İşaretleyicilerin işlenmesi, aşağıdaki kod örneği ile gösterildiği gibi oldukça basittir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingOfSmartMarkers.cs" >}}

{{% alert color="primary" %}}

Yukarıdaki kod örneği, ilk adımda oluşturulan [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfının mevcut örneğini kullanmaktadır. Eğer zaten diskte veya bellekte tasarımcı elektronik tablo dosyası varsa, mevcut tasarımcı elektronik tablosunu yükleyerek [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfının bir örneğini oluşturabilirsiniz.

{{% /alert %}}

## Grafik Oluşturma

Veri yerine getirildikten sonra, yapmamız gereken tek şey veri kaynağına dayalı bir grafik oluşturmaktır. Örneği basit tutmak için [**Chart.SetChartDataRange**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/setchartdatarange) yöntemini kullanacağız, böylece grafikleri daha fazla yapılandırmaya gerek kalmadan kullanabiliriz.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfChart.cs" >}}
