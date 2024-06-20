---
title: Pivot Tablosunda Hesaplanmış Alan Ekleme
type: docs
weight: 130
url: /tr/java/add-calculated-field-in-pivot-table/
description: Aspose.Cells ile bir pivot tablosunda hesaplanmış bir alan eklemenin yolu.
keywords: Pivot tablosuna hesaplanmış bir alan ekleme.
---

## **Olası Kullanım Senaryoları**
Bilgisine sahip olduğunuz verilere dayalı olarak bir pivot tablosu oluşturduğunuzda, içindeki verilerin istediğiniz gibi olmadığını fark edersiniz. İstediğiniz veri, bu orijinal verilerin bir kombinasyonudur. Örneğin, veriden önce verilerin çıkarılması, çarpılması ve bölünmesi gerekebilir. Bu durumda, bir hesaplanmış alan oluşturmanız ve hesaplama için ilgili formülü ayarlamanız gerekir. Daha sonra hesaplanmış alanda bazı istatistikler ve diğer işlemleri gerçekleştirin. 

## **Excel'de Pivot Tablosunda Hesaplanmış Alan Ekleme**
Excel'de bir PivotTable'a hesaplanmış bir alan eklemek için şu adımları izleyin:

1. Bir hesaplanmış alan eklemek istediğiniz PivotTable'ı seçin. 
2. Kuruluş sekmesine gidin ve üzerinde PivotTable Analizi olan sekmeyi seçin.
3. "Alanlar, Öğeler ve Kümeler" üzerine tıklayın ve ardından açılır menüden "Hesaplanmış Alan"ı seçin.
4. "Ad" alanına hesaplanmış alan için bir ad girin.
5. "Formül" alanına, uygun PivotTable alan adlarını ve matematik operatörlerini kullanarak gerçekleştirmek istediğiniz formülü girin. 
<br>
<img src="1.png" width=80% />
6. Hesaplanmış alan oluşturmak için "tamam"a tıklayın.
7. Yeni hesaplanmış alan, Değerler bölümü altında PivotTable Alan Listesinde görünecektir.
8. Hesaplanmış alanı PivotTable'ın Değerler bölümüne sürükleyerek hesaplanmış değerleri görüntüleyin.
<br>
<img src="2.png" width=80% />

## **Pivot Tabloya hesaplanmış alan eklemek**
Lütfen aşağıdaki örnek kodu inceleyin. Kod önce orijinal verileri ayarlar ve bir pivot tablo oluşturur. Daha sonra, pivot tablosundaki mevcut PivotField'a göre hesaplanmış bir alan oluşturur ve hesaplanmış alanı veri alanına ekler. Son olarak, [çıktı XLSX](out.xlsx) formatında workbook'u kaydeder. Örnek kodu çalıştırdıktan sonra bir hesaplanmış alanlı bir pivot tablosu çalışma sayfasına eklenir.

## **Örnek Kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-Add-calculated-field-in-PivotTable.java" >}}
