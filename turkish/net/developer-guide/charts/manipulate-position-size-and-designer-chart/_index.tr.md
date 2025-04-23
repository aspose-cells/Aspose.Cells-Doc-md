---
title: Pozisyon Boyutunu ve Tasarımcı Grafiğini Manipüle Edin
description: Microsoft Excel de konumu, boyutu ve tasarımcı grafiğini etkili bir şekilde manipüle etmeyi Aspose.Cells for .NET kullanarak nasıl öğreneceğinizi öğrenin. Kılavuzumuz, bu özellikleri geliştirilmiş düzen ve görselleştirme için nasıl ayarlayacağınızı gösterecektir.
keywords: Aspose.Cells for .NET, Pozisyon, Boyut, Tasarımcı Grafik, Microsoft Excel, Düzen, Görselleştirme.
type: docs
weight: 45
url: /tr/net/manipulate-position-size-and-designer-chart/
---

## **Grafik Pozisyonu ve Boyutu**
Bazı durumlarda, yeni veya mevcut grafiğin konumunu veya boyutunu değiştirmek isteyebilirsiniz. Aspose.Cells, bunu başarmak için [Chart.ChartObject](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/chartobject) özelliğini sağlar. Yeni **yükseklik** ve **genişlik** ile grafik boyutunu veya yeni **X** ve **Y** koordinatları ile konumunu ayarlamak için alt özelliklerini kullanabilirsiniz.
### **Grafiğin Konumunu ve Boyutunu Kontrol Etmek**
Grafiğin konumunu (X, Y koordinatları) veya boyutunu (yükseklik, genişlik) değiştirmek için bu özellikleri kullanın:

1. [Chart.ChartObject.X](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/x)
1. [Chart.ChartObject.Y](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/y)
1. [Chart.ChartObject.Height](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/height)
1. [Chart.ChartObject.Width](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/width)

Aşağıdaki örnek, yukarıdaki API'ların nasıl kullanılacağını açıklar, mevcut bir işkitabını yükler ve ilk çalışma sayfasında bir grafiği yeniden boyutlandırır ve konumlandırır.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChangeChartPosition-1.cs" >}}
## **Tasarımcı Grafikleri Manipüle Etmek**
Tasarımcı şablon dosyalarında grafikleri manipüle veya değiştirmeniz gereken zamanlar olabilir. Aspose.Cells, tasarımcı grafik içeriğini ve elemanlarını tamamen destekler. Veri, grafik içeriği, arka plan görüntüsü ve biçimlendirmeler doğrulukla korunabilir.
### **Şablon Dosyalarında Tasarımcı Grafiklerini Manipüle Etmek**
Şablon dosyalarında tasarımcı grafiklerini manipüle etmek için grafikle ilgili API'ı kullanın. Örneğin, şablon dosyasındaki mevcut grafik koleksiyonunu elde etmek için Worksheet.Charts özelliğini kullanabilirsiniz.
#### **Bir Grafik Oluşturma**
Aşağıdaki örnek, bir piramit grafiği oluşturmanın nasıl yapıldığını göstermektedir. Bu grafiği daha sonra manipüle edeceğiz.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-HowToCreateChart-1.cs" >}}
#### **Grafiği Manipüle Etmek**
Aşağıdaki örnek, mevcut grafiği nasıl manipüle edeceğimizi göstermektedir. Bu örnekte, yukarıda oluşturulan grafiği değiştireceğiz. Oluşturulan çıktıda, bir veri noktasının tarih etiketinin 'Birleşik Krallık, 30K' olarak ayarlandığına dikkat edin.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyPieChart-1.cs" >}}
#### **Tasarımcı Şablonunda Bir Çizgi Grafiği Manipüle Etmek**
Bu örnekte, bir çizgi grafiği manipüle edeceğiz. Mevcut grafiğe bazı veri serileri ekleyeceğiz ve bunların çizgi renklerini değiştireceğiz.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyLineChart-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
