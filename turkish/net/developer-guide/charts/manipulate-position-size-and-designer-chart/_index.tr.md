---
title: Konum Boyutunu ve Tasarımcı Tablosunu Yönetin
description: Aspose.Cells for .NET'i kullanarak Microsoft Excel'deki konum, boyut ve tasarımcı grafiğini etkin bir şekilde nasıl kullanacağınızı öğrenin. Kılavuzumuz, gelişmiş düzen ve görselleştirme için bu özelliklerin nasıl ayarlanacağını gösterecektir.
keywords: Aspose.Cells for .NET, Position, Size, Designer Chart, Microsoft Excel, Layout, Visualization.
type: docs
weight: 45
url: /tr/net/manipulate-position-size-and-designer-chart/
---
##  **Grafik Konumu ve Boyutu**
 Bazen çalışma sayfasındaki yeni veya mevcut grafiğin konumunu veya boyutunu değiştirmek istersiniz. Aspose.Cells şunları sağlar[Chart.ChartObject](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/chartobject) Bunu başarmak için mülk. Grafiği yeni boyutlarla yeniden boyutlandırmak için alt özelliklerini kullanabilirsiniz.**yükseklik** Ve**Genişlik** veya yenisiyle yeniden konumlandırın**X** ve **Y** koordinatlar.
###  **Grafik Konumunu ve Boyutunu Kontrol Etme**
Grafiğin konumunu (X, Y koordinatları) veya boyutunu (yükseklik, genişlik) değiştirmek için şu özellikleri kullanın:

1. [Chart.ChartObject.X](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/x)
1. [Chart.ChartObject.Y](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/y)
1. [Chart.ChartObject.Height](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/height)
1. [Chart.ChartObject.Width](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/width)

Aşağıdaki örnek, yukarıdaki API'lerin kullanımını açıklamaktadır; ilk çalışma sayfasında bir grafik içeren mevcut çalışma kitabını yükler. Daha sonra Aspose.Cells'i kullanarak grafiği yeniden boyutlandırır ve yeniden konumlandırır.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChangeChartPosition-1.cs" >}}
##  **Tasarımcı Grafiklerini Değiştirme**
Tasarımcı şablon dosyalarındaki grafikleri değiştirmeniz veya değiştirmeniz gereken zamanlar vardır. Aspose.Cells, tasarımcı grafiği içeriklerinin ve öğelerinin değiştirilmesini tamamen destekler. Veriler, grafik içerikleri, arka plan resmi ve biçimlendirmeler doğrulukla korunabilir.
###  **Şablon Dosyalarındaki Tasarımcı Grafiklerini Değiştirme**
Şablon dosyalarındaki tasarımcı grafiklerini değiştirmek için API ile ilgili grafiği kullanın. Örneğin, şablon dosyasındaki mevcut grafikler koleksiyonunu almak için Worksheet.Charts özelliğini kullanabilirsiniz.
####  **Grafik Oluşturma**
Aşağıdaki örnek piramit grafiğinin nasıl oluşturulacağını gösterir. Bu grafiği daha sonra değiştireceğiz.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-HowToCreateChart-1.cs" >}}
####  **Grafiğin Değiştirilmesi**
Aşağıdaki örnek, mevcut grafiğin nasıl değiştirileceğini gösterir. Bu örnekte yukarıda oluşturulan grafiği değiştiriyoruz. Oluşturulan çıktıda bir veri noktasının tarih etiketinin 'Birleşik Krallık, 30K' olarak ayarlandığını unutmayın.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyPieChart-1.cs" >}}
####  **Tasarımcı Şablonunda Çizgi Grafiğini Değiştirme**
Bu örnekte çizgi grafiğini değiştireceğiz. Mevcut grafiğe bazı veri serileri ekleyip çizgi renklerini değiştireceğiz.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyLineChart-1.cs" >}}

