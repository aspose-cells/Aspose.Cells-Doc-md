---
title: Pivot Tabloya hesaplanan alanı ekleme
type: docs
weight: 130
url: /tr/python-net/add-calculated-field-in-pivot-table/
description: Aspose.Cells for Python via .NET ile pivot tabloya hesaplanan alan nasıl eklenir?
keywords: Adding a calculated field in pivot table.
---
##  **Olası Kullanım Senaryoları**
Bilinen verilere dayalı bir pivot tablo oluşturduğunuzda, içindeki verilerin istediğiniz gibi olmadığını görürsünüz. İstediğiniz veriler bu orijinal verilerin birleşimidir. Örneğin, verileri istemeden önce orijinal verileri toplamanız, çıkarmanız, çarpmanız ve bölmeniz gerekir. Şu anda hesaplanmış bir alan oluşturmanız ve hesaplama için ilgili formülü ayarlamanız gerekir. Daha sonra hesaplanan alanda bazı istatistikler ve diğer işlemleri gerçekleştirin.

##  **Excel'deki Pivot Tabloya hesaplanan alanı ekleme**
Hesaplanan alanı Excel'deki PivotTable'a ekleyin ve şu adımları izleyin:

1.  Hesaplanan alanı eklemek istediğiniz PivotTable'ı seçin.
2. Şeritteki PivotTable Analizi sekmesine gidin.
3. "Alanlar, Öğeler ve Kümeler"e tıklayın ve ardından açılır menüden "Hesaplanan Alan"ı seçin.
4. "Ad" alanına hesaplanan alan için bir ad girin.
5. "Formül" alanına, uygun PivotTable alan adlarını ve matematik işleçlerini kullanarak gerçekleştirmek istediğiniz hesaplamanın formülünü girin.
<br>
<img src="1.png" width=80% />
6. Hesaplanan alanı oluşturmak için "tamam"a tıklayın.
7. Hesaplanan yeni alan, Değerler bölümünün altındaki PivotTable Alan Listesi'nde görünecektir.
8. Hesaplanan değerleri görüntülemek için hesaplanan alanı PivotTable'ın Değerler bölümüne sürükleyin.
<br>
<img src="2.png" width=80% />

##  **C# kullanarak Pivot Tabloya hesaplanan alanı ekleyin**
Hesaplanan alanı Aspose.Cells for Python via .NET numaralı telefonu kullanarak Excel dosyasına ekleyin. Lütfen aşağıdaki örnek koda bakın. Örnek kodu çalıştırdıktan sonra çalışma sayfasına hesaplanan alanı içeren bir pivot tablo eklenir.
1.  Orijinal verileri ayarlayın ve bir pivot tablo oluşturun.
2. Hesaplanan alanı pivot tablodaki mevcut PivotField'a göre oluşturun.
 3. Hesaplanan alanı veri alanına ekleyin.
 4. Son olarak çalışma kitabını kaydeder.[çıkış XLSX](out.xlsx) biçim.

##  **Basit kod**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-Add-calculated-field-in-PivotTable.py" >}}
