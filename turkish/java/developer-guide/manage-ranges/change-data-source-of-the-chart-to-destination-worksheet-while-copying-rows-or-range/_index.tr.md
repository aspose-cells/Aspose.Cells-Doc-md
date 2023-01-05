---
title: Satırları veya Aralığı Kopyalarken Grafiğin Veri Kaynağını Hedef Çalışma Sayfasına Değiştirin
type: docs
weight: 850
url: /tr/java/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---
## **Olası Kullanım Senaryoları**
Grafikleri içeren satırları veya aralığı yeni çalışma sayfasına kopyaladığınızda, grafiğin veri kaynağı değişmez. Örneğin, grafiğin veri kaynağı =Sayfa1!$A$1:$B$4 ise, satırları veya aralığı yeni çalışma sayfasına kopyaladıktan sonra, veri kaynağı aynı kalacaktır, yani =Sayfa1!$A$1:$B$4. Hala eski çalışma sayfasına, yani Sayfa1'e atıfta bulunuyor. Bu aynı zamanda Microsoft Excel davranışıdır. Ancak yeni hedef çalışma sayfasına atıfta bulunmasını istiyorsanız, lütfen CopyOptions.ReferToDestinationSheet özelliğini kullanın ve Cells.CopyRows() yöntemini çağırırken bunu doğru olarak ayarlayın. Şimdi, hedef çalışma sayfanız DestSheet ise, grafiğinizin veri kaynağı =Sheet1!$A$1:$B$4 iken =DestSheet!$A$1:$B$4 olarak değişir.
## **Satırları veya Aralığı Kopyalarken Grafiğin Veri Kaynağını Hedef Çalışma Sayfasına Değiştirin**
 Aşağıdaki örnek kod, grafiği içeren satırları veya aralığı yeni çalışma sayfasına kopyalarken CopyOptions.ReferToDestinationSheet özelliğinin kullanımını açıklar. kod kullanır[örnek excel dosyası](5472284.xlsx) ve oluşturur[çıktı excel dosyası](5472283.xlsx) . Ekran görüntüsü, grafiğin veri kaynağının[çıktı excel dosyası](5472283.xlsx) artık Sayfa1 yerine DestSheet'i ifade ediyor.

![yapılacaklar:resim_alternatif_metin](change-data-source-of-the-chart_1.png)







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeDataSource-ChangeDataSource.java" >}}






