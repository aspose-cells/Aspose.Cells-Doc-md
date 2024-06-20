---
title: Pivot Tablo İşleme
type: docs
weight: 20
url: /tr/cpp/manipulate-pivot-table/
---

## **Olası Kullanım Senaryoları**
Yeni pivot tablo oluşturmanın yanı sıra, yeni ve mevcut pivot tablolarının üzerinde çalışabilirsiniz. Pivot tablosunun kaynak aralığındaki verileri değiştirebilir ve ardından pivot tablosunu yenileyebilir ve hesaplayabilir ve pivot tablosu hücrelerinin yeni değerlerine ulaşabilirsiniz. Pivot tablosunun kaynak aralığındaki değerleri değiştirdikten sonra, lütfen yenilemek için [PivotTable.RefreshData()](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/refreshdata/) ve [PivotTable.CalculateData()](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/calculatedata/) yöntemlerini kullanın.
## **Pivot Tablo İşleme**
Aşağıdaki örnek kod, [örnek excel dosyasını](23167013.xlsx) yükler ve ilk çalışma sayfasındaki mevcut pivot tablosuna erişir. Pivot tablosunun kaynak aralığındaki B3 hücresinin değerini değiştirir ve ardından pivot tablosunu yeniler. Pivot tablosunu yenilemeden önce, pivot tablosu hücresi H8'in değerine erişir, bu değer 15'tir ve pivot tablosunu yeniledikten sonra, değeri 6'ya değişir. Lütfen bu kod ile oluşturulmuş [çıktı excel dosyasını](23167014.xlsx) ve örnek excel dosyası üzerinde örnek kodun etkisini gösteren ekran görüntüsünü kontrol edin. Ayrıca aşağıda, pivot tablosunun yenilenmesinden önce ve sonra pivot tablosu hücresinin H8 değerini gösteren konsol çıktısına da bakınız.

![todo:image_alt_text](manipulate-pivot-table_1.png)
## **Örnek Kod**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-PivotTables-ManipulatePivotTable-new.cpp" >}}
## **Konsol Çıktısı**
Aşağıda, sağlanan [örnek excel dosyası](23167013.xlsx) ile birlikte yürütüldüğünde yukarıdaki örnek kodun konsol çıktısı bulunmaktadır.

{{< highlight java >}}

 Before refreshing Pivot Table value of cell H8: 15

After refreshing Pivot Table value of cell H8: 6

{{< /highlight >}}
