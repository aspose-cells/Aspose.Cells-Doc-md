---
title: Pivot Tabloyu Yönet
type: docs
weight: 20
url: /tr/cpp/manipulate-pivot-table/
---
## **Olası Kullanım Senaryoları**
Yeni pivot tablolar oluşturmanın yanı sıra, yeni ve mevcut pivot tabloları da değiştirebilirsiniz. Pivot tablonun kaynak aralığındaki verileri değiştirebilir ve ardından yenileyerek hesaplayabilir ve pivot tablo hücrelerinin yeni değerlerine ulaşabilirsiniz. Lütfen kullan[IPivotTable.RefreshData()](https://reference.aspose.com/cells/cpp/class/aspose.cells.pivot.i_pivot_table#ab6d71ded346508a1d4a93c59680ddaf6) ve[IPivotTable.CalculateData()](https://reference.aspose.com/cells/cpp/class/aspose.cells.pivot.i_pivot_table#a3d6ffec8ce2a7a4ccb58e0452a1733dd)pivot tabloyu yenilemek için pivot tablonun kaynak aralığındaki değerleri değiştirdikten sonra yöntemler.
## **Pivot Tabloyu Yönet**
 Aşağıdaki örnek kod,[örnek excel dosyası](23167013.xlsx) ve mevcut pivot tablonun ilk çalışma sayfasına erişir. Pivot tablonun kaynak aralığı içindeki B3 hücresinin değerini değiştirir ve ardından pivot tabloyu yeniler. Pivot tabloyu yenilemeden önce pivot tablo hücresinin H8 değerine yani 15 değerine erişir ve pivot tabloyu yeniledikten sonra değeri 6 olarak değişir.[çıktı excel dosyası](23167014.xlsx)bu kod ile oluşturulmuş ve örnek kodun örnek excel dosyası üzerindeki etkisini gösteren ekran görüntüsü. Lütfen pivot tabloyu yenilemeden önce ve sonra pivot tablo hücresinin H8 değerini gösteren aşağıdaki konsol çıktısına da bakın.

![yapılacaklar:resim_alternatif_metin](manipulate-pivot-table_1.png)
## **Basit kod**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-PivotTables-ManipulatePivotTable.cpp" >}}
## **Konsol Çıkışı**
 Sağlanan ile çalıştırıldığında, yukarıdaki örnek kodun konsol çıktısı aşağıdadır.[örnek excel dosyası](23167013.xlsx).

{{< highlight "java" >}}

 Before refreshing Pivot Table value of cell H8: 15

After refreshing Pivot Table value of cell H8: 6

{{< /highlight >}}
