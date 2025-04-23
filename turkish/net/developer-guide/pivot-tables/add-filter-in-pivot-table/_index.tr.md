---
title: Pivot Filtreleri
type: docs
weight: 130
url: /tr/net/add-or-clear-pivot-filter/
description: Aspose.Cells ile pivot tablosuna filtre eklemenin nasıl yapıldığını öğrenin.
keywords: Ofis 2013, ofis 2016, ofis 2019 ve ofis 365 olmadan pivot tablosuna filtre eklemek.
---

## **Olası Kullanım Senaryoları**
Bilinen verilerle bir pivot tablo oluşturduğunuzda ve bu tabloyu filtrelemek istediğinizde, filtreyi öğrenmeli ve kullanmalısınız. Bu, istediğiniz veriyi etkili bir şekilde filtrelemenize yardımcı olabilir. Aspose.Cells API kullanarak, Pivot Tablolardaki alan değerlerine filtre ekleyebilir ve temizleyebilirsiniz. 

## **Excel'de Pivot Tabloya Filtre Ekle**
Excel'de Pivot Tabloya filtre eklemek için şu adımları izleyin:

1. Temizlemek istediğiniz PivotTablosunu seçin. 
2. Pivot tabloda eklemek istediğiniz filtre için açılır ok tuşuna tıklayın.
3. Açılır menüden "En Üst 10" seçeneğini seçin.
<br>
<img src="3.png" width=80% />
4. Gösterim modunu ve filtre sayısını ayarlayın.
<br>
<img src="4.png" width=80% />

## **Pivot Tabloya Filtre Ekle**
Lütfen aşağıdaki örnek kodu inceleyin. Veriyi ayarlar ve buna dayalı bir PivotTablo oluşturur. Daha sonra pivot tablosunun satır alanına bir filtre ekler. Son olarak, çalışma kitabını [çıktı XLSX](filterout.xlsx) formatında kaydeder. Örnek kodu çalıştırdıktan sonra, bir sayfada top10 filtresi eklenmiş bir pivot tablosu eklenir.

### **Örnek Kod**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-Add-filter-in-PivotTable.cs" >}}

## **Excel'de Pivot Tabloda Filtre Temizle**
Excel'de Pivot Tablosundaki filtrelemeyi temizleme adımları şunlardır:

1. Temizlemek istediğiniz PivotTablosunu seçin. 
2. Pivot tablosundaki temizlemek istediğiniz filtre için açılır ok'a tıklayın.
3. Açılır menüden "Filtreyi Temizle" seçeneğini seçin.
<br>
<img src="1.png" width=80% />
4. PivotTablosunda tüm filtreleri temizlemek isterseniz, Excel'in Ribbon'ındaki PivotTable Analyze sekmesindeki "Filtreleri Temizle" düğmesine de tıklayabilirsiniz.
<br>
<img src="2.png" width=80% />

## **Pivot Tabloda Filtre Temizle**
Aspose.Cells'i kullanarak Pivot Tablosundaki filtreleri temizleyin. Lütfen aşağıdaki örnek kodu inceleyin. 
1. Verileri ayarlayın ve bunlara dayalı bir PivotTablo oluşturun. 
2. Pivot tablosunun sıra alanına bir filtre ekleyin. 
3. İşlem örneği kodunu çalıştırdıktan sonra, [çıktı XLSX](out_add.xlsx) biçimindeki bir çalışma kitabına bir pivot tablosu ve üst10 filtresi eklenir. 
4. Belirli bir pivot alanındaki filtreyi temizleyin. Filtreyi temizlemek için kodu çalıştırdıktan sonra, belirli pivot alanındaki filtre temizlenecektir. Lütfen [çıktı XLSX](out_delete.xlsx) dosyasını kontrol edin.

### **Örnek Kod**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-Clear-filter-in-PivotTable.cs" >}}
{{< app/cells/assistant language="csharp" >}}
