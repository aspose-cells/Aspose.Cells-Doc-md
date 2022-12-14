---
title: Aspose.Cells for Java 8.2.1 Sürüm Notları
type: docs
weight: 20
url: /tr/java/aspose-cells-for-java-8-2-1-release-notes/
---
{{% alert color="primary" %}} 

 Bu sayfa için sürüm notları içerir[Aspose.Cells for Java 8.2.1](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-8.2.1/)

{{% /alert %}} 

 Aspose.Cells for Java, 8.2.1 sürümüne güncellendi ve bu sürümün 30'dan fazla yeni faydalı iyileştirme getirdiğini duyurmaktan mutluluk duyuyoruz.
Aspose.Cells for Java'i kullanarak uygulamalarınızda XLS, SpreadsheetML, OOXML, XLSB, CSV, HTML, ODS, PDF, XPS ve diğer formatlarla çalışabilirsiniz. Ayrıca Microsoft Excel'i kullanmadan çalışma kitaplarını oluşturabilir, değiştirebilir, dönüştürebilir, işleyebilir ve yazdırabilirsiniz.
Aspose.Cells for Java ile nasıl başlayacağınızı öğrenmek için belgeleri ziyaret edin.
Bu yüklemenin, ürünün tamamen çalışan bir sürümünü içerdiğini, ancak bir lisans seti olmadan bazı sınırlamalarla değerlendirme modunda çalışacağını unutmayın. Aspose.Cells'i bu değerlendirme sınırlamaları olmadan test etmek için 30 günlük ücretsiz bir geçici lisans talep edebilirsiniz.
 Aspose.Cells for Java'in bu sürümündeki değişikliklerin listesi aşağıdadır.

\1) Aspose.Cells

Diğer İyileştirmeler ve Değişiklikler

Yeni özellikler

(CELLSJAVA-40955) - Mutlak konumlandırmayı şekillendir
(CELLSJAVA-40943) - Yalnızca aralıktaki görünür hücreleri yapıştırmak için PasteOptions'a bir seçenek ekleyin

Hatalar

(CELLSJAVA-40977) - Excel dosyası HTML'ye dönüştürüldüğünde koşullu biçimlendirme çalışmıyor
(CELLSJAVA-40959) - HTML çıktısında ekstra hizalama özelliği.
(CELLSJAVA-40954) - HTML çıktısında sütunlar uyumsuz
(CELLSJAVA-40953) - Excel'i html'ye dönüştürürken bazı hücrelerin sınırları biraz genişletildi
(CELLSJAVA-40980) - Bağlantılı hücre değeri harici çalışma kitabından güncellenmiyor
(CELLSJAVA-40957) - Çalışma Sayfasını Lisanslı modda korumak, MS Excel'in önizlemede çökmesine neden oluyor
(CELLSJAVA-40956) - Chart.getName() yanlış grafik adı veriyor
(CELLSJAVA-40952) - Series.hasLeaderLines() doğru değeri döndürmez
(CELLSJAVA-40944) - Katıştırılmış PDF, Çalışma Kitaplarını birleştirdikten sonra bozuluyor
(CELLSJAVA-40979) - İşlenen PDF'deki Pasta grafiğindeki veri etiketlerine bazı kareler iliştirildi
(CELLSJAVA-40975) - XLSX'ten Jpeg'e dönüştürme - Performans
(CELLSJAVA-40973) - setExtractContentPermission'ı devre dışı bırak - "İçeriği kopyalama veya çıkarma izni" seçeneği çalışmıyor
(CELLSJAVA-40965) - Cells PDF'de birbiriyle çakışıyor
(CELLSJAVA-40962) - Aspose.Cells, #YOK değerini MS Excel'den farklı bir şekilde işler
(CELLSJAVA-40926) - %100 yakınlaştırmada tablo kenarlığı kalın yerine normal
(CELLSJAVA-40833) - Tablonun görüntü kalitesi düşük - Grafikten Görüntüye dönüştürme
(CELLSJAVA-40949) - Grafik görüntüsünde yatay eksen görünmüyor
(CELLSJAVA-40948) - Veri noktalarındaki özel görüntü, grafik görüntüsünde gösterilmiyor
(CELLSJAVA-40947) - Grafik görüntüsünde Çince karakterler gösterilmiyor
(CELLSJAVA-40946) - Veri etiketleri grafik görüntüsü içinde yanlış konumda
(CELLSJAVA-40821) - Grafik ToImage kullanılarak EMF olarak kaydedildiğinde Metin Kutusu Eksik
(CELLSJAVA-40819) - Grafik, ToImage kullanılarak EMF olarak kaydedildiğinde yanlış Eksen Değerleri
(CELLSJAVA-40818) - Grafik, ToImage kullanılarak EMF olarak kaydedildiğinde Eksik Eksen Başlığı
(CELLSJAVA-40830) - PDF'ye dışa aktarırken Yığılmış Alanda ve Çubuk Grafikte ters z-endeksi

İstisnalar

(CELLSJAVA-40985) - CellsException: Workbook.save'de dosyanın sonuna ulaşıldı
(CELLSJAVA-40983) - Workbook.save'de java.lang.NullPointerException
(CELLSJAVA-40981) - Aspose.Cells, Parola korumalı Excel 2013 dosyalarını okuyamaz
(CELLSJAVA-40976) - Sparkline, insertRows kullanılırken NullPointerException hatası verir
(CELLSJAVA-40969) - İstisna: "java.lang.StringIndexOutOfBoundsException: Bir Şeklin değeri güncellenirken dize dizini aralık dışında"
(CELLSJAVA-40967) - LineShape'e aktarılamaz

Herkese Açık API ve Geriye Dönük Uyumsuz Değişiklikler

Aşağıda, API numaralı telefon numarasına eklenen, yeniden adlandırılan, kaldırılan veya kullanımdan kaldırılan üyeler gibi genele açık olarak yapılan tüm değişikliklerin ve Aspose.Cells for Java numaralı telefona yapılan geriye dönük uyumlu olmayan değişikliklerin bir listesi bulunmaktadır. Listelenen herhangi bir değişiklikle ilgili endişeleriniz varsa lütfen şu adrese bildirin: Aspose.Cells destek forumu.

 Cell.GetValidation() yöntemini ekler
Hücre için geçerli olan doğrulamayı alır.

 Cell.GetValidationValue() yöntemini ekler
Hücrenin değerinin geçerli olup olmadığını gösterir.

 WorkbookRender.ToPrinter(PrinterSettings PrinterSettings) yöntemini ekler
Çalışma kitabını PrinterSettings aracılığıyla Yazıcıya işleyin.


Not
Aspose.Cells for Java kod tabanı, ilgili .NET sürümünün koduyla eşleştiğinden, Aspose.Cells for .NET v8.2.1'de bulunan değişikliklerin, geliştirmelerin ve düzeltmelerin çoğu bu Aspose.Cells for Java v8.2.1'de de yer almaktadır.
