---
title: Pivot Filtreleri
type: docs
weight: 130
url: /tr/java/add-or-clear-pivot-filter/
description: Aspose.Cells Java kütüphanesi ile pivot tablosuna filtre eklemeyi nasıl yapacağınızı öğrenin.
keywords: Ofis 2013, ofis 2016, ofis 2019 ve ofis 365 olmadan pivot tablosuna filtre eklemek.
---

## **Olası Kullanım Senaryoları**
Bilinen verilerle bir pivot tablo oluştururken ve pivot tablosunu filtrelemek istediğinizde, filtrelemeyi öğrenip kullanmanız gerekmektedir. Aspose.Cells Java API'sini kullanarak Pivot Tablolarında alan değerlerine filtre ekleyebilirsiniz. 

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
Lütfen aşağıdaki örnek kodu inceleyin. Kod, veriyi ayarlar ve buna dayalı olarak bir PivotTable oluşturur. Daha sonra, pivot tablosunun satır alanına bir filtre ekler. Son olarak, [çıktı XLSX](out.xlsx) formatında workbook'u kaydeder. Örnek kodu çalıştırdıktan sonra, worksheet'e en üst 10 filtreli bir pivot tablosu eklenir.

### **Örnek Kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-Add-filter-in-PivotTable.java" >}}


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
Lütfen aşağıdaki örnek kodu inceleyin. Veriyi ayarlar ve ona dayalı olarak bir PivotTable oluşturur. Ardından pivot tablosunun satır alanına bir filtre ekler. Son olarak, çalışılan kitabı [çıktı XLSX](out_add.xlsx) formatında kaydeder. Örnek kodu çalıştırdıktan sonra, çıktı sayfasına bir top10 filtresi eklenmiş bir pivot tablosu eklenir. Bir filtre ekledikten sonra filtresiz veriye ihtiyaç duyduğumuzda, belirli bir pivotfield'daki filtrelemeyi temizleyebiliriz. Filtreyi temizlemek için kodu çalıştırdıktan sonra, belirli bir pivotfield'daki filtre temizlenir. Lütfen [çıktı XLSX dosyasını](out_delete.xlsx) kontrol edin.

### **Örnek Kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-Clear-filter-in-PivotTable.java" >}}
{{< app/cells/assistant language="java" >}}
