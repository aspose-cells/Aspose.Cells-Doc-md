---
title: Pivot Tablosunda Filtreyi Temizle
type: docs
weight: 130
url: /tr/net/clear-filter-in-pivot-table/
description: Aspose.Cells ile pivot tablosundaki belirli bir PivotField dan PivotFilter ı nasıl temizleyeceğinizi öğrenin.
keywords: Pivot tablosundaki PivotFilter ı temizleyin.
---

## **Olası Kullanım Senaryoları**
Bilinen verilerle pivot tablosu oluşturduğunuzda ve tabloyu filtrelemek istediğinizde filtreyi öğrenip kullanmanız gerekir. Bu, istediğiniz veriyi etkili bir şekilde filtrelemenize yardımcı olabilir. Aspose.Cells API'sini kullanarak Pivot Tablolarında alan değerlerinde filtreleme yapabilirsiniz. 

## **Excel'de Pivot Tablosundaki filtrelemeyi temizle**
Excel'de Pivot Tablosundaki filtrelemeyi temizleme adımları şunlardır:

1. Temizlemek istediğiniz PivotTablosunu seçin. 
2. Pivot tablosundaki temizlemek istediğiniz filtre için açılır ok'a tıklayın.
3. Açılır menüden "Filtreyi Temizle" seçeneğini seçin.
<img src="1.png" width=80% />
4. PivotTablosunda tüm filtreleri temizlemek isterseniz, Excel'in Ribbon'ındaki PivotTable Analyze sekmesindeki "Filtreleri Temizle" düğmesine de tıklayabilirsiniz.
<img src="2.png" width=80% />

## **C# Kullanarak Pivot Tablosunda Filtreyi Temizleme**
Aspose.Cells'i kullanarak Pivot Tablosundaki filtreleri temizleyin. Lütfen aşağıdaki örnek kodu inceleyin. 
1. Verileri ayarlayın ve bunlara dayalı bir PivotTablo oluşturun. 
2. Pivot tablosunun sıra alanına bir filtre ekleyin. 
3. İşlem örneği kodunu çalıştırdıktan sonra, [çıktı XLSX](out_add.xlsx) biçimindeki bir çalışma kitabına bir pivot tablosu ve üst10 filtresi eklenir. 
4. Belirli bir pivot alanındaki filtreyi temizleyin. Filtreyi temizlemek için kodu çalıştırdıktan sonra, belirli pivot alanındaki filtre temizlenecektir. Lütfen [çıktı XLSX](out_delete.xlsx) dosyasını kontrol edin.

## **Örnek Kod**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-Clear-filter-in-PivotTable.cs" >}}
