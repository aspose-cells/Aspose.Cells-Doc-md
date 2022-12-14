---
title: Aspose.Cells for Java 19.6 Sürüm Notları
type: docs
weight: 70
url: /tr/java/aspose-cells-for-java-19-6-release-notes/
---
{{% alert color="primary" %}} 

Bu sayfa Aspose.Cells for Java 19.6 için sürüm notları içerir.

{{% /alert %}} 

|**Anahtar**|**Özet**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-42914|Büyük koşullu biçimler, OOM istisnasına neden olur|Artırma|
|CELLSJAVA-42916|Workbook.save() sonrasında veri formatı sorunu|Artırma|
|CELLSJAVA-42930|Excel95 yükleme hatası|Artırma|
|CELLSJAVA-42927|Kaydedilen dosya, sütunları sildikten sonra Excel'de yavaş açılıyor|Artırma|
|CELLSJAVA-42932|Style.getDisplayStyle yöntemiyle koşullu biçimlendirme hatası|Böcek|
|CELLSJAVA-42928|Bazı satırlar XLSX'ten PDF'e dönüştürmede yansıtılmaz|Böcek|
|CELLSJAVA-42904|Üstbilgi görüntüsü görünüşte dosyayı bozuyor|Böcek|
|CELLSJAVA-42907|Çalışma kitabını kaydettikten sonra kaybolan filtre|Böcek|
|CELLSJAVA-42915|Çalışma kitabına bir sayfa eklendikten sonra filtreler değiştirilir|Böcek|
|CELLSJAVA-42918|Dönüştürülen dosyanın grafiği düzleştirildi (XLS'den XLSX'e dönüştürme)|Böcek|
|CELLSJAVA-42938|XLSX dosyasının yüklenmesi uygulamayı durduruyor|Böcek|
|CELLSJAVA-42859|ODS dosyasından Ad yüklemek için CellsException|İstisna|
|CELLSJAVA-42908|Name.getRefersTo() çağrılırken istisna|İstisna|
|CELLSJAVA-42926|Çalışma kitabı yüklenirken IllegalStateException|İstisna|

## **Herkese Açık API ve Geriye Dönük Uyumsuz Değişiklikler**
Aşağıda, API numaralı telefon numarasına eklenen, yeniden adlandırılan, kaldırılan veya kullanımdan kaldırılan üyeler gibi genele açık olarak yapılan tüm değişikliklerin ve Aspose.Cells for Java numaralı telefona yapılan geriye dönük uyumlu olmayan değişikliklerin bir listesi bulunmaktadır. Listelenen herhangi bir değişiklikle ilgili endişeleriniz varsa lütfen şu adrese bildirin: Aspose.Cells destek forumu.
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
