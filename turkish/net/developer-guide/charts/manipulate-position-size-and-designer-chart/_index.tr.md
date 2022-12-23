---
title: Pozisyon Boyutunu ve Tasarımcı Grafiğini İşleyin
type: docs
weight: 45
url: /tr/net/manipulate-position-size-and-designer-chart/
---
## **Grafik Konumu ve Boyutu**
 Bazen, çalışma sayfasındaki yeni veya mevcut grafiğin konumunu veya boyutunu değiştirmek istersiniz. Aspose.Cells şunları sağlar:[Chart.ChartObject](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/chartobject) Bunu başarmak için mülkiyet. Grafiği yenisiyle yeniden boyutlandırmak için alt özelliklerini kullanabilirsiniz.**boy uzunluğu** ve**Genişlik** veya yenisiyle yeniden konumlandırın** X** ve**Y** koordinatları.
### **Grafik Konumunu ve Boyutunu Kontrol Etme**
Grafiğin konumunu (X, Y koordinatları) veya boyutunu (yükseklik, genişlik) değiştirmek için şu özellikleri kullanın:

1. [Chart.ChartObject.X](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/x)
1. [Chart.ChartObject.Y](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/y)
1. [Chart.ChartObject.Height](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/height)
1. [Chart.ChartObject.Width](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/width)

Aşağıdaki örnek, yukarıdaki API'lerin kullanımını açıklar, ilk çalışma sayfasında bir grafik içeren mevcut çalışma kitabını yükler. Ardından, Aspose.Cells'i kullanarak grafiği yeniden boyutlandırır ve yeniden konumlandırır.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChangeChartPosition-1.cs" >}}
## **Tasarımcı Grafiklerini Değiştirme**
Tasarımcı şablon dosyalarındaki grafikleri manipüle etmeniz veya değiştirmeniz gereken zamanlar vardır. Aspose.Cells, tasarımcı grafiği içeriklerini ve öğelerini değiştirmeyi tam olarak destekler. Veriler, grafik içerikleri, arka plan görüntüsü ve biçimlendirmeler doğrulukla korunabilir.
### **Şablon Dosyalarında Tasarımcı Grafiklerini Değiştirme**
Şablon dosyalarındaki tasarımcı grafiklerini değiştirmek için API ile ilgili grafiği kullanın. Örneğin, şablon dosyasındaki mevcut grafikler koleksiyonunu almak için Worksheet.Charts özelliğini kullanabilirsiniz.
#### **Grafik Oluşturma**
Aşağıdaki örnek, bir piramit grafiğinin nasıl oluşturulacağını gösterir. Bu tabloyu daha sonra manipüle edeceğiz.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-HowToCreateChart-1.cs" >}}
#### **Grafiği Manipüle Etme**
Aşağıdaki örnek, mevcut grafiğin nasıl değiştirileceğini gösterir. Bu örnekte, yukarıda oluşturulan grafiği değiştiriyoruz. Oluşturulan çıktıda, bir veri noktasının tarih etiketinin 'İngiltere, 30K' olarak ayarlandığını unutmayın.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyPieChart-1.cs" >}}
#### **Tasarımcı Şablonunda Çizgi Grafiği Değiştirme**
Bu örnekte, bir çizgi grafiğini işleyeceğiz. Mevcut grafiğe bazı veri serileri ekleyeceğiz ve çizgi renklerini değiştireceğiz.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyLineChart-1.cs" >}}

