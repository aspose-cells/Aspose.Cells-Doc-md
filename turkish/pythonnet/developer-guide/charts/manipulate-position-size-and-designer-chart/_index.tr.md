---
title: Pozisyon Boyutunu ve Tasarımcı Grafiğini Manipüle Edin
description: Microsoft Excel de uygun yer, boyut ve tasarımcı grafiği üzerinde etkili bir şekilde manipüle etmek için Aspose.Cells for Python via .NET kullanmayı öğrenin. Kılavuzumuz, bu özellikleri ayarlayarak düzen ve görselleştirmeyi nasıl geliştireceğinizi gösterecek.
keywords: Aspose.Cells for Python via .NET, Konum, Boyut, Tasarımcı Grafik, Microsoft Excel, Düzen, Görselleştirme.
type: docs
weight: 45
url: /tr/python-net/manipulate-position-size-and-designer-chart/
---

## **Grafik Pozisyonu ve Boyutu**
Bazen, çalışma sayfası içindeki yeni veya mevcut grafiğin konumunu veya boyutunu değiştirmek isteyebilirsiniz. Aspose.Cells for Python via .NET bu amacı gerçekleştirmek için [Chart.chart_object](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/chart_object) özelliğini sağlar. Bu özelliğin alt özelliklerini kullanarak, grafiği yeni **yükseklik** ve **genişlik** ile yeniden boyutlandırabilir veya yeni **X** ve **Y** koordinatlarıyla yeniden konumlandırabilirsiniz.
### **Grafiğin Konumunu ve Boyutunu Kontrol Etmek**
Grafiğin konumunu (X, Y koordinatları) veya boyutunu (yükseklik, genişlik) değiştirmek için bu özellikleri kullanın:

1. [Chart.chart_object.x](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/x)
1. [Chart.chart_object.y](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/y)
1. [Chart.chart_object.height](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/height)
1. [Chart.chart_object.width](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/width)

Aşağıdaki örnek, yukarıdaki API'lerin kullanımını açıklar, ilk çalışma sayfasında bir grafik içeren mevcut çalışma kitabını yükler. Daha sonra Aspose.Cells for Python via .NET kullanarak grafiği yeniden boyutlandırır ve yeniden konumlandırır.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ChangeChartPosition-1.py" >}}
## **Tasarımcı Grafikleri Manipüle Etmek**
Zaman zaman, tasarımcı şablon dosyalarındaki grafikleri manipüle etmeniz veya değiştirmeniz gerekebilir. Aspose.Cells for Python via .NET, tasarımcı grafik içeriği ve öğelerini tam destekleyerek, verileri, grafik içeriğini, arka plan resmini ve biçimlendirmeleri doğru şekilde koruyabilir.
### **Şablon Dosyalarında Tasarımcı Grafiklerini Manipüle Etmek**
Şablon dosyalarında tasarımcı grafiklerini manipüle etmek için grafikle ilgili API'ı kullanın. Örneğin, şablon dosyasındaki mevcut grafik koleksiyonunu elde etmek için Worksheet.Charts özelliğini kullanabilirsiniz.
#### **Bir Grafik Oluşturma**
Aşağıdaki örnek, bir piramit grafiği oluşturmanın nasıl yapıldığını göstermektedir. Bu grafiği daha sonra manipüle edeceğiz.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-HowToCreateChart-1.py" >}}
#### **Grafiği Manipüle Etmek**
Aşağıdaki örnek, mevcut grafiği nasıl manipüle edeceğimizi göstermektedir. Bu örnekte, yukarıda oluşturulan grafiği değiştireceğiz. Oluşturulan çıktıda, bir veri noktasının tarih etiketinin 'Birleşik Krallık, 30K' olarak ayarlandığına dikkat edin.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ManipulateChart-ModifyPieChart-1.py" >}}
#### **Tasarımcı Şablonunda Bir Çizgi Grafiği Manipüle Etmek**
Bu örnekte, bir çizgi grafiği manipüle edeceğiz. Mevcut grafiğe bazı veri serileri ekleyeceğiz ve bunların çizgi renklerini değiştireceğiz.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ManipulateChart-ModifyLineChart-1.py" >}}

