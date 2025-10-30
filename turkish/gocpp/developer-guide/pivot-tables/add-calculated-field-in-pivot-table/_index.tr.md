---
title: Pivot Tablosuna Hesaplanmış Alan Ekleme (Golang ve C++ ile)
linktitle: Pivot Tablosunda Hesaplanmış Alan Ekleme
type: docs
weight: 130
url: /tr/go-cpp/add-calculated-field-in-pivot-table/
description: Aspose.Cells for C++ numaralı ile pivot tabloya hesaplanmış alan nasıl eklenir.
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
5. "Formül" alanına, kullanmak istediğiniz PivotTable alan adları ve matematiksel operatörleri kullanarak gerçekleştirmek istediğiniz hesaplama için formülü girin. 
<br>
<img src="1.png" width=80% />
6. Hesaplanmış alan oluşturmak için "tamam"a tıklayın.
7. Yeni hesaplanmış alan, Değerler bölümü altında PivotTable Alan Listesinde görünecektir.
8. Hesaplanmış alanı PivotTable'ın Değerler bölümüne sürükleyerek hesaplanmış değerleri görüntüleyin.
<br>
<img src="2.png" width=80% />

## **C++ kullanarak Pivot Tabloya Hesaplanmış Alan Ekleme**
Aspose.Cells kullanarak Excel dosyasına hesaplanmış alan eklemek. Örnek kodu yürüttükten sonra, hesaplanmış bir alan içeren bir pivot tablo oluşturulur.
1. Orijinal verileri ayarlayın ve bir pivot tablosu oluşturun. 
2. Mevcut PivotField'a göre hesaplanmış alanı oluşturun.
3. Hesaplanmış alanı veri alanına ekleyin. 
4. Son olarak, çalışma kitabını [çıktı XLSX](out.xlsx) formatında kaydeder. 

## **Örnek Kod**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddCalculatedFieldInPivotTable.go" >}}
