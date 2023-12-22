---
title: Pivot Tablodaki filtreyi temizle
type: docs
weight: 130
url: /tr/python-net/clear-filter-in-pivot-table/
description: Aspose.Cells for Python via .NET ile pivot tablodaki belirli PivotField'dan PivotFilter nasıl temizlenir?
keywords: Clear PivotFilter in pivot table.
---
##  **Olası Kullanım Senaryoları**
 Bilinen verilerle pivot tablo oluşturduğunuzda ve pivot tabloyu filtrelemek istediğinizde filtreyi öğrenmeniz ve kullanmanız gerekir. İstediğiniz verileri etkili bir şekilde filtrelemenize yardımcı olabilir. Aspose.Cells for Python via .NET API numaralı telefonu kullanarak Pivot Tablolardaki alan değerlerine filtre uygulayabilirsiniz.

##  **Excel'deki Pivot Tablodaki filtreyi temizle**
Excel'deki Pivot Tablodaki filtreyi temizleyin ve şu adımları izleyin:

1. Filtreyi temizlemek istediğiniz PivotTable'ı seçin.
2. Pivot tabloda temizlemek istediğiniz filtrenin açılır okuna tıklayın.
3. Açılır menüden "Filtreyi Temizle"yi seçin.
<img src="1.png" width=80% />
4. Pivot tablodaki tüm filtreleri temizlemek istiyorsanız Excel'deki şeritte bulunan PivotTable Analizi sekmesindeki "Filtreleri Temizle" butonuna da tıklayabilirsiniz.
<img src="2.png" width=80% />

##  **C#'i kullanarak Pivot Tablodaki filtreyi temizleyin**
 Aspose.Cells for Python via .NET'i kullanarak Pivot Table'daki filtreyi temizleyin. Lütfen aşağıdaki örnek koda bakın.
1.  Verileri ayarlayın ve buna göre bir PivotTable oluşturun.
 2. Pivot tablonun satır alanına bir filtre ekleyin.
 3. Çalışma kitabını kaydedin[çıkış XLSX](out_add.xlsx) biçim. Örnek kodu çalıştırdıktan sonra çalışma sayfasına top10 filtreli bir pivot tablo eklenir.
 4. Belirli bir pivot alanındaki filtreyi temizleyin. Filtreyi temizlemek için kodu çalıştırdıktan sonra, ilgili pivot alanındaki filtre temizlenecektir. lütfen kontrol ediniz[çıkış XLSX](out_delete.xlsx).

##  **Basit kod**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-Clear-filter-in-PivotTable.py" >}}