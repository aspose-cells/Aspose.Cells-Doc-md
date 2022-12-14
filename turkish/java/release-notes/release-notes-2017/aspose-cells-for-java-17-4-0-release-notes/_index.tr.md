---
title: Aspose.Cells for Java 17.4.0 Sürüm Notları
type: docs
weight: 90
url: /tr/java/aspose-cells-for-java-17-4-0-release-notes/
---
{{% alert color="primary" %}} 

 Bu sayfa için sürüm notları içerir[Aspose.Cells for Java 17.4.0](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-17.4.0/).

{{% /alert %}} 

|**Anahtar**|**Özet**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-41975|DBNum (özel kalıp) biçimlendirmesini destekler|Yeni özellik|
|CELLSJAVA-42237|Hücreye erişim, boş satırlarla HTML oluşturur|Artırma|
|CELLSJAVA-42236|Çoklu iş parçacığı ortamında performans sorunu|Artırma|
|CELLSJAVA-42226|Görüntüleri/PDF'yi oluştururken yazı tiplerini kullanmak için bir klasör ve alt klasörleriyle sınırlandırın|Artırma|
|CELLSJAVA-42239|Bir HTML yüklenirken giriş dizesi biçim hatası|Böcek|
|CELLSJAVA-42230|XLSX'i HTML'ye dönüştürürken ek bir hizalama özelliği oluşturulur|Böcek|
|CELLSJAVA-42229|XLSX'i HTML'ye aktar - Gerçek Cell değerlerinin yerine karma semboller oluşturulur|Böcek|
|CELLSJAVA-42218|HTML doğru bir şekilde Excel dosyasına dönüştürülmemiş|Böcek|
|CELLSJAVA-42210|Çıktı HTML'sinde DataBar koşullu biçimlendirmelerinden bazıları eksik|Böcek|
|CELLSJAVA-41783|Arka plan resmi SVG formatında olmalıdır ancak PNG formatındadır.|Böcek|
|CELLSJAVA-42253|Bağımlı hücre değeri, XLS'de hataya neden olur|Böcek|
|CELLSJAVA-42222|Çalışma kitabı hesaplamasından sonra toplam doğru değil|Böcek|
|CELLSJAVA-42254|GridWebServlet?acw_ajax_GridWeb yüklenirken çağrı hatası oluşuyor|Böcek|
|CELLSJAVA-42243|Excel'den PDF'e - Kare, Dikdörtgene benziyor|Böcek|
|CELLSJAVA-42242|Excel'den PDF'e - Çember Oval Şekle benziyor|Böcek|
|CELLSJAVA-42227|"x1.png" resim dosyasında fazladan bir üst kenarlık var ve alt kenarlık eksik|Böcek|
|CELLSJAVA-42212|Bir XLS'yi PDF'ye dışa aktarmayla ilgili performans sorunu|Böcek|
|CELLSJAVA-42246|Excel'den HTML'ye - Grafik Y ekseni etiketindeki metin hizalaması yanlış|Böcek|
|CELLSJAVA-42223|Radar grafiğinin noktaları xy px dönüş 0|Böcek|
|CELLSJAVA-42216|AxisScalingValuesIssue-2.xlsx PDF'ye dönüştürüldüğünde Kabarcık Grafiğinin Y Ekseninin Sınır Değerleri değişir|Böcek|
|CELLSJAVA-42250|Kod, CommandBar türünde değişken tanımını içeriyorsa derleme hatası|Böcek|
|CELLSJAVA-42241|Excel'den PDF'e - Köşeli parantezler bir sonraki satıra geliyor|Böcek|
|CELLSJAVA-42234|XLSM dosyasını XLS olarak kaydetmek, makro eylemini düğmeden kaldırır|Böcek|
|CELLSJAVA-42233|Kodu yükseltin - Grafiğe 3B Format Uygulama|Böcek|
|CELLSJAVA-42225|Şekil Giriş Aralığı ayarlanamıyor|Böcek|
|CELLSJAVA-42224|Yorumları sıralamayla ilgili sorun|Böcek|
|CELLSJAVA-42221|Özel Kontrollerle Kritik Gerileme|Böcek|
|CELLSJAVA-42220|XLSB dosyaları için Sayfa Düzeni Görünümü ayarıyla ilgili sorun|Böcek|
|CELLSJAVA-42217|Aspose API üzerinden VbaModule'a eriştikten sonra ortaya çıkan Excel dosyası vba projesini bozdu|Böcek|
|CELLSJAVA-42213|Yazı tipi istemeden, içine gömülü bir CR ile yorumdaki boyutunu değiştiriyor|Böcek|
|CELLSJAVA-42231|Satır eklerken istisna oluşuyor|İstisna|
## **Herkese Açık API ve Geriye Dönük Uyumsuz Değişiklikler**
Aşağıda, API numaralı telefon numarasına eklenen, yeniden adlandırılan, kaldırılan veya kullanımdan kaldırılan üyeler gibi genele açık olarak yapılan tüm değişikliklerin ve Aspose.Cells for Java numaralı telefona yapılan geriye dönük uyumlu olmayan değişikliklerin bir listesi bulunmaktadır. Listelenen herhangi bir değişiklikle ilgili endişeleriniz varsa lütfen şu adrese bildirin: Aspose.Cells destek forumu.
### **VbaProject.Protect(bool islockedForViewing,string password) yöntemini ekler**
VBA projesini korur veya korumasını kaldırır.
### **VbaProject.IsProtected özelliğini ekler**
vba projesinin korumalı olup olmadığını gösterir.
### **VbaProject.IslockedForViewing özelliğini ekler**
VBA projesinin görüntüleme için kilitli olup olmadığını gösterir.
### **CopyOptions.ExtendToAdjacentRange özelliği ekler**
Aralığı bitişik aralığa kopyalarken aralıkların genişletilip genişletilmediğini gösterir.

{{< highlight "java" >}}

 Workbook wb = new Workbook("sample.xlsx");

Worksheet ws = wb.getWorksheets().get("Sheet1");

CopyOptions co = new CopyOptions();

co.setExtendToAdjacentRange(true);

Cells cells = ws.getCells();

cells.copyRows(cells, 0, 1, 1, co);

{{< /highlight >}}
### **Eski Workbook.ValidateFormula(dize formülü) yöntemini siler**
### **DataSorter.SortAsNumber özelliği ekler**
Sayı gibi görünen herhangi bir şeyin sıralanıp sıralanmadığını gösterir.
### **Kullanım Örnekleri**
Lütfen Aspose.Cells Wiki belgelerine eklenen yardım konularının listesini kontrol edin:

- [Verileri Sıralarken Sıralama Uyarısı Belirtme](/cells/tr/java/specifying-sort-warning-while-sorting-data/)
- [Excel Çalışma Kitabının VBA Projesini Parolayla Koruyun](/cells/tr/java/password-protect-the-vba-project-of-excel-workbook/)
- [VBA Projesinin Korumalı olup olmadığını öğrenin](/cells/tr/java/find-out-if-vba-project-is-protected/)
- [VBA Projesinin Korumalı ve Görüntüleme için Kilitli olup olmadığını kontrol edin](/cells/tr/java/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [DBNum Özel Kalıp Biçimlendirmesini Belirleme](/cells/tr/java/specifying-dbnum-custom-pattern-formatting/)
