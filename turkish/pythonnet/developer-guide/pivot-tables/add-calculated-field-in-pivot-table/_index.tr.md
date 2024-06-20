---
title: Pivot Tablosunda Hesaplanmış Alan Ekleme
type: docs
weight: 130
url: /tr/python-net/add-calculated-field-in-pivot-table/
description: Python için Aspose.Cells ile pivot tablosuna hesaplanmış bir alan eklemek için nasıl yapılır via .NET.
keywords: Aspose.Cells for Python Excel, Excel Python kütüphanesi, Python Excel Kütüphanesi kullanarak pivot tablosunda hesaplanmış alan eklemek.
---

## **Olası Kullanım Senaryoları**
Bilgisine sahip olduğunuz verilere dayalı olarak bir pivot tablosu oluşturduğunuzda, içindeki verilerin istediğiniz gibi olmadığını fark edersiniz. İstediğiniz veri, bu orijinal verilerin bir kombinasyonudur. Örneğin, veriden önce verilerin çıkarılması, çarpılması ve bölünmesi gerekebilir. Bu durumda, bir hesaplanmış alan oluşturmanız ve hesaplama için ilgili formülü ayarlamanız gerekir. Daha sonra hesaplanmış alanda bazı istatistikler ve diğer işlemleri gerçekleştirin. 

## **Excel'de Pivot Tablosuna Hesaplanmış Alan Eklemek**
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

## **Python İçin Aspose.Cells Excel Kütüphanesi Kullanarak Pivot Tablosuna Hesaplanmış Alan Ekleme**
Aspose.Cells for Python via .NET kullanarak Excel dosyasına hesaplanmış alan ekleyin. Lütfen aşağıdaki örnek kodu inceleyin. Örnek kodu yürüttükten sonra, bir hesaplanmış alanın eklendiği bir pivot tablosu oluşturulur.
1. Orijinal verileri ayarlayın ve bir pivot tablosu oluşturun. 
2. Mevcut PivotField'a göre hesaplanmış alanı oluşturun.
3. Hesaplanmış alanı veri alanına ekleyin. 
4. Son olarak, çalışma kitabını [çıktı XLSX](out.xlsx) formatında kaydeder. 

## **Örnek Kod**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-Add-calculated-field-in-PivotTable.py" >}}
