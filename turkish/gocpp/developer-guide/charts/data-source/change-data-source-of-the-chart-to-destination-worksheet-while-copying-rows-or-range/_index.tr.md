---  
title: Kopyalama sırasında Golang ile C++ aracılığıyla Hedef Sayfaya Grafik Veri Kaynağını Değiştirme  
description: Aspose.Cells for C++ te, satırları veya aralığı kopyalarken grafiğin veri kaynağını hedef çalışma sayfasına nasıl değiştireceğinizi öğrenin. Kılavuzumuz, grafiğin veri aralığını güncelleme ve hedef çalışma sayfasına bağlama adımlarını gösterecek, böylece kopyalanan satır veya aralıklar grafikte doğru şekilde yansıtılır.  
keywords: Aspose.Cells for C++, grafik çizimi, veri kaynağı, hedef çalışma sayfası, satırlar, aralık, kopyalama, güncelleme, veri aralığı, bağlantı.  
type: docs  
weight: 440  
url: /tr/go-cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/  
---  

## **Olası Kullanım Senaryoları**

Grafiklerin veri kaynağı, satır veya aralıkları yeni bir çalışma sayfasına kopyaladığınızda değişmez. Örneğin, grafik veri kaynağı =Sheet1!$A$1:$B$4 ise, satırlar veya aralıklar yeni bir çalışma sayfasına kopyalandığında veri kaynağı aynı kalır yani =Sheet1!$A$1:$B$4 olur. Bu, Microsoft Excel'de de aynı davranıştır. Ancak, yeni hedef çalışma sayfasını göstermek istiyorsanız, [**CopyOptions.GetReferToDestinationSheet()**](https://reference.aspose.com/cells/go-cpp/copyoptions/getrefertodestinationsheet/) özelliğini kullanın ve [**Cells.CopyRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/copyrows/) metodunu çağırırken **true** olarak ayarlayın. Hedef çalışma sayfanız DestSheet ise, grafiğin veri kaynağı =Sheet1!$A$1:$B$4'ten =DestSheet!$A$1:$B$4' e değişecektir.

## **Satırları veya Aralıkları Kopyalarken Grafiğin Veri Kaynağını Hedef Çalışma Sayfasına Değiştirme**

Aşağıdaki örnek kod, grafik içeren satır veya aralıkları yeni bir çalışma sayfasına kopyalarken [**CopyOptions.GetReferToDestinationSheet()**](https://reference.aspose.com/cells/go-cpp/copyoptions/getrefertodestinationsheet/) özelliğinin kullanımını açıklamaktadır. Kod, [örnek excel dosyasını](5113699.xlsx) kullanmakta ve [çıktı excel dosyasını](5113697.xlsx) üretmektedir.

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChangeDataSourceOfTheChartToDestinationWorksheetWhileCopyingRowsOrRange.go" >}}
