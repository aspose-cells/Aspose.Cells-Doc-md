---
title: Pivot Tabloda hesaplanan alan ekleme
type: docs
weight: 130
url: /tr/java/add-calculated-field-in-pivot-table/
description: Aspose.Cells ile pivot tabloda hesaplanan alan nasıl eklenir.
keywords: Adding a calculated field in pivot table.
---
##  **Olası Kullanım Senaryoları**
 Bilinen verilere dayalı bir pivot tablo oluşturduğunuzda, içindeki verilerin istediğiniz gibi olmadığını görürsünüz. İstediğiniz veriler, bu orijinal verilerin birleşimidir. Örneğin, verileri istemeden önce orijinal verileri toplamanız, çıkarmanız, çarpmanız ve bölmeniz gerekir. Şu anda, bir hesaplanan alan oluşturmanız ve hesaplama için ilgili formülü ayarlamanız gerekir. Ardından, hesaplanan alanda bazı istatistikler ve diğer işlemler gerçekleştirin.

##  **Excel'de Pivot Tablo'da hesaplanan alan ekleme**
Excel'de bir PivotTable'a hesaplanan bir alan ekleyin, şu adımları izleyin:

1.  Hesaplanmış alan eklemek istediğiniz PivotTable'ı seçin.
2. Şeritte PivotTable Analizi sekmesine gidin.
3. "Alanlar, Öğeler ve Kümeler"e tıklayın ve ardından açılır menüden "Hesaplanan Alan"ı seçin.
4. "Ad" alanına, hesaplanan alan için bir ad girin.
 5. "Formül" alanına, uygun PivotTable alan adlarını ve matematiksel işleçleri kullanarak gerçekleştirmek istediğiniz formülü girin.
<br>
<img src="1.png" width=80% />
6. Hesaplanan alanı oluşturmak için "tamam"a tıklayın.
7. Yeni hesaplanan alan, Değerler bölümünün altındaki PivotTable Alan Listesinde görünecektir.
8. Hesaplanan değerleri görüntülemek için hesaplanan alanı PivotTable'ın Değerler bölümüne sürükleyin.
<br>
<img src="2.png" width=80% />

##  **Pivot Tabloda hesaplanan alan ekleme**
Lütfen aşağıdaki örnek koda bakın. Kod önce orijinal verileri ayarlar ve bir pivot tablo oluşturur. Ardından pivot tablodaki mevcut PivotField'e göre hesaplanan alanı oluşturun ve hesaplanan alanı veri alanına ekleyin. Son olarak, çalışma kitabını şuraya kaydeder:[çıkış XLSX](out.xlsx) biçim. Örnek kodu çalıştırdıktan sonra, çalışma sayfasına hesaplanan alanı olan bir pivot tablo eklenir.

##  **Basit kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-Add-calculated-field-in-PivotTable.java" >}}
