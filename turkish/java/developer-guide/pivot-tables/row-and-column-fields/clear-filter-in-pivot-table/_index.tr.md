---
title: Pivot Tablosunda Filtreyi Temizle
type: docs
weight: 130
url: /tr/java/clear-filter-in-pivot-table/
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

## **Pivot Tablosunda filtrelemeyi temizleme**
Lütfen aşağıdaki örnek kodu inceleyin. Veriyi ayarlar ve ona dayalı olarak bir PivotTable oluşturur. Ardından pivot tablosunun satır alanına bir filtre ekler. Son olarak, çalışılan kitabı [çıktı XLSX](out_add.xlsx) formatında kaydeder. Örnek kodu çalıştırdıktan sonra, çıktı sayfasına bir top10 filtresi eklenmiş bir pivot tablosu eklenir. Bir filtre ekledikten sonra filtresiz veriye ihtiyaç duyduğumuzda, belirli bir pivotfield'daki filtrelemeyi temizleyebiliriz. Filtreyi temizlemek için kodu çalıştırdıktan sonra, belirli bir pivotfield'daki filtre temizlenir. Lütfen [çıktı XLSX dosyasını](out_delete.xlsx) kontrol edin.

## **Örnek Kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-Clear-filter-in-PivotTable.java" >}}
