---
title: Pivot Tabloda filtreyi temizle
type: docs
weight: 130
url: /tr/java/clear-filter-in-pivot-table/
description: Aspose.Cells ile pivot tablodaki belirli PivotField'den PivotFilter nasıl temizlenir.
keywords: Clear PivotFilter in pivot table.
---
##  **Olası Kullanım Senaryoları**
 Bilinen verilerle bir pivot tablo oluşturduğunuzda ve pivot tabloyu filtrelemek istediğinizde, filtreyi öğrenmeniz ve kullanmanız gerekir. İstediğiniz verileri etkili bir şekilde filtrelemenize yardımcı olabilir. Aspose.Cells API ile Pivot Tablolarda alan değerlerine göre filtreleme yapabilirsiniz.

##  **Excel'deki Pivot Tablodaki filtreyi temizle**
Excel'deki Özet Tablo'da filtreyi temizleyin, şu adımları izleyin:

1.  Filtreyi temizlemek istediğiniz PivotTable'ı seçin.
2. Pivot tabloda temizlemek istediğiniz filtre için açılır oka tıklayın.
3. Açılır menüden "Filtreyi Temizle"yi seçin.
<img src="1.png" width=80% />
4. Pivot tablodaki tüm filtreleri temizlemek isterseniz, Excel'de şeritte bulunan PivotTable Analizi sekmesindeki "Filtreleri Temizle" düğmesine de tıklayabilirsiniz.
<img src="2.png" width=80% />

##  **Pivot Tabloda filtreyi temizle**
 Lütfen aşağıdaki örnek koda bakın. Verileri ayarlar ve buna göre bir PivotTable oluşturur. Ardından, pivot tablonun satır alanına bir filtre ekleyin. Son olarak, çalışma kitabını şuraya kaydeder:[çıkış XLSX](out_add.xlsx) biçim. Örnek kodu çalıştırdıktan sonra, çalışma sayfasına top10 filtreli bir pivot tablo eklenir. Bir filtre ekledikten sonra, filtrelenmemiş verilere ihtiyacımız olduğunda, belirli bir pivot alanında filtreyi temizleyebiliriz. Filtreyi temizleme kodunu çalıştırdıktan sonra, belirli pivot alanındaki filtre temizlenecektir. lütfen kontrol ediniz[çıkış XLSX](out_delete.xlsx).

##  **Basit kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-Clear-filter-in-PivotTable.java" >}}