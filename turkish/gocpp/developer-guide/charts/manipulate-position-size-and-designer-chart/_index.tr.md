---
title: Golang ile C++ kullanarak Konumu, Boyutu ve Tasarımcı Grafiklerini Manipüle Et
linktitle: Pozisyon Boyutunu ve Tasarımcı Grafiğini Manipüle Edin
description: Microsoft Excel de pozisyon, boyut ve tasarımcı grafiğini etkili biçimde manipüle etmek için Aspose.Cells for C++ nasıl kullanılır öğrenin. Kılavuzumuz, bu özellikleri ayarlayarak düzeni ve görselleştirmeyi geliştirmeye nasıl yardımcı olacağını gösterecektir.
keywords: Aspose.Cells for C++, Pozisyon, Boyut, Tasarımcı Grafik, Microsoft Excel, Düzen, Görselleştirme.
type: docs
weight: 45
url: /tr/go-cpp/manipulate-position-size-and-designer-chart/
---

## **Grafik Pozisyonu ve Boyutu**
Bazen, çalışma sayfası içindeki yeni veya mevcut grafiğin konumunu veya boyutunu değiştirmek istersiniz. Aspose.Cells, bunu başarmak için [Chart.GetChartObject()](https://reference.aspose.com/cells/go-cpp/chart/getchartobject/) özelliğini sağlar. Alt özelliklerini kullanarak, grafiğin **yükseklik** ve **genişlik** ile yeniden boyutlandırılmasını veya yeni **X** ve **Y** koordinatlarıyla yeniden konumlandırılmasını sağlayabilirsiniz.

### **Grafiğin Konumunu ve Boyutunu Kontrol Etmek**
Grafiğin konumunu (X, Y koordinatları) veya boyutunu (yükseklik, genişlik) değiştirmek için bu özellikleri kullanın:

1. [Chart.GetX()](https://reference.aspose.com/cells/go-cpp/shape/getx/)
1. [Chart.GetY()](https://reference.aspose.com/cells/go-cpp/shape/gety/)
1. [Chart.GetHeight()](https://reference.aspose.com/cells/go-cpp/shape/getheight/)
1. [Chart.GetWidth()](https://reference.aspose.com/cells/go-cpp/shape/getwidth/)

Aşağıdaki örnek, yukarıdaki API'ların nasıl kullanılacağını açıklar, mevcut bir işkitabını yükler ve ilk çalışma sayfasında bir grafiği yeniden boyutlandırır ve konumlandırır.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManipulatePositionSizeAndDesignerChart.go" >}}
## **Tasarımcı Grafikleri Manipüle Etmek**
Tasarımcı şablon dosyalarında grafikleri manipüle veya değiştirmeniz gereken zamanlar olabilir. Aspose.Cells, tasarımcı grafik içeriğini ve elemanlarını tamamen destekler. Veri, grafik içeriği, arka plan görüntüsü ve biçimlendirmeler doğrulukla korunabilir.

### **Şablon Dosyalarında Tasarımcı Grafiklerini Manipüle Etmek**
Şablon dosyalarında tasarımcı grafiklerini manipüle etmek için grafikle ilgili API'ı kullanın. Örneğin, şablon dosyasındaki mevcut grafik koleksiyonunu elde etmek için Worksheet.Charts özelliğini kullanabilirsiniz.

#### **Bir Grafik Oluşturma**
Aşağıdaki örnek, bir piramit grafiği oluşturmanın nasıl yapıldığını göstermektedir. Bu grafiği daha sonra manipüle edeceğiz.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManipulatePositionSizeAndDesignerChart-1.go" >}}
#### **Grafiği Manipüle Etmek**
Aşağıdaki örnek, mevcut grafiği nasıl manipüle edeceğimizi göstermektedir. Bu örnekte, yukarıda oluşturulan grafiği değiştireceğiz. Oluşturulan çıktıda, bir veri noktasının tarih etiketinin 'Birleşik Krallık, 30K' olarak ayarlandığına dikkat edin.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManipulatePositionSizeAndDesignerChart-2.go" >}}
#### **Tasarımcı Şablonunda Bir Çizgi Grafiği Manipüle Etmek**
Bu örnekte, bir çizgi grafiği manipüle edeceğiz. Mevcut grafiğe bazı veri serileri ekleyeceğiz ve bunların çizgi renklerini değiştireceğiz.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManipulatePositionSizeAndDesignerChart-3.go" >}}
