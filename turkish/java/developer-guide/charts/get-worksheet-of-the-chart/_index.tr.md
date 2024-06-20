---
title: Grafik Çalışsayısını Al
type: docs
weight: 80
url: /tr/java/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

Bazen, grafik referansından bir çalışsayısına erişmek istersiniz. Aspose.Cells, grafiği içeren çalışsayısının referansını döndüren [**Chart.getWorksheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#Worksheet) özelliğini sağlar.

{{% /alert %}}

## Örnek

Aşağıdaki örnek, [**Chart.getWorksheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#Worksheet) özelliğinin nasıl kullanılacağını göstermektedir. Kod öncelikle çalışsayısının adını yazdırır, daha sonra çalışsayısı üzerindeki ilk grafiğe erişir. Daha sonra [**Chart.getWorksheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#Worksheet) özelliğini kullanarak tekrar çalışsayı adını yazdırır.

### Çizelge çalışma sayfasına erişmek için Java kodu

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetWorksheetOfChart-GetWorksheetOfChart.java" >}}

### Örnek kod tarafından oluşturulan konsol çıktısı

Aşağıda, örnek kodun sonuçlarına denk gelen konsol çıktısı bulunmaktadır. Görebileceğiniz gibi, her iki kez de aynı çalışma sayfası adını yazdırır.

{{< highlight java >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
