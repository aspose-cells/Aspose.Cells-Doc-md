---
title: Aspose.Cells for Java 17.10 Sürüm Notları
type: docs
weight: 30
url: /tr/java/aspose-cells-for-java-17-10-release-notes/
---
{{% alert color="primary" %}} 

 Bu sayfa için sürüm notları içerir[Aspose.Cells for Java 17.10](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-17.10/).

{{% /alert %}} 

|**Anahtar**|**Özet**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-42423|Workbook.calculateFormula yönteminin uzun süredir devam eden hesaplamasını iptal edin|Yeni özellik|
|CELLSJAVA-42414|MS Excel çalışma sayfasının SheetId alanını alın|Yeni özellik|
|CELLSJAVA-42402|Ekli HTML için gerekli iyi HTML|Artırma|
|CELLSJAVA-42372|Uzun tirelerin konumu Microsoft Excel ile aynı değil|Artırma|
|CELLSJAVA-42399|Pdf çıktısında ok noktaları net değil|Böcek|
|CELLSJAVA-42419|Çıktı HTML'sinde metin kesiliyor|Böcek|
|CELLSJAVA-42418|Kenarlık rengi, çıktı HTML'sindeki MS Excel gibi eşleşmiyor|Böcek|
|CELLSJAVA-42417|Arka plan rengi, çıktı HTML'sindeki Ms Excel gibi eşleşmiyor|Böcek|
|CELLSJAVA-42385|geri arama IFilePathProvider asla çağrılmaz ve ardından HTML dosyasının yolunda 'null' bulunur|Böcek|
|CELLSJAVA-42412|Excel'i PDF'ye dönüştürürken değer ekseni etiketleri eksik|Böcek|
|CELLSJAVA-42408|Çalışma sayfasını görüntüye dönüştürdükten sonra metin çakışması sorunu|Böcek|
|CELLSJAVA-42420|Geniş veri aralığı nedeniyle iptal ve yetersiz bellek sorunu|Böcek|
|CELLSJAVA-42415|Çıktı grafiği, çıktı HTML'sindeki orijinal tablo gibi değil|Böcek|
|CELLSJAVA-42410|Grafik alanı, etiketler, göstergeler vb. çıktı PDF ve PNG'sinde yanlış işleniyor|Böcek|
|CELLSJAVA-42409|Grafik alanı, MS Excel grafiğinin PDF ve PNG çıktılarında doğru şekilde oluşturulmuyor|Böcek|
|CELLSJAVA-41046|Elektronik tablo PDF formatına dönüştürülürken grafiğin açıklama sırası değişti|Böcek|
|CELLSJAVA-40416|Grafiğin renkleri ve stili kayboluyor|Böcek|
## **Herkese Açık API ve Geriye Dönük Uyumsuz Değişiklikler**
Aşağıda, API numaralı telefon numarasına eklenen, yeniden adlandırılan, kaldırılan veya kullanımdan kaldırılan üyeler gibi genele açık olarak yapılan tüm değişikliklerin ve Aspose.Cells for Java numaralı telefona yapılan geriye dönük uyumlu olmayan değişikliklerin bir listesi bulunmaktadır. Listelenen herhangi bir değişiklikle ilgili endişeleriniz varsa lütfen şu adrese bildirin: Aspose.Cells destek forumu.
### **AbstractCalculationMonitor.Interrupt(string) yöntemini ekler**
Kullanıcıların formül hesaplamalarının ilerlemesini kesmesine izin verir.
### **HtmlCrossType.MSExport numaralandırmasını ekler**
Dizeyi MS Excel dışa aktarma HTML'si gibi görüntüler.
### **Worksheet.TabId özelliği ekler**
Sayfa için dahili tanımlayıcıyı alır.
### **Enum OLEDBCommandType.None ekler**
Komut türü belirtilmemiş.
### **Enum ConnectionDataSourceType ekler**
Veri kaynağı bağlantı türünü temsil eder.
### **ExternalConnection.Credentials ve ExternalConnection.ReConnectionMethod özelliği geçersiz**
Bunun yerine ExternalConnection.CredentialsMethodType ve ExternalConnection.ReconnectionMethodType özelliğini kullanın.
### **Eski WebQueryConnection.EditPage özelliği**
Bunun yerine WebQueryConnection.EditWebPage özelliğini kullanın.
### **Series.ValuesFormatCode özelliğini ekler**
Seri değerlerinin sayı biçimi kodunu temsil eder.


### **Kullanım Örnekleri**
Lütfen Aspose.Cells Wiki belgelerine eklenen yardım konularının listesini kontrol edin:

- [Grafik Serisinin Değer Biçim Kodunu Ayarlayın](/cells/tr/java/set-the-values-format-code-of-chart-series/)
- [Aspose.Cells kullanarak OpenXml'nin Sheet.SheetId özelliğini kullanın](/cells/tr/java/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)
- [XLSB dosyasının Harici Bağlantısını Okuma ve Yazma](/cells/tr/java/read-and-write-external-connection-of-xlsb-or-xls-file/)
- [Çalışma Kitabının Formül Hesaplamasını Durdurun veya İptal Edin](/cells/tr/java/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [HtmlCrossType kullanarak çıktı HTML'sinde dizenin nasıl çaprazlanacağını belirtin](/cells/tr/java/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/)
