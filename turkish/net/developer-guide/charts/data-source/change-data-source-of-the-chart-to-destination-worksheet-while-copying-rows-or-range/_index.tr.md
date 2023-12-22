---
title: Satırları veya Aralığı Kopyalarken Grafiğin Veri Kaynağını Hedef Çalışma Sayfasına Değiştirme
description: Aspose.Cells for .NET numaralı telefondan satırları veya aralığı kopyalarken grafiğin veri kaynağını hedef çalışma sayfasına nasıl değiştireceğinizi öğrenin. Rehberimiz size grafiğin veri aralığını nasıl güncelleyeceğinizi ve onu hedef çalışma sayfasına nasıl bağlayacağınızı gösterecek ve kopyalanan satırların veya aralığı grafiğe doğru bir şekilde yansıtılmıştır.
keywords: Aspose.Cells for .NET, charting, data source, destination worksheet, rows, range, copy, update, data range, linkage.
type: docs
weight: 440
url: /tr/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---
##  **Olası Kullanım Senaryoları**

Grafikleri içeren satırları veya aralığı yeni bir çalışma sayfasına kopyaladığınızda grafiğin veri kaynağı değişmez. Örneğin, grafiğin veri kaynağı =Sayfa1!$A$1:$B$4 ise, satırları veya aralığı yeni çalışma sayfasına kopyaladıktan sonra veri kaynağı aynı kalacaktır; yani =Sayfa1!$A$1:$B$4. Hala eski çalışma sayfasına yani Sayfa1'e atıfta bulunuyor. Bu aynı zamanda Microsoft Excel'deki davranıştır. Ancak bunun yeni hedef çalışma sayfasına başvurmasını istiyorsanız lütfen[**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet)özelliği ve bunu şu şekilde ayarlayın:**doğru** ararken[**Cells.CopyRows()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index)yöntem. Artık hedef çalışma sayfanız DestSheet ise, grafiğinizin veri kaynağı =Sheet1!$A$1:$B$4 yerine =DestSheet!$A$1:$B$4 olarak değişecektir.

##  **Satırları veya Aralığı Kopyalarken Grafiğin Veri Kaynağını Hedef Çalışma Sayfasına Değiştirme**

Aşağıdaki örnek kod, kullanımını açıklamaktadır.[**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet) Grafikleri içeren satırları veya aralığı yeni bir çalışma sayfasına kopyalarken özellik. Kod şunu kullanır:[örnek excel dosyası](5113699.xlsx) ve üretir[excel dosyasının çıktısını almak](5113697.xlsx).

![yapılacak şey:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ChangeChartDataSource-1.cs" >}}
