---
title: Pivot Tablosunda Filtreyi Temizle
type: docs
weight: 130
url: /tr/nodejs-cpp/clear-filter-in-pivot-table/
description: Aspose.Cells for Node.js via C++ ile Pivot Tablo daki belirli PivotField tan PivotFilter ı nasıl temizlenir.
keywords: Aspose.Cells for Node.js via C++ Excel, Excel Node.js kütüphanesi, Aspose.Cells for Node.js via C++ Excel Kütüphanesi Kullanarak Pivot Tablo daki PivotFilter Temizleme.
---

## **Olası Kullanım Senaryoları**
Bildiğiniz verilerle oluşturulan pivot tabloda filtreleme yapmak istediğinizde, filtreyi öğrenmeli ve kullanmalısınız. Bu, istediğiniz veriyi etkili bir şekilde filtrelemenize yardımcı olabilir. Aspose.Cells for Node.js via C++ API'sini kullanarak, Pivot Tablolarındaki alan değerlerine filtre ekleyebilirsiniz. 

## **Excel'de Pivot Tablosundaki Filtreyi Temizleme**
Excel'de Pivot Tablosundaki filtrelemeyi temizleme adımları şunlardır:

1. Temizlemek istediğiniz PivotTablosunu seçin. 
2. Pivot tablosundaki temizlemek istediğiniz filtre için açılır ok'a tıklayın.
3. Açılır menüden "Filtreyi Temizle" seçeneğini seçin.
<img src="1.png" width=80% />
4. PivotTablosunda tüm filtreleri temizlemek isterseniz, Excel'in Ribbon'ındaki PivotTable Analyze sekmesindeki "Filtreleri Temizle" düğmesine de tıklayabilirsiniz.
<img src="2.png" width=80% />

## **Aspose.Cells for Node.js via C++ Kullanarak Pivot Tablosunda Filtre Nasıl Temizlenir**
Aspose.Cells for Node.js via C++ Kullanarak Pivot Tablosunda filtreyi temizleyin. Lütfen aşağıdaki örnek kodu inceleyin. 
1. Verileri ayarlayın ve bunlara dayalı bir PivotTablo oluşturun. 
2. Pivot tablosunun sıra alanına bir filtre ekleyin. 
3. İşlem örneği kodunu çalıştırdıktan sonra, [çıktı XLSX](out_add.xlsx) biçimindeki bir çalışma kitabına bir pivot tablosu ve üst10 filtresi eklenir. 
4. Belirli bir pivot alanındaki filtreyi temizleyin. Filtreyi temizlemek için kodu çalıştırdıktan sonra, belirli pivot alanındaki filtre temizlenecektir. Lütfen [çıktı XLSX](out_delete.xlsx) dosyasını kontrol edin.

## **Örnek Kod**
{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-Clear-filter-in-PivotTable.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
