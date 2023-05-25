---
title: Pivot Tabloda filtreyi temizle
type: docs
weight: 130
url: /tr/net/clear-filter-in-pivot-table/
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

##  **C# Kullanarak Pivot Tablodaki filtreyi temizleyin**
 Aspose.Cells kullanarak Özet Tablodaki filtreyi temizleyin. Lütfen aşağıdaki örnek koda bakın.
1.  Verileri ayarlayın ve buna göre bir PivotTable oluşturun.
2. Pivot tablonun satır alanına bir filtre ekleyin.
 3. Çalışma kitabını şuraya kaydedin:[çıkış XLSX](out_add.xlsx) biçim. Örnek kodu çalıştırdıktan sonra, çalışma sayfasına top10 filtreli bir pivot tablo eklenir.
 4. Belirli bir pivot alanındaki filtreyi temizleyin. Filtreyi temizleme kodunu çalıştırdıktan sonra, belirli pivot alanındaki filtre temizlenecektir. lütfen kontrol ediniz[çıkış XLSX](out_delete.xlsx).

##  **Basit kod**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-Clear-filter-in-PivotTable.cs" >}}