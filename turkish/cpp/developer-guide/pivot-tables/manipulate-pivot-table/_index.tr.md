---
title: Pivot Tabloyu Yönetme
type: docs
weight: 20
url: /tr/cpp/manipulate-pivot-table/
---
##  **Olası Kullanım Senaryoları**
Yeni pivot tablolar oluşturmanın yanı sıra yeni ve mevcut pivot tabloları da değiştirebilirsiniz. Pivot tablonun kaynak aralığındaki verileri değiştirebilir, ardından yenileyip hesaplayabilir ve pivot tablo hücrelerinin yeni değerlerine ulaşabilirsiniz. Lütfen kullan[PivotTable.RefreshData()](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/refreshdata/) Ve[PivotTable.CalculateData()](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/calculatedata/)Pivot tabloyu yenilemek için pivot tablonun kaynak aralığındaki değerleri değiştirdikten sonra yöntemleri kullanın.
##  **Pivot Tabloyu Yönetme**
 Aşağıdaki örnek kod,[örnek excel dosyası](23167013.xlsx) ve ilk çalışma sayfasındaki mevcut pivot tabloya erişir. Pivot tablonun kaynak aralığı içindeki B3 hücresinin değerini değiştirir ve ardından pivot tabloyu yeniler. Pivot tabloyu yenilemeden önce pivot tablo hücresi H8'in 15 olan değerine erişir ve pivot tablo yenilendikten sonra değeri 6 olarak değişir.[excel dosyasının çıktısını almak](23167014.xlsx)Bu kod ve örnek kodun örnek excel dosyası üzerindeki etkisini gösteren ekran görüntüsü ile oluşturulmuştur. Lütfen ayrıca pivot tablonun yenilenmesinden önce ve sonra pivot tablo hücresi H8'in değerini gösteren aşağıdaki konsol çıktısına bakın.

![yapılacak şey:image_alt_text](manipulate-pivot-table_1.png)
##  **Basit kod**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-PivotTables-ManipulatePivotTable-new.cpp" >}}
##  **Konsol Çıkışı**
 Aşağıda, yukarıdaki örnek kodun sağlanan kodla çalıştırıldığında konsol çıktısı verilmiştir.[örnek excel dosyası](23167013.xlsx).

{{< highlight "java" >}}

 Before refreshing Pivot Table value of cell H8: 15

After refreshing Pivot Table value of cell H8: 6

{{< /highlight >}}
