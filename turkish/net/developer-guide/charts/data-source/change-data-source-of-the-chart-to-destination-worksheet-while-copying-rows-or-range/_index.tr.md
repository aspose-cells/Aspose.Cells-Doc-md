---
title: Satırları veya Aralığı Kopyalarken Grafiklerin Veri Kaynağını Hedef Çalışma Sayfasına Değiştirme
description: Aspose.Cells for .NET de sıraları veya bir aralığı kopyalarken bir grafik veri kaynağını hedef çalışma sayfasına nasıl değiştireceğinizi öğrenin. Rehberimiz, tablonuzdaki kopyalanan sıraları veya aralığı doğru bir şekilde yansıtmak için grafik veri aralığını güncelleme ve hedef çalışma sayfasına bağlama yöntemlerini gösterecektir.
keywords: Aspose.Cells for .NET, grafik oluşturma, veri kaynağı, hedef çalışma sayfası, sıralar, aralık, kopya, güncelleme, veri aralığı, bağlantı
type: docs
weight: 440
url: /tr/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---

## **Olası Kullanım Senaryoları**

Bir tabloya kopyaladığınızda sıralar veya bir aralık, içerdiği grafiklerin veri kaynağı değişmez. Örneğin, grafiklerin veri kaynağı =Sheet1!$A$1:$B$4 ise, sonra sıraları veya aralığı yeni bir çalışma sayfasına kopyaladıktan sonra, veri kaynağı aynı kalacaktır, yani =Sheet1!$A$1:$B$4 olarak kalacaktır. Hala eski çalışma sayfasına yani Sheet1'e atıfta bulunur. Bu aynı zamanda Microsoft Excel'de de geçerli bir davranıştır. Ancak yeni hedef çalışma sayfasına atıfta bulunmasını istiyorsanız, lütfen [**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet) özelliğini kullanın ve [**Cells.CopyRows()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index) yöntemini çağırırken onu **true** olarak ayarlayın. Şimdi eğer hedef çalışma sayfanız DestSheet ise, grafiğinizin veri kaynağı =Sheet1!$A$1:$B$4'ten =DestSheet!$A$1:$B$4'e değişecektir.

## **Satırları veya Aralıkları Kopyalarken Grafiğin Veri Kaynağını Hedef Çalışma Sayfasına Değiştirme**

Aşağıdaki örnek kod, kopyalanan sıraları veya aralığı içeren bir çalışma sayfasına tablo oluştururken [**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet) özelliğinin nasıl kullanılacağını açıklar. Kod, [örnek excel dosyasını](5113699.xlsx) kullanır ve [çıktı excel dosyasını](5113697.xlsx) oluşturur.

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ChangeChartDataSource-1.cs" >}}
