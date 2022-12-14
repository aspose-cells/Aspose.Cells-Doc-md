---
title: Satırları veya Aralığı Kopyalarken Grafiğin Veri Kaynağını Hedef Çalışma Sayfasına Değiştirin
type: docs
weight: 440
url: /tr/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---
## **Olası Kullanım Senaryoları**

Grafik içeren satırları veya aralığı yeni bir çalışma sayfasına kopyaladığınızda, grafiğin veri kaynağı değişmez. Örneğin, grafiğin veri kaynağı =Sayfa1!$A$1:$B$4 ise, satırları veya aralığı yeni çalışma sayfasına kopyaladıktan sonra, veri kaynağı aynı kalacaktır, yani =Sayfa1!$A$1:$B$4. Hala eski çalışma sayfasına, yani Sayfa1'e atıfta bulunuyor. Bu aynı zamanda Microsoft Excel'deki davranıştır. Ancak, yeni hedef çalışma sayfasına atıfta bulunmasını istiyorsanız, lütfen[**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet)özellik ve bunu ayarlayın**doğru** çağrılırken[**Cells.CopyRows()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index)yöntem. Şimdi, hedef çalışma sayfanız DestSheet ise, grafiğinizin veri kaynağı =Sheet1!$A$1:$B$4 iken =DestSheet!$A$1:$B$4 olarak değişir.

## **Satırları veya Aralığı Kopyalarken Grafiğin Veri Kaynağını Hedef Çalışma Sayfasına Değiştirin**

 Aşağıdaki örnek kod, kullanımını açıklar[**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet) grafikleri içeren satırları veya aralığı yeni bir çalışma sayfasına kopyalarken özelliği. kod kullanır[örnek excel dosyası](5113699.xlsx) ve oluşturur[çıktı excel dosyası](5113697.xlsx).

![yapılacaklar:resim_alternatif_Metin](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ChangeChartDataSource-1.cs" >}}
