---
title: Satırları veya Aralığı Kopyalarken Grafiklerin Veri Kaynağını Hedef Çalışma Sayfasına Değiştirme
type: docs
weight: 850
url: /tr/java/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---

## **Olası Kullanım Senaryoları**
Grafik içeren satırları veya aralığı yeni çalışma sayfasına kopyaladığınızda, grafiklerin veri kaynağı değişmez. Örneğin, grafiklerin veri kaynağı =Sheet1!$A$1:$B$4 ise, satırları veya aralığı yeni çalışma sayfasına kopyaladıktan sonra, veri kaynağı aynı kalır yani =Sheet1!$A$1:$B$4 olarak kalır. Bu da Microsoft Excel davranışıdır. Ancak, yeni hedef çalışma sayfasına işaret etmesini istiyorsanız, Cells.CopyRows() yöntemini çağırırken CopyOptions.ReferToDestinationSheet özelliğini true olarak ayarlayın. Şimdi hedef çalışma sayfanız DestSheet ise, grafiklerinizin veri kaynağı =Sheet1!$A$1:$B$4 yerine =DestSheet!$A$1:$B$4 olacaktır.
## **Satırları veya Aralıkları Kopyalarken Grafiğin Veri Kaynağını Hedef Çalışma Sayfasına Değiştirme**
Aşağıdaki örnek kod, grafik içeren satırları veya aralığı yeni çalışma sayfasına kopyalarken CopyOptions.ReferToDestinationSheet özelliğinin kullanımını açıklar. Kod, [örnek excel dosyasını](5472284.xlsx) kullanır ve [çıktı excel dosyasını](5472283.xlsx) oluşturur. Ekran görüntüsü, [çıktı excel dosyasındaki](5472283.xlsx) grafik veri kaynağının ArtSeyre yapılması gösterir.

![todo:image_alt_text](change-data-source-of-the-chart_1.png)







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeDataSource-ChangeDataSource.java" >}}






