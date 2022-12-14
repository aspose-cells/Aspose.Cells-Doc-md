---
title: Java 19.6 Sürüm Notları aracılığıyla Android için Aspose.Cells
type: docs
weight: 30
url: /tr/java/aspose-cells-for-android-via-java-19-6-release-notes/
---
{{% alert color="primary" %}} 

Bu sayfa, Java 19.6 üzerinden Android için Aspose.Cells için sürüm notları içerir.

{{% /alert %}} 

|**Anahtar**|**Özet**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-42914|Büyük koşullu biçimler, OOM istisnasına neden olur|Artırma|
|CELLSJAVA-42916|Workbook.save() sonrasında veri formatı sorunu|Artırma|
|CELLSJAVA-42930|Excel95 yükleme hatası|Artırma|
|CELLSJAVA-42927|Kaydedilen dosya, sütunları sildikten sonra Excel'de yavaş açılıyor|Artırma|
|CELLSJAVA-42857|Dışa aktarılan PDF'deki şekiller için yanlış değer gösteriliyor|Böcek|
|CELLSJAVA-42890|Görüntü opak ve dönüşümden sonra saydam değil - Excel'den HTML'ye dönüştürme|Böcek|
|CELLSJAVA-42893|Excel'den HTML'ye dönüştürmede grafik eksik|Böcek|
|CELLSJAVA-42899|Excel'den HTML'ye geçiş sorunu|Böcek|
|CELLSJAVA-42903|CentOS'ta Excel'den HTML'ye dönüştürme sorunu|Böcek|
|CELLSJAVA-42882|Bir MS Excel 95 XLS dosyasından veri çıkarılamadı|Böcek|
|CELLSJAVA-42887|MS Excel ve Aspose.Cells arasındaki hesaplama farkı|Böcek|
|CELLSJAVA-42891|XIRR işlevi, aralıkta herhangi bir boş değer varsa sayısal bir hata verir|Böcek|
|CELLSJAVA-42909|DATEVALUE işleviyle ilgili sorun|Böcek|
|CELLSJAVA-42910|Dizede bir karakter olduğunda DÜŞEYARA işleviyle ilgili sorun|Böcek|
|CELLSJAVA-42911|Tarihler için TEXT işlevini kullanırken sorun|Böcek|
|CELLSJAVA-42896|PDF'ye dönüştürme, telefon numaralarını devreder|Böcek|
|CELLSJAVA-42900|PDF'ye dönüştürme metin sırasını değiştirir|Böcek|
|CELLSJAVA-42932|Style.getDisplayStyle yöntemiyle koşullu biçimlendirme hatası|Böcek|
|CELLSJAVA-42928|Bazı satırlar XLSX'ten PDF'e dönüştürmede yansıtılmaz|Böcek|
|CELLSJAVA-42904|Üstbilgi görüntüsü görünüşte dosyayı bozuyor|Böcek|
|CELLSJAVA-42907|Çalışma kitabını kaydettikten sonra kaybolan filtre|Böcek|
|CELLSJAVA-42915|Çalışma kitabına bir sayfa eklendikten sonra filtreler değiştirilir|Böcek|
|CELLSJAVA-42918|Dönüştürülen dosyanın grafiği düzleştirildi (XLS'den XLSX'e dönüştürme)|Böcek|
|CELLSJAVA-42938|XLSX dosyasının yüklenmesi uygulamayı durduruyor|Böcek|
|CELLSJAVA-42881|Bir MS Excel 5.0/95 XLS dosyası yüklenirken "java.lang.IllegalStateException: Geçersiz kodlama: null" istisnası|İstisna|
|CELLSJAVA-42884|Bir MS Excel 5.0/95 XLS dosyası yüklenirken "java.lang.ArrayIndexOutOfBoundsException" istisnası|İstisna|
|CELLSJAVA-42859|ODS dosyasından Ad yüklemek için CellsException|İstisna|
|CELLSJAVA-42908|Name.getRefersTo() çağrılırken istisna|İstisna|
|CELLSJAVA-42926|Çalışma kitabı yüklenirken IllegalStateException|İstisna|
## **Herkese Açık API ve Geriye Dönük Uyumsuz Değişiklikler**
Aşağıda, eklenen, yeniden adlandırılan, kaldırılan veya kullanımdan kaldırılan üyeler gibi genel API'de yapılan tüm değişikliklerin ve Java aracılığıyla Android için Aspose.Cells'de yapılan geriye dönük uyumlu olmayan değişikliklerin bir listesi bulunmaktadır. Listelenen herhangi bir değişiklikle ilgili endişeleriniz varsa, lütfen Aspose.Cells destek forumunda yükseltin.
### **StreamProviderOptions yapıcısını ekler**
Yeni StreamProviderOptions.
### **FileFormatType.GraphChart sıralamasını ekler**
Katıştırılmış grafik grafik dosyasını temsil eder.
### **ImportTableOptions.CheckMergedCells özelliklerini ekler**
Verileri içe aktarırken birleştirilmiş hücrelerin kontrol edilip edilmediğini gösterir.
### **ODSCellFieldCollection, ODSCellField sınıfları ve ODSCellFieldType enum ekler**
ODS'nin hücre alanını temsil eder.
### **Cells.ODSCellFields özelliklerini ekler**
ODS'nin hücre alanlarının listesini alır.
### **ODSPageBackground sınıfını ve PageSetup.ODSPageBackground özelliğini ekler**
ODS'nin arka planını temsil eder.
### **Enum FileFormatType.FODS,FileFormatType.SXC,LoadFormat.FODS,LoadFormat.SXC,SaveFormat.FODS ve SaveFormat.SXC'yi ekler**
.FODS ve .SXC dosya biçimi türlerini temsil eder.
### **Enum WarningType.UnsupportedFileFormat ekler**
Uyarı türleri için desteklenmeyen dosya biçimini temsil eder.
### **Enum ODSGeneratorType ekler**
ods üreteci türünü temsil eder.
### **OoxmlSaveOptions.EmbedOoxmlAsOleObject**
OOXML dosyasının OleObject olarak katıştırılıp yerleştirilmediğini gösterir.
### **Row.CopySettings(Aspose.Cells.Row,System.Boolean) ekler**
Stil, yükseklik, görünürlük, vb. gibi satır ayarlarını kopyalayın.
