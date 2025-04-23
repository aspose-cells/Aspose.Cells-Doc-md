---
title: Satırları veya Aralığı Kopyalarken Grafiklerin Veri Kaynağını Hedef Çalışma Sayfasına Değiştirme
description: Aspose.Cells for Python via .NET kullanarak çizgi veya aralık kopyalarken, grafikteki veri kaynağını hedef çalışma sayfasına nasıl değiştireceğinizi öğrenin. Kılavuzumuz, grafiğin veri aralığını güncelleme ve ona hedef çalışma sayfasını bağlama yollarını gösterecek, böylece kopyalanan satırlar veya aralıklar grafikte doğru şekilde yansıtılır.
keywords: Aspose.Cells for Python via .NET, grafik, veri kaynağı, hedef çalışma sayfası, satırlar, aralık, kopyalama, güncelleme, veri aralığı, bağlantı.
type: docs
weight: 440
url: /tr/python-net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---

## **Olası Kullanım Senaryoları**

Bir tabloya kopyaladığınızda sıralar veya bir aralık, içerdiği grafiklerin veri kaynağı değişmez. Örneğin, grafiklerin veri kaynağı =Sheet1!$A$1:$B$4 ise, sonra sıraları veya aralığı yeni bir çalışma sayfasına kopyaladıktan sonra, veri kaynağı aynı kalacaktır, yani =Sheet1!$A$1:$B$4 olarak kalacaktır. Hala eski çalışma sayfasına yani Sheet1'e atıfta bulunur. Bu aynı zamanda Microsoft Excel'de de geçerli bir davranıştır. Ancak yeni hedef çalışma sayfasına atıfta bulunmasını istiyorsanız, lütfen [**CopyOptions.refer_to_destination_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/copyoptions/refer_to_destination_sheet) özelliğini kullanın ve [**Cells.copy_rows()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_rows) yöntemini çağırırken onu **true** olarak ayarlayın. Şimdi eğer hedef çalışma sayfanız DestSheet ise, grafiğinizin veri kaynağı =Sheet1!$A$1:$B$4'ten =DestSheet!$A$1:$B$4'e değişecektir.

## **Satırları veya Aralıkları Kopyalarken Grafiğin Veri Kaynağını Hedef Çalışma Sayfasına Değiştirme**

Aşağıdaki örnek kod, kopyalanan sıraları veya aralığı içeren bir çalışma sayfasına tablo oluştururken [**CopyOptions.refer_to_destination_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/copyoptions/refer_to_destination_sheet) özelliğinin nasıl kullanılacağını açıklar. Kod, [örnek excel dosyasını](5113699.xlsx) kullanır ve [çıktı excel dosyasını](5113697.xlsx) oluşturur.

![todo:image_alt_text](1.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ChangeChartDataSource-1.py" >}}
